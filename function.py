def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass

isGreater(10,5)
calculateGmean(10,5)

isGreater(67,78)
calculateGmean(67,78)


# Calculate the length of string

def calculation(string):
    length = len(string)
    return length

string = input("Enter the string:")

string_len = calculation(string)

print("The length of string " , string +"  is ",  string_len)
