#!/usr/bin/env python3
# ================================================================= #
# Script Name : ai_code_auditor.py                                  #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 6)     #
# Description : AI-powered Static Application Security Testing (SAST)#
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
MODEL_NAME = "llama3"  # Alternative: "deepseek-r1:8b" or "qwen2.5-coder"
OUTPUT_DIR = "reports"

SYSTEM_PROMPT = """
You are a Senior Source Code Security Auditor and AppSec Specialist.
Your task is to analyze the provided source code snippet for security vulnerabilities (specifically SQL Injection, XSS, CSRF, IDOR, Command Injection, and Hardcoded Credentials).

Your analysis MUST follow this structure:
1. Vulnerability Summary (Vulnerability Type, OWASP Top 10 Category, & Severity Level)
2. Affected Code Snippet & Line Breakdown (Pinpoint exact line and variable handling issues)
3. Exploit Scenario (Explain step-by-step how an attacker can abuse this vulnerability)
4. Secure Refactored Code (Provide clean, production-ready replacement code using PDO prepared statements, proper escaping, or sanitization functions)
"""

def ensure_output_directory():
    """Creates output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def read_source_file(file_path):
    """Reads source code file safely."""
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

def audit_code_with_ai(source_code, file_path):
    """Sends source code snippet to local Ollama API for SAST audit."""
    print(f"[*] Auditing '{file_path}' using local LLM ({MODEL_NAME})... Please wait...")
    
    file_ext = os.path.splitext(file_path)[1].replace('.', '') or 'text'
    user_prompt = f"Audit the following `{file_ext}` source code file for security flaws:\n\n```{file_ext}\n{source_code}\n```"
    
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

def save_report(source_filename, analysis_content):
    """Saves generated Markdown report with a timestamped filename."""
    ensure_output_directory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(source_filename).replace('.', '_')
    report_path = os.path.join(OUTPUT_DIR, f"sast_report_{base_name}_{timestamp}.md")
    
    try:
        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# AI Static Application Security Testing (SAST) Report\n")
            file.write(f"**Target Source File:** `{source_filename}`  \n")
            file.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            file.write(f"**AI Engine:** {MODEL_NAME}  \n\n")
            file.write("=" * 60 + "\n\n")
            file.write(analysis_content)
            
        print(f"\n[+] SAST Report saved successfully to: {report_path}")
    except Exception as e:
        print(f"[!] Failed to save report: {str(e)}")

def main():
    print("==================================================================")
    print("  Ethical Vyaspeeth - AI Code Auditor (SAST for SQLi & XSS)      ")
    print("==================================================================")
    
    if len(sys.argv) > 1:
        source_file = sys.argv[1]
    else:
        source_file = input("Enter path to source code file (e.g., sample_code/vulnerable_login.php): ").strip()

    source_code = read_source_file(source_file)
    if not source_code:
        sys.exit(1)
        
    print(f"\n[+] Loaded '{source_file}' ({len(source_code.splitlines())} lines)...")
    ai_report = audit_code_with_ai(source_code, source_file)
    
    print("\n" + "=" * 20 + " SAST AUDIT REPORT " + "=" * 20 + "\n")
    print(ai_report)
    print("\n" + "=" * 60)
    
    save_report(source_file, ai_report)

if __name__ == "__main__":
    main()
