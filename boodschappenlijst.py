lijstje = {}
def boodschappen (x):
    welkItem = input ('Wat wil je toevoegen aan je boodschappenlijstje? \n')
    hoeveelItem = int(input ('Hoeveel wil je daarvan? \n'))
    if welkItem in lijstje.keys():
            x [welkItem] = x [welkItem] + hoeveelItem 
    else:
        x [welkItem] = hoeveelItem 
    print (x)
    nogmaals = input ('Wil je nog iets toevoegen? \n')
    if nogmaals in ['ja', 'JA', 'Ja', 'j', 'J']:
        return boodschappen(x)
    elif nogmaals in ['nee' ,'NEE', 'Nee', 'n' ,'N']:
        print (f'Je boodschappenlijstje is: \n {x}')
        exit()


boodschappen(lijstje)