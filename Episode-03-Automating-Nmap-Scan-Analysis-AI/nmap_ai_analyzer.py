#!/usr/bin/env python3
# ================================================================= #
# Script Name : nmap_ai_analyzer.py                                 #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 3)     #
# Description : Automated Nmap scan parser & AI security analyzer   #
# ================================================================= #

import os
import sys
from datetime import datetime

try:
    import ollama
except ModuleNotFoundError:
    print("\n[!] Error: 'ollama' Python library is missing.")
    print("[+] Please run: pip3 install ollama (or --break-system-packages)\n")
    sys.exit(1)

# Configuration
MODEL_NAME = "llama3"  # Alternative: "deepseek-r1:8b" or "gemma2"
OUTPUT_DIR = "reports"

SYSTEM_PROMPT = """
You are a Senior Penetration Tester and Automated Vulnerability Analyst.
Your task is to analyze the provided Nmap scan output and generate a structured executive report.

Your analysis MUST include:
1. Executive Summary (High-level overview of identified hosts and risks)
2. Discovered Open Ports & Services Table
3. Critical Security Vulnerabilities & Exploit Risks (Highlight CVEs or outdated software if identifiable)
4. Recommended Next Penetration Testing Steps (Provide exact tool commands like msfconsole, hydra, searchsploit, curl, etc.)
5. Hardening & Remediation Advice for System Administrators
"""

def ensure_output_directory():
    """Creates output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def read_scan_file(file_path):
    """Reads Nmap text file safely."""
    if not os.path.isfile(file_path):
        print(f"[!] Error: File '{file_path}' not found.")
        return None
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read().strip()
            if not content:
                print(f"[!] Error: File '{file_path}' is empty.")
                return None
            return content
    except Exception as e:
        print(f"[!] Error reading file: {str(e)}")
        return None

def analyze_scan_with_ai(scan_data):
    """Sends scan data to local Ollama API."""
    print(f"[*] Querying local LLM ({MODEL_NAME})... Please wait...")
    
    user_prompt = f"Analyze the following Nmap scan raw output and produce a professional report:\n\n```text\n{scan_data}\n```"
    
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

def save_report(scan_filename, analysis_content):
    """Saves generated Markdown report with a timestamped filename."""
    ensure_output_directory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(scan_filename).split('.')[0]
    report_path = os.path.join(OUTPUT_DIR, f"report_{base_name}_{timestamp}.md")
    
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write(f"# Automated Nmap AI Vulnerability Report\n")
            file.write(f"**Target File:** `{scan_filename}`  \n")
            file.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            file.write(f"**AI Engine:** {MODEL_NAME}  \n\n")
            file.write("=" * 60 + "\n\n")
            file.write(analysis_content)
            
        print(f"[+] Report saved successfully to: {report_path}")
    except Exception as e:
        print(f"[!] Failed to save report: {str(e)}")

def main():
    print("==================================================")
    print("  Ethical Vyaspeeth - Automated Nmap AI Analyzer  ")
    print("==================================================")
    
    if len(sys.argv) > 1:
        scan_file = sys.argv[1]
    else:
        scan_file = input("Enter path to Nmap scan file (e.g., sample_nmap_scans/metasploitable2_scan.txt): ").strip()
    
    scan_data = read_scan_file(scan_file)
    if not scan_data:
        sys.exit(1)
        
    print(f"\n[+] Processing '{scan_file}' ({len(scan_data.splitlines())} lines)...")
    ai_report = analyze_scan_with_ai(scan_data)
    
    print("\n" + "=" * 20 + " AI ANALYSIS OUTPUT " + "=" * 20 + "\n")
    print(ai_report)
    print("\n" + "=" * 60 + "\n")
    
    save_report(scan_file, ai_report)

if __name__ == "__main__":
    main()
