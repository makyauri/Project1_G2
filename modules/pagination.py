import sys
sys.path.append('modules\\')

class Paginate:
    def __init__(self, arrsize) -> None:
        self.__size = arrsize
        self.__pagecount = 1
        self.totalPage()
    def totalPage(self):
        answer = self.__size / 10
        self.__total = int(answer)
        if type(answer) is float:
            self.__total += 1
    
    def startindex(self):
        return (self.__pagecount-1) *  10
    
    def endindex(self):
        index = self.__pagecount * 10
        return index

    def nextpage(self):
        if self.__pagecount < self.__total:
            self.__pagecount += 1
    
    def previouspage(self):
        if self.__pagecount > 1:
            self.__pagecount -= 1

    def __str__(self) -> str:
        return f"<Page of {self.__pagecount}/{self.__total}>"