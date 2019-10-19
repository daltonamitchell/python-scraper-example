# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

# This is the page your scraper will visit. Change it to any web page you'd like to analyze
quote_page = "http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+hitting&game_type='R'&season=2019&season_type=ANY&league_code='MLB'&sectionType=st&statType=hitting&page=1&ts=1571522635349&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

# This opens a connection to the web page
page = urlopen(quote_page)

# This converts the page content into something you're program can work with
soup = BeautifulSoup(page, 'html.parser')

# This prints out what you've got so far to your terminal
print(soup)

# Lines that start with '#' are comments. Your progam will ignore them.
# Remove the '#' in front of these lines to execute them

# Example: find an <h1> tag on the page with a class of name (<h1 class="name">)
# name_box = soup.find('h1', attrs={'class': 'name'})

# Example, use the name element to it's text (assuming the line above actually found something)
# name = name_box.text.strip()
# print(name)
