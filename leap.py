y=int(input("enter the current year:"))
num=int(input("enter the limit :"))
print("leap year from 2026 to",num)
for i in range(y,num+1):
    if(i%4==0 and i%100!=0 or i%400==0):
        print(i,"\n")
