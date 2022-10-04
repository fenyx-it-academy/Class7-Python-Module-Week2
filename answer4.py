def multi(num1,num2,num3):
    x = num1*num2*num3
    return(x)
n1 = int(input("1st number:  "))
n2 = int(input("2nd number:  "))
n3 = int(input("3rd number:  "))
result = multi(n1,n2,n3)
print(f"multiplication result:  {result}")

for i in range(1,result):
    if (str(i)== str(i)[::-1]):
      m= print(i,end=",")

