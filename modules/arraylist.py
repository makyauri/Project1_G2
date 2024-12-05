import sys
sys.path.append('modules\\')

from track import Track, timedelta
from pagination import Paginate
class ArrayList:
    def __init__(self, max_size: int = 50) -> None:
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__length = 0
        self.__currcount = 0
        self.page = Paginate(self.__length)
    def getcount(self):
        return self.__currcount
    
    def incrCount(self):
        self.__currcount +=1
    
    def add(self, item:Track) -> None:
        if self.__length >= self.__max_size:
            self.__expand()
        self.__elements[self.__length] = item
        self.__length += 1

    @staticmethod
    def formatduration(time:timedelta, type:str = 'analog'):
        total_sec = time.total_seconds()
        hours = int(total_sec // 3600)
        minutes = int((total_sec % 3600) // 60)
        seconds = int(total_sec % 60)
        if hours > 0:
            if type == 'analog':
                return f"{hours:02}:{minutes:02}:{seconds:02}"
            elif type == 'display':
                return f"{hours:02} hr {minutes:02} min {seconds:02} sec"
        else:
            if type == 'analog':
                return f"{minutes:02}:{seconds:02}"
            elif type == 'display':
                return f"{minutes:02} min {seconds:02} sec"
        
    def get_list(self):
        return self.__elements[:self.__length]

    def getitem(self, position: int):
        if 0 <= position < self.__length:
            return self.__elements[position]
    def empty(self):
        self.__elements = [None]*self.__max_size
    
    def __expand(self) -> None:
        self.__max_size *= 2
        self.__elements += [None] * self.__max_size

    def length(self) -> int:
        return self.__length
    
    def __str__(self, counter=False) -> str:
        s = ''
        for item in self.get_list():
            if counter:
                self.__currcount += 1
                s+= f"[{self.__currcount}] {str(item)}\n"
            else:
                s+= f"{str(item)}\n"
        return s+str(self.page)
