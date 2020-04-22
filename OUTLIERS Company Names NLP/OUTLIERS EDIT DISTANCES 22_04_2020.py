#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def getEditDistance(string_one,string_two,ngrams=1,jaro_winkler=False,jaccard=False,bag=False,cosine=False,longest_common_substring= False):
    
    solutions = {}
    scores = []
    
    if jaro_winkler != False:
        solution = textdistance.JaroWinkler(qval=ngrams).normalized_similarity(string_one,string_two)
        solutions["jaro-winkler"] = solution
        
        
    if jaccard != False:
        solution = textdistance.Jaccard(qval=ngrams).normalized_similarity(string_one,string_two)
        solutions["jaccard"] = solution
    
    if bag != False:
        solution = textdistance.Bag(qval=ngrams).normalized_similarity(string_one,string_two)
        solutions["bag"] = solution
            
    if cosine != False:
        solution = textdistance.Cosine(qval=ngrams).normalized_similarity(one,two)
        solutions["cosine"] = solution
        
    if longest_common_substring != False:
        solution = textdistance.LCSStr(qval=ngrams).normalized_similarity(one,two)
        solutions["LCSS"] = solution
#     print(solutions)
    
        
    for key in solutions.keys():
        scores.append(solutions[key])
    
    return round((sum(scores)/(len(scores))),2)
        


# In[ ]:





# In[ ]:




