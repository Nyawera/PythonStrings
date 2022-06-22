play="childrenplayingground"
child=""
i=0
for n in play:
    if i <=len(play)/2:
        child+=(play[i].upper())
        i+=1
    else:
        child+=play[i]
        i+=1
print(child)    