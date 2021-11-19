#IMPORT
import random
import os 

class kleur:
    blauw = '\033[94m'
    groen = '\033[92m'
    geel = '\033[93m'                               #begin en eindig dat wat je wilt inkleur met kleur.KIESKLEUR
    rood = '\033[91m'
    standaard = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    roodBG = '\033[0;37;41m'
    blauwBG = '\033[0;37;44m'
    witBG = '\033[0;30;47m'


#DOBBELSTENEN
dobbelsteenRood = 	[1 , 2 , 3  , 4  , 5 , 6]
dobbelsteenBlauw =	[1 , 2 , 3  , 4  , 5 , 6]
dobbelsteenWit =	[1 , 1 , 1 , 2 , 2 , 3]


#SCOREVLAKKEN
scorevlakRood = [-2,None,None,None,None,None,None,None,None,None]           #de None wordt later veranderd in 0
scorevlakBlauw = [None,None,None,None,None,None,None,None,None,-2]
scorevlakWit = []
print (f'{kleur.BOLD}\nWELKOM BIJ DOBBEL TROBBEL{kleur.standaard}')


def cls():

    os.system('cls' if os.name=='nt' else 'clear')         # function om t scherm te clearen en opnieuw score te potsen?

def rolDobbelstenen():                                      # function om de dobbelstenen te rollen
    scorevlakken()
    lengteCheck = 0
    print ('we rollen de dobbelstenen... \n')
    rolRood = random.choice(dobbelsteenRood)
    rolBlauw = random.choice(dobbelsteenBlauw)
    rolWit = random.choice(dobbelsteenWit)
    print (f"""
    {kleur.rood}ROOD:   {rolRood}{kleur.standaard}
    {kleur.blauw}BLAUW:  {rolBlauw}{kleur.standaard}
    WIT:    {rolWit}\n""")
    berekenen(rolRood,rolBlauw,rolWit,lengteCheck)  #roep function op

#berekenen:
# 1 blauw + rood + wit = getal
# 2 blauw + rood - wit = getal
# 3 blauw + rood = getal
# 4 hoogst gerolde dobbelsteen - laagst gerolde dobbelsteen = getal

def berekenen(rolRood, rolBlauw, rolWit,lengteCheck):              # function om de berekeningen te maken
    berekening1 = rolBlauw + rolRood + rolWit
    berekening2 = rolBlauw + rolRood - rolWit
    berekening3 = rolBlauw + rolRood
    gerold = [rolRood,rolBlauw,rolWit]                      
    berekening4 = max(gerold) - min(gerold)
    roodBlauw = [rolRood, rolBlauw]

    print (f'{kleur.BOLD}KIES EEN VAN DE VOLGENDE GETALLEN:{kleur.standaard}')
    print (f"""
    {rolBlauw} + {rolRood} + {rolWit} =     {kleur.geel}{berekening1}{kleur.standaard}
    {rolBlauw} + {rolRood} - {rolWit} =     {kleur.geel}{berekening2}{kleur.standaard}
    {rolBlauw} + {rolRood} =         {kleur.geel}{berekening3}{kleur.standaard}
    {max(gerold)} - {min(gerold)} =         {kleur.geel}{berekening4}{kleur.standaard}\n""")

    kiesBerekening = int(input ('ik kies: '))

                                         #EXIT ALS ALLE 5 DE VAKJES VAN WIT VOL ZIJN!!!! scroll naar onder                       
    if min(roodBlauw) ==  rolBlauw:
        kleurRij = f'{kleur.blauw}de blauwe{kleur.standaard}'
        welkeRij = scorevlakBlauw
    if min(roodBlauw) ==  rolRood:
        kleurRij = f'{kleur.rood}de rode{kleur.standaard}'
        welkeRij = scorevlakRood
    if min(roodBlauw) == max(roodBlauw):
        kiesRij = input (f'kies de rij: {kleur.rood}rood {kleur.standaard}of {kleur.blauw}blauw{kleur.standaard}\n')
        if kiesRij == 'rood':
            kleurRij = f'{kleur.rood}de rode{kleur.standaard}'
            welkeRij = scorevlakRood
        if kiesRij == 'blauw':
            kleurRij = f'{kleur.blauw}de blauwe{kleur.standaard}'
            welkeRij = scorevlakBlauw

    
    # SCHRIJF HIER NOG EEN LOOP OM TE CHECKEN OF KIESBEREKENING WEL GELIJK IS AAN EEN VAN DE KEUZES VOOR DE ZEKERHEID
    print (f'\nplaats je gekozen getal {kleur.geel}{kiesBerekening}{kleur.standaard} in een lege plek in {kleurRij} rij {kleur.standaard}')
    legePlek(kiesBerekening,welkeRij,berekening3,berekening4,rolWit)

