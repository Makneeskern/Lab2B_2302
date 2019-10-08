# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:06:18 2019

@author: Mikef
"""

class Node(object):
    password = ""
    occurance = -1
    next = None
    
    def __init__(self, password = None, count = 0, next = None):
        self.password = password
        self.occurance = count
        self.next = next

    def printContents(self):
        print("There are", self.occurance, "copy(ies) of" , self.password , "in the file.")
        
    def setPassword(self, password):
        self.password = password
            
    def setOccurance(self, occurance):
        self.occurance = occurance

    def setNext(self, next):
        self.next = next
    
    def getPassword(self):
        return self.password

    def getOccurance(self):
        return self.occurance

    def getNext(self):
        return self.next
    
    def hasNext(self):
        if next == None:
            return False
        else:
            return True
        
    def bump(self):
        temp = self.occurance
        temp = temp + 1
        self.occurance = temp