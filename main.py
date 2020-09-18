from requests_html import HTMLSession
import random

URL = 'https://www.imdb.com/chart/top/'

session = HTMLSession()
r = session.get(URL)

movie_table = r.html.find('.titleColumn')

movies = []

for i in movie_table:
    movies.append(i.text)
    
r_number = random.randint(0, len(movies))

print(f'Your movie for today is {movies[r_number]}')