#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}[*] Starting BullSploit installation...${NC}"

if ! command -v python3 &> /dev/null
then
    echo -e "${RED}[!] Python3 not found. Please install it first.${NC}"
    exit
fi

echo -e "${GREEN}[*] Creating virtual environment (venv)...${NC}"
python3 -m venv venv

echo -e "${GREEN}[*] Installing dependencies from requirements.txt...${NC}"
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
    echo -e "${GREEN}[+] Dependencies installed successfully!${NC}"
else
    echo -e "${RED}[!] requirements.txt not found!${NC}"
fi

echo -e "${GREEN}[+] Installation complete.${NC}"
echo -e "To start BullSploit, use:"
echo -e "./BullsploitFramework.py"
