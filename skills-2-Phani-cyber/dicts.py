"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """
def wordsD(text):
    myList = text.lower().split('.')
    myDict = {}

    for i in range(len(myList)):
        words = myList[i].split()
        print(words)
        for word in words:
        
            if word not in myDict:
                myDict[word] = 1
            else:
                myDict[word] += 1

    return myDict
print(wordsD("rose is a rose is a rose"))




     #return




def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """
melons = {
    "Honeydew"  :2.50, 
    "Cantaloupe" : 2.50, 
    "Watermelon" : 2.95,
    "Musk" : 3.25,
    "Crenshaw" : 3.25,
    "Christmas" : 14.25}

for k in (melons):
    if(melons[k] ==2.50):
        print(k, melons[k])


for k in (melons):
    if(melons[k] ==2.95):
        print(k, melons[k])


def translate_to_pirate_talk(sentence):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    piratedict = {'sir' : 'matey', 'hotel' : 'fleabag inn' , 'student' : 'swabbie', 'man' : 'mattey', 'professor' : 'foul blaggert' , 'restaurent' : 'galley', 'your' : 'yer' ,'excuse' : 'arr' , 'students' : 'swabbies' , 'are' :'be' ,'restroom' : 'head' ,'my' : 'me' ,'is' : 'be'}
    pirateSentence = ''
    wordlist = sentence.split()
    for i in wordlist:
        if  i in piratedict:
            i = piratedict[i]
        pirateSentence = pirateSentence + ' ' + i
    return pirateSentence
print (translate_to_pirate_talk('my student is not a man'))


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:
        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    words = names

    word_dict = {}
    first_word = None
    for word in words:
        if(first_word is None):
            for i in range(1, len(words)):
                if(word[-1] == words[i][0]):
            
                    word_dict[word] = words[i]
                    words.pop(i)
                    break
                first_word = words[0]
    words.pop(0)
    #print(words)
    for word in words:
        if(word not in word_dict and word not in word_dict.values()):
            for i in range(1, len(words)):
                if(words[i] not in word_dict and words[i] not in word_dict.values()):
                    if(word[-1] == words[i][0]):
                        word_dict[word] = words[i]
    return word_dict
names = ["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"]
print(kids_game(names))
    
