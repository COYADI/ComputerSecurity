#!/usr/bin/env python3
from sympy import *
import random
import os

def op1(p, s):
    return sum([i * j for i, j in zip(s, p)]) % 256

def revop2(m, k):
    return bytes([i ^ j for i, j in zip(m, k)])

def revop3(m, p):
    result = [None]*len(m)
    for i in range(len(m)):
        result[p[i]] = m[i]
    return bytes(result)

def revop4(m, s):
    result = [None]*len(m)
    for x in range(len(m)):
        result[x] = s.index(m[x])
#    print(result)    
    return bytes(result)

'''
Linear Feedback Shift Register
'''
def stage0(m):
    random.seed('oalieno')
    p = [int(random.random() * 256) for i in range(16)]
    s = [int(random.random() * 256) for i in range(16)]
    c = b''
    for x in m:
        k = op1(p, s)
        c += bytes([x ^ k])
        s = s[1:] + [k]
    return c

'''
Substitution Permutation Network
'''
def stage1(m):
    random.seed('oalieno')
    k = [int(random.random() * 256) for i in range(16)]
    p = [i for i in range(16)]
    random.shuffle(p)
    s = [i for i in range(256)]
    random.shuffle(s)

    c = m
    for i in range(16):
  #      print(m, "YASSSSSSSSSSSSSSSSSS")
        c = revop4(c, s)
        c = revop3(c, p)
        c = revop2(c, k)
    return c

def decrypt(m, key):
    stage = [stage0, stage1]
    for i in map(int, f'{key:08b}'):
        m = stage[abs(i - 1)](m)
    return m

if __name__ == '__main__':
#    flag = open('flag', 'rb').read()
 #   assert(len(flag) == 16) 
  #  key = open('key', 'rb').read()
   # assert(E ** ( I * pi ) + len(key) == 0) #len(key) = 1
    #open('cipher', 'wb').write(encrypt(flag, int.from_bytes(key, 'little')))
    for i in range(256):
        key = i
        result = open('cipher', 'rb').read()
        print(decrypt(result, key))
    os.system("pause")
