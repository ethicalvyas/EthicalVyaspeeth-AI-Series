# Episode 08: AI for Blue Team: Building an Automated SOC Log Analyzer 🛡️🔍

Welcome to **Episode 8** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we pivot to **Blue Team defensive operations** by building an automated **SOC Log Analyzer & Threat Hunter** using Python and a local **Ollama LLM**. This tool parses Linux system authentication logs (`auth.log`) and web server access logs (Apache/Nginx) to automatically detect SSH brute-force attacks, directory traversal, and SQL Injection attempts while generating mitigation commands (e.g., `iptables` drop rules).

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** AI for Blue Team — Building an Automated SOC Log Analyzer
* **Language:** Hindi / Hinglish

---

## 🛠️ Key Features
* 🔍 **Automated Threat Hunting:** Analyzes raw log streams to identify anomalous user activity and exploit attempts.
* 🗺️ **MITRE ATT&CK Mapping:** Automatically maps identified attacks to official MITRE techniques (e.g., T1110 Brute Force, T1190 Exploit Public-Facing Application).
* 🔒 **100% Private Log Analysis:** Processes sensitive internal system logs entirely offline without cloud data exposure.
* 🛡️ **Automated Incident Response:** Generates copy-paste firewall rules (`iptables` / `fail2ban`) to block attacker IP addresses immediately.

---

## 🚀 Quick Setup Instructions

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```
(On Kali Linux with active PEP 668 restriction, use pip3 install ollama --break-system-packages)

### Step 2: Ensure Ollama is Active
```bash
systemctl status ollama
ollama pull llama3
```
### Step 3: Run the Log Analyzer
SSH Brute-Force Log Analysis:
```bash
python3 soc_log_analyzer.py --log sample_logs/auth.log
```
Apache Web Exploit Log Analysis:
```bash
python3 soc_log_analyzer.py --log sample_logs/apache_access.log
```

---

## 📝 Episode Assignment
1. Clone this repository to your Kali Linux or Ubuntu environment.
2. Run soc_log_analyzer.py against /var/log/auth.log or a custom log file.
3. Verify the generated firewall mitigation rule and share your incident report in our Telegram group!

---

## ⚠️ Legal & Ethical Disclaimer
This tool and instructional material are created strictly for defensive cybersecurity operations, authorized security analysis, and educational research. Always ensure you have permission before analyzing logs or running firewall commands on production networks.
