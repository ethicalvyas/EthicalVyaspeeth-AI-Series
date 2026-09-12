#!/usr/bin/env python3
# ================================================================= #
# Script Name : phishing_forensics_analyzer.py                      #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 9)     #
# Description : AI-Powered Phishing & Deepfake Forensic Analyzer    #
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
You are a Senior Digital Forensics Investigator, Email Security Specialist, and Social Engineering Expert.
Your task is to analyze raw email files (.eml), header metadata, or call transcripts to detect Phishing, Business Email Compromise (BEC), Domain Typosquatting, and AI-Generated Voice (Deepfake Vishing) social engineering indicators.

Your analysis MUST strictly follow this structure:
1. Executive Incident Summary (Threat Category, Confidence Score %, Targeted Role/Victim)
2. Header & Authentication Forensic Breakdown (Inspect Return-Path vs. From header, SPF/DKIM/DMARC flags, Originating IP)
3. Content & URL Analysis (Identify typosquatting domains, suspicious link targets, urgent call-to-action pressure tactics)
4. AI / Synthetic Marker Evaluation (Identify AI-generated text patterns or deepfake audio transcript anomalies)
5. Recommended Mitigation & Takedown Actions (Mail gateway block rules, Exchange transport rules, user advisory notes)
"""

def ensure_output_directory():
    """Creates output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def read_sample_file(file_path):
    """Reads raw email or transcript file safely."""
    if not os.path.isfile(file_path):
        print(f"[!] Error: File '{file_path}' not found.")
        return None
    
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().strip()
            if not content:
                print(f"[!] Error: File '{file_path}' is empty.")
                return None
            return content
    except Exception as e:
        print(f"[!] Error reading file: {str(e)}")
        return None

def analyze_forensic_data(raw_data, filename):
    """Sends raw email or transcript text to local Ollama API for forensic inspection."""
    print(f"[*] Analyzing '{filename}' using local LLM ({MODEL_NAME})... Please wait...")
    
    user_prompt = f"Perform deep forensic analysis on the following sample data:\n\n```text\n{raw_data}\n```"
    
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

def save_report(filename, analysis_content):
    """Saves generated Markdown report with a timestamped filename."""
    ensure_output_directory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(filename).replace('.', '_')
    report_path = os.path.join(OUTPUT_DIR, f"forensic_report_{base_name}_{timestamp}.md")
    
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# AI Phishing & Deepfake Forensic Investigation Report\n")
            file.write(f"**Analyzed File:** `{filename}`  \n")
            file.write(f"**Investigation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            file.write(f"**AI Engine:** `{MODEL_NAME}`  \n\n")
            file.write("=" * 60 + "\n\n")
            file.write(analysis_content)
            
        print(f"\n[+] Forensic investigation report saved successfully to: {report_path}")
    except Exception as e:
        print(f"[!] Failed to save report: {str(e)}")

def main():
    print("==================================================================")
    print("  Ethical Vyaspeeth - AI Phishing & Deepfake Forensic Analyzer    ")
    print("==================================================================")
    
    parser = argparse.ArgumentParser(description="AI Phishing & Deepfake Forensics - Ethical Vyaspeeth")
    parser.add_argument("--email", help="Path to raw email / header / transcript file (e.g., sample_emails/fake_ceo_urgent.eml)")

    args = parser.parse_args()
    
    if args.email:
        file_path = args.email
    else:
        file_path = input("Enter path to email/transcript file (e.g., sample_emails/fake_ceo_urgent.eml): ").strip()

    raw_data = read_sample_file(file_path)
    if not raw_data:
        sys.exit(1)
        
    print(f"\n[+] Loaded '{file_path}' ({len(raw_data.splitlines())} lines)...")
    ai_report = analyze_forensic_data(raw_data, file_path)
    
    print("\n" + "=" * 20 + " FORENSIC INVESTIGATION REPORT " + "=" * 20 + "\n")
    print(ai_report)
    print("\n" + "=" * 60)
    
    save_report(file_path, ai_report)

if __name__ == "__main__":
    main()
