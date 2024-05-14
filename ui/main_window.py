#main_window.py

from tkinter import *
from tkinter import ttk
from assistant import VoiceRecognize,AppOpener, GoogleSearch, PlayCommand
from utils import HandleSearch

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
          
        #Voice Recognition Class   
        detect_voice=VoiceRecognize
        
        #Main UI            
        self.title("Voice Assistant")
        
        self.geometry('355x250')
        
        mainframe = ttk.Frame(self, padding="10 10 12 12")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        style = ttk.Style()
        style.configure('TFrame', background="#151515")
        style.configure('TButton', padding=10)
        style.configure('TEntry', padding=10, borderwidth=15, relief='groove', background='#000000')
        

        #change this to change the mic image 
        mic_img=PhotoImage(file='assets/mic.png')
        self.mic_img_resized=mic_img.subsample(10)
        
        style.configure('Rounded.TButton', borderwidth=15, relief='groove', background='#000000')
        
        #function to execute the voice command
        def execute_voice_command():
            
            detect_voice.recognizeVoice(self)
            
            #set the value of query entry to the voice input
            self.recognized_query=detect_voice.getQuery(self)
            
            if self.recognized_query=="Try Again":
                query.set(str(self.recognized_query))
            
            else:
                self.split_query=self.recognized_query.split(" ")
                
                query.set(str(self.recognized_query))
                #Handle the query meaning process the Query
                HandleSearch(self.recognized_query,self.split_query,AppOpener, GoogleSearch, PlayCommand)
                 
        #function to handle searched query
        def executeQuery():
            self.recieved_query=str(query.get())
            self.split_query=self.recieved_query.split(" ")
            
            HandleSearch(self.recieved_query,self.split_query,AppOpener, GoogleSearch, PlayCommand)
            print(self.recieved_query)         
             
        #mic button    
        self.mic_button = ttk.Button(mainframe, image=self.mic_img_resized,command=execute_voice_command, width=20, style='Rounded.TButton')
        self.mic_button.grid(column=2, row=1, sticky=[E],padx=30)

        query = StringVar()
        query_entry = ttk.Entry(mainframe, width=22, textvariable=query, font=('Helvetica', 15))
        query_entry.grid(column=2, row=4, sticky=(W,E),pady=20)
        
      
         
        #search Image
        search_img=PhotoImage(file='assets/search.png') 
        self.search_img_resized=search_img.subsample(30)
           
        #search Button    
        ttk.Button(mainframe, image=self.search_img_resized, command=executeQuery,style='Rounded.TButton').grid(column=4, row=4, sticky=E, padx=25,pady=20)
        
        
        
            
            
            
