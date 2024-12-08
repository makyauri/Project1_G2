from datetime import timedelta
from modules.trackarraylist import TrackArrayList
import random
class Queue:
    def __init__(self, array):
        self.__arrlist:TrackArrayList = array
        self.__duration:timedelta = self.__arrlist.totalDuration()
        self.__pause = False
        self.__shuffle = False
        self.__repeat = False
        self.__current_index = 0  # To track the currently playing track
        self.__end =10

    def isshuffle(self):
        return self.__shuffle
    
    def isrepeat(self):
        return self.__repeat
    
    def ispause(self):
        return self.__pause
    def shuffle(self, state=True):
        self.__shuffle = state
        self.__shuffledArray = self.__arrlist.get_list()
        random.shuffle(self.__shuffledArray)

    def pause(self, state=True):
        self.__pause = state
    def repeat(self, state=True):
        self.__repeat = state

    def next(self):
        if self.__current_index != self.__arrlist.length()-1:
            currtrack = self.__arrlist.get_list()[self.__current_index]
            self.__subtrDuration(currtrack)
            self.__current_index += 1
            self.__end +=1
        else:
            if self.__repeat:
                self.__current_index = 0
                self.__current_index = 0
                self.__end = 10


    def previous(self):
        if self.__current_index != 0:
            self.__current_index -= 1
            currtrack = self.__arrlist.get_list()[self.__current_index]
            self.__addDuration(currtrack)
            self.__end -=1
    
    def currentTrack(self):
        return self.__arrlist.getitem(self.__current_index)

    def getpage(self):
        if not self.__shuffle:
            array = self.__arrlist.get_list()
        else:
            array = self.__shuffledArray
        return array[self.__current_index+1:self.__end-1]
    
    def __addDuration(self, t):
        self.__duration = self.__duration.__add__(t.getDuration())

    def __subtrDuration(self, t):
        self.__duration = self.__duration.__sub__(t.getDuration())

    def __parsepage(self):
        s = ''
        count = self.__arrlist.page.startindex()
        for track in self.getpage():
            self.__arrlist.incrCount()
            count += 1
            s+= f'({count})\t{str(track)}\n'
        return s
    def __str__(self) -> str:
        return f"""
=================================
              QUEUE
=================================
Total Duration: {TrackArrayList.formatduration(self.__duration, 'display')}
Shuffled: {"Yes" if self.__shuffle else "No"}
Repeat: {"Yes" if self.__repeat else "No"}
Tracks:
    Currently playing{' (Paused)' if self.__pause else ''}:
        {self.currentTrack()}
Next:
{self.__parsepage()}
{str(self.__arrlist.page)}"""
        
    
