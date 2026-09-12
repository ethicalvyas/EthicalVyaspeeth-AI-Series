# Episode 09: Deepfake & AI Phishing Forensic Analysis 🔍🕵️‍♂️

Welcome to **Episode 9** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we build an automated **Phishing & Deepfake Forensic Analyzer** using Python and a local **Ollama LLM**. This tool inspects raw email header metadata (`.eml`), validates SPF/DKIM/DMARC alignment, identifies typosquatting phishing links, and evaluates voice phishing (vishing) call transcripts for AI-generated social engineering patterns.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** Deepfake & AI Phishing Forensic Analysis
* **Language:** Hindi / Hinglish

---

## 🛠️ Key Features
* 📧 **Header Metadata Inspection:** Checks SPF/DKIM/DMARC authentication status and detects `Return-Path` vs. `From` header spoofing.
* 🔗 **Link & Typosquatting Isolation:** Pinpoints hidden redirect domains, Cyrillic Unicode tricks, and phishing targets.
* 🎙️ **Deepfake & Synthetic Marker Analysis:** Evaluates voice call transcripts and AI-crafted text for social engineering pressure tactics.
* 🔒 **100% Offline & Private:** Analyzes sensitive corporate email logs locally without exposing confidential data to cloud APIs.

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
### Step 3: Run the Forensic Analyzer
Email Spoofing & Header Analysis:
```bash
python3 phishing_forensics_analyzer.py --email sample_emails/fake_ceo_urgent.eml
```
Deepfake Vishing Transcript Analysis:
```bash
python3 phishing_forensics_analyzer.py --email sample_emails/deepfake_vishing_transcript.txt
```

---

## 📝 Episode Assignment
1. Clone this repository on your Kali Linux environment.
2. Export raw headers from any real spam/phishing email in your inbox.
3. Pass the sample into phishing_forensics_analyzer.py and share your forensic report in our Telegram group!

---

## ⚠️ Legal & Ethical Disclaimer
This tool and instructional material are designed strictly for authorized digital forensics, incident response, and educational research. Always ensure proper authorization before auditing or analyzing third-party message logs.
