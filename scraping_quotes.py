import requests
from bs4 import BeautifulSoup
from csv import writer

with open("quotes.csv", "w", newline="", encoding="utf-8") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["quote", "author", "bio url"])
	page = 1
	while True:
		url = "http://quotes.toscrape.com/page/" + str(page) + "/"
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "html.parser")
		quotes = soup.select(".quote")
		for quote in quotes:
			text = quote.select(".text")[0].get_text()
			author = quote.select(".author")[0].get_text()
			url = quote.find("a")["href"]
			csv_writer.writerow([text, author, url])
		if soup.select(".next"):
			page += 1
		else:
			break

