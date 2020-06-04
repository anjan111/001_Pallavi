# wap print the factorial of a number
# 5 --> 1*2*3*4*5
N = input("enter N : ")
i = 1
fact = 1
while(i <= N ):
    fact = fact * i # fact *= i
    i += 1  #   i = i+1

print N,"! =",fact
