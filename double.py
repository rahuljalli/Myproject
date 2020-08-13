a=[]
n=int(input("enter how many numbers"))



for i in range(n):
    numbers=int(input("enter the numbers"))

for i in range(n):
    a[i]=a[i]*2
    a.append(a[i])

   

print(a)
