#!/usr/bin/env python3
# ================================================================= #
# Script Name : nmap_ai_analyzer.py                                 #
# Author      : Ethical Vyaspeeth                                    #
# Series      : AI for Cybersecurity: Zero to Hero (Episode 3)     #
# Description : Automated Nmap scan parser & AI security analyzer   #
# ================================================================= #

# Required Libraries & Imports
import subprocess
import xml.etree.ElementTree as ET
import sys
import ollama

# Function 1: Running Nmap & Generating XML Output
def run_nmap_scan(target_ip):
    print(f"[+] Running Nmap scan against target: {target_ip}...")
    xml_file = "scan_results.xml"
    
    # Executing Nmap using subprocess
    command = ["nmap", "-sV", "--top-ports", "50", "-oX", xml_file, target_ip]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("[+] Nmap scan completed successfully!")
    return xml_file
    
# Function 2: Parsing Nmap XML to Extract Clean Data
def parse_nmap_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    parsed_data = []
    
    for host in root.findall('host'):
        for port in host.find('ports').findall('port'):
            state = port.find('state').get('state')
            if state == 'open':
                port_id = port.get('portid')
                service_elem = port.find('service')
                service_name = service_elem.get('name') if service_elem is not None else "unknown"
                service_version = service_elem.get('product', '') + " " + service_elem.get('version', '')
                
                parsed_data.append(f"Port {port_id}: {service_name} ({service_version.strip()})")
                
    return "\n".join(parsed_data)
    
# Function 3: Passing Parsed Data to Ollama AI
def analyze_with_ai(scan_data):
    print("[+] Sending scan results to Local AI for vulnerability analysis...")
    
    prompt = f"""
    You are an expert penetration tester. Analyze the following open ports and service versions from an Nmap scan:
    
    {scan_data}
    
    Provide a concise risk assessment:
    1. Identify high-risk services.
    2. List potential CVEs or known exploit vectors.
    3. Suggest exact CLI commands for further manual validation.
    """
    
    response = ollama.chat(
        model="llama3", # या "deepseek-r1:8b"
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['message']['content']
    
# Main Execution Block
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 nmap_ai_scanner.py <Target IP>")
        sys.exit(1)
        
    target = sys.argv[1]
    xml_out = run_nmap_scan(target)
    extracted_data = parse_nmap_xml(xml_out)
    
    print("\n--- Extracted Service Data ---")
    print(extracted_data if extracted_data else "No open ports found.")
    
    if extracted_data:
        ai_report = analyze_with_ai(extracted_data)
        print("\n================ AI VULNERABILITY REPORT ================")
        print(ai_report)
        print("=========================================================")
        
