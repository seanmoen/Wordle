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
    print(letters)
    
    #Evaluate
    for letter in letters:
        word_count = len(word_list)
        print(word_count)
        #If only one letter
        if len(letters[letter]) == 1:
            letter_pos = letters[letter][0][0]
            letter_color = letters[letter][0][1]
            print("Checking letter: " + letter + " which is at: " + str(letter_pos) + " and is the color " + letter_color)  
            #Easiest case, only one letter occurence
            if letter_color == "Green":
                green_letter(letter, letter_pos, word_list)
            if letter_color == "Yellow":
                yellow_letter(letter, letter_pos, word_list)
            if letter_color == "Gray":
                gray_letter(letter, word_list)
        #Multiple letters
        else:
            has_yellow = False
            is_all_gray = True
            #Check if any letters are gray
            for occurence in letters[letter]:
                position = occurence[0]
                color = occurence[1]
                print("Checking letter:" + letter + " at position: " + str(position) + " which is: " + color)
                if color == "Yellow":
                    has_yellow = True
                if color != "Gray":
                    is_all_gray = False                 
            for occurence in letters[letter]:
                position = occurence[0]
                color = occurence[1]
                if color == "Green":
                    green_letter(letter, position, word_list)
                elif color == "Yellow":
                    yellow_letter(letter, position, word_list)
                #If all gray letters - that letter is not in word
                #If there is only green and gray - only that amount of letters
                #   remove all except at green
                #If there is yellow and gray, - letter is not at gray
                #   normal yellow and single gray suffices
                #   because

                #Note: green and yellow will have done their code for their own letters
                #Gray's behavior is based off the presence of the other letters
                else:
                    if is_all_gray:
                        #Remove all occurences of letter
                        gray_letter(letter, word_list)
                    #is gray, yellow, and possibly green
                    elif has_yellow:
                        #Remove current spot as letter cannot be there
                        gray_letter_single_spot(letter, position, word_list)
                    #Is green and gray, keep green get rid of rest 
                    else:
                        green_positions = []
                        for occurence in letter:
                            if occurence[1] == "Green":
                                green_positions.append(occurence[0])
                        letter_pos = 0
                        while letter_pos < len(word):
                            if letter_pos not in green_positions:
                                gray_letter_single_spot(letter, letter_pos, word_list)
                            letter_pos += 1
            print(occurence)
        print("Dropped words: " + str(word_count - len(word_list)))
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

input_word = "horse"
input_colors = ["Gray", "Gray", "Gray", "Yellow", "Gray"]
print(evaluate_word(input_word, input_colors, possible_words))

input_word = "assay"
input_colors = ["Gray", "Yellow", "Gray", "Gray", "Gray"]
print(evaluate_word(input_word, input_colors, possible_words))

input_word = "ficus"
input_colors = ["Gray", "Yellow", "Gray", "Gray", "Yellow"]
print(evaluate_word(input_word, input_colors, possible_words))

input_word = "skill"
input_colors = ["Green", "Gray", "Green", "Green", "Green"]
print(evaluate_word(input_word, input_colors, possible_words))

input_word = "spill"
input_colors = ["Green", "Gray", "Green", "Green", "Green"]
print(evaluate_word(input_word, input_colors, possible_words))

input_word = "still"
input_colors = ["Green", "Green", "Green", "Green", "Green"]
print(evaluate_word(input_word, input_colors, possible_words))

print(len(possible_words))

print(possible_words)
