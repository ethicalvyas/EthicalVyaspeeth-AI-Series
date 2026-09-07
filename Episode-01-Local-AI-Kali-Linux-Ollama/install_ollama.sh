#!/bin/bash
# ================================================================= #
# Script Name: install_ollama.sh                                    #
# Channel: Ethical Vyaspeeth                                        #
# Description: Automated Setup Script for Episode 1                 #
# ================================================================= #

echo "[+] Updating Kali Linux repositories..."
sudo apt update -y

echo "[+] Installing Ollama..."
curl -fsSL https://ollama.com/install.sh | sh

echo "[+] Checking Ollama Service Status..."
if systemctl is-active --quiet ollama; then
    echo "[+] Ollama is running successfully!"
else
    echo "[!] Starting Ollama service..."
    sudo systemctl start ollama
fi

echo "[+] Pulling default Llama3 model (This may take a few minutes)..."
ollama pull llama3

echo "[+] Setup complete! Run 'ollama run llama3' to start your local AI."
