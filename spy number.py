

a = int(input("giie:"))
b=a
c=0
v=1
d = len(str(a))
while a>0:
    e = a%10
    c=c+e
    v=v*e
    a=a//10
if v == c :
    print(f"{b}is an spy number")
    print(f"{v}=product,sum={c}")
else:
    print(f"{b} not an spy number")
