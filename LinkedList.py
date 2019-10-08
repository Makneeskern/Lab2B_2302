# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:37:38 2019

@author: Mikef
"""

from Node import Node

class LinkedList(object):
    head = Node
    length = 0
    
    def __init__(self, head = None):
        self.head = head
        if head == None:
            self.length = 0
        else:
            self.length = 1
    
    def setHead(self, head):
        iter = None
        if self.head.hasNext():
            iter = self.head.getNext()
        self.head = Node(head, 1, None)
        self.head.setNext(iter)
    
    def getHead(self):
        return self.head

    def getLength(self):
        return self.length

    def addData(self, password):
        newHead = Node(password, 1, self.head)
        self.head = newHead
        temp = self.length
        temp = temp + 1
        self.length = temp
        
    def addDataOmni(self, password, occurance):
        if self.head == None:
            self.head = Node(password, occurance)
            temp = self.length
            temp = temp + 1
            self.length = temp
            return
        iter = self.head
        while iter.next != None:
            iter = iter.next
        iter.next = Node(password, occurance)
        temp = self.length
        temp = temp + 1
        self.length = temp
    
    def contains(self, key):
        node = self.head
        for i in range(self.length):
            if node.getPassword() == key:
                return i
            node = node.getNext()
        return -1
            
    
    def printContents(self):
        iter = self.head
        while iter != None:
            iter.printContents()
            iter = iter.getNext()
            
    def checkAndStore(self, key):
        if self.length == 0:
            self.addData(key)
        iter = None
        check = self.contains(key)
        if check == -1:
            self.addData(key)
        else:
            iter = self.head
            while check > 0:
                iter = iter.getNext()
                check = check - 1
            iter.bump()
    
    def appendNode(self, node):
        if self.head == None:
            self.head = node
        iter = self.head
        while iter.next != None:
            iter = iter.next
        iter.next = node
        bump = self.length
        bump = bump + 1
        self.length = bump
        
    def size(self):
        if self.head == None:
            return 0
        iter = self.head
        i = 0
        while iter != None:
            iter = iter.next
            print(i)
            i = i + 1
        return i