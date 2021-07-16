def Age():
    print('Hello and welcome to this system!')
    print()
    input ('Press enter to continue')
    name = input('What is your name please?: ')
    age = int(input('And what is your age?: '))

    if age>18:
        print('Hi',name, 'you are', (age), 'years old and You are an adult' )
    else:
        print('Hi',name, 'you are', (age), 'years old and You are still a kid' )

Age()