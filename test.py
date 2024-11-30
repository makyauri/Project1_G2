from modules import MusicLibrary, Playlist
from modules import Track
from datetime import timedelta
m = MusicLibrary()
p = Playlist("test")
# playlist_manager = PlaylistManager()
def loadML():
    m.add(Track("Song A", "Artist 1", "Album 1", timedelta(minutes=3, seconds=45)))
    m.add(Track("Song B", "Artist 2", "Album 2", timedelta(minutes=4, seconds=20)))
    m.add(Track("Song C", "Artist 1", "Album 1", timedelta(minutes=2, seconds=50)))
    m.add(Track("Song D", "Artist 3", "Album 3", timedelta(minutes=5, seconds=10)))
    m.add(Track("Song E", "Artist 2", "Album 2", timedelta(minutes=3, seconds=30)))
    m.add(Track("Song F", "Artist 1", "Album 1", timedelta(minutes=4, seconds=15)))
    m.add(Track("Song G", "Artist 2", "Album 2", timedelta(minutes=3, seconds=50)))
    m.add(Track("Song H", "Artist 3", "Album 3", timedelta(minutes=2, seconds=30)))
    m.add(Track("Song I", "Artist 1", "Album 1", timedelta(minutes=4, seconds=0)))
    m.add(Track("Song J", "Artist 2", "Album 2", timedelta(minutes=3, seconds=5)))
    m.add(Track("Song K", "Artist 3", "Album 3", timedelta(minutes=4, seconds=45)))
    m.add(Track("Song L", "Artist 1", "Album 1", timedelta(minutes=3, seconds=15)))

def loadPL():
    p.add(Track("Song A", "Artist 1", "Album 1", timedelta(minutes=3, seconds=45)))
    p.add(Track("Song B", "Artist 2", "Album 2", timedelta(minutes=4, seconds=20)))
    p.add(Track("Song C", "Artist 1", "Album 1", timedelta(minutes=2, seconds=50)))
    p.add(Track("Song D", "Artist 3", "Album 3", timedelta(minutes=5, seconds=10)))
    p.add(Track("Song E", "Artist 2", "Album 2", timedelta(minutes=3, seconds=30)))
    p.add(Track("Song F", "Artist 1", "Album 1", timedelta(minutes=4, seconds=15)))
    p.add(Track("Song G", "Artist 2", "Album 2", timedelta(minutes=3, seconds=50)))
    p.add(Track("Song H", "Artist 3", "Album 3", timedelta(minutes=2, seconds=30)))
    p.add(Track("Song I", "Artist 1", "Album 1", timedelta(minutes=4, seconds=0)))
    p.add(Track("Song J", "Artist 2", "Album 2", timedelta(minutes=3, seconds=5)))
    p.add(Track("Song K", "Artist 3", "Album 3", timedelta(minutes=4, seconds=45)))
    p.add(Track("Song L", "Artist 1", "Album 1", timedelta(minutes=3, seconds=15)))

t = Track("Song A", "Artist 1", "Album 1", timedelta(minutes=3, seconds=45))
loadPL()
loadML()
print(p.__str__(mode='internal'))
p.play()
q = p.getQueue()
for i in range(1000):
    q.next()
print(q)