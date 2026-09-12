#!/usr/bin/env python3
# ================================================================= #
# Script Name : soc_log_analyzer.py                                #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 8)     #
# Description : AI-Powered Automated SOC Log Analyzer & Threat Hunter#
# ================================================================= #

import os
import sys
import argparse
from datetime import datetime

try:
    import ollama
except ModuleNotFoundError:
    print("\n[!] Error: 'ollama' Python library is missing.")
    print("[+] Please run: pip3 install ollama (or --break-system-packages)\n")
    sys.exit(1)

# Configuration
MODEL_NAME = "llama3"  # Alternative: "deepseek-r1:8b" or "mistral"
OUTPUT_DIR = "reports"

SYSTEM_PROMPT = """
You are a Senior SOC Analyst, Incident Responder, and Threat Hunting Specialist.
Your task is to analyze raw system and web server log files (e.g., Linux auth.log, Apache access logs, Syslog) to detect ongoing security incidents, malicious activities, brute-force attempts, and web attacks.

Your analysis MUST strictly follow this structure:
1. Incident Executive Summary (Threat Type, Severity Level, Target Service, Attacker IP Address)
2. Malicious Evidence Breakdown (Highlight exact log entries and line numbers showing malicious behavior)
3. Threat Analysis & MITRE ATT&CK Mapping (Identify techniques e.g., T1110 - Brute Force, T1190 - Exploit Public-Facing Application)
4. Immediate Defensive Actions & Remediation (Provide exact IPTables firewall drop rules, fail2ban setup commands, or WAF rules)
"""

def ensure_output_directory():
    """Creates output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def read_log_file(log_path):
    """Reads raw log files safely."""
    if not os.path.isfile(log_path):
        print(f"[!] Error: Log file '{log_path}' not found.")
        return None
    
    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().strip()
            if not content:
                print(f"[!] Error: Log file '{log_path}' is empty.")
                return None
            return content
    except Exception as e:
        print(f"[!] Error reading file: {str(e)}")
        return None

def analyze_log_with_ai(log_data, log_filename):
    """Sends raw log data to local Ollama API for Blue Team analysis."""
    print(f"[*] Analyzing '{log_filename}' using local LLM ({MODEL_NAME})... Please wait...")
    
    user_prompt = f"Analyze the following security log entries for malicious activity:\n\n```text\n{log_data}\n```"
    
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"[!] Error communicating with Ollama: {str(e)}"

def save_report(log_filename, analysis_content):
    """Saves generated Markdown report with a timestamped filename."""
    ensure_output_directory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(log_filename).replace('.', '_')
    report_path = os.path.join(OUTPUT_DIR, f"soc_report_{base_name}_{timestamp}.md")
    
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# AI SOC Incident Response & Log Analysis Report\n")
            file.write(f"**Analyzed Log File:** `{log_filename}`  \n")
            file.write(f"**Generated Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            file.write(f"**AI Engine:** `{MODEL_NAME}`  \n\n")
            file.write("=" * 60 + "\n\n")
            file.write(analysis_content)
            
        print(f"\n[+] SOC Incident Report saved successfully to: {report_path}")
    except Exception as e:
        print(f"[!] Failed to save report: {str(e)}")

def main():
    print("==================================================================")
    print("  Ethical Vyaspeeth - AI Blue Team Automated SOC Log Analyzer    ")
    print("==================================================================")
    
    parser = argparse.ArgumentParser(description="AI SOC Log Analyzer - Ethical Vyaspeeth")
    parser.add_argument("--log", help="Path to raw log file (e.g., sample_logs/auth.log, sample_logs/apache_access.log)")

    args = parser.parse_args()
    
    if args.log:
        log_file = args.log
    else:
        log_file = input("Enter path to log file (e.g., sample_logs/auth.log): ").strip()

    log_data = read_log_file(log_file)
    if not log_data:
        sys.exit(1)
        
    print(f"\n[+] Loaded '{log_file}' ({len(log_data.splitlines())} log lines)...")
    ai_report = analyze_log_with_ai(log_data, log_file)
    
    print("\n" + "=" * 20 + " SOC THREAT HUNTING REPORT " + "=" * 20 + "\n")
    print(ai_report)
    print("\n" + "=" * 60)
    
    save_report(log_file, ai_report)

if __name__ == "__main__":
    main()
