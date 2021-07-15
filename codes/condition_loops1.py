#Prints all the rest except apple

fruits=["apple","banana","cherry"]
for x in fruits:
	if x =="apple":
		continue
	print (x)

print('\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n')

#Only prints apple from the list

for x in fruits:
	if x =="apple":
		break
print (x)