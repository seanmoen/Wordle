#Sean Moen
# May 19, 2023
# May 13, 2024 refactor
# A program to give possible Wordle words after given input
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
    word_list[:] = [word for word in word_list if word.count(letter) >= num_occurences]

def remove_too_many_letters(letter, num_occurences, word_list):
    #Check amount of letters in word and remove if its not enough
    word_list[:] = [word for word in word_list if word.count(letter) <= num_occurences]

class Letter:
    def __init__(self, character, color, position):
        self.character = character
        self.color = color
        self.position = position

def evaluate_word(word, colors, word_list):
    word = word.lower()
    #letters is a list of letters
    letters = []
    unique_letters = []
    letter_pos = 0
    while letter_pos < len(word):
        letter = Letter(word[letter_pos], colors[letter_pos], letter_pos)
        letters.append(letter)
        if word[letter_pos] not in unique_letters:
            unique_letters.append(word[letter_pos])
        letter_pos += 1    

    for unique_letter in unique_letters:
        has_non_gray = False
        min_letters_in_answer = 0
        max_letters_in_answer = len(word)
        occurences = []
        for letter in letters:
            if letter.character == unique_letter:
                occurences.append(letter)
                if letter.color == "Yellow" or letter.color == "Green":
                    has_non_gray = True
                if letter.color == "Gray":
                    max_letters_in_answer -= 1
                else:
                    min_letters_in_answer += 1

        #remove all words with less than letters in the word
        remove_not_enough_letters(unique_letter, min_letters_in_answer, word_list)
        remove_too_many_letters(unique_letter, max_letters_in_answer, word_list)
        for occurence in occurences:
            # For single green and multiple green occurences
            if occurence.color == "Green":
                green_letter(occurence.character, occurence.position, word_list)
            # For single Yellow occurence
            elif occurence.color == "Yellow" and len(occurences) == 1:
                yellow_letter(occurence.character, occurence.position, word_list)
            # For Yellow with multiple occurences
            elif occurence.color == "Yellow":
                gray_letter_single_spot(occurence.character, occurence.position, word_list)
            # Only Gray
            elif occurence.color == "Gray" and not has_non_gray:
                gray_letter(occurence.character, word_list)
            # For Gray with Yellow and/or Green
            elif occurence.color == "Gray" and has_non_gray:
                #Remove current spot as letter cannot be there
                gray_letter_single_spot(occurence.character, occurence.position, word_list)

if __name__ == "__main__":
    #Input file
    possible_words = []
    with open("answers.txt", 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            current_word = line[:-1]
            possible_words.append(current_word)
    while (len(possible_words) > 1):
        word = ""
        while len(word) != 5:
            word = input("Enter a 5-letter word: ")
        color_string = ""
        valid_color = False      
        while not valid_color:
            color_string = input("Enter the first letter of each color (green = g, yellow = y, black = b): ")
            colors = []
            for letter in color_string:
                if letter == "g":
                    colors.append("Green")
                if letter == "y":
                    colors.append("Yellow")
                if letter == "b":
                    colors.append("Gray")
            if len(colors) == 5:
                valid_color = True
        evaluate_word(word, colors, possible_words)
        if len(possible_words) > 1:
            print("Possible Words:")
            print(possible_words)
        elif len(possible_words) == 1:
            print(f"The word is: {possible_words[0]}")
        else:
            print("No possible words. (Perhaps a misinput?)")
