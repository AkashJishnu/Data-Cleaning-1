#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel("C:\\Users\\akash\\Downloads\\Customer Call List.xlsx")


# In[3]:


df


# In[4]:


df=df.drop_duplicates()


# In[5]:


df=df.drop(columns="Not_Useful_Column")


# In[6]:


df["Last_Name"]=df["Last_Name"].str.strip("._/") 


# In[7]:


df


# In[8]:


df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')


# In[9]:


df['Phone_Number']= df['Phone_Number'].apply(lambda x: str(x))


# In[10]:


df["Phone_Number"]=df['Phone_Number'].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])


# In[11]:


df.dtypes


# In[12]:


df


# In[13]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--',"")
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--',"")
df


# In[14]:


df[['Street_Address','State','Post_Code']]=df["Address"].str.split(',',2,expand=True)


# In[15]:


df.drop(['Address'],axis=1)


# In[16]:


df['Paying Customer']=df["Paying Customer"].str.replace('Yes','Y')


# In[17]:


df["Paying Customer"] = df["Paying Customer"].str.replace('No','N')


# In[18]:


df


# In[19]:


df['Do_Not_Contact'] = df["Do_Not_Contact"].str.replace('Yes','Y')


# In[ ]:





# In[20]:


df['Do_Not_Contact'] = df["Do_Not_Contact"].str.replace('No','N')


# In[21]:


df


# In[22]:


df=df.replace('N/a','')


# In[23]:


df = df.fillna('')


# In[24]:


df


# In[25]:


#Running a loop to remove customers that should not be contacted.

for x in df.index:
    if df.loc[x,"Phone_Number"] == '':
        df.drop(x, inplace=True)
        


# In[26]:


df


# In[27]:


df.reset_index(drop=True)


# In[29]:


df.to_csv('C:\\Users\\akash\\OneDrive\\Desktop\\cleaned_data.csv', index=False)


# In[ ]:




