n=int(input("write the number"))
sum=0
t=n
while t>=0:
    digit= t % 10
    sum=sum+digit ** 3
    t=t // 10
if t==sum:
    print("it is an armstrong number")
else:
    print("not am armstrong number")
    