# find the no of digits in a number
# 4534 ---->> 4 , 5,  3, 4 ====>>> 4
num = input("enter num : ")
temp = num
var =0
print num," is having total ,",
while(temp != 0):
    temp =  temp / 10
    var = var + 1
else:
    print var," digits"
