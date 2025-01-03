# Automatic Penetration Testing Tool Installer

This Python script automates the installation of penetration testing tools on Debian-based Linux distributions. It provides a user-friendly interface that allows users to either install all the listed tools or choose specific ones for installation.

## Requirements

- Python 3
## Installation

Clone the repository:
```bash

git clone https://github.com/XsakesenseiX/tools-downloader.git
```
Navigate to the project directory:
```bash

cd tools-downloader
```
## Usage

Run the script:

```bash

python3 main.py
```
The script will display a list of available tools and prompt you to choose an installation option:

```bash
1. Install specific tools (comma-separated)
2. Install all tools
Enter your choice (1 or 2):
```

If you select option 1, you will be prompted to enter the names of the tools you want to install, separated by commas.
For example, to install nmap and dirsearch, you would type:
```bash
Enter the tools you want to install (comma-separated): nmap,dirsearch
```
The script will then attempt to install the specified tools.
Install all tools:

If you select option 2, the script will attempt to install all the tools listed in the script.
## Supported Tools

The script currently supports the installation of the following penetration testing tools:

- nmap
- dirsearch
- git-dumper
- hydra
- hashcat
- sqlmap
- pipx
- wpscan
- bettercap
- curl
- dumpsterdiver
- exiftool
- exploitdb
- ffuf
- metasploit
- ollydbg
- sherlock
- wireshark
- zaproxy
## Note:

This script has been tested on Debian-based systems. The installation commands may need to be modified for other Linux distributions.
Some of the listed tools may require additional dependencies. The script will attempt to install these dependencies automatically.
It is recommended to run this script with sudo privileges to ensure proper installation permissions.
Contributing

We welcome contributions to this project. If you would like to add support for a new tool, please feel free to submit a pull request.

## Disclaimer!

This script is provided for educational purposes only. The authors are not responsible for any misuse of this script or the tools it installs.