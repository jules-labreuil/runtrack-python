liste = [2, 4, 6, 8, 10]

print("Liste avant l'échange :", liste)

temp = liste[0]
liste[0] = liste[-1]
liste[-1] = temp

print("Liste après l'échange :", liste)