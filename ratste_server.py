#!/usr/bin/env python

""" 
ratste's server component.

ratste is a basic general purpose multi-platform Remote Access Tool written in
Python3.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "https://github.com/StefanoRatto/"
__license__ = "GPLv3"
__version__ = "1.0.0"

import socket
import sys
import base64
import logging
import time
import datetime

try:
    LHOST = str(sys.argv[1])
    LPORT = int(sys.argv[2])
except:
    print 'ratste > usage: ./ratste_server.py <local_ip> <local_port>'
    print 'ratste > using default host (127.0.0.1) and port (7261)' 
    LHOST = '127.0.0.1'
    LPORT = 7261

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
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_socket.bind((LHOST, LPORT))
        tcp_socket.listen(10)
    except:
        print 'ratste > network error, exiting...'
        sys.exit(1)

    log_file = ('logs/ratste-{}_UTC.log'.
        format(datetime.datetime.utcnow()).replace(" ", "_"))
    logging.Formatter.converter = time.gmtime
    logging.basicConfig(format='%(asctime)s.%(msecs)03d_UTC %(message)s', 
        datefmt="%Y-%m-%d_%H:%M:%S", filename=log_file, level=logging.DEBUG)

    print 'ratste > server listening on {}:{}'.format(LHOST, LPORT)
    logging.debug('ratste > server listening on {}:{}'.format(LHOST, LPORT))
    print 'ratste > session log file: {}'.format(log_file)
    print 'ratste > type "quit" or ctrl-c to exit'
    logging.debug('ratste > type "quit" or ctrl-c to exit')

    connection, _ = tcp_socket.accept()

    connection.send(encode('client_discovery'))
    client_info = decode(connection.recv(4096).rstrip())
    platform, hostname, user, version, arch = client_info.split('|')

    print 'ratste > check-in by {}@{}'.format(user, hostname)
    logging.debug('ratste > check-in by {}@{}'.format(user, hostname))
    print 'Platform: {}'.format(platform)
    logging.debug('Platform: {}'.format(platform))
    print 'Version: {}'.format(version)
    logging.debug('Version: {}'.format(version))
    print 'Architecture: {}\n'.format(arch)
    logging.debug('Architecture: {}\n'.format(arch))

    while True:
        command = raw_input('ratste ~ {}@{} > '.format(user, 
            hostname)).rstrip()
        logging.debug(str('ratste ~ {}@{} > {}'.format(user, 
            hostname, command)).rstrip())

        # allow noop
        if command == '':
            continue

        # send command to client
        connection.send(encode(command))

        # stop server
        if command == 'quit':
            tcp_socket.close()
            sys.exit(0)

        data = decode(connection.recv(4096))
        print data
        logging.debug(data)

if __name__ == '__main__':
    main()