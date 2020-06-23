#!/usr/bin/env python
# coding: utf-8

# ## Creating JSON File

# #### Can be ignored if already created

# In[2]:


import json


# In[8]:


data = {"weather today" : "30",
"weather tomorrow" : "40",
"Schedule today" : "10:00 AM"
       }


# In[9]:


with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)


# In[ ]:





# ## Functions For Input And Output 

# In[40]:


def values(ques,dicti):
    for i in ques :
        i=i.lower()
        try:
            dicti[i]+=1
        except:
            try: #for extra end character 
                dicti[i[:-1]]+=1
            except:
                try : #for any extra pre space
                    dicti[i[1:]]+=1
                except:
                    continue
    arr=[]
    for i in dicti: #We are only cocerned with the frequency of terms 
        arr.append(dicti[i])
        dicti[i]=0
    return arr


# ## Preprocessing
# ### Need to be executed only once

# In[41]:


def preprocessing(): 
    import json
    with open('data_file.json') as json_file: #reading json
        data = json.load(json_file)
    dic={}
    result_index=[]
    for i in data:
        result_index.append(data[i])
        for j in i.split(" "):
            dic[j.lower()]=0
    predata=[]
    for i in data :
        predata.append(values(i.split(" "),dic))
    return dic,result_index,predata


# ## Need To Run Every Time The Response Is Reqired

# In[42]:


def calculate(ques):
    ques=ques.split(" ")
    res=values(ques,dic)
    final=[]
    for i in predata :
        s=0
        for j in range(len(i)):
            s+=abs(i[j]-res[j])
        final.append(s)
    print(res)
    return result_index[final.index(min(final))]


# ## Execute Beforehand

# In[47]:


def clicked():
    a=messageWindow.get("1.0",END)
    messageWindow.delete("1.0",END)
    chatWindow.insert(END ,"User : "+a.strip()+"\n")
    response=calculate(a.strip())
    chatWindow.insert(END ,"Response : "+response+"\n")
    chatWindow.insert(END , "\n")
    chatWindow.yview(END)
    print(a,response)


# ## TKinter GUI

# In[48]:


dic,result_index,predata=preprocessing()
from tkinter import *
root = Tk()
root.title("Chat Bot")
root.geometry("400x500")
root.resizable(width=False, height=False)
main_menu = Menu(root)
chatWindow = Text(root, bd=1,  width="50", height="8", font=("Arial", 10), foreground="black")
chatWindow.place(x=6,y=6, height=385, width=370)

messageWindow = Text(root, bd=0, width="30", height="4", font=("Arial", 10), foreground="black")
messageWindow.place(x=128, y=400, height=88, width=260)
scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

Button= Button(root, text="Send",  width="12", height=5, bd=0, bg="#0080ff", command=clicked, activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12))
Button.place(x=6, y=400, height=88)



root.mainloop()


# In[ ]:




