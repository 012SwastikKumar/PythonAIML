# 0 1 1 2 3 5 8 13 21 34 55 89 144  .....
a = 0
b = 1
n=int(input("Enter the number of terms to be present in series : "))
print(a,"\n",b)
for x in range(n-1):
    s=a+b
    print(s)
    a=b
    b=s
print(input("Press any key to exit"))
