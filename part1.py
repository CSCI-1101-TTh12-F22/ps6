import sys

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
englishwords = set()
alpha2num = {}



# This reads the top 2000 most common words
# into a global variable set called englishwords
# You do not need to modify this function.
def setenglishdictionary():
    f = open("top2K.txt", encoding="utf=8")
    words = f.read().split()
    f.close()
    englishwords.update(words)

# This void function populates the global variable dictionary alpha2num
# by mapping each letter in the alphabet global variable to its index.
# The alpha2num dictionary should map A to 0, B to 1, C to 2, and so on.
def setalpha2num():
    return

# This function takes two arguments: (1) shiftsize (i.e., the amount 
# to shift the alphabet) and (2) text (i.e., the text you want to decode). 
# It takes the input text character by character, and shifts each character
# by the amount indicated with shiftsize. It then returns the shifted
# text as a string.
def decode(shiftsize, text):
    return


# This boolean function takes a text, splits it into a list of words
# then it checks to see whether each word is in the englishwords
# global variable dictionary. It keeps track of how many of the
# wods are "real words" by trying to find them in the dictionary.
# If at least 1/3 of the words are in the dictionary, return True.
# Otherwise, return false.
def checkgoodness(text):
    return

# This function tries every possible decoding (i.e., shift)
# until it gets a decoding that is likely to be English
# by calling checkgoodness. When it finds a likely 
# English decoding, it returns the shiftsize and the decoded text.
def solvethecipher(text):
    return
        

# Here is a main method I wrote for you.
def main():

    # Call the function I wrote for you that builds
    # the dictionary of English words.
    setenglishdictionary()

    # Call the function that maps each letter to 
    # its corresponding index.
    setalpha2num()

    # Read in a file into a string variable, mytext.
    f = open(sys.argv[1], encoding="utf-8")
    mytext = f.read()
    f.close()

    # Decode the text via brute force.
    beststep, besttext = solvethecipher(mytext)

    # Print out the decoded text.
    print(besttext)
    print("The shift size was: ", beststep)

main()
