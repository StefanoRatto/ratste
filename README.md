![ratste_logo](./images/ratste.png)

# ratste
General purpose Remote Access Tool written in Python3.

...WIP...

### Client
* Requirements
  - Run on Windows, Linux, or MacOS
  - Developed in Python 3
  - Use only Python Modules in Standard Library only
* Features
  - A mechanism to retrieve commands from the Server
  - A mechanism to execute retrieved commands
  - A mechanism to deliver the command results back to the Server
* Extra Mile
  - Develop a compiled client (C/C++, Golang, C# etc)
  - Leverage OOP
  - Obfuscate or encrypt client side code
  - Obfuscate or encrypt command & control traffic
  - Capable of traversing a web proxy

### Server
* Requirements 
  - Run on Linux
  - Developed in Python 3
  - Use only Python Modules in Standard Library only
* Features
  - A mechanism to queue tasks for clients
  - A mechanism to deliver commands to a client
  - A mechanism to display results of a command returned by the client
  - Long term storage of commands and subsequent results
* Extra Mile
  - Leverage OOP
  - Configurable Server
    + Bind port
    + Bind IP
    + Database Backend

## System Requirements

Both client and server components require Python 3.

## Installation

...WIP...

```Bash
git clone https://github.com/StefanoRatto/rat-by-raste.git
```

## Usage

...WIP...

## Licensing

The tool is licensed under the [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Scrapbook

* https://null-byte.wonderhowto.com/how-to/program-your-own-little-rat-part-1-getting-server-working-0167490/
* https://dev.to/tman540/simple-remote-backdoor-with-python-33a0
* https://github.com/yed3926/basicRAT
* https://github.com/awesome-security/basicRAT
