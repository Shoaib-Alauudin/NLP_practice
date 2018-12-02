# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 00:53:00 2018

@author: Ghulam
 
TF - Term Frequency
IDF - Inverse Document Frequency

TF-IDF = TF * IDF

TF:
               (Number of Occurance of a word in a document)
Formula -->   ---------------------------------------------
                  (Number of words in that document) 

Example: "to be or not to be"   

to = (1+1)/6 = 0.33
be = (1+1)/6 = 0.33
or = (1)/6 = 0.16
not = 1/6 = 0.16


IDF:

                        (Number of documents)
Formula = log ----------------------------------------
               (Number of documents containing word)

Example: 
    "to be or not to be"
    "i have to be"
    "you got to be"

Number of document = 3
    
    to = log(3/3) = 0  (to - contains in all documents)
    be = log(3/3) = 0  (be - contains in all documents)
    have = log(3/1)    (have - only contain in 2nd document (1-time) )
    


"""

import nltk
import re
import numpy as np
print("------------------TF-IDF(Term frequency- Inverse Document Frequency)------------------")


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
    sentences[i] = sentences[i].lower()
    sentences[i] = re.sub(r'\W', ' ', sentences[i])
    sentences[i] = re.sub(r'\d',' ', sentences[i])
    sentences[i] = re.sub(r'\s+',' ', sentences[i])
    
"""    Creating the histogram        """    
word_occur = {}
for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    for word in words:
        if word not in word_occur.keys():
            word_occur[word] = 1
        else:
            word_occur[word] += 1



"""     Most frequent Words Dictionary      """
import heapq 
frequent_words = heapq.nlargest(157, word_occur, key=word_occur.get)

""" IDF matrix (Inverse Document Frequency) """
IDF_words = {}
for word in frequent_words:
    doct_count = 0
    for sentence in sentences: 
        if word in nltk.word_tokenize(sentence):
            doct_count += 1
    IDF_words[word] = np.log((len(sentences)/doct_count)+1)
    
    
"""-------TF matrix-------"""
tf_matrix = {}
for word in frequent_words:
    doc_tf = []
    for sentence in sentences:
        freq = 0
        for sent_word in nltk.word_tokenize(sentence):
            if word == sent_word:
                freq += 1
        tf_word = freq/len(nltk.word_tokenize(sentence))
        doc_tf.append(tf_word)
    tf_matrix[word] = doc_tf 

""" TF-IDF Calculation """
tf_idf_matrix = []
for word in tf_matrix.keys():
    tf_idf_word = []
    for value in tf_matrix[word]:
        score = value * IDF_words[word]
        tf_idf_word.append(score)
    tf_idf_matrix.append(tf_idf_word)
    
import numpy as np
tf_idf_X = np.asarray(tf_idf_matrix)
tf_idf_X = np.transpose(tf_idf_X)