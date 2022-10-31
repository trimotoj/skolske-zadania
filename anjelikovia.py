import random
mena = ['mama', 'otec', 'ivan', 'kika', 'sara', 'beni', 'timo']
print(mena)
def algoritmus():
    mena2 = []
    for i in range(len(mena)):
        choosingNames = mena[:i] + mena[i+1:]
        choosingNames = [i for i in choosingNames if i not in mena2]
        try:
            meno = random.choice(choosingNames)
        except IndexError:
            algoritmus()
        mena2.append(meno)
    print(mena2)   
algoritmus()

