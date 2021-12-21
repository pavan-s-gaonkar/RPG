# RPG - Random Password Generator

## Introduction
This is a standalone tool which can generate 
random passwords based on your configuration. 
It does not store nor use internet to upload the passwords

## Features
This tool has features:
1. Generate random password based on random package from python standard library.
2. Password can consist of alphabets (lower case and upper case), numbers and symbols from the ASCII table.
3. Password can be configured to avoid numbers and symbols at the start and end of the password
4. Password can be copied into clipboard using a single click so that it can be used outside the application.

## Developer commands
### Prerequisites
- Windows 10
- Python 3.10.1
- PyQt5
- QtCreator
- Pycharm(optional)

### Commands
- The following command is to be used everytime we change the Gui.ui file
  - pyuic5 artifact\gui.ui -o Gui.py
- The following command is to be used to build the executable
  - pyinstaller .\RPG.spec .\RPG.py