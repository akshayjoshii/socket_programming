# File Transfer Simulation with MD5 Hash Check - Socket Programming

![Welcome](server_received_files/asset.png)

**The application respects the following protocol:**

1. Handshake Phase:

    * The server awaits for a new connection.
    * The client connects to the server.
    * The server expects one of the following commands from the client:

        > LIST FILES: The client sends the “LIST FILE” command in ASCII and awaits from the server a reply with a list of files that are available for download. The server’s reply format is “file1 id;file1 name;file1 size (newline) file2 id;file2 name;file2 size (newline) ...” or a custom message in case there are no files (for example: “No files available at the moment”)
        >
        >
        > DOWNLOAD: The client sends the “DOWNLOAD” command in ASCII. The server will reply, asking for a “file id” of the file that should be downloaded to the client. Then, the client sends the “file id” and awaits for the file as byte-stream.
        >
        >
        > UPLOAD: The client sends the “UPLOAD” command in ASCII. The server will reply, asking for the “File Name” and “File Size”. The client sends the file details in the following format “file_name;file size” in ASCII. Once the server receives the file details, it will reply that it’s ready to receive the file as byte-stream. Only after this reply the client will start sending the file as byte-stream.

2. Verification Phase:  

> To check whether an uploaded or downloaded file was transferred intact, a verification is required. To achieve this, both the server and client each generate an MD5 hash of the file. When uploading, the server will send its generated hash to the client for comparison. When downloading, you can utilize the “file id” as the MD5 hash.

**Simulation order is as follows:**

1. Start the server (listens to clients).
2. Start the client.
3. The client connects to the server.
4. The client sends a 'LIST_FILES' command.
5. The server will reply with a message that there are no files at the moment.
6. The client then sends the 'UPLOAD' command.
7. The server asks for the filename and filesize.
8. The client sends the file details (for example: “my_file.jpg;123456”).
9. The server sends a notification message (for example: “ready to receive a file”).
10. The client starts sending the file.
11. The server receives the file and generates the MD5 Hash (the hash will be used as file id).
12. The server saves the received file (writes the received data into a file).
13. The server sends the MD5 hash to the client.
14. The client generates his own MD5 hash of the file and compares it to the one received from the server. In case of a match the client will print a “Success” message, otherwise a “Fail” message will be printed.
15. The client sends again a 'LIST_FILES' command.
16. The server will reply with the available files (in this case: “file id;my_file.jpg;12345”, where file id is the MD5 hash of the file).
17. The client sends a 'DOWNLOAD' command.
18. The server asks for a file id (for example: “Please send a file ID”).
19. The client sends the file id extracted from the previous LIST_FILES command.
20. The server sends the file to the client.
21. The client receives the file and generates the MD5 hash.
22. The client disconnects from the server.

## Image used to simulate the file transfer

![Hacker Cat](hacker_cat.jpg)

## Data Networks Team

1. Akshay Joshi
2. Jan Stieling

## Requirements

All the below entries are core packages within **Python 3**, so no need to install them from PIP/APT

1. os
2. time
3. socket
4. hashlib

## Execution Steps

1. Switch to 'Question 3' directory i.e., Run the command (in a terminal): 'cd Question_3'.
2. Run Server: 'python server.py'.
3. Run Client: 'python client.py'.

### Note

* Attached log.txt of results for both Client & Server code (after test runs).

### Author

[Akshay Joshi](https://akshayjoshi.tech)
