from inputs import message

msg = message("Message")

parityCount = 0

while True:
    case1 = 2**parityCount
    case2 = len(msg)+parityCount+1
    if(case1 == case2):
        break
    else:
        parityCount+=1

parityValue = nonParityValue = 0
array =list(range(0,len(msg)+parityCount))


# Creating Temporary array
for k in range(1,len(msg)+parityCount+1):
    if(k == 2**parityValue):
        array[k-1] = "0"
        parityValue+=1
    else:
        array[k-1] = msg[nonParityValue]
        nonParityValue+=1

# initialize
for par in range(0,parityCount):
    let = 2**par
    count = 0
    s= let-1
    while (s<len(array)):
        for a in range(s,s+let):
            if(int(array[a])==1):count+=1
        s+= 2**let
    if(count%2 == 0):
        pass
    else:
        array[let-1] = "1"

print(f"Hamming code: {' '.join(array)}")
        











