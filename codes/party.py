import requests
import urllib.request
import urllib.parse
import urllib
import base64
import sys
import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

cipher_undecode = 'TLTfjOSKuooU481HiIHtOGG0QupkvgaRT9CO4Pb7y2OQtVLIuwPeZbrfL0lIcnu9CTU2VNLtZjyZDCT6Dy%2BtaV9vd03zYF%2B00SQHzV8Rc%2F2vO0mzORx0qWuNfPvjv7lW'
cipher = list(map(int, base64.b64decode(urllib.parse.unquote(cipher_undecode))))
print(cipher)

base = 16
blocks = int(len(cipher) / base)
middle = cipher.copy()
result = []
flag = []
temp = 0

for i in range(blocks):
	for j in range(base):
		for k in range(256):
			middle[len(middle) - j - base - 1] = k
			temp = 0
			#print(middle)
			#print(k)
			cookies = {'FLAG':  urllib.parse.quote(base64.b64encode(bytes(middle))), 'PHPSESSID': 'iblvei8djevkg1u8fj9sd72en7'}
			r = requests.post('https://edu-ctf.csie.org:10190/party.php', cookies=cookies,  verify=False)
			#print(r.text)
			if 'Your flag seems strange @@... okay....' in r.text:
				temp = middle[len(middle) - j - base - 1] ^ cipher[len(middle) - j - base - 1]
				print(middle[len(middle) - j - base - 1], cipher[len(middle) - j - base - 1])  #test
				result.insert(0, temp)
				print(result)
				break
			elif k == 255:
				print('not found')
				middle[len(middle) - j - base - 1] = cipher[len(middle) - j - base - 1]###
				temp = middle[len(middle) - j - base - 1]
				result.insert(0, temp)###
				print(result)
				#sys.exit()
		print('a number found!')
		for q in range(j + 1):
			middle[len(middle) - q - base - 1] ^= ((j + 1) ^ (j + 2))
			#print(middle)  #test		
		print(middle)
	for p in range(base):
		flag.insert(0, middle[len(middle) - p - base - 1] ^ cipher[len(middle) - p - base - 1])
	print(flag)
	middle = cipher.copy()
	for q in range(base * (i + 1)):
		middle.pop()
	if not middle:
		break

print(flag)
for i in range(len(flag)):
	flag[i] ^= 0x10
print(map(chr, flag))
