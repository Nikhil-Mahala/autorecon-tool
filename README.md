📝 Complete README.md (for AutoRecon Tool)

    # 🔍 AutoRecon Tool

    A Python-based automated reconnaissance script for red teamers and CTF players. It scans a target IP using Nmap and runs service-specific enumeration tools like `enum4linux` and `gobuster` based on discovered ports.

    ---

    ## 🚀 Features

    - Runs Nmap with version detection
    - Automatically launches:
    - enum4linux (on port 139/445)
    - gobuster (on port 80/443)
    - Saves output to folders for logging
    - Simple CLI interface for easy targeting
    ---
    ## 📦 Requirements

    - Python 3
    - nmap
    - enum4linux
    - gobuster

    Install them via:
    ```bash
    sudo apt install nmap gobuster enum4linux



📁 Installation

    -git clone https://github.com/Nikhil-Mahala/autorecon-tool.git
    -cd autorecon-tool




💻 Usage

    -python3 autorecon.py <target-ip>



📂 Output Structure

    output/192.168.1.10/
    ├── nmap.txt          ← Nmap full scan
    ├── enum4linux.txt    ← Only if SMB ports found
    ├── gobuster.txt      ← Only if web server detected 




✍️ Author

    Made with ❤️ by Nikhil Mahala
    Cybersecurity learner & red teamer in training
    Feel free to fork this repo or contribute.