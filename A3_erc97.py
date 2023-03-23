#!/usr/bin/env python
# coding: utf-8

# # A3
# 
# Deadline - 12 May, 2022 (11:59 PM)
# 
# Your task is to use community detection algorithms to identify communities in a social network graph of Facebook users’ friend lists.
# 
# ## Question 1
# Start with the ‘Karate Club’ dataset which was composed by asking 33 children who were all in the same karate club to list their friends. Each edge represents a friendship, and each node represents a child in Karate club. 
# 
# Since this is a very small graph, we can play around with it and visualize it to see what’s actually going on as we’re developing our code
# 

# In[1]:


import networkx as nx
G = nx.karate_club_graph()


# In[2]:


G


# In[3]:


print(nx.info(G))


# ### [1 pts] Part 1A: Make a visualization of the network (hint: draw()). Title this visualization “Karate Network”.

# In[4]:


import matplotlib.pyplot as plt


# In[5]:


nx.draw(G,with_labels=True, alpha=0.5)
plt.title('Karate Network');


# ### [2 pts] Part 1B: Using the Louvain method for undirected graphs, find the best partition of the network. How many communities does this method produce? List the size of each community in descending order.

# In[6]:


#pip install python-louvain


# In[7]:


from community import community_louvain


# In[8]:


communities = community_louvain.best_partition(G)


# In[9]:


communities # node : community assignment


# In[10]:


import numpy as np


# In[11]:


# How many communities does this method produce?
np.unique(list(communities.values()))


# There are 4 communities produced by the Louvain method for partitioning the network.

# In[12]:


from collections import Counter


# In[13]:


counts = Counter(communities.values())
counts


# In[14]:


#  List the size of each community in descending order.
counts.most_common() # community label, community size


# ### [2 pts] Part 1C: Use the Girvan Newman method to split the Karate community into two groups. How big are these two groups? (list in descending order).

# In[15]:


from networkx.algorithms.community.centrality import girvan_newman


# In[16]:


comms = girvan_newman(G)
node_groups = []
for comm in next(comms):
    node_groups.append(list(comm))
node_groups


# In[17]:


print(f"The biggest group has {len(node_groups[1])} nodes and the smaller group has {len(node_groups[0])} nodes.")


# In[18]:


node_groups.reverse()


# In[19]:


node_groups # list in descending order


# ### [2 pts] Part 1D: Make a visualization of the network, now where the nodes are colored by which community they belong to, according to the Louvain method. Title this visualization "Visualization of Louvain Groups".

# In[20]:


cmap = {
    0 : 'blue',
    1 : 'orange',
    2 : 'teal', 
    3 : 'pink',
}
node_cmap = [cmap[v] for _,v in communities.items()]
nx.draw(G, node_size = 75, alpha = 0.8, node_color=node_cmap)
plt.title('Visualization of Louvain Groups');


# ## Question 2
# Download the Facebook data ‘facebook_combined.txt’ (Edges from all egonets combined) from this website: https://snap.stanford.edu/data/ego-Facebook.html
# 
# Using the Louvain method for undirected graphs, find the best partition of the network.

# In[21]:


edges = []
with open("facebook_combined.txt") as f:
    for line in f:
        (k, v) = line.split()
        edges+=[(int(k),int(v))]
len(edges)


# In[22]:


G = nx.Graph()
G.add_edges_from(edges)


# ### [1 pts] Part 2A: How many communities does this method produce?

# In[23]:


coms = community_louvain.best_partition(G)


# In[24]:


coms # node : community


# In[25]:


np.unique(list(coms.values()))


# In[26]:


print(f"This method produces {len(np.unique(list(coms.values())))} communities.")


# ### [2 pts] Part 2B: List the size of each community in descending order.

# In[27]:


counts = Counter(coms.values())
counts


# In[28]:


#  List the size of each community in descending order.
counts.most_common() # community, size

