print('Enter correct username and password\n=========================================')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='Hardcode' and username=='Hardcode':
        print('Login Successfully')
        break
    else:
        print('Try again.')
        count += 1
