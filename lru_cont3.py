
# coding: utf-8

# In[16]:

__author__ = 'Nishant'
import numpy as np
class lru_cont:

    def __init__(self, cap):
        self.cache_count =0
        self.avg =0
        self.capacity=cap
        self.r_cache = np.zeros(cap)
        
    def get_capacity(self):
        return self.capacity
    
    def set(self, val):
        if(self.cache_count < self.capacity):
            self.r_cache[self.cache_count] = val
            self.avg = np.average(self.r_cache[:self.cache_count+1])
        else:
            top = self.r_cache[0]
            self.r_cache=np.append(self.r_cache[1:],[val])
            self.avg = np.average(self.r_cache)
        self.cache_count+=1
        
    def get_average(self):
        return self.avg
    
    def get_items(self):
        return self.r_cache
        
    


# In[ ]:



