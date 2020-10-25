#import unreal_engine as ue
import csv
import importlib

class Vocabulary:

    def __init__(self):
        self.begin_play()

    def begin_play(self):
        self.dataPath = "D:\\Coding\\UE4\\RoboWorld_BP22\\Content\\Python\\Data\\"
        self.preData = "PreprocessingData.csv"
        self.actions = "Actions.csv"

    def addRecord(self, command, answer):
        pass

    def getRecord(self, index):
        pass

    def delRecord(self, index):
        pass

    def getText(self):
        return "\n\nOK!!!"


    def getDataString(self):
        out = str()
        with open(self.dataPath+self.preData) as file:
            reader = csv.reader(file, delimiter=';')

            for row in reader:
                out += '[ %s ] -> [ %s ] : [ %s ]\n' % \
                       (row[0], row[1], row[2])
        return out

    def getActionsStringList(self):
        out = list()
        with open(self.dataPath + self.actions) as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                out.append(row["Действик"])
        return out







