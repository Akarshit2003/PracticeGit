
# Increasing pattern
for i in range(1,7):
    for j in range(1,i+1):
        print("*" ,end=" ")
    print()

print()

# Decreasing Pattern
for i in range(7,0,-1):
    for j in range(1,i+1):
        print("*" ,end=" ")
    print()

for i in range(1,5):
		for j in range(1,8):
			if j>=5-i and j<= 3+i:
				print("*" , end='')
			else:
				print(" " , end='')
		print()
		


print()

for i in range(1,5):
		for j in range(1,8):
			if j>=i and j<= 8-i:
				print("*" , end='')
			else:
				print(" " , end='')
		print()

print()	

for i in range(1,5):
        for j in range(1,8):
            if j<=5-i or j>=3+i:
                print("*", end='')
            else:
                print(" " , end='')
        
        print()






	    