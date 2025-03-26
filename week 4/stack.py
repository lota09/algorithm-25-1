'''*******************************************************************
  - Project          : algorithm_0326
  - File name        : stack.py
  - Description      : stack dependancy class lib
  - Owner            : Seokmin Kang
  - Revision history : 1) 2025.03.26 : Initial release
*******************************************************************'''

# 스택 구현
class stack:
    def __init__(self):
        self.s_list=[]

    def push(self,item):
        self.s_list.append(item)

    def pull(self):
        return self.s_list.pop()
    
    def isEmpty(self):
        return self.s_list.__len__() == 0 
    
    def size(self):
        return self.s_list.__len__()
    
    def clear(self):
        self.__init__()
