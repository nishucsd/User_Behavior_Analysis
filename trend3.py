
# coding: utf-8

# In[5]:




# In[21]:

__author__ = 'Nishant'
from lru import LRU
from lru_cont3 import lru_cont as lru2
import numpy as np
from scipy import spatial
class trend:
    def __init__(self, c_ip, c_times, c_domains, c_rows, c_events, c_users ):
        self.topic_count =1
        self.l1 = LRU(c_ip)
        self.l2 = LRU(c_times)
        self.l3 = LRU(c_domains)
        self.l4 = LRU(c_users)
        
        self.l5 = lru2(c_rows)
        self.l6 = lru2(c_events)
         
    def set_cate(self, f_dic, lru):
        for k in f_dic.keys():
            v = lru.get(k,0)
            lru[k]=v+f_dic[k]
    
    def set_cont(self, val, topic_cache):
        topic_cache.set(val)
 
    def set_cluster(self, u_act):
        self.set_cate(u_act[1][0][0],self.l1)
        self.set_cate(u_act[1][0][1],self.l2)
        self.set_cate(u_act[1][0][2],self.l3)
        
        self.set_cate({u_act[0]:1},self.l4)
        self.set_cont(u_act[1][1][0],self.l5)
        self.set_cont(u_act[1][1][1],self.l6)
        self.topic_count+=1
 
    def get_similarity(self,u_act):
        ip_sum = 1
        time_sum = 1
        domain_sum = 1
        ip_match =0
        time_match=0
        domain_match=0
        h_ind =0
        u_ind =0
        w_ind =0
        c=0
        i1 = self.l1.get_size()
        t1 = self.l2.get_size()
        d1 = self.l3.get_size()
        for ip in u_act[1][0][0]:
            ip_sum+= self.l1.get(ip,0)
            if(self.l1.has_key(ip)):
#                 ind = self.l1.keys().index(h)
#                 h_ind+= h1 - ind
                ip_match+= 1
        for time in u_act[1][0][1]:
            time_sum+= self.l2.get(time,0)
            if(self.l2.has_key(time)):
                time_match+=1
#                 u_ind+= u1 - self.l2.keys().index(u)
        for domain in u_act[1][0][2]:
            domain_sum+= self.l3.get(domain,0)
            if(self.l3.has_key(domain)):
                domain_match+= 1
#                 w_ind+= w1 - self.l3.keys().index(w)
#         if(h_match !=0):
#             c = h_match -1
        # print(h_ind,h1,u_ind,u1,w_ind,w1, h_sum,w_sum,)
        sim_cate = (ip_match/(i1+1))*(ip_sum/sum(self.l1.values() +[1])) + (time_match/(t1+1))*(time_sum/sum(self.l2.values()+[1])) + (domain_match/(d1+1))*(domain_sum/sum(self.l3.values()+[1])) 
        
        vec1 = [u_act[1][1][0],u_act[1][1][1]]
        vec_avg = [self.l5.get_average(),self.l6.get_average()]
        result = 1 - spatial.distance.cosine(vec1, vec_avg)
        similarity = np.linalg.norm([sim_cate, result])
        return similarity
#     def get_similarity():


# In[ ]:



