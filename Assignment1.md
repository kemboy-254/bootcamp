##1. Compose a program that writes the Hello, World message 10 times. 
        print("Hello World\n"*10)

##2.	Describe what happens if you omit the following in helloworld.py: 

            •	the first '  
                o	 Error  
            •	the second '  
                o	Error  
            •	the print() statement  
                o	Error  

##3.	Which one of the following is the correct way to execute useargument.py using the terminal: •
            o	python useargument.py 
            o	python3 useargument.py
##4.	Modify helloworld.py to compose a program that takes three names and writes a proper sentence with the names in the reverse of the order they are given, so that, for example, python helloworld.py Alice Bob Carol writes the string 'Hi Carol, Bob, and Alice'

            first_name =str(input('Please enter the first name: '))
            second_name =str(input('Please enter the second name: ')) 
            third_name =str(input('Please enter the third name: ')) 

            print ("Hi", third_name,",",second_name, "and", first_name )
