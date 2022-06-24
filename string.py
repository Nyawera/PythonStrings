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


#palindrome ,2 pointer view

#Write a program to create a new string made of an input string’s first, middle, and last character.
str1 = 'James'
print("Original String is", str1)

# Get first character
res = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mi = int(l / 2)
# Get middle character and add it to result
res = res + str1[mi]

# Get last character and add it to result
res = res + str1[l - 1]

print("New String:", res)

for x in "banana":
    print(x)

# x = "Tomorrow"
# a = []
# b = list(x)
# for n in x:
#     if n not in a:
#      a.append(n):
#     else:
#      print(x)