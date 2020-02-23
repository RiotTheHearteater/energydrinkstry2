DrinksList=[
        "Monster" + " has a total of" + (" ") + str(250) + " calories",
        "Rockstar"+ " has a total of" + (" ") + str(300) + " calories"
        ]


outputFile=open('DrinksList.txt','w')
for drink in DrinksList:
    outputFile.write (drink + "\n")
outputFile.close()

inputFile=open("DrinksList.txt","r")
print(inputFile.readline().key("Monster"))
inputFile.close()
