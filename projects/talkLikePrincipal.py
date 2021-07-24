print("="*15,"The Principal's Speech",+"="*15)

def nounWord():
    print("Enter nouns: ")
    nounWords=[]

    for n in range(5):
        input1=input("{}".format(n+1))
        nounWords.append(input1)

    return nounWords


def verbword():
    print("Enter verbs: ")
    verbwords = []

    for n in range(5):
        input1 = input("[{}".format(n + 1))
        verbwords.append(input1)

    return verbwords

def adjword():
    print("Enter adjectives: ")
    adjwords = []

    for n in range(5):
        input1 = input("{}".format(n + 1))
        adjwords.append(input1)

    return adjwords


nounwords1 = nounWord()
verbwords1 = verbword()
adjwords1 = adjword()



principlestory="How are you "+nounwords1[0]+". I would like to "+verbwords1[1]+" all "+adjwords1[2]+" prefects "+"for the "+adjwords1[3]+" job done. Make sure you "+verbwords1[2]+" hard to get good results. Have a "+adjwords1[4] +nounwords1[3]

print(principlestory)