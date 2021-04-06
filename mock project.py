name = input("What is your name?\n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = "Password"

if(name in allowedUsers):
    password = input("Your password?\n")

    if(password == allowedPassword):
        print('Welcome %s' % name)
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')
