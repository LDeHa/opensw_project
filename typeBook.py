from bookGPT import *

class typeBook :
    title = ""
    author = ""
    bookGpt = bookGPT()

    def __init__(self, title, author) :
        self.title = title
        self.author = author

    def Review(self) :
        return self.bookGpt.review(self.title, self.author)

    def Debate(self) :
        return self.bookGpt.debate(self.title, self.author)
    
    def Quote(self) :
        return self.bookGpt.quote(self.title, self.author)
    
    def Summary(self) :
        return self.bookGpt.summary(self.title, self.author)
    
    def setTitle(self, title) :
        self.title = title

    def getTitle(self, title) :
        return self.title

    def setAuthor(self, author) :
        self.author = author

    def getAuthor(self, author) :
        return self.author   
