# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85

import string

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
	word = word.upper()
	letterPoints = ""
	for char in word:
		for point_value in OLD_POINT_STRUCTURE:
			if char in OLD_POINT_STRUCTURE[point_value]:
				letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)
	return letterPoints

def transform(dict):
	new_dict = {}
	new_dict[" "] = 0
	for key in dict:
		for char in (dict[key]):
			new_dict[char.lower()] = key
	return new_dict

new_point_structure = transform(OLD_POINT_STRUCTURE)

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
	print("Let's play some Scrabble!\n")
	user_word = input("Please enter a word to be scored: ")
	while user_word == "":
		print("Please enter a valid word.")
		user_word = input("Please enter a word to be scored: ")
	for i in range(len(user_word)):
		while user_word[i] not in new_point_structure.keys():
			print("Please enter a valid word.")
			user_word = input("Please enter a word to be scored: ")
	return user_word

def simple_scorer(word):
	word = word.replace(" ", "") 
	return len(word)

def vowel_bonus_scorer(word):
	vowels = ["A","E","I","O","U"]
	total = 0
	word = word.replace(" ", "")
	for char in word:
		if char.upper() not in vowels:
			total += 1
		else:
			total += 3
	return total

def scrabble_scorer(word):
	total = 0
	for char in word:
		total += new_point_structure[char.lower()]
	return total

scoring_algorithms = ()
simple_scorer_dict = {
	"name" : "Simple Score",
	"description" : "Each letter is worth 1 point.",
	"scoring_function" : simple_scorer 
} 
vowel_bonus_scorer_dict = {
	"name" : "Bonus Vowels",
	"description" : "Vowels are 3 pts, consonants are 1 pt.",
	"scoring_function" : vowel_bonus_scorer
}
old_scrabble_scorer_dict = {
	"name" : "Scrabble",
	"description" : "The traditional scoring algorithm.	",
	"scoring_function" : scrabble_scorer 
} 

scoring_algorithms = list(scoring_algorithms)
scoring_algorithms.append(simple_scorer_dict)
scoring_algorithms.append(vowel_bonus_scorer_dict)
scoring_algorithms.append(old_scrabble_scorer_dict)
scoring_algorithms = tuple(scoring_algorithms)

def scorer_prompt(word):
	print("Which scoring algorirthm would you like to use?\n")
	for i in range(len(scoring_algorithms)):
		print(f"{i} - {scoring_algorithms[i]['name']}: {scoring_algorithms[i]['description']}")	
	user_choice = (input("Enter 0, 1, or 2: "))
	while user_choice == "" or user_choice not in string.digits or int(user_choice) < 0 or int(user_choice) > 2:
		print("Please enter a valid option")
		user_choice = (input("Enter 0, 1, or 2: "))
	user_choice = int(user_choice)
	print(f"Score for '{word}': {scoring_algorithms[user_choice]['scoring_function'](word)}")
	
def run_program():
	word = initial_prompt()
	scorer_prompt(word)

