from datetime import timedelta
from arraylist import ArrayList

class Queue:
    def __init__(self, array):
        self.__arrlist = array
        self.__duration = self.__arrlist.totalDuration()
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

    def previous(self):
        if self.__current_index != 0:
            self.__current_index -= 1
            currtrack = self.__arrlist.get_list()[self.__current_index]
            self.__addDuration(currtrack)
            self.__end -=1
    
    def currentTrack(self):
        return self.__arrlist.getitem(self.__current_index)

    def getpage(self):
        array = self.__arrlist.get_list()
        return array[self.__current_index+1:self.__end]
    
    def __addDuration(self, t):
        self.__duration = self.__duration.__add__(t.getDuration())

    def __subtrDuration(self, t):
        self.__duration = self.__duration.__sub__(t.getDuration())

    def __parsepage(self):
        s = ''
        for track in self.getpage():
            self.__arrlist.incrCount()
            s+= f'({self.__arrlist.getcount()}){str(track)}\n'
        return s
    def __str__(self) -> str:
        return f"""
=================================
              QUEUE
=================================
Total Duration: {ArrayList.formatduration(self.__duration, 'display')}
Shuffled: {"Yes" if self.__shuffle else "No"}
Repeat: {"Yes" if self.__repeat else "No"}
Tracks:
    Currently playing{' (Paused)' if self.__pause else ''}:
        {self.currentTrack()}
Next:
{self.__parsepage()}
{str(self.__arrlist.page)}"""
        
    
