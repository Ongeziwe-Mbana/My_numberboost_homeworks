
print("Lets play with words!!")
print()
print("Please enter the first word where the first character occurs more than once!")
print()
print("The word doesn't have to be an actual word!")

#prompt the user to input word and set it by default to lowercase

word = input().lower()

print()
print("Now please enter a character that you want to switch the other occurrences to ")

#prompt the user to enter any character and store the character in a variable
nu_char = input()

#make sure the user enters just1 character
while len(nu_char)>1:

    print("Enter just 1 character")
    nu_char = input()

print("Your word is "+word+ "You'll have to enter " +str(len(word)-1)+ "words")

#separate the rest of the word from the first char and replace the other occurence with the char enteres by user
word1 = word.replace(word[0], nu_char)[1:]

#now change the first character back to its original character
word2 = word1.replace(word1[0], word[0:1])[0]

# combine word1 and word2 for the final word and uppercase first letter
new_word =word[0].upper()+word[0]+word1+word2

#create empty list to store the words
lst = []

#add the final first word to list
lst.append(new_word)

# Declare and initialize counter
cnt = 0

print("The program will continue requiring words that have re occurring characters")
print()
print("All that depending on as many times equivalent to the length of the first word")
print()
print("Enter more words")

# loop by the length of the first word
while cnt < (len(word)-1):
    # prompt the user to input word and set it by default to lowercase
    other_word = input().lower()
    #increment the value of the counter by 1
    cnt +=1

    # separate the rest of the word from the first char and replace the other occurence with the char enteres by user
    other_word1 = other_word.replace(other_word[0], nu_char)[1:]

    # now change the first character back to its original character and uppercase it
    other_word2 = other_word1.replace(other_word1[0], other_word[0:1])[0]

    # combine other_word1 and other_word2 for the final word
    newer_word =other_word[0].upper()+other_word1+other_word2

    #add word to the list
    lst.append(newer_word)



#print each word in a newline
for i in (lst):

    print(i)