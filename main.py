from modules import Playlist
from modules.musiclibrary import MusicLibrary, ArrayList, Track
from modules.Queue import Queue
from modules.database import load, save
from datetime import time, datetime, timedelta

options = {"Main": [
    "Enter Music Library",
    "View List of Playlists",
    "Create Playlist",
    "View Albums",
    "Exit"
],
"track": [
    "Add to a Playlist",
    "Delete",
    "Exit"
],
"musiclibrary": [
    "Search",
    "Select",
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
    "Clear",
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
                    print(f"[{count}] {choice.format('On') if q.isshuffle() else choice.format('On')}")
                else:
                    print(f"[{count}] {choice}")
            else:
                print(f"[{count}] {choice}")

def displayTrack(t: Track):
    print(t.__str__("inside"))
    MENU('track')
    choice = choose("Enter choice: ")
    if choice == '1':
        playlist_name = choose("Enter Playlist Name to add the track: ")
        print(f"Track '{t.title}' added to playlist '{playlist_name}'.")
    elif choice == '2':
        confirmation = choose("Are you sure you want to delete this track? (yes/no): ")
        if confirmation.lower() == 'yes':
            print(f"Track '{t.title}' has been deleted.")
    elif choice == '3':
        print("Exiting track options.")
    else:
        print("Invalid choice. Please try again.")
        displayTrack(t)

def displayqueue(q:Queue):
    while True:
        print(q)
        MENU('queue', q=q)
        choice = choose("Enter choice: ")
        if choice == 1:
            if q.pause():
                q.pause(False)
            q.pause()
        elif choice == 2:
            if q.repeat():
                q.repeat(False)
            q.repeat()
        elif choice == 3:
            if q.shuffle():
                q.shuffle(False)
            q.shuffle()
        elif choice == 4:
            q.next()
        elif choice == 5:
            q.previous()
        
        elif choice == 7:
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

def displayMusicLibrary(m:MusicLibrary, al:ArrayList):
    print("Entering Music Library...")
    # Implement search, select, play, create track, next page, previous page options here
    if m:
        print(m)
    else:
        print("Music Library is not loaded")

    MENU('musiclibrary')
    choice = choose("Enter choice: ")
    if choice == '1':
        search_term = choose("Enter search term: ")
        print(f"Searching for '{search_term}' in music library...")
    elif choice == '2':
        print("Selecting a track...")
        # Implement logic to select a track
    elif choice == '3':
        print("Playing music library")
        m.play()
        displayqueue(m.getQueue())
    elif choice == '4':
        t=createTrack()
        
        m.add(t)
    elif choice == '5':
        print("Next page of music library...")
        # Implement logic for next page
    elif choice == '6':
        print("Previous page of music library...")
        # Implement logic for previous page
    elif choice == '7':
        print("Exiting music library.")
    else:
        print("Invalid choice. Please try again.")
        displayMusicLibrary()

def displayPlaylists(pll):
    print("Viewing List of Playlists...")
    print(f'''
=================================
            PLAYLISTS
=================================
''')
    print(pll.__str__(counter = True))
    # Implement logic to display playlists
    MENU('playlist-external')
    choice = choose("Enter choice: ")
    if choice == '1':
        playlist_name = choose("Enter Playlist Name to select: ")
        print(f"Selected Playlist: '{playlist_name}'.")
        # Implement logic to view the selected playlist
    elif choice == '2':
        print("Next page of playlists...")
        # Implement logic for next page
    elif choice == '3':
        print("Previous page of playlists...")
        # Implement logic for previous page
    elif choice == '4':
        print("Exiting playlist options.")
    else:
        print("Invalid choice. Please try again.")
        displayPlaylists()

def createPlaylist(db:ArrayList):
    playlist_name = choose("Enter Playlist Name: ")
    pl = Playlist.create(playlist_name)
    db.add(pl)
    print(f"Playlist '{playlist_name}' created.")
    # Implement logic to actually create the playlist

def viewAlbums(ab):
    print("Viewing Albums...")
    # Implement logic to view albums
    print(f'''
===============================
            ALBUMS
===============================
''')
    print(ab)
    # You could use a different menu if needed
    choice = choose("Enter choice: ")
    if choice == '1':
        print("Viewing album details...")
        # Implement logic to view album details
    elif choice == '2':
        print("Exiting album view.")
    else:
        print("Invalid choice. Please try again.")
        viewAlbums()

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
            displayMusicLibrary(ml, al)
        elif choice == '2':
            displayPlaylists(pll)

        elif choice == '3':
            createPlaylist(pll)

        elif choice == '4':
            ab = load('albums')
            viewAlbums(ab)
        elif choice == '5':
            print("Exiting the application.")
            save(ml, 'musiclibrary')
            save(pll, 'playlists')
            # save(al, 'albums')
            return  # Exit the application
        else:
            print("Invalid choice. Please try again.")
            displayMain()

# Start the application by displaying the main menu
displayMain()