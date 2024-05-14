#query_reply.py

import win32com.client as wincl

class QueryReply:
    def __init__(self,query_string):
        self.query=query_string
        self.speak=wincl.Dispatch("SAPI.SpVoice")
        self.speak.Speak(self.query)