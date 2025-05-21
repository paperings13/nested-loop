print("Character Occurence")
word = str(input(" Enter any word " ))
character = str(input(" Enter the character to check the ocurence " ))
count = 0
for i in word:
    if i == character:
      count = count + 1
print(count)
print("\n")
j = 0
check = 0
while( j < len(word)):
   
   if (word[j] == character):
      check = check + 1
      
    j = j + 1
print("The occurence is" , check, "times")


