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

            starttime = time.time()
            result = linearSearch(search_item, dictionary)
            endtime = time.time()
            if result == -1:
                print(f"item not in dictonary({endtime - starttime} seconds)")
            else:
                print(f"item is in line {result} of dictonary({endtime - starttime} seconds)")

        elif menu_selection == "2":

            search_item = input("Please Enter a Word:")

            starttime = time.time()
            result = binarySearch(search_item, dictionary)
            endtime = time.time()
            if result == -1:
                print(f"item not in dictonary({endtime - starttime} seconds)")
            else:
                print(f"item is in line {result} of dictonary({endtime - starttime} seconds)")

        elif menu_selection == "3":

            search_item = input("Please Enter a Word:")

            starttime = time.time()
            result = linearSearch(search_item, aliceWords)
            endtime = time.time()
            if result == -1:
                print(f"item not in alice in wonderland ({endtime - starttime} seconds)")
            else:
                print(f"item is in line {result} of alice in wonderland ({endtime - starttime} seconds)")
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


def linearSearch(input, dictonary):
    for i in range(len(dictonary)):
        if dictonary[i] == input:
            return i

    return -1

def binarySearch(item, dictonary):
    lower_index = 0
    higher_index = len(dictonary) - 1
    while lower_index <= higher_index:
        middle_index = ( lower_index + higher_index ) // 2
        if item == dictonary[middle_index]:
            return middle_index
        elif item < dictonary[middle_index]:
            higher_index = middle_index - 1
        elif item > dictonary[middle_index]:
            lower_index = middle_index + 1
    return -1


# Call main() to begin program
main()

