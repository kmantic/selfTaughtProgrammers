#!/usr/bin/env python3
"""
https://github.com/dev0ps221/wordgen/tree/dev?fbclid=IwAR1jRpl6r-9FJAoRhFzCm1NpDuNF0Dv0rS933q2HD_NwE3pzFxjSZ9vCZAs

"""
__author__ = "kharris"
__version__ = "0.1.0"
__license__ = "MIT"

import sys 

#global list of lists 
lists = []

####################
###
def main():
    print("main()")

    #init list of lists 
    buildList()

    cnt = 0 
    while cnt < 5: 
        cnt += 1
        print("Running iteration #: ", cnt)
        cloneLastList()
        
        #send in the 2nd to last array (not the cloned array)
        flips = getFlipIndex(lists[ len(lists)-1 ])
        #print("flips: ", flips[0], flips[1]) 
        print("list now:", lists)
        flipAppropriateElem(flips) 
        print("Final: ", lists ) 

####################
### flip element value in last lists[list] (index to flip, letter to change to)
def flipAppropriateElem(myTuple): 
    lists[len(lists)-1][myTuple[0]] = myTuple[1]

####################
###
def cloneLastList():
    i = len(lists)-1 
    if len(lists) == 1: 
        newList = lists[0].copy()
    else: 
        newList = lists[i].copy()
  
    lists.append(newList)

####################
### build initial list 
def buildList(): 
    if len(lists) == 0: 
        lists.append([])
        #modify range for desired list size (your problem has 8)
        for i in range(3): 
            lists[0].append("a")

####################
### get next letter 'a' returns 'b', 'z' returns 'a', etc.
def getNextLetter(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65).lower()

####################
### returns tuple (index, letter) in the last list in lists which is due to flip 
def getFlipIndex(myList): 

    for idx, letter in enumerate(myList): 
        if idx == 0: 
            continue
        try: 
            #print("idx: ", idx) 
            #print("letter: ", letter) 
            #print("last: ", myList[idx-1], "\n===========\n")
            if letter > myList[idx-1]: 
                return (idx-1, getNextLetter(myList[idx-1]))
        except: 
            print("exception")
            continue 

    #list is done 
    #modify to 7, 7 for list with size of 8 
    return (2, getNextLetter(myList[2]))

if __name__ == "__main__":
    main()
