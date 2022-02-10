from player_addition import *
from clear_function import *
from sleep_function import *
scoreCounter = []
scoreDict = {
        }
winnersDict = {
        }
def questioning():
        global scoreDict
        global pTotal
        global pList
        global scoreCounter
        N = pTotal
        correctAnswersCounter = 0
        wrongAnswersCounter = 0
        qDict = {
            "1": "Which country is a football team called \"Young Boys\"?", 
            "2": "Which country is football player called Luis Figu from?",
            "3": "Which country won the European Championship 2020",
            "4": "Which team did Sir Alex Ferguson managed the longest?",
            "5": "How many times has Brazil won the World Cup"
            }
        ansDict = {
            "1": "a)France   b)Spain   c)Switzerland",
            "2": "a)Czech Republic   b)Portugal   c)England",
            "3": "a)Italy   b)Slovakia   c)Poland",
            "4": "a)Sparta Prague   b)Manchester United   c)Real Madrid",
            "5": "a)7   b)5   c)10"
            }
        correctDict = {
            "1": "c",
            "2": "b",
            "3": "a",
            "4": "b",
            "5": "b"
            }
        print("\n")
        for pIndex in range(len(pList)):
            print(pList[pIndex] + " starts! Good luck!")
            print("\n")
            for qIndex in qDict:
                print(qDict[qIndex])
                print(ansDict[qIndex])
                answer = input()
                if answer == correctDict[qIndex]:
                    print("Correct!")
                    correctAnswersCounter = correctAnswersCounter+1
                    print("\n")
                else:
                    print("Wrong!")
                    wrongAnswersCounter = wrongAnswersCounter+1
                    print("\n")
            convertedCorrectAnswersCounter = str(correctAnswersCounter)
            convertedWrongAnswersCounter = str(wrongAnswersCounter)            
            print(pList[pIndex] + " has collected " + convertedCorrectAnswersCounter + " correct answer/s and " + convertedWrongAnswersCounter + " wrong answer/s.")
            scoreCounter.append(correctAnswersCounter)
            scoreDict[pList[pIndex]] = correctAnswersCounter
            correctAnswersCounter = 0
            wrongAnswersCounter = 0
            print("\n")
            twosecfunc()
        print("SCOREBOARD:")

        for x, y in zip(range(len(pList)), range(len(scoreCounter))):
            print(pList[x] + " : " + str(scoreCounter[y]) + " correct answers." )

        print("\n")
        listOfWinners = list()
        print("Winners:")
        winner = max(scoreDict.items(), key=lambda x: x[1])
        for key, value in scoreDict.items():
            if value == winner[1]:
                listOfWinners.append(key)
        print(listOfWinners)
                

