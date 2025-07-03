#!/usr/bin/env python3

import os
import sys
import subprocess

def run_cmd(command, output_file=None):
    print(f"[+] Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if output_file:
        with open(output_file, "w") as f:
            f.write(result.stdout)
    return result.stdout

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 autorecon.py <target-ip>")
        sys.exit(1)

    target = sys.argv[1]
    out_dir = f"output/{target}"
    os.makedirs(out_dir, exist_ok=True)

    # Nmap Scan
    run_cmd(f"nmap -sV -oN {out_dir}/nmap.txt {target}")

    # Check for ports and run additional tools
    with open(f"{out_dir}/nmap.txt", "r") as f:
        nmap_data = f.read()
        if "139/tcp" in nmap_data or "445/tcp" in nmap_data:
            run_cmd(f"enum4linux -a {target}", f"{out_dir}/enum4linux.txt")
        if "80/tcp" in nmap_data or "443/tcp" in nmap_data:
            run_cmd(f"gobuster dir -u http://{target} -w /usr/share/wordlists/dirb/common.txt", f"{out_dir}/gobuster.txt")

if __name__ == "__main__":
    main()
