hilcsv = open("hilfig.csv", "r")
mega = hilcsv.read()
hell = mega.split("\n")
listme = []
hell.pop(0)
for i in hell:
    i = i.split(',')
    listme.append(float(i[0]))
print(hell)
print(listme)

hilcsv.close()
#print(mega)