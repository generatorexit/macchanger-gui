#!/usr/bin/sh

echo "[+] Installing Requirements..."
pip3 install tkintertable
sudo apt-get install python3-tk
echo "[+] tkintertable installed successfully..."
echo "[+] Starting gui..."
sleep 1
sudo python3 macchanger-gui.py