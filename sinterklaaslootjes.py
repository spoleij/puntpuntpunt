#SINTERKLAASLOOTJES
#LEERPAD 6
#STEPH POLEIJ
#99033734

import random


# create allNames list with .split (empty spaces between names = seperate variables) // check if there's more than 2 participants // if there is, add those to the allNames list until at least 3
allNames = (input ('Welke namen doen allemaal mee? \n').split())
print (allNames)
print (len(allNames))                   #test code
while len(allNames) <3:
    moreNames = (input ('Ik heb minstens 3 namen nodig, wie zijn de rest van de deelnemers? \n').split())
    allNames += moreNames
    print (len(allNames))               #test code
print (allNames)
print (len(allNames))                   #test code

# remove duplicates from list and make that the new allNames
allNames = (list(set(allNames)))              
print (allNames)                        #test code

# link two names to each other / no doubles / not your own name
def drawLootjes(allNames):
    defAllNames = allNames                                                                  
    chooseName = defAllNames.copy()                                                                 # copy list and call it chooseName. we now have 2 of the same. defAllNames and chooseName
    finalDuos = []                                                                                  # new list for actual duos = who draws who
    for i in defAllNames:                                                                           # for loop for all elements in defAllNames
        allNames = defAllNames.copy()                                                               # copy defAllNames and give it back to allNames ???
        allNames.pop (allNames.index(i))                                                            # remove from allNames for i amount of times (in defAllNames)
        chosen = random.choice(list(set(chooseName)&set(allNames)))                                 # choose random names, one from chooseName and allNames and also remove it from allNames
        finalDuos.append((i,chosen))                                                                # give for index i one of the chosen names from the variable chosen
        chooseName.pop(chooseName.index(chosen))                                                    # remove the chosen name index equal to chooseName from chooseName
                                                                                                    # repeat this i amount of times  
    print (f'dit zijn de duos! \n {finalDuos}')                                                     # finally print the duos / who draws who!

drawLootjes(allNames)