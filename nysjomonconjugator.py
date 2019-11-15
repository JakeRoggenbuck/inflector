space = '               '
noun_place_dict = {"['nom', 'sg']":0, "['nom', 'pl']":1, "['acc', 'sg']":2, "['acc', 'pl']":3,
					"['dat', 'sg']":4, "['dat', 'pl']":5} #Converting endings into list locations
verb_place_dict = {"['1', 'sg']":0, "['2', 'sg']":1, "['3', 'sg']":2,
"['1', 'pl']":3, "['2', 'pl']":4, "['3', 'pl']":5}
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'ø']

def valid_input(question, allowed):
	while True:
		user_input = input(question)
		if user_input not in allowed:
			continue;
		else:
			return user_input

def noun(stem):
	anim = valid_input("Is this noun living or still? ", ['living', 'still'])

	form = valid_input("Would you like a list or a single one? Please type 'single' or 'list'. ", ['single', 'list'])

	if anim == 'living':
		noun_list = [stem, [stem+'an', stem+'na'], stem+'e', stem+'il', stem+'u', stem+'ø'] #List of conjugations
	else:
		noun_list = [stem+'ju', stem+'jan', stem, [stem+'at', stem+'ta'], stem, stem+'um'] #By number, then by case.

	if form == 'list':
		print(noun_list[0] + space + str(noun_list[1]) + '\n' + noun_list[2]
+ space + str(noun_list[3]) + '\n' + noun_list[4] + space + noun_list[5])
	else:
		case = valid_input("What case would you like? Please type 'nom', 'acc', or 'dat'. ", ['nom', 'acc', 'dat'])
		number = valid_input("What number? Is it 'sg' or 'pl'? ", ['sg', 'pl'])

		print(noun_list[noun_place_dict[str([case, number])]])

def syllable_count(stem):
	output = 0
	for char in stem:
		if char in vowel_list: #Defining 'syllable' as a vowel.
			output += 1
	return output

def second_syl(stem):
	if syllable_count(stem) < 2:
		return None
	else: #This SHOULD repeat the second syllable at the beginning.
		word_vowels = []
		for num in range(0, len(stem)):
			char = stem[num]
			if char in vowel_list:
				word_vowels.append(char)
				if len(word_vowels) == 2:
					vowel_index = num
		return (stem[vowel_index-1] + stem[vowel_index])

def redup(stem):
	if syllable_count(stem) == 1:
		if stem[-1] in vowel_list:
			return (stem + stem)
		else:
			return (stem[-1] + 'y' + stem)
	else:
		return second_syl(stem) + stem

def verb(stem):
	print("Sorry, there are too many conjugations. You may only ask for one.")
	tense = valid_input("What tense is the verb? Please type 'present', 'past', or 'future'. ", ['present', 'past', 'future'])
	aspect = valid_input("Is the action a one-time occurrence or a many-time one? Type 'one-time' or 'many-time'. ", ['one-time', 'many-time'])
	if stem[-1] in ['s', 'k', vowel_list, 'n']:
		pl = 't'
	else:
		pl - 'yt'
	present_list = [stem + 'se', stem + 'en', stem, stem + pl, stem + 'on', stem + pl]
	past_list = [stem + 'sen', stem + 'ed', stem + 'píen', stem + 'in', stem + 'o', stem + 'ton']
	if [tense, aspect] == ['present', 'one-time']:
		verb_list = present_list
	elif [tense, aspect] == ['present', 'many-time']:
		verb_list = [stem + 'ote', stem + 'ot', stem + 'ot', stem + 'oten', stem + 'otí', stem + 'otí']
	elif [tense, aspect] == ['past', 'one-time']:
		verb_list = past_list
	elif [tense, aspect] == ['past', 'many-time']:
		verb_list = past_list
		for yeet in verb_list:
			yeet = redup(yeet)
	elif [tense, aspect] == ['future', 'one-time']:
		verb_list = present_list
		for num in range(0, len(verb_list)):
			verb_list[num] = 'te ' + verb_list[num]
	else:
		verb_list = present_list
		for num in range(0, len(verb_list)):
			yeet = 'te ' + redup(verb_list[num])
	print("Now you can choose list form or individual. ")
	form = valid_input("Please choose 'list' or 'individual' ", ['list', 'individual'])
	if form == 'list':
		print(verb_list[0] + space + str(verb_list[3]) + '\n' + verb_list[1]
+ space + str(verb_list[4]) + '\n' + verb_list[2] + space + verb_list[5])
	else:
		ps = valid_input("What person is it? Type '1', '2', or '3'. ", ['1', '2', '3'])
		nm = valid_input("And what number? Is it singular (sg) or plural (pl)? ", ['sg', 'pl'])
		print(verb_list[verb_place_dict[str([ps, nm])]])

def mainloop():
	stem = input("What is your stem? ")
	while True:
		stem_type = input("Is it a noun or a verb? ")
		if stem_type in ['noun', 'verb']:
			break
		else:
			print("Please type 'noun' or 'verb'.")

	if stem_type == 'noun':
		noun(stem)
	else:
		verb(stem)

mainloop()