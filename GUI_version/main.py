###GUI Movie Recommender By scrapping  IMDB pages

from bs4 import BeautifulSoup as SOUP
import requests as HTTP
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def Output(Page1,genre,fgc,bgc):
    Page1.destroy()
    Page2 = Canvas(root)
    Page2.configure(bg='#cce6ff')

    heading = "TOP 50 MOVIES OF "+ genre.upper() +" GENRE ARE :"
    head = Label(Page2,text = heading, fg="black", bg='#1affff', height=2, width=50,font=("Times New Roman", 16,'bold'))
    head.grid(row=0,column = 0,columnspan = 5)

    ###main heart/core of the application
    movies_display = "RANK\tMOVIE NAME\t\t\t\tYEAR\t        RATING\n"
    movies_display+=('-'*5 + '\t' + '-'*35 + '\t\t\t\t' + '-'*7 + '\t        ' + '-'*10 + '\n')
    url = 'https://www.imdb.com/search/title/?genres=' + genre + '&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=HJGEZ0WGPGEPNBKSJH8A&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_3'
    response = HTTP.get(url)  ##to get to whole page content
    data = response.text
    soup = SOUP(data, "lxml")  ##parsing the data to xml format
    movies = soup.find_all('div', {'class': 'lister-item-content'})

    ind = 1
    for movie in movies:
        title = movie.find_all('a')
        title = str(title).split('>')

        year = movie.find_all('span', {'class': 'lister-item-year text-muted unbold'})
        year = str(year).split('>')

        rating = movie.find_all('strong')
        rating = str(rating).split('>')

        title_final = title[1][:-3]

        if (len(rating) == 1):
            movies_display+=str(ind) + "\t" + title_final[:35] + "\t\t\t\t" + year[1][:-6] + "\t\t" + "---\n"
        else:
            movies_display+=str(ind) + "\t" + title_final[:35] + "\t\t\t\t" + year[1][:-6] + "\t\t" + rating[1][:3]+"\n"
        ind += 1
    ##


    display = ScrolledText(Page2,width=60, height=25, bg = bgc,fg = fgc,font = ("Comic Sans MS",12))
    display.insert(END,movies_display)
    display.grid(row=1,column=0,columnspan=5,rowspan=5,padx=10,pady=10)
    display.configure(state = DISABLED)

    back_button = Button(text="Back", fg="white", bg='#003366', height=1, width=8, font=("Comic Sans MS", 14),command = lambda: Input(Page2))
    back = Page2.create_window(10,690,anchor = SW,window = back_button)

    end_button = Button(text="Quit", fg="white", bg='#660000', height=1, width=8, font=("Comic Sans MS", 14),command=Finish)
    back = Page2.create_window(630, 690, anchor=SE, window=end_button)

    Page2.pack()


