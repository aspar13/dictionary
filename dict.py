from json import load
from difflib import get_close_matches as gcm


data = load(open("data.json"))


word = input('enter the word. ').lower()

def meaning(word):
	if word in data:
		return data[word]
	elif gcm(word,data.keys()) != []:
		check = input(f'did you mean "{gcm(word,data.keys())[0]}" instead ? Enter yes(y) or no(n)')
		if check == 'y':
			return data[gcm(word,data.keys())[0]]
		elif check == 'n':
			return "please type the word again"
		else:
			return "The word doesn't exist in the dictonary" 
	else:
		return 'word not found'

ans = meaning(word)

if type(ans) == list:
	for i,item in enumerate(ans):
		print(i,item+'\n')
else:
	print(ans)