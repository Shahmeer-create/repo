#!/bin/bash
cd /home/ubuntu/myapp
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart myapp
chmod +x scripts/install_dependencies.sh
