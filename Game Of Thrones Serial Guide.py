import webbrowser

link = 'http://hdrezka-ag.com/series/fantasy/45-igra-prestolov-2011-tv-series-1.html#t:65-s:season-e:episode'
print("Hey! I can help you to navigate to the 'Game of Thrones' any season and episode!")
season = int(input("First type the number of the season you want to watch: "))
episode = int(input("Now type the number of the episode you want to see: "))
if season > 8:
    print("Incorrect value. GoT has only 8 seasons. Try again.", )
    exit(0)
elif episode > 10:
    print("Incorrect value. That season has 10 episodes. Try again.")
    exit(0)
elif season == 7 and episode > 7:
    print("Incorrect value. Season 7 has 7 episodes. Try again.")
    exit(0)
elif season == 8 and episode > 6:
    print("Incorrect value. Season 8 has 6 episodes. Try again.")
    exit(0)
print("Enjoy:)")
readyLink = link.replace('season', str(season)).replace('episode', str(episode))
webbrowser.open(readyLink)