def Input(Page2):
    Page2.destroy()
    Page1 = Canvas(root)
    Page1.configure(bg='#cce6ff',width=750,height=750)

    main_heading = Label(Page1, text="GENRE BASED MOVIE RECOMMENDER", fg="black", bg='#b366ff', height=2, width=50,font=("Times New Roman", 16,'bold'))
    main_heading.grid(row=0, column=0, columnspan=4)

    genres_option = Label(Page1, text="Choose one of the below genres :", fg="white", bg='#001a66', height=2, width=50,font=("Comic Sans MS", 14))
    genres_option.grid(row=1, column=0, columnspan=4)

    # ---------
    comedy = Button(Page1, text="Comedy", fg="black", bg='#ffcc00',activebackground = "#ff0000",height=3, width=13, font=("Comic Sans MS", 14),command = lambda :Output(Page1,"comedy","black",'#ffcc00'))
    comedy.grid(row=2, column=0, padx=10, pady=10)

    action = Button(Page1, text="Action", fg="white", bg='#800040', height=3, width=13,activebackground = "#ff0000",font=("Comic Sans MS", 14),command= lambda :Output(Page1,"action","white",'#800040'))
    action.grid(row=2, column=1, padx=10, pady=10)

    drama = Button(Page1, text="Drama", fg="black", bg='#33cc33', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"drama","black",'#33cc33'))
    drama.grid(row=2, column=2, padx=10, pady=10)

    horror = Button(Page1, text="Horror", fg="white", bg='#333300', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"horror","white",'#333300'))
    horror.grid(row=2, column=3, padx=10, pady=10)
    # -----

    scifi = Button(Page1, text="Sci-Fi", fg="black", bg='#33ccff', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"sci_fi","black",'#33ccff'))
    scifi.grid(row=3, column=0, padx=10, pady=10)

    romance = Button(Page1, text="Romance", fg="white", bg='#cc0052', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"romance","white",'#cc0052'))
    romance.grid(row=3, column=1, padx=10, pady=10)

    musical = Button(Page1, text="Musical", fg="black", bg='#ff33ff', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"musical","black",'#ff33ff'))
    musical.grid(row=3, column=2, padx=10, pady=10)

    family = Button(Page1, text="Family", fg="white", bg='#000066', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"family","white",'#000066'))
    family.grid(row=3, column=3, padx=10, pady=10)
    # -----

    adventure = Button(Page1, text="Adventure", fg="black", bg='#aaff00', height=3, width=13,activebackground = "#ff0000",font=("Comic Sans MS", 14), command= lambda :Output(Page1,"adventure","black",'#aaff00'))
    adventure.grid(row=4, column=0, padx=10, pady=10)

    war = Button(Page1, text="War", fg="white", bg='#663300', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"war","white",'#663300'))
    war.grid(row=4, column=1, padx=10, pady=10)

    mystery = Button(Page1, text="Mystery", fg="black", bg='#ff9933', height=3,activebackground = "#ff0000", width=13, font=("Comic Sans MS", 14),command= lambda :Output(Page1,"mystery","black",'#ff9933',))
    mystery.grid(row=4, column=2, padx=10, pady=10)

    crime = Button(Page1, text="Crime", fg="white", bg='#4d0000', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command= lambda :Output(Page1,"crime","white",'#4d0000'))
    crime.grid(row=4, column=3, padx=10, pady=10)
    # -----

    thriller = Button(Page1, text="Thriller", fg="black", bg='#9999ff', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command=lambda :Output(Page1,"thriller","black",'#9999ff'))
    thriller.grid(row=5, column=0, padx=10, pady=10)

    animation = Button(Page1, text="Animation", fg="white", bg='#006666', height=3, width=13,activebackground = "#ff0000",font=("Comic Sans MS", 14), command=lambda :Output(Page1,"animation","white",'#006666'))
    animation.grid(row=5, column=1, padx=10, pady=10)

    history = Button(Page1, text="History", fg="black", bg='#b2b266', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command=lambda :Output(Page1,"history","black",'#b2b266'))
    history.grid(row=5, column=2, padx=10, pady=10)

    fantasy = Button(Page1, text="Fantasy", fg="white", bg='#990099', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command=lambda :Output(Page1,"fantasy","white",'#990099'))
    fantasy.grid(row=5, column=3, padx=10, pady=10)
    # -----

    biography = Button(Page1, text="Biography", fg="black", bg='#c68c53', height=3, width=13,activebackground = "#ff0000",font=("Comic Sans MS", 14), command=lambda :Output(Page1,"biography","black",'#c68c53'))
    biography.grid(row=6, column=0, padx=10, pady=10)

    talkshow = Button(Page1, text="Talk-Show", fg="white", bg='#660066', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command=lambda :Output(Page1,"talk_show","white",'#660066'))
    talkshow.grid(row=6, column=1, padx=10, pady=10)

    gameshow = Button(Page1, text="Game-Show", fg="black", bg='#ff4da6', height=3, width=13,activebackground = "#ff0000", font=("Comic Sans MS", 14),command=lambda :Output(Page1,"game_show","black",'#ff4da6'))
    gameshow.grid(row=6, column=2, padx=10, pady=10)

    documentary = Button(Page1, text="Documentary", fg="white", bg='#004d00', height=3,activebackground = "#ff0000", width=13,font=("Comic Sans MS", 14),command=lambda :Output(Page1,"documentary","white",'#004d00'))
    documentary.grid(row=6, column=3, padx=10, pady=10)

    Page1.pack()


def Finish():
    root.destroy()



if __name__ == '__main__':
    root = Tk()
    root.title("Movie Recommender")
    root.geometry("700x700+400+50")
    root.configure(bg='#cce6ff')

    Page2 = Canvas(root)
    Page2.configure(bg='#cce6ff')
    Page2.pack()

    Input(Page2)

    root.mainloop()
