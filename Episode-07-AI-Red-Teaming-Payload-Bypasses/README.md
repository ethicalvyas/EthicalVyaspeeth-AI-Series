# Episode 07: AI for Red Teaming: Crafting Bypasses & Custom Payloads 🎯🛡️

Welcome to **Episode 7** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we leverage local **Ollama LLMs** to build a context-aware **Red Team Payload & Bypass Builder**. This tool generates obfuscated reverse shells, WAF-bypass web payloads (SQLi, XSS, Command Injection), and PowerShell execution vectors tailored to bypass string detection and static input filters.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** AI for Red Teaming — Crafting Bypasses & Custom Payloads
* **Language:** Hindi / Hinglish

---

## 🛠️ Key Features
* 🎭 **Context-Aware Obfuscation:** Generates payloads tailored to specific OS targets (Linux/Windows) and execution environments (Bash, PowerShell, Web).
* 🛡️ **Filter & WAF Evasion:** Accepts custom constraints (e.g., "no spaces", "avoid alert keyword", "base64 encoding").
* 🔒 **100% Private & Local:** Keeps exploit development logic completely offline on your local Kali Linux machine.
* 📝 **Automated Logging:** Exports structured Markdown reports with listener configurations into `outputs/`.

---

## 🚀 Quick Setup Instructions

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```
(On Kali Linux with active PEP 668 restriction, use pip3 install ollama --break-system-packages)
### Step 2: Ensure Ollama Service is Active
```bash
systemctl status ollama
ollama pull llama3
```
### 💡 Usage Examples
Example 1: Obfuscated Linux Reverse Shell (Base64 Bypass)
```bash
python3 redteam_payload_builder.py --type reverse_shell --target linux --ip 10.0.2.15 --port 4444 --bypass "encode with base64 to avoid spaces and special characters"
```
Example 2: WAF Bypass XSS Payload (Avoiding <script> & alert)
```bash
python3 redteam_payload_builder.py --type xss_bypass --target web --bypass "avoid script tag and do not use alert keyword"
```

---

## 📝 Episode Assignment
1. Clone this repository on your Kali Linux environment.
2. Run redteam_payload_builder.py to generate an obfuscated Windows PowerShell reverse shell using -EncodedCommand.
3. Set up a local Netcat listener (nc -lvnp 4444) and verify your payload execution!

---

## ⚠️ Legal & Ethical Disclaimer
This tool and instructional material are designed strictly for authorized Red Team testing, security evaluation, and educational research. Executing unauthorized payloads against target systems without consent is strictly illegal.
