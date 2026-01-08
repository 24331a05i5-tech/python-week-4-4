n1=float(input("enter 1st number:"))
n2=float(input("enter 2nd number:"))
n3=float(input("enter 3rd number:"))
max=n1 if n1>n2 and n1>n3 else n2 if n2>n1 and n2>n3 else n3
print(max,"is largest")
min=n1 if n1<n2 and n1<n3 else n2 if n2<n1 and n2<n3 else n3
print(min,"is smallest")
