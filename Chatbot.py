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
    

    if "proefstuderen" in topicArray:
        finalAnswer = finalAnswer + "de eerstvolgende proefstudeerdag is op 30 mei, hier kan je de sfeer van de opleiding proeven en kijken of de manier van lesgeven wat voor jou is!"
    if "aanmelden" in topicArray:
        finalAnswer = finalAnswer + "Aanmeldingen kunnen vanaf onze site gedaan worden t/m 31 juli, dus wees snel!"    
    if "kosten" in topicArray:
        finalAnswer = finalAnswer + "kosten info"
    if "afstuderen" in topicArray:
        finalAnswer = finalAnswer + "Vaak kom je er tijdens je afstudeerstage in het vierde jaar achter wat je na je studie wil doen. Als zelfstandig consultant of toch liever op de IT-afdeling van een multinational? Vraag tijdens een open dag verder over het afstuderen."
    if "stage" in topicArray:
        finalAnswer = finalAnswer + "Je krijgt de gelegenheid werkervaring op te doen tijdens een stage in het derde jaar. Vijf maanden werk je bij een bedrijf om in praktijk te brengen wat je hebt geleerd!"
    if "periodes" in topicArray:
        finalAnswer = finalAnswer + "periode info"    


    ReturnAnswer(finalAnswer)
    
def ReturnAnswer(questionAnswer):
    print(questionAnswer)

def AskForAnotherQuestion():
    print("Zijn er nogmeer vragen?")
    GetUserInput()
    

## RUN
main()