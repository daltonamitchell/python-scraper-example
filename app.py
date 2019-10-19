# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

quote_page = "http://mlb.mlb.com/stats/sortable.jsp#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Team+hitting&game_type='R'&season=2019&season_type=ANY&league_code='MLB'&sectionType=st&statType=hitting&page=1&ts=1571522635349&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

print(soup)

# name_box = soup.find('h1', attrs={'class': 'name'})
# name = name_box.text.strip()

# print(name)
