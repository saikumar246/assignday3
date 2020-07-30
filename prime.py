#assignment opearators
a = 21
b = 10
c = 0
c = a + b
print("Value of c is ", c)

c += a
print("Value of c is ", c)

c *= a
print("Value of c is ", c)

c /= a
print("Value of c is ", c)

c  = 2
c %= a
print("Value of c is ", c)

c **= a
print("Value of c is ", c)

c //= a
print("Value of c is ", c)

#Bitwise operators
a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
print ('a=',a,':',bin(a),'b=',b,':',bin(b))
c = 0

c = a & b;
print ("result of AND is ", c,':',bin(c))

c = a | b;
print ("result of OR is ", c,':',bin(c))

c = a ^ b;
print ("result of EXOR is ", c,':',bin(c))

c = ~a;
print ("result of COMPLEMENT is ", c,':',bin(c))

c = a << 2;
print ("result of LEFT SHIFT is ", c,':',bin(c))

c = a >> 2;
print ("result of RIGHT SHIFT is ", c,':',bin(c))

#python program for checking prime numbers with out using loops
def isPrime(n, i=2):
    # Base cases
    if (n <= 2):
        return True if (n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return true
 # Check for next divisor
    return isPrime(n, i + 1)

n =2
if (isPrime(n)):
    print("Yes,It is a prime")
else:
    print("It is not a prime")
#arbitary functions
def sai(*p):
    print("python is easy"+" "+p[1])
sai("for sai","to learn")
#tuples in python programming

tuple = (1,2,3,4,5,6,7)
#element 1 to end
print(tuple[1:])
#element 0 to 3 element
print(tuple[:4])
#element 1 to 4 element
print(tuple[1:5])
# element 0 to 6 and take step of 2
print(tuple[0:6:2])
print(tuple[::-1])
print(tuple[-2])
#dictionary in python programming
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
print(type(Employee))
print("printing Employee data .... ")
print(Employee)
print("Deleting some of the employee data")
del Employee["Name"]
del Employee["Company"]
print("printing the modified information ")
print(Employee)
print(Employee)
Employee1 = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
for x in Employee1:
    print(Employee1[x])
#lambda functions
s=lambda a:a+100
print(s(200))
d=lambda a,b:a**b
print(d(2,3))
#random module
import random
print(random.random())
li=["Mango","Apple","orange",2,3,"sai"]
random.shuffle(li)
print(li)
#requesta module
import requests
x=requests.get("https://www.youtube.com")
print(x.text)
