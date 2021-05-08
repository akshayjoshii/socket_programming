__author__ = "Akshay Joshi"

import os
from hashlib import md5

# Set root directory of the repo into PATH
import sys
sys.path.append('../Question_3/')

# Delimiter between filename & filesize strings
SEP = ";"

# Encoding/Decoding format to transform str to byte representation
FORMAT = "ascii"

# Server Open PORT & URL
PORT = 9999
URL = "localhost"

BUFFER_CAPACITY = 4096

# Commands stored in a list
COMMANDS = ['LIST_FILES', 'UPLOAD', 'DOWNLOAD']

# Check if the "server_received_files" directory is present. If not, create it
# before proceeding further (important)
RECEIVED_FILES_PATH = os.path.join("server_received_files")

if not os.path.isdir(RECEIVED_FILES_PATH):
    os.makedirs(RECEIVED_FILES_PATH)


"""
Generate ASCII values for the characters in above commands (not required as we 
can instead use the encode & decode method with 'ascii' format directly - 
realized this later, but anyway i'll leave this in here).
"""
COMMANDS_DEPRECATED = {'LIST_FILES':[], 'UPLOAD':[], 'DOWNLOAD':[]}

for key in COMMANDS_DEPRECATED.keys():
    COMMANDS_DEPRECATED[key] = [ord(char) for char in key]