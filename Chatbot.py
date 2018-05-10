from random import randint

Classifiers = [ "open dag", "proefstuderen", "aanmelden", 
                "kosten", "eerste jaar", "1e jaar",
                "tweede jaar", "2e jaar", "derde jaar",
                "3e jaar", "vierde jaar", "4e jaar", 
                "afstuderen", "zelfstudie", "stage",
                "periodes","werk", "beroepen"]

GreetingsArray=["Hey! waarmee kan ik je helpen?",
                "Hallo! Wat wil je weten over informatica?",
                "Hey, welkom bij Hogeschool Rotterdam! Heb je een vraag?"]


def main():
    ##wait for input
    InitiateConversation()

def InitiateConversation():
    print(GreetingsArray[randint(0,2)])
    GetUserInput()

def GetUserInput():
    userInput = str.lower(input(""))
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
    
    #if "open dag" in topicArray:
    #    finalAnswer = finalAnswer + "open dag info"
    if "proefstuderen" in topicArray:
        finalAnswer = finalAnswer + "de eerstvolgende proefstudeerdag is op 30 mei, hier leer je "
    if "aanmelden" in topicArray:
        finalAnswer = finalAnswer + "aanmeldings info"    
    if "kosten" in topicArray:
        finalAnswer = finalAnswer + "kosten info"
    #if "eerste jaar" or "1e jaar" in topicArray:
    #    finalAnswer = finalAnswer + "eerste jaars info"
    #if "tweede jaar" or "2e jaar" in topicArray:
    #    finalAnswer = finalAnswer + "tweede jaars info"
    #if "derde jaar" or "3e jaar" in topicArray:
    #    finalAnswer = finalAnswer + "derde jaars info"    
    #if "vierde jaar" or "4e jaar" in topicArray:
    #    finalAnswer = finalAnswer + "vierde jaars info"
    if "afstuderen" in topicArray:
        finalAnswer = finalAnswer + ""
    if "stage" in topicArray:
        finalAnswer = finalAnswer + "stage info"
    if "periodes" in topicArray:
        finalAnswer = finalAnswer + "periode info"    
    #if "werk" and "beroepen" in topicArray:
    #    finalAnswer = finalAnswer + "werk/beroepen info"

    ReturnAnswer(finalAnswer)
    
def ReturnAnswer(questionAnswer):
    print(questionAnswer)
    

## RUN
main()