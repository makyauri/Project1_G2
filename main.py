from modules import Playlist, ArrayList
from modules.musiclibrary import MusicLibrary, TrackArrayList, Track
from modules.Queue import Queue
from modules.database import load, save
from datetime import time, datetime, timedelta

options = {"Main": [
    "Enter Music Library",
    "View List of Playlists",
    "Create Playlist",
    "Exit"
],
"track": [
    "Add to a Playlist",
    "Exit"
],
"musiclibrary": [
    "Search",
    "Play",
    "Create Track",
    "Next Page",
    "Previous Page",
    "Exit"
],
"playlist-internal": [
    "Play",
    "Next Page",
    "Previous Page",
    "Exit"
],
"playlist-external": [
    "Select Playlist",
    "Next Page",
    "Previous Page",
    "Exit"
],
"queue": [
    "{}",
    "Turn Repeat {}",
    "Turn shuffle {}",
    "Next",
    "Previous",

    "Exit"
]}

def choose(string):
    c = input(string)
    if c == '':
        print('user input cannot be empty')
        return choose(string)
    return c

def MENU(interface:str, q:Queue = None):
    if interface in options:
        count = 0

        for choice in options[interface]:
            count +=1
            if interface == 'queue':
                if count == 1:
                    print(f"[{count}] {choice.format('Play') if q.ispause() else 'Pause'}")
                elif count == 2:
                    print(f"[{count}] {choice.format('On') if q.isrepeat() else choice.format('Off')}")
                elif count == 3:
                    print(f"[{count}] {choice.format('On') if q.isshuffle() else choice.format('Off')}")
                else:
                    print(f"[{count}] {choice}")
            else:
                print(f"[{count}] {choice}")

def displayTrack(t: Track, pll:ArrayList):
    print(t.__str__("inside"))
    MENU('track')
    choice = choose("Enter choice: ")
    if choice == '1':
        playlist_name = choose("Enter Playlist Name to add the track: ")
        i = pll.search(playlist_name)
        if i is not None:
            pll.getitem(i).insert(t)
            print(pll.getitem(i))
            print(f"Track '{t.getTitle()}' added to playlist '{playlist_name}'.")
        else:
            print("Playlist not found.")
    elif choice == '2':
        print("Exiting track options.")
    else:
        print("Invalid choice. Please try again.")
        displayTrack(t, pll)

def displayqueue(q:Queue):
    while True:
        print(q)
        MENU('queue', q=q)
        choice = choose("Enter choice: ")
        if choice == '1':
            if q.ispause():
                q.pause(False)
            else:
                q.pause()
        elif choice == '2':
            if q.isrepeat():
                q.repeat(False)
            else:
                q.repeat()
        elif choice == '3':
            if q.isshuffle():
                q.shuffle(False)
            else:
                q.shuffle()
        elif choice == '4':
            q.next()
        elif choice == '5':
            q.previous()
        
        elif choice == '6':
            break 

def createTrack():
    title = choose("Enter title: ")
    artist = choose("Enter artist: ")
    album = choose("Enter Album: ")
    try:
        h = int(input("Enter hour: "))
        m = int(input("Enter minute: "))
        s = int(input("Enter second: "))
    except ValueError as err:
        print(err)
        return createTrack()
    return Track(title, artist, album, timedelta(hours=h, minutes=m, seconds=s))

def displayMusicLibrary(m:MusicLibrary, pll:None, al:ArrayList):
    print("Entering Music Library...")
    # Implement search, play, create track, next page, previous page options here
    while True:
        if m:
            print(m)
        else:
            print("Music Library is not loaded")

        MENU('musiclibrary')
        choice = choose("Enter choice: ")
        if choice == '1':
            search_term = choose("Enter search term: ")
            print(f"Searching for '{search_term}' in music library...")
            i = m.search(search_term)
            if i is not None:
                displayTrack(m.getitem(i), pll)
        elif choice == '2':
            print("Playing music library")
            m.play()
            displayqueue(m.getQueue())
        elif choice == '3':
            t=createTrack()
            m.insert(t)
        elif choice == '4':
            print("Next page of music library...")
            m.page.nextpage()
        elif choice == '5':
            print("Previous page of music library...")
            m.page.previouspage()
        elif choice == '6':
            print("Exiting music library.")
            break

def displayPlaylist(pl:Playlist):
    while True:
        print(pl.__str__('internal'))
        MENU("playlist-internal")
        choice = choose("Enter choice: ")
        if choice == '1':
            displayqueue(pl.getQueue())
        elif choice == '2':
            pl.page.nextpage()
        elif choice == '3':
            pl.page.previouspage()
        elif choice == '4':
            break

def displayPlaylists(pll:ArrayList):
    print("Viewing List of Playlists...")
    while True:
        print(f'''
    =================================
                PLAYLISTS
    =================================
    ''')
        print(pll.__str__(counter=True))
        MENU('playlist-external')
        choice = choose("Enter choice: ")
        if choice == '1':
            playlist_name = choose("Enter Playlist Name to select: ")
            i = pll.search(playlist_name)
            if i is not None:
                displayPlaylist(pll.getitem(i))
            else:
                print("Playlist not found.")
        elif choice == '2':
            print("Next page of playlists...")
            pll.page.nextpage()
        elif choice == '3':
            print("Previous page of playlists...")
            pll.page.previouspage()
        elif choice == '4':
            break

def createPlaylist(db:ArrayList):
    playlist_name = choose("Enter Playlist Name: ")
    i = db.search(playlist_name)
    if i is None:
        pl = Playlist.create(playlist_name)
        db.insert(pl)
        print(f"Playlist '{playlist_name}' created.")
    else:
        print("Playlist already created.")


def load_data(file_name):
    try:
        return load(file_name)
    except Exception as e:
        print(f"Error loading {file_name}: {e}")
        return None
    
def displayMain():
    pll = load_data('playlists')
    ml = load_data('musiclibrary')
    al = load_data('albums')
    while True:
        print(f'''
===================================================
        Project 1 - Listen to the Music
===================================================
''')
        MENU('Main')
        choice = choose("Enter choice: ")
        if choice == '1':
            displayMusicLibrary(ml, pll, al)
        elif choice == '2':
            displayPlaylists(pll)

        elif choice == '3':
            createPlaylist(pll)

        elif choice == '4':
            print("Exiting the application.")
            save(ml, 'musiclibrary')
            save(pll, 'playlists')
            return  # Exit the application
        else:
            print("Invalid choice. Please try again.")
            displayMain()

# Start the application by displaying the main menu
displayMain()