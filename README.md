![ratste_logo](./images/ratste.png)

# ratste

General purpose cross platform Remote Access Tool written in Python3.

## System Requirements

Both client and server components require Python 3, Standard Library only.

## Installation

Clone the GitHub repo and move into the ratste `$HOME` folder with:

```Bash
git clone https://github.com/StefanoRatto/rat-by-raste.git
cd ratste
export RATSTE_HOME=$(pwd)
```

The server and client components are single Python `.py` files and can be moved to and executed from anywhere in the file system.

The client component must be delivered to and invoked on the target machine(s) with the help of strategies and tools that are outside of the scope of the tool itself.

## Usage

### Server component:

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

### Client component:

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



## Compiled (Native) Client Executables

Native client executables can be created with [PyInstaller](http://www.pyinstaller.org/) on all supported platforms (Microsoft Windows, Mac OS X, Linux). 

This process has been tested and validated on all three platforms and it is recommended to run PyInstaller from within the `$RATSTE_HOME/bin` folder:

```Bash
cd $RATSTE_HOME
pyinstaller --onefile ../ratste_client.py
```

Once PyInstaller has worked its magic, the platform native single file executable can be found in the `$RATSTE_HOME/bin/dist` folder.

## Encoding and obfuscation

By design, `base64` encoding of all communications between client and server has been preferred over encryption.

## Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Legal Disclaimer

Usage of this tool to interact with targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. Only use for educational purposes.

## TODOs

* Client
  - Develop a compiled client (C/C++, Golang, C# etc)
  - Leverage OOP
  - Obfuscate or encrypt client side code
  - Capable of traversing a web proxy

* Server
  - A mechanism to queue tasks for clients
  - Long term storage of commands and subsequent results
  - Leverage OOP
  - Database Backend