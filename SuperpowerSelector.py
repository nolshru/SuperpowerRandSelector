import random as r

def ReadFile(filename):
    array = []
    with open (filename,"r") as file:
        item = file.readline().rstrip("\n")
        while item:
            array.append(item)
            item = file.readline().rstrip("\n")
        return array

superpowers = ReadFile("PlaintextSuperpowerList.txt")
index = r.randrange(0,len(superpowers))
print (superpowers[index])

#end script
