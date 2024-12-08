import sys
sys.path.append("modules\\")
from modules.trackarraylist import TrackArrayList, Paginate
from Queue import Queue
from track import Track, timedelta

class MusicLibrary(TrackArrayList):
    def __init__(self) -> None:
        super().__init__()
        self.__queue=None
        self.__total:timedelta =timedelta(hours=0,minutes=0,seconds=0)

    def totalDuration(self):
        return self.__total

    def getQueue(self):
        return self.__queue

    def play(self):
        if not self.__queue:
            self.__queue = Queue(self)

    def insert(self, track: Track):
        """Inserts a new track at the correct index point based on title.

        Args:
            track (Track): Track to be inserted.
        """
        if self.length() == 0:
            self.setItematIndex(0, track)
        else:
            if self.length() == self.getMax():
                self.expand()
            self.setItematIndex(self.length(), track)
        self.increaseLength()
        self.__addDuration(track)
        self.page = Paginate(self.length())

    def __findindexInsertion(self, track: Track) -> int:
        """Finds the index to insert based on track title using binary __findindex.

        Args:
            track (Track): Track to compare and to be inserted.

        Returns:
            int: Node insertion point for new track.
        """

        low, high = 0, self.length() - 1
        while low <= high:
            mid = (low + high) // 2
            if self.getitem(mid).getTitle() < track.getTitle():
                low = mid + 1
            else:
                high = mid - 1
        return low  # The insertion point
    

    def search(self, title: str):
        for i in range(len(self.get_list())):
            if self.getitem(i).getTitle() == title:
                return i  # Return the index if the track is found
        print(f"'{title}' not found in music library")  # Print only if not found

    def __findindex(self, track_title: str) -> int:
        """Finds the index of a track based on its title.

        Args:
            track_title (str): The title of the track to find.

        Returns:
            int: The index of the track if found, None otherwise.
        """
        low, high = 0, self.length() - 1
        while low <= high:
            mid = (low + high) // 2
            if self.getitem(mid).getTitle() < track_title:
                low = mid + 1
            elif self.getitem(mid).getTitle() > track_title:
                high = mid - 1
            else:
                return mid  # Track found
        return None  # Track not found

    def __adjustArray(self, start: int, end: int, dir: str = "f") -> None:
        """Adjusts the arrangement of this array from start to end.

        Args:
            start (int): Start index for adjustment.
            end (int): End index for adjustment.
            dir (str): Direction of adjustment: "f" for forward, "b" for backward.
        """
        if dir == 'f':
            for index in range(end, start, -1):
                self.setItematIndex(index, self.getitem(index - 1))
        elif dir == 'b':
            for index in range(start, end):
                self.setItematIndex(index, self.getitem(index + 1))

    def __addDuration(self, t:Track):
        self.__total = self.__total.__add__(t.getDuration())
    
    def __subtrDuration(self, t:Track):
        self.__total = self.__total.__sub__(t.getDuration())
    def __str__(self, counter=True) -> str:
        banner = '''
===================================
           MUSIC LIBRARY
===================================
'''
        return banner+super().__str__(counter)

al = MusicLibrary()
from datetime import timedelta

tracks = [
    Track("Blinding Lights", "The Weeknd", "After Hours", timedelta(minutes=3, seconds=20)),
    Track("Shape of You", "Ed Sheeran", "÷ (Divide)", timedelta(minutes=3, seconds=53)),
    Track("Dance Monkey", "Tones and I", "The Kids Are Coming", timedelta(minutes=3, seconds=29)),
    Track("Someone You Loved", "Lewis Capaldi", "Divinely Uninspired to a Hellish Extent", timedelta(minutes=3, seconds=2)),
    Track("Bad Guy", "Billie Eilish", "When We All Fall Asleep, Where Do We Go?", timedelta(minutes=3, seconds=14)),
    Track("Senorita", "Shawn Mendes & Camila Cabello", "Shawn Mendes", timedelta(minutes=3, seconds=11)),
    Track("Watermelon Sugar", "Harry Styles", "Fine Line", timedelta(minutes=3, seconds=41)),
    Track("Old Town Road", "Lil Nas X", "7", timedelta(minutes=2, seconds=37)),
    Track("Levitating", "Dua Lipa", "Future Nostalgia", timedelta(minutes=3, seconds=23)),
    Track("Peaches", "Justin Bieber", "Justice", timedelta(minutes=3, seconds=18)),
    Track("Stay", "The Kid LAROI & Justin Bieber", "F*CK LOVE 3: OVER YOU", timedelta(minutes=2, seconds=21)),
    Track("Good 4 U", "Olivia Rodrigo", "SOUR", timedelta(minutes=2, seconds=58)),
    Track("Montero (Call Me By Your Name)", "Lil Nas X", "Montero", timedelta(minutes=2, seconds=18)),
    Track("Kiss Me More", "Doja Cat ft. SZA", "Planet Her", timedelta(minutes=3, seconds=28)),
    Track("drivers license", "Olivia Rodrigo", "SOUR", timedelta(minutes=4, seconds=2)),
    Track("Save Your Tears", "The Weeknd", "After Hours", timedelta(minutes=3, seconds=35)),
    Track("Positions", "Ariana Grande", "Positions", timedelta(minutes=2, seconds=52)),
    Track("Shivers", "Ed Sheeran", "=", timedelta(minutes=3, seconds=27)),
    Track("Cold Heart (PNAU Remix)", "Elton John & Dua Lipa", "The Lockdown Sessions", timedelta(minutes=3, seconds=22)),
    Track("Take My Breath", "The Weeknd", "After Hours", timedelta(minutes=3, seconds=40)),
    Track("Butter", "BTS", "Butter", timedelta(minutes=2, seconds=44)),
    Track("Industry Baby", "Lil Nas X & Jack Harlow", "Montero", timedelta(minutes=3, seconds=32)),
    Track("Happier Than Ever", "Billie Eilish", "Happier Than Ever", timedelta(minutes=5, seconds=15)),
    Track("Leave The Door Open", "Bruno Mars & Anderson .Paak", "An Evening with Silk Sonic", timedelta(minutes=4, seconds=2)),
    Track("All of Me", "John Legend", "Love in the Future", timedelta(minutes=4, seconds=27)),
    Track("Perfect", "Ed Sheeran", "÷ (Divide)", timedelta(minutes=4, seconds=23)),
    Track("Rolling in the Deep", "Adele", "21", timedelta(minutes=3, seconds=48)),
    Track("Uptown Funk", "Mark Ronson ft. Bruno Mars", "Uptown Special", timedelta(minutes=4, seconds=30)),
    Track("Thinking Out Loud", "Ed Sheeran", "x (Multiply)", timedelta(minutes=4, seconds=41)),
    Track("Shake It Off", "Taylor Swift", "1989", timedelta(minutes=3, seconds=39)),
    Track("Royals", "Lorde", "Pure Heroine", timedelta(minutes=3, seconds=10)),
    Track("Chasing Cars", "Snow Patrol", "Eyes Open", timedelta(minutes=4, seconds=27)),
    Track("I Will Always Love You", "Whitney Houston", "The Bodyguard", timedelta(minutes=4, seconds=31)),
    Track("Billie Jean", "Michael Jackson", "Thriller", timedelta(minutes=4, seconds=54)),
]

# for t in tracks:
#     al.insert(t)

# print(al.get_list())
# print(al.__str__(counter= True))
# al.delete("All of Me")
# al.play()
# q = al.getQueue()
# q.pause()
# print(q)