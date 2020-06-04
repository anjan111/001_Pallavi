# wap print non prime numbers using continue in between 10  to 30
num = 9
while(num<30):
    num = num +1
    f_c = 0
    for e in range(1, num+1):
        if(num % e != 0 ):
           continue
        f_c = f_c+1
    if(f_c == 2):
        continue
    print "non prime : ", num
    
