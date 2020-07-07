n = int(input("Enter the no "))
fact = 1
if (n == 0):
    print("factorial = 1")
for  i in range (1,(n+1)):
      fact = (fact*i)
print(fact)