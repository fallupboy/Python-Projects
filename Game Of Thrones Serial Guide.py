import webbrowser

link = 'http://hdrezka-ag.com/series/fantasy/45-igra-prestolov-2011-tv-series-1.html#t:65-s:season-e:episodes'
print("Hey! I can help you to navigate to the 'Game of Thrones' any season and episode!")
season = (input("First type the number of the season you want to watch: "))
episodes = (input("Now type the number of the episode you want to see: "))
choice = [season, episodes]
if choice[0] > '8':
    print("Incorrect value. GoT has only 8 seasons! Try again.", )
    exit(0)
elif choice[0] == '7' and choice[1] > '7':
    print("Incorrect value. Season 7 has 7 episodes. Try again.")
    exit(0)
elif choice[0] == '8' and choice[1] > '4':
    print("Incorrect value. Season 8 has 6 episodes and there are only 4 series have been released. Try again!",)
    exit(0)
print("Enjoy:)")
readyLink = link.replace('season', season).replace('episodes', episodes)
webbrowser.open(readyLink)
