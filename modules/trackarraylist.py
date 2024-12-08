import sys
sys.path.append('.')

from track import Track, timedelta
from arraylist import ArrayList
from pagination import Paginate
class TrackArrayList(ArrayList):
    def __init__(self, max_size: int = 50) -> None:
        super().__init__(max_size)
        self.__max_size = max_size
        self.__elements = [None] * self.__max_size
        self.__length = 0
        self.__currcount = 0
        self.page = Paginate(0)


    def getcount(self):
        return self.__currcount
    
    def incrCount(self):
        self.__currcount +=1
    
    def decreaseLength(self):
        self.__length -= 1
    
    def increaseLength(self):
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
    
    def setItematIndex(self, index:int, value):
        # assert index < self.__length, 
        self.__elements[index] = value
    def empty(self):
        self.__elements = [None]*self.__max_size
    
    def insert(self, track: Track):
        if self.length() < self.__max_size:
            self.setItematIndex(self.__length, track)
            self.increaseLength()
        else:
            self.expand()
            self.setItematIndex(self.__length, track)
            self.increaseLength()

    def __findIndexInsertion(self, track: Track) -> int:
        """Finds the index to insert based on track title using binary search.

        Args:
            track (Track): Track to compare and to be inserted.

        Returns:
            int: Node insertion point for new track.
        """

        low, high = 0, self.__length-1
        while low <= high:
            mid = (low + high) // 2
            if self.__elements[mid] < track:
                low = mid + 1
            else:
                high = mid - 1
        return low  # The insertion point
    def __adjustArray(self, start: int, end: int, dir: str = "f") -> None:
        """Adjusts the arrangement of this array from start to end.

        Args:
            start (int): Start index for adjustment.
            end (int): End index for adjustment.
            dir (str): Direction of adjustment: "f" for forward, "b" for backward.
        """
        if dir == 'f':
            for index in range(end, start, -1):
                self.__elements[index] = self.__elements[index - 1]
    
        elif dir == 'b':
            for index in range(start, end):
                self.__elements[index] = self.__elements[index + 1]
    def expand(self) -> None:
        new_max_size = self.__max_size * 2
        new_elements = [None] * new_max_size
        for i in range(self.__length):
            new_elements[i] = self.__elements[i]
        self.__elements = new_elements
        self.__max_size = new_max_size

    def length(self) -> int:
        return self.__length
    
    def __currentpage(self):
        return self.get_list()[self.page.startindex():self.page.endindex()]
    def __str__(self, counter=False) -> str:
        s = ''
        count = self.page.startindex()
        for item in self.__currentpage():
            if counter:
                count += 1
                s+= f"[{count}] {str(item)}\n"
            else:
                s+= f"{str(item)}\n"
        return s+str(self.page)

