import os

TOOLS = {
    "nmap": [
        "sudo apt-get update",
        "sudo apt-get install nmap -y"
    ],
    "dirsearch": [
        "git clone https://github.com/maurosoria/dirsearch.git",
        "cd dirsearch && pip install -r requirements.txt",
        "cd"
    ],
    "git-dumper": [
        "pip install git-dumper",
        "echo 'Git-Dumper installed successfully!'"
    ],
    "hydra": [
        "sudo apt-get update",
        "sudo apt-get install hydra -y"
    ],
    "hashcat": [
        "sudo apt-get update",
        "sudo apt-get install hashcat -y"
    ],
    "sqlmap": [
        "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev",
        "cd sqlmap-dev && pip3 install -r requirements.txt",
        "cd"
    ],
    "pipx": [
        "pip install pipx",
        "echo 'pipx' installed successfully!"
    ],
    "wpscan": [
        "sudo apt-get update",
        "sudo apt-get install rubygems",
        "gem install wpscan"
    ],
    "bettercap": [
        "sudo apt-get update",
        "sudo apt-get install bettercap"
    ],
    "netcat": [
        "sudo apt-get update",
        "sudo apt-get install netcat"
    ],
    "curl": [
       "sudo apt-get update",
        "sudo apt-get install curl"
    ],
    "dumpsterdiver": [
        "sudo apt-get update",
        "sudo apt-get install dumpsterdiver"
    ],
    "exiftool": [
       "sudo apt-get update",
        "sudo apt-get install exiftool"
    ],
    "exploitdb": [
        "sudo apt-get update",
        "sudo apt-get install exploitdb"
    ],
    "ffuf": [
       "sudo apt-get update",
        "sudo apt-get install ffuf"
    ],
    "metasploit": [
       "sudo apt-get update",
        "sudo apt-get install metasploit-framework"
    ],
    "ollydbg": [
       "sudo apt-get update",
        "sudo apt-get install ollydbg"
    ],
    "sherclock": [
       "sudo apt-get update",
        "sudo apt-get install sherlock"
    ],
    "wireshark": [
        "sudo add-apt-repository ppa:wireshark-dev/stable",
        "sudo apt-get update",
        "sudo apt-get install bettercap"
    ],
    "zap-proxy": [
       "sudo apt-get update",
        "sudo apt-get install zaproxy"
    ],
}



class ToolInstaller:
    def __init__(self, tool_name, install_commands):
        self.tool_name = tool_name
        self.install_commands = install_commands

    def install(self):
        print(f"Installing {self.tool_name}...")
        for command in self.install_commands:
            os.system(command)
        print(f"{self.tool_name} installed successfully.")
        
        
class NmapInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("nmap", TOOLS["nmap"])

class DirsearchInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("dirsearch", TOOLS["dirsearch"])

class GitDumperInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("git-dumper", TOOLS["git-dumper"])
        
class HydraInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("hydra", TOOLS["hydra"])
        
class HashCatInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("hashcat", TOOLS["hashcat"])

class SqlMapInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class PipxInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class WpScanInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class betterCapInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class NetCatInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class CurlInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class DumpsterDiverInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])

class ExifToolInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class ExploitDBInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class FFUFInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class MetaSploitInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class OllyDbgInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class SherlockInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class WireSharkInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
class ZaproxyInstaller(ToolInstaller):
    def __init__(self):
        super().__init__("sqlmap", TOOLS["sqlmap"])
        
        
class PentestToolsManager:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        self.tools.append(tool)

    def install_all(self):
        for tool in self.tools:
            tool.install()
            
            
def main():
    print("Available tools:")
    for tool in TOOLS:
        print(f"- {tool}")

    selected_tools = input("Enter the tools you want to install (comma-separated): ").strip().split(",")
    selected_tools = [tool.strip() for tool in selected_tools]

    manager = PentestToolsManager()

    for tool in selected_tools:
        if tool in TOOLS:
            manager.add_tool(ToolInstaller(tool, TOOLS[tool]))
        else:
            print(f"Tool '{tool}' not found. Skipping.")

    manager.install_all()

if __name__ == "__main__":
    main()