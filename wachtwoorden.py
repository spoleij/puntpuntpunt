import random
import string

cijfers = (string.digits)
letters = (string.ascii_lowercase)
hoofdletters = (string.ascii_uppercase)
tekens = ['@' ,'#' ,'$' ,'%' ,'&', '_' ,'?']

# 2 tot 6 hoofdletters.
# Minimaal 8 kleine letters.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
# De speciale tekens mogen niet op de eerste of laatste positie staan en ook niet op een vaste plek.
# 4 tot 7 cijfers (0 t/m 9).
# Op de eerste 3 posities mag geen cijfer staan.

# met *import string* kan je de string.ascii_lowercase/uppercase + digits toevoegen. dan doe je bv cijfers = string.digits ipv de list die ik nu heb
minLetters = []
minTekens = []
minCijfers = []
voorkant = []
midden = []
achterkant = []
lengteTotaal = []
###########

def wwGenerator ():
    for i in range (random.randint(2,6)):
        minLetters.append(random.choice(hoofdletters))
    for i in range (3):
        minTekens.append(random.choice(tekens))                          # WORK IN PROGRESS
    for i in range (random.randint(4,7)):
        minCijfers.append(random.choice(cijfers))
    lengteTotaal.extend(minLetters)
    lengteTotaal.extend(minTekens)                                    #listName.extend()  combines 2 lists!
    lengteTotaal.extend(minCijfers)      #lengteTotaal is om de totale lengte te weten voordat we gaan aanvullen tot 24
    lengteCheck = len(lengteTotaal)
    while lengteCheck < 24:
        minLetters.append(random.choice(letters))
        lengteCheck = lengteCheck + 1               #we vullen de lengte van de list niet echt, alleen de lengteCheck variable +1

    random.shuffle(minLetters)                      #shuffle letters op deze plek!
    voorkant.append(minLetters.pop())
    voorkant.append(minLetters.pop())
    voorkant.append(minLetters.pop())               #3 random letters voor de eerste 3 plekken. geen cijfers tm 3e en geen teken op de 1e
    achterkant.append(minLetters.pop())             # en 1 voor de achterste plek. dit mag geen teken zijn
    midden.extend(minLetters)
    midden.extend(minTekens)
    midden.extend(minCijfers)                       #de rest van de verzamelde dingetjes gaan naar het middenstuk
    random.shuffle(midden)
    
    wachtwoord = voorkant + midden + achterkant
    print (f'TEST!!! de lengte van dit wachtwoord is: {len(wachtwoord)}')
    print (*wachtwoord)                              
                                                            # het is kut dat je dit niet gewoon kan shuffelen en dat je perse dingen wel/niet mag

wwGenerator()