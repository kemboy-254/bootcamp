# Python Program to print Even Numbers from 1 to 100
for num in range(1,100):
	if num%2==0:
		print (num, end = '  ')
	num=num+1
print('\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')

# Python Program to print Odd Numbers from 1 to 100

for numb in range(1,100):
      
    # checking condition
    if numb % 2 != 0:
        print(numb, end = " ")

print('\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')

# Python Program to print Prime Numbers from 1 to 100
 
for Number in range (1, 100):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')