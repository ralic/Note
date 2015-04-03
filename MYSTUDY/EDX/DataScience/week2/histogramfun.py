import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    pylab.xlabel('words')
    pylab.ylabel('times')
    count = 0
    hist = [len(filter(lambda x: x in ['a', 'e', 'o', 'u', 'i'], word)) for word in wordList]
    # for word in wordList:
    #     vowel = 0
    #     for letter in word:
    #         if letter in ['a', 'e', 'i', 'o', 'u']:
    #             vowel += 1
    #     less = vowel / float(len(word))
    #     if less <= 0.5:
    #         count += 1
    pylab.xlim()
    pylab.hist(hist, bins=numBins)
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
