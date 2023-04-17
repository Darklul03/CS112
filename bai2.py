import os
import math
import numpy as np
from random import randint
test_num = 100
test_name = "Modulo"


def solve(type, a, b, c):
    if type == 1:
        return a*b % c
    else:
        lcm = b*c//math.gcd(b, c)
        cnt = a//lcm
        mi = min(b, c)
        ans = cnt*mi-1+min(a-cnt*lcm+1, mi)
        return ans


def generate_constraint_1(id):
    if not os.path.isdir("./"+test_name+"/test"+id):
        os.mkdir("./"+test_name+"/test"+id)
    fi = open("./"+test_name+"/test"+id+"/Modulo.inp", "w")
    fo = open("./"+test_name+"/test"+id+"/Modulo.out", "w")
    q = randint(1,10**5)
    if id=="20":
        q=10**5
    fi.write(str(q)+'\n')
    for _ in range(q):
        type = 1
        a = randint(1,10**9)
        b = randint(1,10**9)
        c = randint(1,10**9)
        fi.write(str(type)+" "+str(a)+" "+str(b)+" "+str(c)+'\n')
        ans = solve(type, a, b, c)
        fo.write(str(ans)+'\n')



def generate_constraint_2(id):
    if not os.path.isdir("./"+test_name+"/test"+id):
        os.mkdir("./"+test_name+"/test"+id)
    fi = open("./"+test_name+"/test"+id+"/Modulo.inp", "w")
    fo = open("./"+test_name+"/test"+id+"/Modulo.out", "w")
    q = randint(1,10**3)
    if id=="40":
        q=10**3
    fi.write(str(q)+'\n')
    for _ in range(q):
        type = 2
        a = randint(1,10**4)
        b = randint(1,10**2)
        c = randint(1,10**2)
        while max(b, c) > a:
            a = randint(1,10**4)
        fi.write(str(type)+" "+str(a)+" "+str(b)+" "+str(c)+'\n')
        ans = solve(type, a, b, c)
        fo.write(str(ans)+'\n')



def generate_constraint_3(id):
    if not os.path.isdir("./"+test_name+"/test"+id):
        os.mkdir("./"+test_name+"/test"+id)
    fi = open("./"+test_name+"/test"+id+"/Modulo.inp", "w")
    fo = open("./"+test_name+"/test"+id+"/Modulo.out", "w")
    q = randint(1,10**5)
    if id=="60":
        q=10**5
    fi.write(str(q)+'\n')
    for _ in range(q):
        type = randint(1, 2)
        a = randint(1,10**9)
        b = randint(1,10**5)
        c = randint(1,10**5)
        while max(b, c) > a:
            a = randint(1,10**9)
        fi.write(str(type)+" "+str(a)+" "+str(b)+" "+str(c)+'\n')
        ans = solve(type, a, b, c)
        fo.write(str(ans)+'\n')



def generate_constraint_4(id):
    if not os.path.isdir("./"+test_name+"/test"+id):
        os.mkdir("./"+test_name+"/test"+id)
    fi = open("./"+test_name+"/test"+id+"/Modulo.inp", "w")
    fo = open("./"+test_name+"/test"+id+"/Modulo.out", "w")
    q = randint(1,10**5)
    if id=="100":
        q=10**5
    fi.write(str(q)+'\n')
    for _ in range(q):
        type = randint(1, 2)
        a = randint(1,10**18)
        b = randint(1,10**12)
        c = randint(1,10**12)
        while max(b, c) > a:
            a = randint(1,10**18)
        fi.write(str(type)+" "+str(a)+" "+str(b)+" "+str(c)+'\n')
        ans = solve(type, a, b, c)
        fo.write(str(ans)+'\n')


if not os.path.isdir("./"+test_name):
    os.mkdir("./"+test_name)
for i in range(test_num):
    if i < 20:
        generate_constraint_1(str(i+1))
    elif i < 40:
        generate_constraint_2(str(i+1))
    elif i < 60:
        generate_constraint_3(str(i+1))
    elif i < 100:
        generate_constraint_4(str(i+1))
