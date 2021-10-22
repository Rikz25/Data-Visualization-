#!/usr/bin/env python
# coding: utf-8

# In[16]:


from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

salary_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(ages_x, salary_y, label="All Devs")


plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")



plt.show()


# In[33]:


from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]


salary_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(ages_x, salary_y, color="#444444", label="All Devs")

py_salary_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_salary_y, color="#008fd5", label="Python")

js_salary_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_salary_y, color="#e5ae38", label="JavaScript")

plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")



plt.show()


# In[29]:


import numpy as np
from matplotlib import pyplot as plt


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_indexes=np.arange(len(ages_x))
x_indexes


# In[38]:


width=0.25

salary_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes-width, salary_y,width=width, color="#444444", label="All Devs")

py_salary_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_salary_y, width=width,color="#008fd5", label="Python")

js_salary_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes+width, js_salary_y, width=width,color="#e5ae38", label="JavaScript")

plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")



plt.show()


# In[40]:


width=0.25

salary_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes-width, salary_y,width=width, color="#444444", label="All Devs")

py_salary_y = [45372, 48876, 53850, 57287, 63016,
             65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes, py_salary_y, width=width,color="#008fd5", label="Python")

js_salary_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes+width, js_salary_y, width=width,color="#e5ae38", label="JavaScript")

plt.legend()

#To avoid having index for x axis
plt.xticks(ticks=x_indexes,labels=ages_x)

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")



plt.show()


# In[8]:


import csv
import numpy as np
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    row=next(csv_reader)
    print(row)
    


# In[9]:


import csv
import numpy as np
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    row=next(csv_reader)
    print(row['LanguagesWorkedWith'].split(';'))
    


# In[10]:


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

print(language_counter)
    


# In[11]:


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
print(language_counter.most_common(15))


# In[12]:


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

        languages=[]
        popularity=[]
        
        for item in (language_counter.most_common(15)):
            languages.append(item[0])
            popularity.append(item[1])
            
        print(languages)
        print(popularity)


# In[13]:


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

        languages=[]
        popularity=[]
        
        for item in (language_counter.most_common(15)):
            languages.append(item[0])
            popularity.append(item[1])
            
plt.barh(languages,popularity)

plt.title("Most Popular Programming Languages")

plt.xlabel("No.of people who use")



plt.show()


# In[17]:


import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

#Grab data from csv file
with open('data.csv') as csv_file:
    csv_reader= csv.DictReader(csv_file)
    
    language_counter=Counter()
    
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

        languages=[]
        popularity=[]
        
    for item in (language_counter.most_common(15)):
            languages.append(item[0])
            popularity.append(item[1])
            
    languages.reverse()
    popularity.reverse()
    
plt.barh(languages,popularity)

plt.title("Most Popular Programming Languages")

plt.xlabel("No.of people who use")



plt.show()


# In[22]:


import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of People Who Use")


plt.show()


# In[ ]:





# In[ ]:




