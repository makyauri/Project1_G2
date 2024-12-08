import sys
sys.path.append('modules\\')
from modules.trackarraylist import TrackArrayList
from Queue import Queue
from datetime import timedelta, datetime
from track import Track

class Playlist(TrackArrayList):
    def __init__(self, title, date=datetime.now()) -> None:
        super().__init__()
        self.__datecreated = date
        self.__title = title
        self.__queue=None
        self.__total:timedelta =timedelta(hours=0,minutes=0,seconds=0)

    def totalDuration(self):
        return self.__total
    def getdate(self):
        return self.__datecreated
    def title(self):
        return self.__title
    def insert(self, t:Track):
        if type(t) is Track:
            self.__addDuration(t)
            return super().insert(t)
        else:
            print("Invalid given argument type.")

    def play(self):
        if not self.__queue:
            self.__queue = Queue(self)
    
    def getQueue(self):
        if not self.__queue:
            self.play()
        return self.__queue
    
    def delete(self, track_title: str) -> bool:
        """Deletes a track by its title.

        Args:
            track_title (str): The title of the track to be deleted.

        Returns:
            bool: True if the track was deleted, False if it was not found.
        """
        index = self.search(track_title)
        if index is not None:
            # Shift elements to the left to fill the gap
            track = self.getitem(index)
            self.__subtrDuration(track)
            print(track, 'successfully deleted.')
            self.__adjustArray(start=index, end=self.length(), dir='b')
            self.setItematIndex(self.length() - 1, None)
            self.decreaseLength()
        else:
            print(f"'{track_title} not found in music library.'")

    def search(self, track_title: str) -> int:
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
    
    def __addDuration(self, t:Track):
        self.__total = self.__total.__add__(t.getDuration())
    
    def __subtrDuration(self, t:Track):
        self.__duration = self.__duration.__sub__(t.getDuration())

    @classmethod
    def create(cls,title):
        return cls(title)
    def __str__(self, mode:str = 'external') -> str:
        if mode == 'external':
            return self.__title
        elif mode == 'internal':
            s = f'''
================================
            PLAYLIST
================================
Playlist Name: {self.__title}
Total Duration: {self.formatduration(self.__total, 'display')}
tracks:
'''
            for track in self.get_list():
                s += str(track)+'\n'
            s+=str(self.page)
            return s