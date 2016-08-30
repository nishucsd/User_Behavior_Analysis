
# coding: utf-8

# In[1]:

import random
import time
import pylab as plt
# In[2]:

import numpy as np


# In[3]:

from trend3 import trend


# In[4]:

from lru_cont3 import lru_cont as lru2


# In[5]:


# In[6]:

import ujson
j=0
fname='topics7.json'
with open(fname) as f:
    content = f.readlines()


# In[7]:

trends = np.array([trend(8,4,6,20,20,30)])
content=content[:27]


# In[8]:

content1 = [ujson.loads(i) for i in content]


# In[9]:

def should_split(u_act,trends):
    domains=u_act[1][0][2].keys()
    matching_domains = [len(set(domains).intersection(set(i.l3.keys()))) for i in trends]
    if(len(list(filter(lambda x : x<=3,matching_domains))) == len(trends)):
        return True
    else:
        return False



# In[ ]:

i=[1,2,3,3,4,4,4,4]
i[:3]


# In[ ]:


max_trends=12
count=0
c_old=np.zeros(max_trends)
start_time=time.time()


# In[ ]:

def print_counts(c_vector, topics):
    annotate = np.arange(max_trends)
    temp = sorted(zip(c_vector,topics, annotate), key = lambda x:-x[0])
    for i in temp :
        print( "Trend: ", i[2])
        print(sorted(i[1].l1.items(), key = lambda x : -x[1])[:20])
        print(sorted(i[1].l2.items(), key = lambda x : -x[1])[:20])
        print(sorted(i[1].l3.items(), key = lambda x : -x[1])[:20])
        print(sorted(i[1].l4.items(), key = lambda x : -x[1])[:20])
        print(sorted(i[1].l5.get_items(), key = lambda x : -x)[:20])
        print(sorted(i[1].l6.get_items(), key = lambda x : -x)[:20])
        print()


# In[ ]:

list(content1[0].items())[0][0]


# In[ ]:

trends[0].set_cluster(list(content1[0].items())[0])
del content1[0][list(content1[0].items())[0][0]]



# calculate similarity with every topic
#         for i in range(trends.size):
X = np.arange(max_trends)
Y = [random.randrange(30) for i in range(max_trends)]
plt.ylim(0,np.ptp(Y))
plt.ion()
plt.xlabel("Current Trends")
plt.ylabel("Velocities")
plt.title("Trend Analysis")
graph = plt.plot(X,Y)[0]
for u_dict in content1:
    for item in list(u_dict.items()):    
        similarity = [i.get_similarity(item) for i in trends]
#         print(similarity)
#             self.similarity[i] = self.topics[i].get_similarity(hashtags, usernames, words)
        decision = should_split(item,trends)
        
        if(decision == True):
            if(trends.size < max_trends):
                trends = np.append(trends, trend(8,4,6,20,20,30))
                max_ind = trends.size -1
            else:
                max_ind = random.randrange(0,trends.size)
        else:
            max_ind = np.argmax(similarity)

        #add the activity to the trend at max index
        trends[max_ind].set_cluster(item)
        count+=1
        if(count%80 ==0):
            current = time.time()
            # print("--- %s seconds ---" % (current - start_time))
            start_time=current
            count=0
            counts_vector = [i.topic_count for i in trends]
            counts_vector += [0]*(max_trends-len(counts_vector))
            # calculate velocity of trend
            delta = np.subtract(counts_vector,c_old)
#             acc = np.subtract(delta,self.v_old)
            Y=delta
            graph.set_ydata(Y)
            plt.ylim(0, np.ptp(Y))
            plt.draw()
            plt.pause(0.5)
            # remove the comment from next line to save acceleration file
#             f_writer.writerow(acc)
            print("counts are: ",counts_vector)
            print("velocities are: ", delta)
            # ax1.plot(delta)

            c_old = counts_vector
#             self.v_old = delta
            # time.sleep(4)
            # remove the comment from next line to save topics file
#             self.json_counts(  self.sr_no,file2, counts_vector, self.topics)
#             self.sr_no+=1
            print_counts( counts_vector, trends)
            print("\n")

while True:
    plt.pause(0.05)


# In[ ]:




# In[ ]:



