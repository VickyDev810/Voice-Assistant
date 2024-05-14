from utils import QueryReply
import webbrowser


class PlayCommand:
    def __init__(self, query_string):
        self.query = query_string
        
        self.video_name=""
        for i in range(1,len(self.query)):
            self.video_name+=self.query[i]+" "
       
        #Reply from Voice Assistant
        self.reply = 'Playing' + self.video_name
        QueryReply(self.reply)
        
        #play a song will open any video you set here
        if self.video_name=="a song " or self.video_name=="song " or self.video_name=="something ":
            webbrowser.open('https://www.youtube.com/watch?v=bpOSxM0rNPM')
        #else it will search for the query on youtube
        else:
            webbrowser.open('https://www.youtube.com/results?search_query=%s' %self.video_name)
        