def legePlek (kiesBerekening,welkeRij,berekening3,berekening4,rolWit):      #check of de lege plek wel lager/hoger/geldig is!!!!
    geldigheid = [False,]*10
    for x in range(10):        
        if welkeRij == scorevlakRood:
            if scorevlakRood[x] is not None:
                continue

            geldigheidRood = [False,]*10
            geldigheidRood[x] = True
            for i in range(x):
                geldigheidRood[i] = scorevlakRood[i] == None or scorevlakRood[i] < kiesBerekening
            for j in range(x + 1, 10):
                geldigheidRood[j] = scorevlakRood[j] == None or scorevlakRood[j] > kiesBerekening

            geldigheid[x] = (False in geldigheidRood) == False
        elif welkeRij == scorevlakBlauw:
            if scorevlakBlauw[x] is not None:
                continue

            geldigheidBlauw = [False,]*10
            geldigheidBlauw[x] = True
            for i in range(x):
                geldigheidBlauw[i] = scorevlakBlauw[i] == None or scorevlakBlauw[i] > kiesBerekening
            for j in range(x + 1, 10):
                geldigheidBlauw[j] = scorevlakBlauw[j] == None or scorevlakBlauw[j] < kiesBerekening
            
            geldigheid[x] = (False in geldigheidBlauw) == False

    positie = 0
    print(geldigheid)
    if True in geldigheid:
        positie = int(input ('welke lege plek kies je?\n')) - 1         # -1 vanwege index
    else:
        return sluitspel()

    if geldigheid[positie] == False:                        # als het hoger/lager/geldig dingetje niet geldig is
        print ('kies een andere plek')                      
        return legePlek(kiesBerekening,welkeRij, berekening3, berekening4, rolWit)

    
    welkeRij [positie] = kiesBerekening         # zet de berekening op de gekozen plek/positie
                                                             
    if kiesBerekening == berekening3 or kiesBerekening == berekening4:      
        scorevlakWit.append (rolWit)
        #lengteCheck += 1
        if len(scorevlakWit) == 5:                                        
            sluitspel() 
            return  
    cls()
    rolDobbelstenen()

def scorevlakken():                                 # het design van het scoreboard                   
    # Posities
    x = kleur.BOLD + '    Positie:  '
    for i in range (10):
        x += '[' + str(i+1)+']'
    x+= '' + kleur.standaard
    print (x)

    # Rood
    x = f'    {kleur.roodBG}Rood:     '
    for i in range (10):
        getal = scorevlakRood[i]
        if (getal == None):
            x += '[ ]'
        else:
            x += '[' + str(scorevlakRood[i])+']'
    x+= '' + kleur.standaard
    print (x)

    # Blauw
    x = f'    {kleur.blauwBG}Blauw:    '
    for i in range (10):
        getal = scorevlakBlauw[i]
        if (getal == None):
            x += '[ ]'
        else:
            x += '[' + str(scorevlakBlauw[i])+']'
    x+= '' + kleur.standaard
    print (x)

    # Wit
    x = f'    {kleur.witBG}Wit:      '
    for i in range (5):
        getal = None
        if (i < len(scorevlakWit)):
            getal = scorevlakWit[i]

        if (getal == None):
            x += '[ ]'
        else:
            x += '[' + str(scorevlakWit[i])+']'
    x+= '' + kleur.standaard
    print (x)    

def sluitspel():                                                        #functie voor eindscore berekenen
    cls()
    scorevlakken()
    print ('LATEN WE NAAR JE SCORE KIJKEN:\n')
    roodKeerBlauw = []
    legeVakjes = 0
    for i in range (10):
        rood = scorevlakRood[i]
        blauw = scorevlakBlauw[i]
        if (rood == None):
            rood = 0
            legeVakjes+=1
        if (blauw == None):
            blauw = 0
            legeVakjes+=1
        roodKeerBlauw.append (rood * blauw)
    waarde1 = sum(roodKeerBlauw)
    waarde2 = sum(scorevlakWit) * legeVakjes
    score = waarde1 - waarde2

    print(score)                   #dit print de gehele som van alle getallen in de list score

rolDobbelstenen()

####