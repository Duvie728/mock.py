##import datime
##now = datetime.now()
##today = now.strftime("%d/%m/%Y %H:%M:%S")
##print(today)

##from datetime import date
##date(2002, 12, 4).isoformat()
##'2002-12-04'

name = input("what is your username ? \n")
allowedusers = ['seyi','richard','paul']
allowedpassword =['Passwordseyi','passwordrichard','passwordpaul']
    if(name in allowedusers):
    password = input("your password ?\n")
    if(password == allowedpassword):
        print('welcome to Zuri bank  %s' %name)
        time=('3/30/2021 \n 1:48PM')
        else:
            print('password incorrect please try again')
else:
    print('Name not found please try again')
print('This are the available options')
print('1. How much will you like to withdraw ?')
print('2. How much will you like to deposit ?')
print('3. Complaints')
selectedoption= int (input('Please select an option \n'))
if(selectedoption==1):
  print('You selected %d' % selectedoption)
  print('How much will you like to withdraw ? \n')
  amount= input(' Enter Amount \n')
  print('Take your cash \n Transaction successful')
  pass
elif(selectedoption==2):
  print('You selected %d' % selectedoption)
  print('How much will you like to deposit?')
  amount= input('Enter Amount \n')
  print('Deposit successful \n Current Balance 10,000')
  pass
elif(selectedoption==3):
  print('You selected %d' % selectedoption)
  print('What issue will you like to report? \n')
  text= input('Enter your complaint \n')
  print("Thank you for contacting us")
  pass
else:
  print('Invalid option selected, please try again')

L
