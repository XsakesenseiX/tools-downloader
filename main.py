import os

TOOLS = {
    "nmap": [
        "sudo apt-get update",
        "sudo apt-get install nmap -y"
    ],
    "dirsearch": [
        "git clone https://github.com/maurosoria/dirsearch.git",
        "cd dirsearch && pip install -r requirements.txt"
    ],
    "git-dumper": [
        "pip install git-dumper",
        "echo 'Git-Dumper installed successfully!'"
    ],
    # Add more tools as needed
}



import os

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