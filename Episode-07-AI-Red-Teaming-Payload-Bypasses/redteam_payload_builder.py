#!/usr/bin/env python3
# ================================================================= #
# Script Name : redteam_payload_builder.py                         #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 7)     #
# Description : AI-Powered Red Team Payload & Evasion Builder      #
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
MODEL_NAME = "llama3"  # Alternative: "deepseek-r1:8b" or "qwen2.5-coder"
OUTPUT_DIR = "outputs"

SYSTEM_PROMPT = """
You are an expert Red Teamer, Exploit Developer, and Evasion Specialist.
Your task is to generate functional, context-aware, and obfuscated security testing payloads based on specified target environments and filter constraints.

Your output MUST strictly follow this structure:
1. Technical Strategy & Evasion Breakdown (Explain the obfuscation or encoding mechanism)
2. Raw / Unobfuscated Reference Payload
3. Obfuscated / Evasion Payload (Clean, production-ready copy-paste block)
4. Listener & Execution Instructions (Exact terminal command for listener setup e.g., nc -lvnp, msfconsole, powershell)
"""

def ensure_output_directory():
    """Creates output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_payload(payload_type, target_env, attacker_ip, port, bypass_constraints):
    """Queries local Ollama instance for red team payload generation."""
    print(f"[*] Querying Local AI ({MODEL_NAME}) for Red Team '{payload_type}' Payload...")
    
    user_prompt = f"""
    Target Environment: {target_env}
    Payload Type: {payload_type}
    Attacker Listener IP: {attacker_ip}
    Attacker Listener Port: {port}
    Filter Constraints & Evasion Requirements: {bypass_constraints if bypass_constraints else 'Standard Obfuscation'}
    """
    
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

def save_output(payload_type, target_env, content):
    """Saves generated payload report with a timestamped filename."""
    ensure_output_directory()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"payload_{payload_type}_{target_env}_{timestamp}.md"
    file_path = os.path.join(OUTPUT_DIR, filename)
    
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Red Team Payload & Bypass Report\n")
            f.write(f"**Payload Type:** `{payload_type}`  \n")
            f.write(f"**Target Environment:** `{target_env}`  \n")
            f.write(f"**Generated Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n")
            f.write(f"**AI Engine:** `{MODEL_NAME}`  \n\n")
            f.write("=" * 60 + "\n\n")
            f.write(content)
            
        print(f"\n[+] Payload report successfully saved to: {file_path}")
    except Exception as e:
        print(f"[!] Failed to save payload report: {str(e)}")

def main():
    print("==================================================================")
    print("  Ethical Vyaspeeth - AI Red Team Payload & Bypass Builder       ")
    print("==================================================================")
    
    parser = argparse.ArgumentParser(description="AI Red Team Payload Builder - Ethical Vyaspeeth")
    parser.add_argument("--type", required=True, help="Payload Type (e.g., reverse_shell, xss_bypass, sqli_bypass, cmd_injection)")
    parser.add_argument("--target", default="linux", help="Target Environment (e.g., linux, windows, web)")
    parser.add_argument("--ip", default="10.0.2.15", help="Attacker IP Address")
    parser.add_argument("--port", default="4444", help="Attacker Listener Port")
    parser.add_argument("--bypass", default="", help="Filter constraints (e.g., 'no spaces', 'avoid alert keyword', 'base64 encoding')")

    args = parser.parse_args()
    
    result = generate_payload(args.type, args.target, args.ip, args.port, args.bypass)
    
    print("\n" + "=" * 20 + " GENERATED RED TEAM PAYLOAD " + "=" * 20 + "\n")
    print(result)
    print("\n" + "=" * 60)
    
    save_output(args.type, args.target, result)

if __name__ == "__main__":
    main()
