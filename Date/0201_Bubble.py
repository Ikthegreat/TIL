Bubble = [55, 7, 78, 12, 42]

for i in range(len(Bubble)-1):
    if Bubble[i] > Bubble[i+1]:
        Bubble[i], Bubble[i+1] = Bubble[i+1], Bubble[i]
    else:
        continue

print(Bubble)