#query_handler.py

class HandleSearch:
    def __init__(self,original_query,query_list,AppOpener, GoogleSearch, PlayCommand):

        self.original_query=original_query 
        
        self.query=query_list
        
        self.query_first_index=(self.query[0])
        
        
        if self.query_first_index=="open":
            AppOpener(self.query)
            
        elif self.query_first_index=="play":
            PlayCommand(self.query)          
              
        else:
            GoogleSearch(self.original_query)