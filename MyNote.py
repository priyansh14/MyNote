#!/usr/bin/env python
# coding: utf-8

# In[14]:


from tkinter import *

import os
from tkinter.messagebox import showinfo

  
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
        
def about():
    showinfo("MyNote","A NotePad by Priyansh Tiwari")
    

def quitApp():
    root.destroy()
    
def newFile():
    global file
    root.title("Untitled - MyNote")
    file = None
    TextArea.delete(1.0,END)    #From Line 1 Character 0 to End,clear up everything
    
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - MyNote")
        TextArea.delete(1,0,END)
            
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled Document.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
                
            root.title(os.path.basename(file)+" - MyNote")
            print("Text Secured")
    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()



if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - MyNote")
    root.geometry("644x788")
    root.wm_iconbitmap("1.png")
    
    TextArea = Text(root,font = "lucida 13")
    TextArea.pack(expand = True,fill=BOTH)
    file = None
    
    MenuBar = Menu(root)
    root.config(menu=MenuBar)
    FileMenu = Menu(MenuBar,tearoff=0)
    FileMenu.add_command(label = "New", command = newFile)
    
    FileMenu.add_command(label="Open",command = openFile)
    FileMenu.add_command(label="Save",command = saveFile)
    
    FileMenu.add_command(label = "Exit",command = quitApp)
    MenuBar.add_cascade(label="File",menu = FileMenu)
    
    
    sb = Scrollbar(TextArea)
    sb.pack(side = RIGHT,fill= Y)
    sb.config(command = TextArea.yview)
    TextArea.config(yscrollcommand=sb.set)
    #--------------------------------------FILE TAB ENDED----------------------------------------
    #EDIT MENU TAB
    EditMenu =  Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label = "Copy",command=copy)
    EditMenu.add_command(label = "Cut",command=cut)
    EditMenu.add_command(label = "Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu = EditMenu)
    #--------------------------------------------------------------------------------------------
    #HELP TAB
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label = "About",command = about)
    MenuBar.add_cascade(label = "Help",menu=HelpMenu)
    #--------------------------------------------------------------------------------------------
    #TIME TO MAKE FUNCTIONS !!!
    root.mainloop()
            


# In[ ]:





# In[ ]:




