import array
import requests
import base64
import random
import base64
from binascii import unhexlify
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

def hex():
    h = input("Enter hex string:")
    print(bytes.fromhex(h).decode('utf-8'))

def ascii():
    e = list(input('Enter Text:').encode('ascii')) 
    print(e)

def base():
    h = input("Enter base64 string:")
    base64_bytes = h.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    print(sample_string)

def byte():
    c = input("Enter base64 string:")
    hex = unhexlify(c)
    flag = base64.b64encode(hex)
    print(flag)   
   
def big():
    data=int(input("Enter string: "))
    bytes = long_to_bytes(data)
    print(bytes)
    

print ('''\033[32m

  _____  ______ _____ _______     _______ _______ ____    _______ ____   ____  _      
 |  __ \|  ____/ ____|  __ \ \   / /  __ \__   __/ __ \  |__   __/ __ \ / __ \| |     
 | |  | | |__ | |    | |__) \ \_/ /| |__) | | | | |  | |    | | | |  | | |  | | |     
 | |  | |  __|| |    |  _  / \   / |  ___/  | | | |  | |    | | | |  | | |  | | |     
 | |__| | |___| |____| | \ \  | |  | |      | | | |__| |    | | | |__| | |__| | |____ 
 |_____/|______\_____|_|  \_\ |_|  |_|      |_|  \____/     |_|  \____/ \____/|______|
                                                                                      
This tool is used to decode the flag in CTF competitions 🔑\033[36m                                                                                  
Version 1.1
 By 👻 Abdulazeez Mohammed Almashani \033[32m🇴
''')
print('''
\033[31m[01]\033[36m Hex

\033[31m[02]\033[36m Text toASCII

\033[31m[03]\033[36m Base64 to ASCII

\033[31m[04]\033[36m Hex to Base64 

\033[31m[05]\033[36m Bytes and Big Integers

\033[31m[00]\033[36m Exit
''')
chinput = input('\033[35mSelect Number : \033[39m')
if chinput == '1':
    hex()
elif chinput == '2':
    ascii()  
elif chinput == '3':
    base()
elif chinput == '4':
    byte()   
elif chinput == '5':
    big()                    
elif chinput == '00':
    print('''
    By Abdulazeez Mohammed
    ''')    