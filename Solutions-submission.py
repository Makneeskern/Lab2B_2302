# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:17:31 2019

@author: Mikef
"""

from LinkedList import LinkedList
import time

def sort_Bubble(llist):
    swapMade = True
    while swapMade:
        swapMade = False
        front = llist.head.next
        back = llist.head
        prev = None
        while front != None:
            if back.occurance < front.occurance:
                if prev == None:
                    llist.head = front
                else:
                    prev.next = front
                back.next = front.next
                front.next = back
                swapMade = True
                temp = front
                front = back
                back = temp
            if prev == None:
                prev = llist.head
            else:
                prev = prev.next
            front = front.next
            back = back.next
    return llist

def sort_Merge(llist, size):
    if size == 1:
        return llist
    sizeBef = size // 2
    sizeAft = size - sizeBef
    listBef = LinkedList()
    listAft = LinkedList()
    iter = llist.head
    for i in range(size):
        if i < sizeBef:
            listBef.addDataOmni(iter.password, iter.occurance)
        else:
            listAft.addDataOmni(iter.password, iter.occurance)
        iter = iter.next
    listBef = sort_Merge(listBef, sizeBef)
    listAft = sort_Merge(listAft, sizeAft)
    newList = LinkedList()
    iterBef = listBef.head
    iterAft = listAft.head
    while iterBef != None and iterAft != None:
        if iterBef.occurance > iterAft.occurance:
            newList.addDataOmni(iterBef.password, iterBef.occurance)
            iterBef = iterBef.next
        else:
            newList.addDataOmni(iterAft.password, iterAft.occurance)
            iterAft = iterAft.next
    if iterBef == None:
        while iterAft != None:
            newList.addDataOmni(iterAft.password, iterAft.occurance)
            iterAft = iterAft.next
    else:
        while iterBef != None:
            newList.addDataOmni(iterBef.password, iterBef.occurance)
            iterBef = iterBef.next
    return newList

def mainLL ():
    passwords = LinkedList()
    file = open("250-thousond-combos.txt", 'r')
    uncollected = file.readlines()
    for line in uncollected:
        seperated = line.strip().split()
        passwords.checkAndStore(seperated[len(seperated) - 1])
        
    passwords = sort_Bubble(passwords)
    
    iter = passwords.head
    for numbers in range(20):
        print("there are " + str(iter.occurance) + " copies of " + iter.password)
        iter = iter.next
        
        
def mainDic():
    dict = {}
    file = open("250-thousond-combos.txt", 'r')
    uncollected = file.readlines()
    found = False
    passwords= LinkedList()
    for line in uncollected:
        found = False
        seperated = line.strip().split()
        for key in dict.keys():
            if key == seperated[len(seperated) - 1]:
                temp = dict[key]
                temp = temp + 1
                dict[key] = temp
                found = True
        if found == False:
            dict[seperated[len(seperated) - 1]] = 1
    for items in dict.keys():
        passwords.addDataOmni(items, dict[items])
    
    passwords = sort_Bubble(passwords)
    
    iter = passwords.head
    for numbers in range(20):
        print("there are " + str(iter.occurance) + " copies of " + iter.password)
        iter = iter.next
    
start = time.time()    
mainLL()
end = time.time()
print()
print(end - start)