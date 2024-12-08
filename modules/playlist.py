import sys
sys.path.append('modules\\')
from arraylist import ArrayList
from Queue import Queue
from datetime import timedelta, datetime
from track import Track

class Playlist(ArrayList):
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
    def add(self, t:Track):
        if type(t) is Track:
            self.__addDuration(t.getDuration())
            return super().add(t)
        else:
            print("Invalid given argument type.")
    
    def play(self):
        if not self.__queue:
            self.__queue = Queue(self)
    
    def getQueue(self):
        if not self.__queue:
            self.play()
        return self.__queue

    def __addDuration(self, t:timedelta):
        self.__total = self.__total.__add__(t)
    
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