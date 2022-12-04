'''
num=int(input("enter the number"))
x=num
sum=0
rem=0
while num>0:
rem=num%10
    num=num//10
   sum=sum+rem
print("sum of digits :",sum)    

print square of number :
num=2
while num<=20 :
    print("sum of input")
    
write done the program to display the reverse of the number.

num=int(input("enter any number :"))
rem=0
rev=0
while num>0 :
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(rev)   

range(begin,end,step)
for i(we have to write the veriable) range(1,10,2)

 -- reverse order by using for loop.

  square of number .
-- print even number from 0 to 10 by using the for loop .

'''
for i in range(1,20) :
    if i%4==0 :
       print(i)
