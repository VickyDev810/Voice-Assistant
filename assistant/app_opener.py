#app_opener.py

from utils import QueryReply
import os

class AppOpener:
    def __init__(self,query_string):
 
        self.query=query_string
        self.appName=""
        for i in range(1,len(self.query)):
            self.appName+=(self.query[i])
        
        self.reply='Okay Opening '+ self.appName
        
        # Responce from voice assistant
        QueryReply(self.reply)

        os.system(self.appName+'.exe')
        
        
# this works only on few apps that are defined in your os path 
# some commands are
# open calc
# open notepad
# open explorer
# open spotify works when you have spotify installed from microsoft store
# open cmd this command may cause errors as it will open the cmd in vs code terminal itself