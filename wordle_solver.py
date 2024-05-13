#Sean Moen
#May 19, 2023
#A program to give possible Wordle words after given input
#TODO: Add a visual way to input, possibly through a webapp

def green_letter(letter, position, word_list):
    word_list[:] = [word for word in word_list if word[position] == letter]

def gray_letter(letter, word_list):
    word_list[:] = [word for word in word_list if letter not in word]

def gray_letter_single_spot(letter, position, word_list):
    #Get rid of all words with letter at that spot
    word_list[:] = [word for word in word_list if word[position] != letter]

def yellow_letter(letter, position, word_list):
    #Get rid of all words without the letter
    word_list[:] = [word for word in word_list if letter in word]
    #Get rid of all words with letter at that spot
    word_list[:] = [word for word in word_list if word[position] != letter]

def remove_not_enough_letters(letter, num_occurences, word_list):
    #Check amount of letters in word and remove if its not enough
    word_list[:] = [word for word in word_list if word.count(letter) > num_occurences]

def evaluate_word(word, colors, word_list):
    word = word.lower()
    #letters is a dictionary of a list of lists
    #one list for each occurence of letter
    #each occurence contains letter position and its color
    letters = {}
    letter_pos = 0
    while letter_pos < len(word):
        #Add letter to dictionary if it is not there
        if word[letter_pos] not in letters:
            letters[word[letter_pos]] = []
        letters[word[letter_pos]].append([letter_pos, colors[letter_pos]])
        letter_pos += 1    
    #Evaluate
    for letter in letters:
        #If only one letter
        if len(letters[letter]) == 1:
            letter_pos = letters[letter][0][0]
            letter_color = letters[letter][0][1]
            #Easiest case, only one letter occurence
            if letter_color == "Green":
                green_letter(letter, letter_pos, word_list)
            if letter_color == "Yellow":
                yellow_letter(letter, letter_pos, word_list)
            if letter_color == "Gray":
                gray_letter(letter, word_list)
        #Multiple letters
        else:
            #Check if any letters are yellow and the min amount of letters in the word
            has_yellow = False
            min_letters_in_word = 0
            for occurence in letters[letter]:
                position = occurence[0]
                color = occurence[1]
                if color == "Yellow":
                    has_yellow = True
                if color != "Gray":
                    min_letters_in_word += 1
            #remove all words with less than letters in the word
            #remove_not_enough_letters(letter, min_letters_in_word, word_list)             
            for occurence in letters[letter]:
                position = occurence[0]
                color = occurence[1]
                if color == "Green":
                    green_letter(letter, position, word_list)
                elif color == "Yellow":
                    yellow_letter(letter, position, word_list)
                else:
                    #Is all gray
                    if min_letters_in_word == 0:
                        #Remove all occurences of letter
                        gray_letter(letter, word_list)
                    #is gray, yellow, and possibly green
                    elif has_yellow:
                        #Remove current spot as letter cannot be there
                        gray_letter_single_spot(letter, position, word_list)
                    #Is green and gray, keep green get rid of rest
                    #Only green and gray
                    else:
                        #Remove all occurences of letter except at green positions
                        green_positions = []
                        for occurence in letters[letter]:
                            if occurence[1] == "Green":
                                green_positions.append(occurence[0])
                        letter_pos = 0
                        while letter_pos < len(word):
                            if letter_pos not in green_positions:
                                gray_letter_single_spot(letter, letter_pos, word_list)
                            letter_pos += 1

#Input file
possible_words = []
with open("answers.txt", 'r') as filehandle:
    filecontents = filehandle.readlines()
    for line in filecontents:
        current_word = line[:-1]
        possible_words.append(current_word)

input_word = "aback"
input_colors = ["Yellow", "Gray", "Gray", "Yellow", "Gray"]
evaluate_word(input_word, input_colors, possible_words)

input_word = "cacao"
input_colors = ["Green", "Green", "Gray", "Gray", "Yellow"]
evaluate_word(input_word, input_colors, possible_words)

input_word = "canoe"
input_colors = ["Green", "Green", "Green", "Green", "Green"]
evaluate_word(input_word, input_colors, possible_words)

print("Total possible words: " + str(len(possible_words)))

print(possible_words)
