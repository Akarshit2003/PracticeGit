# Dictionary 
dict1 = {1:"Clix",2:"Capital"}
print(type(dict1))
print(dict1.get(1))
dict1[1] = "Cllix"
dict1[3] = "Gurgaon"
dict1["Pincode"] =  122010
print(dict1.pop("Pincode"))

# print(dict1.pop(3))
print(dict1)


# Lists
l1 = [1,3,4,5,9]
# print(type(l1))
l1.append(34)
l1.pop()
# print(l1)



# Tuples
t1 =(2,5,67,547,2,4)
# print(type(t1))
len(t1)

# t1.count(2)
# print(t1.count(2))
# print(len(t1))
# print(sorted(t1))



# Sets
s1 ={34,56,12,45.7}
s1.add(38)
s1.remove(45.7)
# s1.clear()
# print(type(s1))
# print(s1)