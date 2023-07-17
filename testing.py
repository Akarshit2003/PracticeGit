 # dictionary , list , tuple , set , json ,class ,object ,function , method ,
    #  star  print programs , factorial , prime number ,
    # database , select , insert , update queries with where clause
    #    dictionary/ list  operations , GET , PUT  , UPDATE , DELETE , concatenete
    #    API methods
    # Palindrome (Don't use buit -in methods of python)
print("Hello")

# Star Pattern program
# n = 4
# for i in range(n):
#     for j in range(n):
#         print("*" , end=" ")
#     print()


# Increasing pattern

# print("Increasing Triangle")

# n =6
# for i in range(n):
#     for j in range(i+1):
#         print("#" ,  end =" ")
#     print()

for i in range(1,7):
    for j in range(1,i+1):
        print("*" ,end=" ")
    print()


print()


# Decreasing pattern

# print("Decreasing Triangle")
# n =7
# for i in range(n):
#     for j in range( i,n):
#         print("#" , end=" ")
#     print()

for i in range(7,0,-1):
    for j in range(1,i+1):
        print("*" ,end=" ")
    print()


print()

for i in range(1,7):
    for k in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*" , end=" ")
    print()


print() 
        
for i in range(7,0,-1):
    for k in range(1 ,8-i):
        print(" " , end=" ")
    for j in range(1,i+1):
        print("*" , end=" ")
    print()

# Right Triangle
# print("Right angled Triangle")

# n =7
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*" , end=" ")
#     print()

# Decreasing Star Triangle

# print("Decreasing Star Triangle")

# n =10
# for i in range(n):
#     for j in range(i +1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*" ,end=" ")
#     print()


print()

for  i in range(1,6):
    for k in range(1,6-i):
        print(" " , end="")
    for j in range(1,(2*i-1) +1):
        print("*" , end="")
    print()


# Reverse the above pattern
print()

for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" " , end="")
    for j in range(1 , (2*i-1) + 1):
        print("*" , end="")
    print()



# Program for factorial of a number

# print()
# print("Factorial number")

# num = int(input("Enter a number for factorial :"))
# factorial =1

# if num ==0:
#     print("Factorial is 1")
# else:
#     for i in range(1 , num +1):
#         factorial = factorial*i
#     print("Factorial of " , num , "is" , factorial)


# Program for fibonacci series

# print("Fibonacci Series")
# a = 0
# b = 1
# n = int(input("Enter the number :"))
# if num ==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)


# Program for Palindrome


# print("Palindrome ")

# for string Input
# a = input("Enter the value: ")

# reverse = a[::-1]
# if( a ==reverse):
#     print("The value is Palindrome")
# else:
#     print("The value is not  Palindrome")



# For Number input
i = int(input("Enter the value: "))
reverse =0
x=i
while (i>0):
    reverse = (reverse*10) + i%10
    i=i//10
if(x==reverse):
    print("Palindrome")
else:
    print("Not Palindrome")



