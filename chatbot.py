#Description: This is a chat bot GUI
#Import the library
from tkinter import *
import random
name=""
root = Tk()
def check_Db(reply):
    file=open("history.txt","r")
    line=file.read().splitlines()
    file.close()
    for x in range(len(line)):
        if(reply == line[x]):
            return False
    return True

def get_sentence():
    file=open("sentences.txt","r")
    line=file.read().splitlines()
    file.close()
    
    file=open("history.txt","r")
    line2=file.read().splitlines()
    file.close()

    if(len(line2)<3):
        return line[random.randrange(0,3)]
    
    return random.choice(line)

def parseReply(sentence,reply):
    file=open("history.txt","r")
    line=file.read().splitlines()
    file.close()
    sample=reply
    li=list(sample.split(' '))
    rule={'I':' you ',"I'm":" you're ",'my':" you're ", "i":" you  ","me":" you ", "am":" are ","are":" am ","My":" your ","you":" i ","You":" I ","Your":" My ","your":" my ","yes":"","and":"","also":"","Because":"","because":""}
        
    if(sentence in ["Please tell me more..."]):
        return ''
    elif(sentence in ["As I have recalled you had said that","You have said earlier that"]):
    # just pick random from history that is not the past reply
        sample=line[random.randrange(0,len(line)-1)]
        li=list(sample.split(' '))
    #normal conversion of string
    #Dictionary
    for x in range(len(li)):
        for key, value in rule.items():
            if(li[x]==key):
                li[x]=value
    str1=" "
    return str1.join(li)


def parse(reply):
    #implement the robots reply structure
    sen=get_sentence()
    return sen+" "+parseReply(sen,reply)


def robot(reply):
    """response"""
    response=""
    # robot does all the computing
    # first get the reply of user
    #second look if same reply happend previously then reply "Yeah I Know" and dont store the reply in history return boolean
    if(not(check_Db(reply))):
        chatWindow.insert(END,"Robot: Earlier you said that"+"\n","robot")
        messageWindow.delete('1.0', END)
    else:
        # third if succesful parse the string as a reply
        response=parse(reply)
        #put reply in db
        file=open("history.txt","a")
        file.write("{}\n".format(reply))
        file.close()
    #return the parsed respsonse
    return response
def reply():
    global name
    if(name==""):
        name = messageWindow.get(1.0, "end-1c")
        if(name=="quit"):
            #in text box chat window display robot response
            chatWindow.insert(END,"Robot: Bye Bye\n","robot")
            #destroy the whole window
            root.destroy()
            #then disply user reply
        chatWindow.insert(END,name+"\n","user")
        #first set the greet of robot to user
        chatWindow.insert(END,"Robot: Hello "+name+" What can I do for you?\n","robot")
        # upon completion of input and submission delet value in textbox
        messageWindow.delete('1.0', END)
    else:
        #get user reply upon btn press
        reply=messageWindow.get(1.0, "end-1c")
        if(reply=="quit"):
            chatWindow.insert(END,"Robot: Bye Bye\n","robot")
            root.destroy()
        elif(reply=="" or reply==" "):
            chatWindow.insert(END,"Robot: Please input something...\n","robot")
        else:
            chatWindow.insert(END,name+": "+reply+"\n","user")
        # the set the robots response
            response=robot(reply)
            if(response):
                chatWindow.insert(END,"Robot: "+response+"\n","robot")
        messageWindow.delete('1.0', END)

def par():
    return 'break'

root.title("Psychotherapy ChatBot")
root.geometry("400x500")
root.resizable(width=FALSE, height=FALSE)


chatWindow = Text(root, bd=1, bg="black",  width="50", height="8", font=("Arial", 15))
chatWindow.place(x=6,y=6, height=385, width=370)
chatWindow.insert(END, "Robot: Hello whats your name?\n","robot")
chatWindow.tag_config('robot', foreground="white")
chatWindow.tag_config('user', foreground="#00ffff")

messageWindow = Text(root, bd=0, bg="black", insertbackground='white',width="30", height="4", font=("Arial", 15), foreground="#00ffff")
messageWindow.place(x=128, y=400, height=88, width=260)
messageWindow.bind('<Return>',par())

scrollbar = Scrollbar(root, command=chatWindow.yview, cursor="star")
scrollbar.place(x=375,y=5, height=385)

Button= Button(root, text="Send",  width="12", height=5,
                    bd=0, bg="#0080ff", activebackground="#00bfff",foreground='#ffffff',font=("Arial", 12),command=reply)
Button.place(x=6, y=400, height=88)

root.mainloop()
