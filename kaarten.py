from itertools import count
import random
standaardDeck = ['joker', 'joker', 'harten boer', 'harten vrouw', 'harten heer', 'harten aas', 'harten2' ,'harten3', 'harten4', 'harten5' ,'harten6', 'harten7',
    'harten8' ,'harten9' ,'harten10', 'klaveren boer', 'klaveren vrouw' ,'klaveren heer' ,'klaveren aas', 
    'klaveren2' ,'klaveren3' ,'klaveren4' ,'klaveren5' ,'klaveren6' ,'klaveren7' ,'klaveren8', 'klaveren9', 'klaveren10', 'schoppen boer', 'schoppen vrouw' ,
    'schoppen heer' ,'schoppen aas' ,'schoppen2' ,'schoppen3', 'schoppen4', 'schoppen5',
    'schoppen6' ,'schoppen7' ,'schoppen8', 'schoppen9' ,'schoppen10' ,'ruiten boer' ,'ruiten vrouw',
    'ruiten heer', 'ruiten aas', 'ruiten2', 'ruiten3' ,'ruiten4' ,'ruiten5' ,'ruiten6' ,'ruiten7', 'ruiten8', 'ruiten9' ,'ruiten10']
random.shuffle(standaardDeck)
overigeKaarten = standaardDeck[8:54]
bovensteZeven =standaardDeck[0:7]
indexTeller, kaart = (0,1)
for i in range (7):
    print (f'kaart {kaart}: {bovensteZeven[indexTeller]}')
    kaart +=1
    indexTeller += 1
print (f'\ndeck (47 kaarten): {overigeKaarten}')