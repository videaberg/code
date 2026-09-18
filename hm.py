import random
totalsumma = 0
loopa = True
while(loopa):
    T = random.randint(1,6)
    totalsumma = totalsumma + T
    print('Du fick. ',T)
    print(totalsumma)
    if(totalsumma == 21):
        print('Spelaren vinner.')
        yes = True
        while(yes):
            svar = input('Vill du kasta igen? ')
            if(svar == 'nej'):
                loopa = False
                yes = False
            elif(svar != 'ja'):
                print('???')
            elif(svar == 'ja'):
                yes = False
    elif(totalsumma > 21):
        print('Spelaren förlorar.')
        loopa = False
    elif(totalsumma < 21):
        loop = True
        while(loop):
            svar = input('Vill du kasta igen? ')
            if(svar == 'nej'):
                loopa = False
                loop = False
            elif(svar != 'ja'):
                print('???')
            elif(svar == 'ja'):
                loop = False