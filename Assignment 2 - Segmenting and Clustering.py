#!/usr/bin/env python
# coding: utf-8

# ## Applied Data Science Capstone Assignment 2 :Segmenting and Clustering Neighborhoods in Toronto

# In[1]:


# Import necessary libraries
get_ipython().system('pip install lxml')
import requests
import lxml.html as lh
import pandas as pd


# In[2]:


url='https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')


# In[4]:


# Parse the first row as our header
tr_elements = doc.xpath('//tr')

#Create empty list
col=[]
i=0

#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))


# In[5]:


#Since out first row is the header, data is stored on the second row onwards
for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 3, the //tr data is not from our table 
    if len(T)!=3:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=int(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


# In[7]:


# Check the length of each column. Ideally, they should all be the same
[len(NoofColumns) for (title,NoofColumns) in col]


# #### Creating the pandas data frame 

# In[8]:


Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)


# #### Rearranging and renaming the columns

# In[10]:


df.columns = ['Borough', 'Neighbourhood','Postcode']

cols = df.columns.tolist()
cols

cols = cols[-1:] + cols[:-1]

df = df[cols]

df.head()


# #### Cleaning the messy string in the Borough column

# In[11]:


df = df.replace('\n',' ', regex=True)
df.head()


# #### Dropping all cells with a borough that is Not assigned

# In[12]:


df.drop(df.index[df['Borough'] == 'Not assigned'], inplace = True)

# Reset the index and dropping the previous index
df = df.reset_index(drop=True)

df.head(10)


# #### Combining Neighbourhoods based on similar Postcode and Borough  

# In[13]:


df = df.groupby(['Postcode', 'Borough'])['Neighbourhood'].apply(','.join).reset_index()
df.columns = ['Postcode','Borough','Neighbourhood']
df.head(10)


# #### Removing any space in the start of the string

# In[14]:


df['Neighbourhood'] = df['Neighbourhood'].str.strip()


# #### Assigning Borough values to the Neignbourhood where vlaue is "Not assigned"

# In[15]:


df.loc[df['Neighbourhood'] == 'Not assigned', 'Neighbourhood'] = df['Borough']


# In[16]:


# Check if the Neighbourhood for Queen's Park changed 
df[df['Borough'] == 'Queen\'s Park']


# In[17]:


# Check the shape of the data frame
df.shape

