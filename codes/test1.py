target = [0x0F, 0x09, 0x02, 0x0C, 0xF8, 0xFA, 0x30, 0xF0, 0x22, 0x22, 0xFA, 0x30, 0xF0, 0x22, 0x22, 0xFA, 0x30, 0xF0, 0x22, 0x22, 0x35, 0xED, 0xE4, 0xF6, 0xFA, 0xE4, 0xEC, 0x35, 0xE1, 0x22, 0x22, 0xC6]
result = []

for i in range(len(target)):
	result.append((target[i]^0x66)-0x23)
	print(chr(result[i]))
