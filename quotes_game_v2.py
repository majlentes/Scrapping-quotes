from csv import reader
from random import choice
import requests
from bs4 import BeautifulSoup

def read_quotes(filename):
	with open(filename, encoding="utf-8") as file:
	    csv_reader = reader(file)
	    return list(csv_reader)

quotes = read_quotes("quotes.csv")

def start_game(quotes):

	random_quote = choice(quotes)
	text = random_quote[0]
	print("Here's a quote: ")
	print(text)
	answer = random_quote[1]
	remaining_guesses = 4
	guess = ""

	while guess.lower() != answer.lower() and remaining_guesses > 0:
	    guess = input(f"Who said this quote? Guesses remaining: {remaining_guesses} \n")
	    remaining_guesses -= 1
	    if guess.lower() == answer.lower():
	    	print("You got it right!")
	    	break
	    if remaining_guesses == 3:
	        url = "http://quotes.toscrape.com" + random_quote[2]
	        response = requests.get(url)
	        soup = BeautifulSoup(response.text, "html.parser")
	        birth_date = soup.find(class_="author-born-date").get_text()
	        birth_place = soup.find(class_="author-born-location").get_text()
	        print(f"Wrong answer :( Here's a hint!:\nThe author was born in {birth_date} {birth_place}")
	    elif remaining_guesses == 2:
	        print(f"Wrong answer :( Here's a hint!:\nAuthor's name starts with letter {answer[0]}")
	    elif remaining_guesses == 1:
	        print(f"Wrong answer :( Here's a hint!:\nAuthor's surname starts with letter {answer.split()[1][0]}")
	    else:
	    	print(f"Sorry you ran out of quesses. The answer was {answer}")

	again = ""
	while again.lower() not in ("y", "yes", "n", "no"):
		again = input("Do you want to play again (y/n)")
	if again.lower() in ("y", "yes"):
		print("Ok, let's play again!")
		return start_game()
	else:
		print("Thanks for playing. Bye!")

start_game(quotes)