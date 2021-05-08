__author__ = "Akshay Joshi"

import os
import time

# Set root directory of the repo into PATH
import sys
sys.path.append('../Question_3/')

# Import python socket library & custom file to track static variables
from socket import *
from parameters import *

class Server:
    """
        Code to simulate operations of a Server.
        Operations implemented: 
            1. Connection Setup
            2. LIST_FILES
            3. Upload
            4. Download
            5. Hash Generation & Matching
    """

    def __init__(self):
        self.server_port = PORT  # Server Port
        self.server_url = URL    # Server URL
        self.commands = COMMANDS    # File Commands
        self.seperator = SEP  # Separator token for file name & file size strings
        self.buffer_size = BUFFER_CAPACITY  # Buffer size
        self.received_files_path = RECEIVED_FILES_PATH

    def send_md5_hash(self):
        # Send the generated md5 hash back to client
        self.connectSocket.send(self.hacker_cat_img_md5.encode())


    def receive_command(self):
        received = self.connectSocket.recv(self.buffer_size).decode(FORMAT)

        # Check if LIST_FILES command is received
        if received == COMMANDS[0]:
            print(f"\nCommand received: {received}\n")

            if os.listdir(self.received_files_path) == []:
                msg = "[SERVER]: No files available at the moment!"
                self.connectSocket.send(msg.encode())
                self.connectSocket.send('DONE'.encode())

            else:
                files_available = os.listdir(self.received_files_path)
                msg = "[SERVER]: Following files are available:-"
                self.connectSocket.send(msg.encode())

                for each_file in files_available:
                    self.connectSocket.send(each_file.encode())

                self.connectSocket.send('DONE'.encode())
        
        # Check if UPLOAD command is received
        elif received == COMMANDS[1]:
            print(f"\nCommand received: {received}\n")

            msg = "[SERVER]: Please send corresponding filename and filesize!"
            self.connectSocket.send(msg.encode())

            data_received = self.connectSocket.recv(self.buffer_size).decode()
            self.file_name, self.file_size = data_received.split(self.seperator)

            # Typecasting from str to int
            self.file_size = int(self.file_size)

            msg = "[SERVER]: Ready to receive the file"
            self.connectSocket.send(msg.encode())

            try:
                hacker_cat_temp_file = os.path.join(self.received_files_path, 'temp') + '.jpg'
                with open(hacker_cat_temp_file, 'wb') as hacker_cat_img:
                    while True:
                        data_bytes = self.connectSocket.recv(self.buffer_size)
                        md5().update(data_bytes)

                        # When the End of File flag is reached (which means file transfer is complete)
                        if data_bytes == 'EOF'.encode():
                            break

                        hacker_cat_img.write(data_bytes)
                    self.hacker_cat_img_md5 = md5().hexdigest()
                    hacker_cat_img.close()

                # Rename the temp file to something meaningfull
                hacker_cat_save_file = os.path.join(self.received_files_path, 
                                    self.hacker_cat_img_md5 + ';' + self.file_name[:-4] 
                                    + ';' + str(self.file_size)) + '.jpg'

                if not os.path.isfile(hacker_cat_save_file):
                    os.rename(hacker_cat_temp_file, hacker_cat_save_file)
                    hacker_cat_img.close()

                else:
                    os.remove(hacker_cat_temp_file)

            
            except Exception as e:
                print(e)

        elif received == COMMANDS[2]:
            print(f"\nCommand received: {received}\n")

            msg = "[SERVER]: Please send a file ID"
            self.connectSocket.send(msg.encode())

            # Find the file which contains the respective file ID
            file_id = self.connectSocket.recv(self.buffer_size).decode()
            for fil_name in os.listdir(self.received_files_path):
                if file_id in fil_name:
                    desired_file = fil_name

            # Open the desired image based on the file ID (first 32 chars in the filename)
            with open(os.path.join(self.received_files_path, desired_file), 'rb') as hacker_cat_img:

                # Send the data
                while True:
                    data_bytes = hacker_cat_img.read(self.buffer_size)
                    md5().update(data_bytes)

                    if not data_bytes:
                        break   # All the data sent or empty file

                    # Using sendall instead of send as this method continues to send data 
                    # from data_bytes until either all data has been sent or an error occurs.

                    # Don't need to use encode() as we are already loading the file in 'rb'
                    # mode
                    self.connectSocket.sendall(data_bytes)
                
                time.sleep(0.1)
                self.connectSocket.send('EOF'.encode())

                self.hacker_cat_img_md5 = md5().hexdigest()
                hacker_cat_img.close()
                    
    def communicate_to_client(self):
        # Create TCP socket for future connections
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        
        # Bind URL and Port to the created socket
        self.serverSocket.bind((self.server_url, self.server_port))

        # Start listening for incoming connection (1 client at a time)
        self.serverSocket.listen(1)
        print("Server is listening on port: " + str(self.server_port))

        while True:
            # Accept incoming client connection
            self.connectSocket, addr = self.serverSocket.accept()
            print("Client connected: " + str(addr))
            print("\n")

            # Receive the command & decide suitable action (ex: upload/download)
            self.receive_command()
            self.receive_command()
            
            # Send MD5 hash generated by the server
            self.send_md5_hash()
            
            self.receive_command()
            self.receive_command()
            self.send_md5_hash()

            # Close TCP connection
            self.connectSocket.close()


# Driver code
if __name__ == "__main__":
    client = Server()
    client.communicate_to_client()