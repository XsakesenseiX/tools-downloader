Automatic Penetration Testing Tool Installer

This Python script automates the installation of penetration testing tools on Debian-based Linux distributions. It provides a user-friendly interface that allows users to either install all the listed tools or choose specific ones for installation.

Requirements

Python 3
Installation

Clone the repository:
Bash

git clone https://github.com/your-username/automatic-penetration-testing-tool-installer.git
Navigate to the project directory:
Bash

cd automatic-penetration-testing-tool-installer
Install the required libraries:
Bash

pip install os
Usage

Run the script:
Bash

python main.py
The script will display a list of available tools and prompt you to choose an installation option:

1. Install specific tools (comma-separated)
2. Install all tools
Options

Install specific tools (comma-separated):

If you select this option, you will be prompted to enter the names of the tools you want to install, separated by commas.
For example, to install nmap and dirsearch, you would type:
Enter the tools you want to install (comma-separated): nmap,dirsearch
The script will then attempt to install the specified tools.
Install all tools:

If you select this option, the script will attempt to install all the tools listed in the script.
Supported Tools

The script currently supports the installation of the following penetration testing tools:

nmap
dirsearch
git-dumper
hydra
hashcat
sqlmap
pipx
wpscan
bettercap
curl
dumpsterdiver
exiftool
exploitdb
ffuf
metasploit
ollydbg
sherlock
wireshark
zaproxy
Note:

This script has been tested on Debian-based systems. The installation commands may need to be modified for other Linux distributions.
Some of the listed tools may require additional dependencies. The script will attempt to install these dependencies automatically.
It is recommended to run this script with sudo privileges to ensure proper installation permissions.
Contributing

We welcome contributions to this project. If you would like to add support for a new tool, please feel free to submit a pull request.

Disclaimer

This script is provided for educational purposes only. The authors are not responsible for any misuse of this script or the tools it installs.