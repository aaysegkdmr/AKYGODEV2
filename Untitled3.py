#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import request
URL="http://colormind.io/api/' --data-binary '{"model":"default"}"
result=request.get(URL)
data=result.json()
print(data)

