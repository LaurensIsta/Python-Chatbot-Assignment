from random import randint
import os
import json

clear = lambda:os.system('cls')

Classifiers = [ "open dag", "proefstuderen", "aanmelden", 
                "kosten", "eerste jaar", "1e jaar",
                "tweede jaar", "2e jaar", "derde jaar",
                "3e jaar", "vierde jaar", "4e jaar", 
                "afstuderen", "zelfstudie", "stage",
                "periodes","werk", "beroepen",
                "nee", "doei"]

GreetingsArray=["Hey! waarmee kan ik je helpen?",
                "Hallo! Wat wil je weten over informatica?",
                "Hey, welkom bij Hogeschool Rotterdam! Heb je een vraag?"]

Chathistory = []

Username = "Ik"
Botname = "BOT"

def main():
    ##wait for input
    clear()
    InitiateConversation()

def ShowChat():
    for sentence in Chathistory:
        print(sentence)

def formatText(name, text, ret=False):
  formattedText = '{:<4s} {:<1s}'.format(name, "| " + text)
  if ret == True:
    return (formattedText)
  else:
    print(formattedText)

def InitiateConversation():
    ICformatted =formatText(Botname,GreetingsArray[randint(0,2)],ret=True)
    Chathistory.append(ICformatted)
    print(ICformatted)
    GetUserInput()

def GetUserInput():
    userInput = str.lower(input(""))
    UserInputformatted = formatText(Username,userInput,True)
    Chathistory.append(UserInputformatted)
    clear()
    ShowChat()
    HandleInput(userInput)
        
def HandleInput(userInput):
    userInputArray = userInput.split()
    InterpretInput(userInputArray)

def InterpretInput(userInputArray):
    topicArray = []
    for word in userInputArray:
        if word in Classifiers:
            topicArray.append(word)

    ComposeAnswer(topicArray)   
    


def ComposeAnswer(topicArray):
    finalAnswer = ""
    
    if topicArray == []:
        emptyTopicArrayResponse = formatText(Botname, "Ik snap je vraag niet, probeer het nog een keer!",True)
        Chathistory.append(emptyTopicArrayResponse)
    else:
        if "proefstuderen" in topicArray:
            finalAnswer = finalAnswer + "de eerstvolgende proefstudeerdag is op 30 mei, hier kan je de sfeer van de opleiding proeven en kijken of de manier van lesgeven wat voor jou is!"
        if "aanmelden" in topicArray:
            finalAnswer = finalAnswer + "Aanmeldingen kunnen vanaf onze site gedaan worden t/m 31 juli, dus wees snel!"    
        if "kosten" in topicArray:
            finalAnswer = finalAnswer + "Deze opleiding volgen kan vanaf €2000 per jaar."
        if "afstuderen" in topicArray:
            finalAnswer = finalAnswer + "Vaak kom je er tijdens je afstudeerstage in het vierde jaar achter wat je na je studie wil doen. Als zelfstandig consultant of toch liever op de IT-afdeling van een multinational? Vraag tijdens een open dag verder over het afstuderen."
        if "stage" in topicArray:
            finalAnswer = finalAnswer + "Je krijgt de gelegenheid werkervaring op te doen tijdens een stage in het derde jaar. Vijf maanden werk je bij een bedrijf om in praktijk te brengen wat je hebt geleerd!"
        if "periodes" in topicArray:
            finalAnswer = finalAnswer + "Alle leerjaren zijn in 4 periodes verdeeld."    
        if "doei" in topicArray:
            finalAnswer = formatText(Botname,"Tot snel!",True)
            Chathistory.append(finalAnswer)
            EndConversation() 
        
    ReturnAnswer(finalAnswer)
    
def ReturnAnswer(questionAnswer):
    RAformatted = formatText(Botname,questionAnswer,True)
    Chathistory.append(RAformatted)
    print(RAformatted)
    AskForAnotherQuestion()

def AskForAnotherQuestion():
    AFAQFormatted = formatText(Botname,"Zijn er nog meer vragen?",True)
    Chathistory.append(AFAQFormatted)
    print(AFAQFormatted)
    GetUserInput()

def SaveChatHistory():
    i = 0
    data = {}
    data["chat"] = []
    for sentence in Chathistory:
        
        data["chat"].append({i : sentence})
        i = i + 1
    with open('ChatOutput.json', 'w') as outfile:  
        json.dump(data, outfile)

def EndConversation():
    clear()
    ShowChat()
    SaveChatHistory()
    TerminateProgram()

def TerminateProgram():
    quit()

## RUN
main()