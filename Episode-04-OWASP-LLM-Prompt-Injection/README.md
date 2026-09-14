
# Episode 04: OWASP Top 10 for LLMs — Live Prompt Injection & Defense Lab 🛡️🧪

Welcome to **Episode 4** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we explore **OWASP LLM01: Prompt Injection** and **Data Leakage**. Using Python and a local **Ollama LLM** (`llama3`), we build an interactive security laboratory (`llm_security_lab.py`) that demonstrates both **Direct Jailbreak Attacks** and **Indirect Prompt Injection (Document Poisoning)**. 

Furthermore, we implement a multi-layered defense model combining **Environment Isolation (`.env`)**, **Regex Input Guardrails**, and **Programmatic Output Sanitization Shields** to prevent sensitive API key exposure.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** OWASP Top 10 for LLMs — Live Prompt Injection Attacks & Defense Lab
* **Language:** Hindi / Hinglish

---

## 🛠️ Key Features & Laboratory Architecture

### 1. Direct Prompt Injection Sandbox (Unprotected Mode)
* Simulates direct system prompt override attacks against an internal HR Assistant (`HR-Bot`).
* Demonstrates how adversarial prompts induce LLMs to bypass system instructions and leak confidential credentials.
* **Automatic Vulnerability Detection:** Flags responses in red terminal text (`[!] VULNERABILITY DETECTED`) whenever secret API keys are leaked.

### 2. Indirect Prompt Injection (Resume Processing Demo)
* Demonstrates third-party data poisoning attacks (RAG / Document Processing Flaws).
* Processes untrusted resumes (`payloads/indirect_injection_resume.txt`) containing embedded instruction overrides to hijack the AI's execution flow.

### 3. Multi-Layered Defensive Mode
* **API Key Isolation (`.env`):** Loads operational master keys from environment variables using `python-dotenv` instead of hardcoding credentials in source files.
* **Input Guardrails (`input_sanitizer()`):** Uses regex matching to intercept blacklisted prompt injection tokens (`ignore previous instructions`, `developer mode`, `system prompt`).
* **Programmatic Output Shielding (`sanitize_output()`):** A code-level fallback layer that intercepts LLM outputs and redacts exposed keys to `[REDACTED_API_KEY_SHIELD]`.

---

## 🚀 Quick Setup Instructions
### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```
(On Kali Linux with PEP 668 restriction, use pip3 install -r requirements.txt --break-system-packages)

### Step 2: Configure Environment Variables
Copy .env.example to .env:
```bash
cp .env.example .env
```
### Example .env configuration:
Code snippet
```
OLLAMA_HOST=http://localhost:11434
LLM_API_KEY=VYASPEETH_SECRET_KEY_2026
```
### Step 3: Run the Security Lab
Launch the interactive CLI lab:
```bash
python3 llm_security_lab.py
```
## 📝 Episode Assignment
1. Clone this repository to your local environment.
2. Create a new prompt payload in payloads/indirect_injection_resume.txt that attempts to alter the resume summary rating.
3. Test option [1] vs option [3] and share your terminal screenshots in our Telegram group!

## ⚠️ Legal & Ethical Disclaimer
This tool and instructional material are designed strictly for authorized security research, LLM application auditing, and educational purposes. Always ensure proper authorization before auditing third-party LLM endpoints.
