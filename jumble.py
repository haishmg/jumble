#!/usr/bin/python
import sys
import os.path


pattern = {}
dict_all = {}

# poupulate all the words into a dict - dict_all
def populate_all(f):
    for word in f :
        word = word.lower().strip()
        if word not in dict_all:
          dict_all[word] = 1
          

    
# populate all the valid words into a dict - pattern 
def populate_valid(key):
        l=[]
        flattened_l=[]
        for i in range(len(key)):
         k = combinations(key)
         l.append(k)
         
        for x in l :
            for z in x :
              flattened_l.append(z)  
                      
        for word in flattened_l:
         if word in dict_all:
            if key not in pattern : 
              pattern[key] = [word]
            elif word not in pattern[key]:
             pattern[key].append(word)
        
        
# All possible combinations for a given word        
def combinations (word):
    for i in range(len(word)):
         yield (word[i])
         for d in combinations(word[:i] + word[i+1:]):
             yield(word[i] + d)
     



if __name__ == '__main__':
  
  f = open(str(sys.path[0])+'/2of12inf.txt','r')  
  populate_all(f)

  while True:
   ip =  raw_input("Enter the word or q to quit :")
   if ip.lower() == "q":
       break
   else:
     #Check if the word is already present in the dict  
     if ip not in pattern :   
         populate_valid(ip)
     if ip in pattern :
       print "The words are:",pattern[ip]
     else :
       print "No valid words found"     
  
