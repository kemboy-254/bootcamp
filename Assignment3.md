##1. What is the difference between = and ==? 
		 = is used to assign a variable to a value.  
		 == is ised to indicate that both the values on the left and the right are equal.  

##2. Can I leave out the colon in an if, while, or for statement? Yes/No 
		 No
##3. Should I use tab characters to indent my code? Yes/No 
		 No

##4. Compose a program that takes three integer command-line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise.
		 num1 =int(input('Please enter the first number:'))
		 num2 =int(input('Please enter the second number:'))
		 num3 =int(input('Please enter the third number:'))

		 if num1==num2==num3:
			 print('Equal')
		 else:
			 print('Not equal')
		 
##5. What is the value of j after each of the following code fragments is executed?

	a.	j = 0
	  	for i in range (0, 10) :
	  	j += i

	   	 0
		 1
		 3
		 6
		 10
		 15
		 21
		 28
		 36
		 45

	b.	j = 1
		for i in range (0, 10) :
		j += j

		 2
		 4
		 8
		 16
		 32
		 64
		 128
		 256
		 512
		 1024

	c.	for j in range (0, 10) :
		j += j
		 0  
		 2  
		 4  
		 6  
		 8   
		 10  
		 12  
		 14  
		 16  
		 18  


##6. What are m and n after the following code is executed? 
	n = 123456789
	m = 0

	while n != 0:
	m = (10 * m) + (n % 10)
	n //= 10

	print (m)
	print (n)

		 9
		 12345678
		 98
		 1234567
		 987
		 123456
		 9876
		 12345
		 98765
		 1234
		 987654
		 123
		 9876543
		 12
		 98765432
		 1
		 987654321
		 0

##7 What does this code do?
	f = 0
	g = 1

	for i in range (0, 10):
		f = f + g
		g = f - g

		print (f)

			 1
			 1
			 2
			 3
			 5
			 8
			 13
			 21
			 34
			 55

##Bonus: Is there an example for when the following for and while loops are not equivalent?


