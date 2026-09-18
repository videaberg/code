password = "Python"
loopa = True
försök = 0
while(loopa and försök < 3):
    svar = input('Give me the password. ')
    if(svar == password):
        loopa = False
        print('Welcome in')
    else:
        försök = försök + 1
        print('Wrong password')
