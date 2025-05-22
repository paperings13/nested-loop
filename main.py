print("Character Occurence")
word = str(input(" Enter any word " ))
character = str(input(" Enter the character to check the ocurence " ))
count = 0
for i in word:
    if i == character:
      count = count + 1
print(count)



