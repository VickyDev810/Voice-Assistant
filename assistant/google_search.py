import webbrowser
from utils import QueryReply

class GoogleSearch:
    def __init__(self, query_string):
        self.query = query_string
        
        self.reply = "Searching for "+self.query
        
        QueryReply(self.reply)
        
        webbrowser.open("https://google.com/search?q=%s" % self.query)