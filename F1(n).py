#O(k^n)

def F1(n):
    if (n <= 2):
        return 1
    else:
        return (F1(n-1) + F1(n-2))

input = open("input1.txt", "r")
fileRead = input.readlines()
output = open("output1.txt", "w")
 
for x in fileRead:
    num = (F1(int(x)))
    output.write(str(num)+ "\n")




