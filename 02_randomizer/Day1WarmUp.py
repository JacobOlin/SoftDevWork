import random
KREWES = {
    'orpheus': ['Emily','Kevin','Vishwaa'],
    'rex': ['William','Joseph'],
    'Endymion': ['Grace','Nahi','Derek','Jun Tao']
}
    


def pickRandomName():
    rng = random.randint(0,2)
    key = -1
    if rng == 0:
        key = 'orpheus'
    if rng == 1:
        key = 'rex'
    if rng == 2:
        key = 'endymion'
    print (KREWES[key][random.randint(0,len(KREWES[key]) - 1)])

pickRandomName()

