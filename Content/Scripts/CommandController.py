import unreal_engine as ue

from Vocabulary import Vocabulary
import re
import os

import csv

class CommandController:

    def __init__(self):
        self.begin_play()

    def begin_play(self):
        self.dataPath = ue.get_content_dir()+ "\\Scripts\\Data\\"
        self.preData = "Dialogs.csv"
        self.actions = "Actions.csv"
        self.actionList = list()
        self.generateVocabulary()
        self.vocab, self.intToWord = self.loadVocab()
        self.questions, self.answers, self.context = self.loadDialogIndexes()
        self.subjects = self.loadSubjects()


    def set_dataPath(self, path):
        self.dataPath = path.split("CommandController.py")[0]
        #self.dataPath = "D:\\Coding\\RoboWorld_BP22\\Content\\Scripts\\Data\\"
        self.preData = "Dialogs.csv"
        self.actions = "Actions.csv"
        self.actionList = list()
        self.generateVocabulary()
        self.vocab = self.loadVocab()
        self.questions, self.answers, self.context = self.loadDialogIndexes()
        self.subjects = self.loadSubjects()

    def loadSubjects(self):
        subjs=[]
        for line in self.answers:
            if line[0] not in subjs:
                subjs.append(line[0])
        return  subjs

    def commandToListIndex(self, command):
        com = command.lower()
        com = re.compile("([.,!?\"':;)( ])").split(com)
        return [self.vocab[word] for word in com]


    def generateVocabulary(self):
        self.dialogCSVDataList = list()
        vocab = list()
        comList = []
        ansList = []
        conList = []

        def writeFile(file, indexes):
            for ind in indexes:
                file.write(str(ind) + ' ')
            file.write('\n')

        def appendVocab(vocab, words):
            for word in words:
                if word.lower() not in vocab:
                    vocab.append(word.lower())

        with open(self.dataPath + self.preData) as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                com, ans, con = row['Команда'], row['Ответ'], row['Контекст']
                command = list()
                command.extend(re.compile("([.,!?\"':;)( ])").split(com))
                comList.append(command)
                answer = list()
                answer.extend(re.compile("([.,!?\"':;)(\->])").split(ans))
                ansList.append([word for word in answer if word !='-' and word !='' and word !='>'])
                context = []
                context.extend(re.compile("([.,!?\"':;)(])").split(con))
                conList.append(context)

        for line in ansList:
            appendVocab(vocab, line)
        for line in conList:
            appendVocab(vocab, line)
        for line in comList:
            appendVocab(vocab, line)
        indexesDialog = open(self.dataPath+'indexesDialog.txt', 'w')
        with open(self.dataPath+'vocab.txt', 'w') as f:
            for word in vocab:
               f.write(word + '\n')

        vocab = { vocab[i]  : i for i in range(0, len(vocab) ) }

        for i in range(len(comList)):
            comInds = [vocab[word.lower()] for word in comList[i] ]
            writeFile(indexesDialog, comInds)

            ansInds = [vocab[word.lower()] for word in ansList[i] if word != '-' and word !='>' and word != '']
            writeFile(indexesDialog, ansInds)

            conInds = [vocab[word.lower()] for word in conList[i] ]
            writeFile(indexesDialog, conInds)

        indexesDialog.close()

    def loadVocab(self):
        vocab = []
        with open(self.dataPath+'\\vocab.txt') as f:
            for line in f:
                vocab.append(line[:-1])

        return {vocab[i]: i for i in range(0, len(vocab))}, {i: vocab[i]for i in range(0, len(vocab))}

    def loadDialogIndexes(self):
        questions = []
        answers = []
        contexts = []
        with open(self.dataPath + '\\indexesDialog.txt') as f:
            k=0
            for line in f:
                numbers = [int(c) for c in line.split()]
                if k==0:
                    questions.append(numbers)
                if k==1:
                    answers.append(numbers)
                if k==2:
                    contexts.append(numbers[0])
                k+=1
                if k==3:
                    k=0

        return questions, answers, contexts

    def checkCommand(self, userCommand, temp_command):

        if set(userCommand).issubset(temp_command):
            return True
        else:
            return False


    def getActionListFromCommandString(self, command, context='любой'):
        print("Взял командку : "+command)
        com = self.commandToListIndex(command)
        
        actList = []
        conID = self.vocab[context]


        for i in range(len(self.questions)):
            quest = self.questions[i]
            con = self.context[i]
            if quest[0] == 61:
                n=1

            if quest == com and self.answers[i] not in actList:
                actList.append(self.answers[i])
        strList = []
        for line in actList:

            for ind in line:
                strList.append(str(ind))


        return self.checkDoubles(strList)

    def checkDoubles(self, comList):
        i=0
        n = len(comList)
        while i<n:
            buf = comList[i]
            c=0
            checkDouble= False
            for j in range(n):
                if comList[j] == buf:
                    c+=1
                if c>1:
                    comList.pop(j)
                    n-=1
                    checkDouble = True
                    break
            if checkDouble:
                i=0
            else:
                i+=1
        return comList





    def stringIntToInt(self, strVal):
        return int(strVal)

    def isAction(self, id):
        return id in self.subjects

    def getCommandStringFromIdsArray(self, array):
        comIds = [int(num) for num in array.split()]
        outString = 'Последовательность действий [ '
        for id in comIds:
            outString+=self.intToWord[id] + ', '
        outString+=']'
        print (outString)
        return outString

    def getActionStringFromCommandString(self, command):
        ids = self.getActionListFromCommandString(command)
        comstr = str()
        for id in ids:
            comstr+=id + ' '

        return self.getCommandStringFromIdsArray(comstr)

    def getWordFromID(self, id):
        return self.intToWord[int(id)]



if __name__=='__main__':
    command = ''
    print(CommandController().getActionStringFromCommandString(command))
    print(CommandController().getActionListFromCommandString(command))
