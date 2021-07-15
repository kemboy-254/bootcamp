#1. Compose a program that creates a one-dimentional array a containing exactly 1000 integers, and then attempts to access a[1000]. What happens when yu run the program?  

       d. indexing error




#2. What is wrong with the following code fragment?  

a = []  
for i in range (10):  
	a[i] = i * i  

    a is declared as an empty array Initially. And therefore, no elements are appended to the array. Therefore attempting to use its elements in an assignment statement will raise a run-time error.

#3. What does the following code fragment write?  

a = stdarray.create1D(10, 0)  
for i in range(10):  
   a[i] = 9 - i  
for i in range(10):  
   a[i] = a[a[i]]  
for v in a:  
   stdio.writeln(v)  


          It didn't work on my side


#4. What is a[] after executing the following code fragment?

n = 10
a = [0, 1]
for i in range(2, n):
   a += [a[i-1] + a[i-2]]
   print (a)


       [0, 1, 1]
       [0, 1, 1, 2]
       [0, 1, 1, 2, 3]
       [0, 1, 1, 2, 3, 5]
       [0, 1, 1, 2, 3, 5, 8]
       [0, 1, 1, 2, 3, 5, 8, 13]
       [0, 1, 1, 2, 3, 5, 8, 13, 21]
       [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#Bonus: Compose a program that takes an integer command-line argument n and writes n poker hands (five cards each) from a shuffled deck, separated by blank lines.
