lijstje = {} #boodschappenlijstje!!
def boodschappen (lijstje):
    welkItem = input ('Wat wil je toevoegen aan je boodschappenlijstje? \n')
    hoeveelItem = int(input ('Hoeveel wil je daarvan? \n'))
    if welkItem in lijstje.keys():
            lijstje [welkItem] = lijstje [welkItem] + hoeveelItem 
    else:
        lijstje [welkItem] = hoeveelItem 
    print (lijstje)
    nogmaals = input ('Wil je nog iets toevoegen? \n')
    if nogmaals in ['ja', 'JA', 'Ja', 'j', 'J']:
        return boodschappen(lijstje)
    elif nogmaals in ['nee' ,'NEE', 'Nee', 'n' ,'N']:
        print (f'Je boodschappenlijstje is: \n {lijstje}')
        exit()
boodschappen(lijstje)