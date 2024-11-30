from datetime import timedelta, datetime

class Track:
    def __init__(self, title:str, artist:str,album:str, duration:timedelta, added = None) -> None:
        self.__title = title
        self.__artist = artist
        self.__album = album
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
    
    def getAlbum(self):
        return self.__album
    
    def getDuration(self):
        return self.__duration

    def getTitle(self):
        return self.__title

    def getArtist(self):
        return self.__artist
    
    def getAlbum(self):
        return self.__album

    def getDuration(self):
        return self.__duration
    
    # Not finished
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
    
    def __str__(self, option="outside") -> str:
        if option =="outside":
            return f"{self.__title} - {self.__artist} ({self.__formatduration()})"
        elif option == "inside":
            return f"Title: {self.__title}\nArtist: {self.__artist}\nAlbum: {self.__album}\nDuration: {self.__duration}"