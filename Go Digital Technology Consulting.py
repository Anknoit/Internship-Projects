#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np


# ### TASK 1

# In[63]:


file1 = pd.read_csv('employee_data.csv')
file2 = pd.read_csv('insurance_data.csv')
file3 = pd.read_csv('vendor_data.csv')
print(file1.columns)
print(file2.columns)
print(file3.columns)


# In[49]:


output1 = pd.merge(file2, file1,
                   on = "AGENT_ID",
                   how = "left")
# print(output1)
output1.head()

output2 = pd.merge(file2, file3,
                   on = "VENDOR_ID",
                   how = "left")


# In[46]:


print(output2)


# ### TASK 2

# In[47]:


clmamt3 = file2.nlargest(3, 'CLAIM_AMOUNT')
clmamt3['INSURANCE_TYPE']


# ### TASK 3

# In[48]:


custseg = file2.loc[file2['RISK_SEGMENTATION']=="H"]
clmamt5 = custseg.nlargest(5, 'CLAIM_AMOUNT')
clmamt5['STATE']


# ### TASK 4

# In[ ]:


#Colocation
file1["COLOCATION"] = ""
file1.to_csv('insurance_data.csv',index="False")
# file1["COLOCATION"] = file1[(file2["STATE"] == file2["INCIDENT_STATE"]) & file2["INCIDENT_STATE"] == file1["STATE"]]
#use lambda


# ### TASK 5

# In[ ]:




