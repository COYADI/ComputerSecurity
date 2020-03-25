from pwn import *
from Crypto.Util.number import *

#r = process('./server.py')
r = remote('edu-ctf.csie.org', 10192)

r.sendlineafter('>', '1')
r.recvuntil('c = ')
c = r.recvline()
r.recvline()
r.recvuntil('n = ')
n = r.recvline()
#print(c)
#print(n)

c = long(c)
n = long(n)
bot_line = 0
top_line = n
e = 65537
base = 16

runtime = 0
while bot_line != top_line:
	r.sendlineafter('>', '2')
	c = c * pow(16, e, n)
	r.sendline(str(c))
	r.recvuntil('m = ')
	result = r.recvline()
	result = int(result)
	print(result)
	area_start_with = 0
	for i in range(16):
		if -(i * n) % 16 == result:
			area_start_with = i
	#print(area_start_with)

	bot_line, top_line = bot_line + (top_line - bot_line) * area_start_with // 16, bot_line + (top_line - bot_line) * (area_start_with + 1) // 16
	print(bot_line)
	print(top_line)
	#print(long_to_bytes(top_line))
	runtime += 1
	print(runtime)

r.close()


print(long_to_bytes(top_line))
