import string

class Sources:
    def __init__(self,id:string,name,description,url):
        self.id=id,
        self.name=name,
        self.description=description
        self.url=url
        
class Articles:
    '''Define article model'''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt

