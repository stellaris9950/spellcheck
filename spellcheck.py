# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    loop = True
    while loop:
        print("\n***  MAIN MENU ***"
              "\n* 1: Spell Check a Word (Linear Search)"
              "\n* 2: Spell Check a Word (Binary Search)"
              "\n* 3: Spell Check Alice In Wonderland (Linear Search)"
              "\n* 4: Spell Check Alice In Wonderland (Binary Search)"
              "\n* 5: Exit")
        menu_selection = input("* Enter Option #: ")

        if menu_selection == "1":
            search_item = input("Please Enter a Word:")
            linearSpellCheck(search_item, dictionary)
        elif menu_selection == "2":
            print("constructing")
        elif menu_selection == "3":
            print("constructing")
        elif menu_selection == "4":
            print("constructing")
        elif menu_selection == "5":
            print("\nGOODBYE!\n")
            loop = False

# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()

def linearSpellCheck(input, dictonary):
    starttime = time.time()

    position = 0
    for i in range(len(dictonary)):
        if dictonary[i] == input:
            check = True
            position = i
        else:
            check = False
        endtime = time.time()
    if check == True:
        endtime = time.time()
        print(f"item is in line{i} of dictonary({endtime - starttime} seconds)")
    else:
        endtime = time.time()
        print(f"item not in dictonary({endtime - starttime} seconds)")
    return -1



# Call main() to begin program
main()
