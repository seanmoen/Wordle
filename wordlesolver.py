class Word:
    def __init__(self, word, colors):
        self.word = word.lower()
        self.colors = colors
        

def green_letter(letter, position, words):
    words[:] = [word for word in words if word[position] == letter]

def gray_letter(letter, words):
    words[:] = [word for word in words if letter not in word]

def yellow_letter(letter, position, words):
    #Get rid of all words without the letter
    words[:] = [word for word in words if letter in word]
    #Get rid of all words with letter at that spot
    words[:] = [word for word in words if word[position] != letter]

def evaluate_word(word, word_list):
    letters = {}
    #Get letters and how frequent they are
    for letter in word.word:
        #Add letter to list and increment if not there and increment it by 1
        letters[letter] = letters.get(letter, 0) + 1
    
    #Evaluate
    #Check for green - easiest
    letter_pos = 0
    print(len(word.word))

    while letter_pos < len(word.word):
        print("Checking letter number: " + str(letter_pos) + " which is: " + word.word[letter_pos])        
        #Easiest case, only one letter occurence
        if letters[word.word[letter_pos]] == 1:
            if word.colors[letter_pos] == "Green":
                green_letter(word.word[letter_pos], letter_pos, word_list)
            if word.colors[letter_pos] == "Yellow":
                yellow_letter(word.word[letter_pos], letter_pos, word_list)
            if word.colors[letter_pos] == "Gray":
                gray_letter(word.word[letter_pos], word_list)
        """
        else:
            #The same
            if word.colors[letter_pos] == "Green":
                green_letter(word.word[letter_pos], letter_pos, word_list)
            #Yikes
            if word.colors[letter_pos] == "Yellow":
                yellow_letter(word.word[letter_pos], letter_pos, word_list)
            #Even more yikes
            if word.colors[letter_pos] == "Yellow":
                yellow_letter(word.word[letter_pos], letter_pos, word_list)
        """
        letter_pos += 1
    return letters

#Input file

possible_words = []
#possible_words = ["avata", "betas", "charl", "delta", "epsil", "fable", "bounce"]


with open("C:\\Users\\Sean Moen\\vscode\\Wordle\\answers.txt", 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        current_word = line[:-1]
        possible_words.append(current_word)

print(len(possible_words))

input_word = Word("Hello", ["Green", "Gray", "Yellow", "Gray", "Gray"])

print(evaluate_word(input_word, possible_words))

print(len(possible_words))






#Test
"""
gray_letter("d", possible_words)
gray_letter("a", possible_words)
yellow_letter("n", 2, possible_words)
gray_letter("c", possible_words)
yellow_letter("e", 4, possible_words)

gray_letter("h", possible_words)
yellow_letter("e", 1, possible_words)
yellow_letter("r", 2, possible_words)
gray_letter("o", possible_words)
yellow_letter("n", 4, possible_words)

green_letter("i", 0, possible_words)
green_letter("n", 1, possible_words)
gray_letter("f", possible_words)
yellow_letter("e", 3, possible_words)
yellow_letter("r", 4, possible_words)

print(len(possible_words))

print(possible_words)
"""