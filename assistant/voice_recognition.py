#voice_recognize.py

import speech_recognition as sr

class VoiceRecognize():
    def recognizeVoice(self):
        self.query= None
        self.recognizer = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print('Say Something')
                audio=self.recognizer.listen(source, timeout=5)
            self.query=self.recognizer.recognize_google(audio)
            print("" + self.recognizer.recognize_google(audio))
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            self.query = None    
        except sr.RequestError as e:
            print("Couldn't get the results. Check your internet connection.")
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
    
    def getQuery(self):
        if self.query:
            return self.query
        else:
            print("Some error occured")
            self.query = "Try Again"
            return self.query
        
   