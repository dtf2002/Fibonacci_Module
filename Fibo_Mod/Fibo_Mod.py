#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def forFib(N):
    seq = np.arange(N)
    for i in np.arange(2,N):
        seq[i] = seq[i-2]+seq[i-1]
    return seq

def whileFib(N):
    seq = np.arange(N)
    x = 2
    while x < N:
        seq[x] = seq[x-1] + seq[x-2]
        x+=1
    return seq

def recFib(N,L=[0,1]):
    if len(L) < N:
        next_term = L[-1] + L[-2]
        L.append(next_term)
        recFib(N,L)
    return L

