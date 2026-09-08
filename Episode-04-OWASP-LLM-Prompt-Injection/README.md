# Episode 04: OWASP Top 10 for LLMs — Live Prompt Injection Attacks 🛡️🤖

Welcome to **Episode 4** of the **AI for Cybersecurity: Zero to Hero** series by **Ethical Vyaspeeth**!

In this episode, we take a hands-on look at the **OWASP Top 10 for Large Language Model Applications**, specifically focusing on **LLM01: Prompt Injection** (both Direct Jailbreaking and Indirect Prompt Injection). We run practical injection attacks against a local **Ollama** AI instance and build Python-based defensive guardrails to mitigate the risk.

---

## 📺 Episode Overview
* **Channel:** Ethical Vyaspeeth
* **Series:** AI for Cybersecurity: Zero to Hero
* **Topic:** OWASP Top 10 for LLMs — Live Prompt Injection Attacks & Defenses
* **Language:** Hindi / Hinglish

---

## 🎯 Key Concepts Covered
1. **LLM01: Direct Prompt Injection (Jailbreaking):** Bypassing system prompts using persona overrides, roleplay scenarios, and instruction hijacking.
2. **LLM01: Indirect Prompt Injection:** Exploiting AI applications that process untrusted external data (PDFs, resumes, web scrapers) to execute hidden malicious instructions.
3. **LLM02: Insecure Output Handling:** Risks associated with executing raw LLM outputs directly in terminal scripts or web applications.
4. **Defensive Guardrails:** Building regex input sanitization, token blacklists, and structural prompt isolation in Python.

---

## 🚀 Quick Setup Instructions

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
```
(On Kali Linux with active PEP 668, use pip3 install ollama --break-system-packages)

### Step 2: Run the Security Lab
```Bash
python3 llm_security_lab.py
```
---

## 💡 How to Test in the Lab
1. Option 1 (Direct Jailbreak): Test direct payload overrides from payloads/direct_jailbreaks.txt against HR-Bot.
2. Option 2 (Indirect Injection): Watch HR-Bot process payloads/indirect_injection_resume.txt and hijack the response summary.
3. Option 3 (Defensive Guardrails Active): Test how input filtering blocks malicious patterns before reaching the LLM engine.
---

## 📝 Episode Assignment
1. Clone this repository onto your local system or Kali Linux environment.
2. Run llm_security_lab.py and craft a novel jailbreak prompt that bypasses default system constraints in Option 1.
3. Enhance the input_sanitizer() function in llm_security_lab.py to detect encoded inputs (e.g., Base64-encoded injection strings).
---

## ⚠️ Legal & Ethical Disclaimer
This code and educational material are strictly intended for security research, defense evaluation, and educational testing in local lab environments. Unauthorized testing against third-party production AI services without consent is illegal.
