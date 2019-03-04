#O(n)

def F2(n):
    if(n <= 2 ):
        return 1
    else:
        p = 1
        q = 1
        r = 0
        for i in range (3,n+1):
            r = p + q
            p = q
            q = r
        return r
input = open("input2.txt", "r")
fileRead = input.readlines()
output = open("output2.txt", "w")
 
for x in fileRead:
    num = (F2(int(x)))
    output.write(str(num)+ "\n")
