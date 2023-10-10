
from typing import Union


class AddOrConcatNumber(object):

    def __init__(self,arg1:Union[int,str],arg2:Union[int,str]) -> Union[int,str,None]:
        
        self.arg1=arg1
        
        self.arg2=arg2

    def add_num_or_str(self):
        
        if isinstance(self.arg1, str) and isinstance(self.arg1, str):

            return self.arg1+self.arg2
        
        elif isinstance(self.arg1, int) and isinstance(self.arg1, int):
            
            return self.arg1+self.arg2
        
        else:
            
            raise TypeError()