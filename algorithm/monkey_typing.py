import random
#define list of alphbet character
keyboard_character = "qwertyuiopasdfghjklzxcvbnm "
characterList = [char for char in keyboard_character]
#print(characterList)

targetSentence = "methiks it is like a weasel"

#Function generates a random string with 27 character long 

def Shakespeare_Sentence_Generator(length):
	sentence = ''
	i = 1
	while i<=length:
		r = random.randrange(0,length,1)
		sentence += characterList[r]
		i+=1
	return sentence

#print(Shakespeare_Sentence_Generator(27))

def Evaluate_Matching(generated_sentence, target_sentence):
	#looping through the length of string matching one by one and count the matching pair
	min_length = len(generated_sentence) if len(generated_sentence)<= len(target_sentence) else len(target_sentence)
	matching_score = 0

	for i in range(min_length):
		if generated_sentence[i] == target_sentence[i]:
			matching_score += 1
	#print("You compare following strings: \n%s\n%s" % (generated_sentence, target_sentence))
	#print("Matching score is: %r" % matching_score)

	return matching_score

#####Now try to run 1000 round and find the best.

generated_sentence = ""
best_sentence = ""
best_matching_score = 0

for i in range(1000000):
	generated_sentence = Shakespeare_Sentence_Generator(27)
	matching_score = Evaluate_Matching(generated_sentence, targetSentence)
	if matching_score > best_matching_score:
		best_matching_score = matching_score
		best_sentence = generated_sentence
		print("the better result of turn %d is matching score %r, and sentence %r" % (i, best_matching_score, best_sentence))

print("The best matching sentence in 1000 generates is %s with matching score as %d" % (best_sentence, best_matching_score))

