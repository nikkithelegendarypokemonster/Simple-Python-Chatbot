import random
name="sample"

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
    return random.choice(line)

def parseReply(sentence,reply):
    file=open("history.txt","r")
    line=file.read().splitlines()
    file.close()
    sample=reply
    if(sentence in ["Please tell me more..."]):
        return ''
    elif(sentence in ["As I have recalled you had said that","You have said earlier that"] and len(line)>5):
    # just pick random from history that is not the past reply
        sample=line[random.randrange(0,len(line)-2)]
        print(line)
        li=list(sample.split(' '))
        rule={'I':' you ',"I'm":" you're ",'my':" you're ", "i":" you  ","me":" you ", "am":" are ","are":" am ","My":" your ","you":" i ","You":" I ","Your":" My ","your":" my "}
        for x in range(len(li)):
            for key, value in rule.items():
                if(li[x]==key):
                    li[x]=value
        str1=" "
        return str1.join(li)
    else:
    #normal conversion of string
    #Dictionary
        li=list(sample.split(' '))
        rule={'I':' you ',"I'm":" you're ",'my':" you're ", "i":" you  ","me":" you ", "am":" are ","are":" am ","My":" your ","you":" i ","You":" I ","Your":" My ","your":" my ","yes":"","and":"","also":""}
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


"""" responses"""
def robot(reply):
    """response"""
    # robot does all the computing
    # first get the reply of user
    if(reply =="quit"):
        print("bye bye")
        return 0
    #second look if same reply happend previously then reply "Yeah I Know" and dont store the reply in history return boolean
    if(not(check_Db(reply))):
        print("Please Reply Something Else...")
    else:
        # third if succesful parse the string as a reply
        response=parse(reply)
        #put reply in db
        file=open("history.txt","a")
        file.write("{}\n".format(reply))
        file.close()
        #ROBOT TALK
        print("Robot: ",response)
    converse()
    return 0


def user():
    """reply"""
    #just reply anything and send to robot
    reply = input("{} : ".format(name))
    return reply

def converse():
    robot(user())
    return 0

def main():
    print("You're Name:",end="\n")
    Name=input()
    global name
    name=Name
    """ first greet"""
    print("Good Day ",Name," How are you today?")
    converse()


# The entry point for program execution
if __name__ == "__main__":
    main()
