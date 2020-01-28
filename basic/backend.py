from bs4 import BeautifulSoup as SOUP
import requests as HTTP

###---genres---
genres = ['comedy','sci-fi','horror','romance','musical','action','war','thriller','biography','drama','mystery','crime','family','western','animation','history','documentary','adventure','fantasy','short','comedy,romance','action,comedy','talk-show','game-show']
print("-----------GENRES-------------")
c = 0
for r in range(24):
    print(genres[r],end="\t\t")
    c+=1
    if c==5:
        c = 0
        print()
print("\n"+"-"*30)
###--------------

genre = input("Enter a genre to search : ")
url = 'https://www.imdb.com/search/title/?genres='+genre+'&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=HJGEZ0WGPGEPNBKSJH8A&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3'

response = HTTP.get(url)        ##to get to whole page content
data = response.text
soup = SOUP(data,"lxml")        ##parsing the data to xml format

movies = soup.find_all('div',{'class':'lister-item-content'})

##---print header----
print("-"*30)
print("S.No\tName |||  Year  |||  Rating")
print("-"*30)
##-------------------
ind = 1
for movie in movies:
    title = movie.find_all('a')
    title = str(title).split('>')

    year = movie.find_all('span',{'class':'lister-item-year text-muted unbold'})
    year = str(year).split('>')

    rating = movie.find_all('strong')
    rating = str(rating).split('>')

    if(len(rating)==1):
        print(str(ind)+"\t\t"+title[1][:-3]+"  |||  "+year[1][:-6]+"  |||  "+"Unrated")
    else:
        print(str(ind)+"\t\t"+title[1][:-3]+"  |||  "+year[1][:-6]+"  |||  "+rating[1][:3])
    ind+=1
