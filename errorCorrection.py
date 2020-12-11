from inputs import message
from termcolor import colored

array = message("Received Code")
parityCount=0
error_bit =""
intial=0

while True:
    value = 2**intial-1
    if(value<len(array)):
        parityCount+=1
        intial+=1
    else:
        break

for par in range(0,parityCount):
    let = 2**par
    count = 0
    s= let-1
    while (s<len(array)):
        for a in range(s,s+let):
            if(int(array[a])==1):count+=1
        s+= 2**let
    if(count%2 == 0):
        error_bit += "0"
    else:
        error_bit +="1"

print(error_bit)
