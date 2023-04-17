import os
import numpy as np
from numpy.random import randint
test_num=20
test_name="giaitri"
def solve(a,b):
    return a**b+b**a
def generate(id):
    if not os.path.isdir("./"+test_name+"/test"+id):
        os.mkdir("./"+test_name+"/test"+id)
    fi= open("./"+test_name+"/test"+id+"/giaitri.inp","w")
    fo= open("./"+test_name+"/test"+id+"/giaitri.out","w")
    test_case=randint(200)+1
    fi.write(str(test_case)+'\n')
    a = 1000
    b = 1000
    fi.write(str(a)+' '+str(b)+'\n')
    ans= solve(a,b)
    fo.write(str(ans)+'\n')
    for _ in range(test_case-1):
        a = randint(1000)+1
        b= randint(1000)+1
        fi.write(str(a)+' '+str(b)+'\n')
        ans= solve(a,b)
        fo.write(str(ans)+'\n')
    fi.close()
    fo.close()
if not os.path.isdir("./"+test_name):
    os.mkdir("./"+test_name)
for i in range(test_num):
    generate(str(i+1))
    print("TEST ",str(i+1)+" has completed. ")
    