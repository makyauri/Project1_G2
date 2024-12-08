from datetime import timedelta, datetime

class Track:
    def __init__(self, title:str, artist:str, duration:timedelta, added = None) -> None:
        self.__title = title
        self.__artist = artist
        self.__duration:timedelta = duration
        self.__added = added
    
    def dateAdded(self):
        return self.__added
    
    def setdateadded(self):
        self.__added = datetime.now()

    def getTitle(self):
        return self.__title
    
    def getArtist(self):
        return self.__artist
    
    
    def getDuration(self):
        return self.__duration

    def getTitle(self):
        return self.__title

    def getArtist(self):
        return self.__artist
    

    def getDuration(self):
        return self.__duration
    
    def __formatduration(self, type:str = 'analog'):
        total_sec = self.__duration.total_seconds()
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

    def getattrs(self, name: str) -> any:
        if name == 'title':
            return self.__title
        elif name == 'artist':
            return self.__artist

        elif name == 'duration':
            return self.__duration
        elif name == 'added':
            return self.__added
    
    def __repr__(self) -> str:
        return self.__title
    
    def __str__(self, option="outside") -> str:
        if option =="outside":
            return f"{self.__title} - {self.__artist} ({self.__formatduration(type='analog')})"
        elif option == "inside":
            banner = f"""
=================================
              TRACK
=================================
"""
            return banner + f"Title: {self.__title}\nArtist: {self.__artist}\nDuration: {self.__duration}"