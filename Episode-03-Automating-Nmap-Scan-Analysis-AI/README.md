# Episode 03: Automating Nmap Scan Analysis with AI 🎯🤖

Welcome to **Episode 3** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we build an automated Python script that reads raw **Nmap scan text files**, parses open ports and services, sends them directly to a local **Ollama LLM**, and automatically generates a comprehensive **Markdown Security Audit Report**.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** Automating Nmap Scan Analysis using Python & Ollama API
* **Language:** Hindi / Hinglish

---

## 🛠️ Key Features
* 📂 **File Parser:** Automatically reads standard Nmap scan text file outputs (`-oN`).
* 🧠 **Custom Security Prompting:** Enforces structured threat analysis, CVE identification, and command recommendations.
* 📝 **Automated Reporting:** Exports clean, timestamped Markdown reports into a `reports/` folder.
* 🔒 **100% Offline & Private:** Keeps sensitive network infrastructure data entirely on your local machine.

---

## 🚀 Quick Setup Instructions

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```
(If on Kali Linux with PEP 668 active, use pip3 install ollama --break-system-packages)
### Step 2: Run a Quick Nmap Scan
```Bash
nmap -sV -sC -T4 10.0.2.15 -oN sample_nmap_scans/my_scan.txt
```
### Step 3: Run the AI Analyzer
```Bash
python3 nmap_ai_analyzer.py sample_nmap_scans/my_scan.txt
```
## 📊 Sample Generated Report Output
Reports are saved inside reports/report_<scan_name>_<timestamp>.md. They contain:
1. Executive Summary
2. Port & Service Inventory Table
3. High Risk Exploits (e.g., vsftpd 2.3.4 Backdoor, Samba Symlink)
4. Recommended Next Commands (msfconsole, searchsploit, hydra)
5. Mitigation Strategies

## 📝 Episode Assignment
1. Scan any VulnHub machine or Metasploitable VM on your local NAT network.
2. Run nmap_ai_analyzer.py against your saved -oN Nmap output.
3. Open the generated file inside reports/ and check if the recommended exploit commands worked!

## ⚠️ Legal & Ethical Disclaimer
This code and instructional material are intended solely for authorized security testing and educational research. Unauthorized testing of systems without written consent is strictly illegal.
