# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 01:38:48 2018

@author: Ghulam
"""

import nltk
import random
import re

paragraph = """Thank you all so very much. Thank you to the Academy. 
               Thank you to all of you in this room. I have to congratulate 
               the other incredible nominees this year. The Revenant was 
               the product of the tireless efforts of an unbelievable cast
               and crew. First off, to my brother in this endeavor, Mr. Tom 
               Hardy. Tom, your talent on screen can only be surpassed by 
               your friendship off screen … thank you for creating a t
               ranscendent cinematic experience. Thank you to everybody at 
               Fox and New Regency … my entire team. I have to thank 
               everyone from the very onset of my career … To my parents; 
               none of this would be possible without you. And to my 
               friends, I love you dearly; you know who you are. And lastly,
               I just want to say this: Making The Revenant was about
               man's relationship to the natural world. A world that we
               collectively felt in 2015 as the hottest year in recorded
               history. Our production needed to move to the southern
               tip of this planet just to be able to find snow. Climate
               change is real, it is happening right now. It is the most
               urgent threat facing our entire species, and we need to work
               collectively together and stop procrastinating. We need to
               support leaders around the world who do not speak for the 
               big polluters, but who speak for all of humanity, for the
               indigenous people of the world, for the billions and 
               billions of underprivileged people out there who would be
               most affected by this. For our children’s children, and 
               for those people out there whose voices have been drowned
               out by the politics of greed. I thank you all for this 
               amazing award tonight. Let us not take this planet for 
               granted. I do not take tonight for granted. Thank you so very much."""
               
               
sentences = nltk.sent_tokenize(paragraph)
for i in range(len(sentences)):
    sentences[i] = re.sub(r'\d',' ',sentences[i])
    sentences[i] = re.sub(r'\W',' ',sentences[i])
    sentences[i] = re.sub(r'\s+',' ',sentences[i])
    
n = 6

ngrams = {}

# Creating the n-grams

for si in range(len(sentences)):
    for i in range(len(sentences[si]) - n):
        gram = sentences[si][i:i+n] # sent[i][0:3] = tha
        
        if gram not in ngrams.keys():
                ngrams[gram] = []
                
        # Check the next char is not already in list of chars
        if sentences[si][i+n] not in ngrams[gram]:
            ngrams[gram].append(sentences[si][i+n])
        
'''        
        if sentences[si][i+n] != ' ': # Check if the nest char is not a blank space
            
            # append the next coming letters to the ngrams dictionary of lists
            if gram not in ngrams.keys():
                ngrams[gram] = []
                
            # Check the next char is not already in list of chars
            if sentences[si][i+n] not in ngrams[gram]:
                ngrams[gram].append(sentences[si][i+n])
'''
new_sentences = []              
# testing our N-Gram character level model
for si in range(len(sentences)):
    print("Original Sent: ",sentences[si])
    
    currentGram = sentences[si][0:n]
    result = currentGram
    for i in range(100):
        if currentGram not in ngrams.keys():
            break
        
        possibilities = ngrams[currentGram]
        nextWord = possibilities[random.randrange(len(possibilities))]
        result += nextWord
        currentGram = result[len(result)-n:len(result)]
    
    new_sentences.append(result)
    print("New sent:",result)
    print("------------------------------")
    
         
