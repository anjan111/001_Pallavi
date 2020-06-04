# wap find the prime numbers from any seq

seq = input("enter a seq : ")
prime = []
for num in seq :
    i = 1
    f_c = 0
    while(i <= num ):
        if(num % i == 0):
            f_c += 1
        i = i+1
    if(f_c == 2):
        prime = prime +[num]
print prime
