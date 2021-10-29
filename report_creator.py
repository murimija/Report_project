import operator
import re
import datetime
import math

from pip._vendor.tenacity._utils import now


def arrayInStr(array, str):
    res = False
    for i in array:
        if i in str:
            res = True
    return res


def printListAnim(array):
    for i in array:
        i.printAnim()


class Anim:

    def __init__(self, name, project):
        self.name = name
        self.project = project

    def printAnim(self):
        print(self.name, self.project)

    def getName(self):
        return self.name

    def getProj(self):
        return self.project


class Proj:
    def __init__(self, name, listOfAnim):
        self.name = name
        self.listOfAnim = listOfAnim

    def appendAnimToProj(self, app):
        self.listOfAnim.append(app)

    def printProj(self):
        print(self.name)
        for i in self.listOfAnim:
            print(i)


def setInitialReport(irl):
    global initial_report
    initial_report = irl


def getInputReport(initial_report_local,
                   wordsToDelete):  # Возврадает массив строк без "Новые", "Орг" и прочего ненужного

    # with open('otchet.txt', 'r', encoding='utf-8') as f:
    #     initial_report_local = f.read().splitlines()

    for i in initial_report_local:  # Правки, орг и остальное из wordsToDelete
        if arrayInStr(wordsToDelete, i):
            initial_report_local.remove(i)

    for i, value in enumerate(initial_report_local):  # Удаляем Новые и часть строки, которая после
        initial_report_local[i] = value.partition("Новые")[0] # Вот здесь приписал i-1, не знаю, почему это работает!

    #print(initial_report_local)

    for i, value in enumerate(initial_report_local):  # Удаляем табы
        initial_report_local[i] = value.replace('\"', '')

    initial_report_local = [i for i in initial_report_local if i != ""]  # Удаляем оставшиеся пробелы

    #print(initial_report_local)

    return initial_report_local


def countEdit(edit):  # Считает, сколько правок в одной записи
    if "(1)" in edit:
        return 1
    elif "(2)" in edit:
        return 2
    elif "(3)" in edit:
        return 3
    elif "(4)" in edit:
        return 4
    elif "(5)" in edit:
        return 5
    elif "(6)" in edit:
        return 6
    elif "(7)" in edit:
        return 7
    elif "(8)" in edit:
        return 8
    elif "(9)" in edit:
        return 9
    elif "(10)" in edit:
        return 10
    else:
        return 1


def countAllEdits(list):
    summ = 0
    for i in list:
        summ += countEdit(i.getName())
    return summ


def printProjAndAnim(listOfAnim):
    if len(listOfAnim) == 0:
        return
    current_project = listOfAnim[0].getProj()
    print(current_project)
    for i in listOfAnim:
        a = i.getProj()
        if a == current_project:
            print(i.getName())
        else:
            print(a)
            current_project = a
            print(i.getName())


# def printOtchet():
#     print("Отчет (ДАТА)")
#     print()
#     print("Новые (", len(listOfAnimation), ")")
#     print()
#     print("Легкие (", len(listOfEasy), ")")
#     printProjAndAnim(listOfEasy)
#     print()
#     print("Средние (", len(listOfMedium), ")")
#     printProjAndAnim(listOfMedium)
#     print()
#     print("Сложные (", len(listOfHard), ")")
#     printProjAndAnim(listOfHard)
#     print()
#     a = countAllEdits(listOfEdit)
#     print("Правки (", a, ")")
#     printProjAndAnim(listOfEdit)


def toListProjAndAnim(listOfAnim, listToAdd):
    if len(listOfAnim) == 0:
        return
    currenProject = listOfAnim[0].getProj()
    listToAdd.append(currenProject)
    for i in listOfAnim:
        a = i.getProj()
        if a == currenProject:
            listToAdd.append(i.getName())
        else:
            listToAdd.append(a)
            currenProject = a
            listToAdd.append(i.getName())


# Создаем счетчики для всего, они нам будут нужны
numOfEasy = 0
numOfMedium = 0
numOfHard = 0
numOfEdit = 0
numOfHo = 0
numOfLoc = 0


def createReportList(inputData):
    # Получили на вход ЧТО-ТО

    wordsToDelete = ["орг", "Правки", "Локализации"]
    wordsOfDifficulties = ["(л)", "(ср)", "(сл)", "(Л)", "(Ср)", "(Сл)", "(СР)", "(СЛ)"]

    wordsOfEasy = ["(л)", "(Л)"]
    wordsOfMedium = ["(ср)", "Ср", "СР"]
    wordOfHard = ["(сл)", "(Сл)", "(СЛ)"]

    wordsOfProject = ["SE", "CE", "se", "ce", "Se", "Ce", "srv", "Srv", "SRV"]

    countNewEditFromDaily(inputData)

    local_initial_report = getInputReport(inputData, wordsToDelete)  # Удаляем орг и пробелы

    #print(local_initial_report)

    listOfAll = []
    listOfAnimation = []
    listOfEdit = []

    listOfEasy = []
    listOfMedium = []
    listOfHard = []

    listOfHo = []
    listOfLoc = []

    currenProject = ""

    for i in local_initial_report:  # Переписываем исходный список в формате Аним-Проект (для этого есть отдельны тип)
        #if arrayInStr(wordsOfProject, i):
        if re.fullmatch(r'\b\w\w.{1,2}\s.{2,3}', i):
            currenProject = i
        else:
            anim = Anim(i, currenProject)
            listOfAll.append(anim)

    for i in listOfAll:  # Делим список на Аним и Правки
        if arrayInStr(wordsOfDifficulties, i.name):
            listOfAnimation.append(i)
        elif not re.search(r'\s', i.name):
            listOfLoc.append(i)
            #print("Я нашел локо: " + str(i.name))
        else:
            listOfEdit.append(i)

    for i in listOfAnimation:  # Делим аним на три сложности
        if re.search(r'\bho', i.name):
            listOfHo.append(i)
        elif arrayInStr(wordsOfEasy, i.name):
            listOfEasy.append(i)
        elif arrayInStr(wordsOfMedium, i.name):
            listOfMedium.append(i)
        else:
            listOfHard.append(i)

    # Сортируем по Проектам списки с аним всех сложностей и правки

    listOfEasy = sorted(listOfEasy, key=operator.attrgetter('project'))
    listOfMedium = sorted(listOfMedium, key=operator.attrgetter('project'))
    listOfHard = sorted(listOfHard, key=operator.attrgetter('project'))
    listOfEdit = sorted(listOfEdit, key=operator.attrgetter('project'))

    # Формируем массив строк из всего, что получилось

    #Тест!

    reportList = []

    currentStr = str( "ОТЧЕТ (" + str(datetime.datetime.now().day) +  "." + str(datetime.datetime.now().month) +  "." + str(datetime.datetime.now().year) + ")")
    reportList.append(currentStr)

    reportList.append("")

    currentStr = "Новые (" + str(len(listOfAnimation)) + ")"
    reportList.append(currentStr)

    reportList.append("")

    currentStr = "Легкие (" + str(len(listOfEasy)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfEasy, reportList)

    reportList.append("")

    currentStr = "Средние (" + str(len(listOfMedium)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfMedium, reportList)

    reportList.append("")

    currentStr = "Сложные (" + str(len(listOfHard)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfHard, reportList)

    reportList.append("")

    currentStr = "Правки (" + str(countAllEdits(listOfEdit)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfEdit, reportList)

    reportList.append("")

    currentStr = "Хо (" + str(len(listOfHo)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfHo, reportList)

    reportList.append("")

    currentStr = "Локализация (" + str(len(listOfLoc)) + ")"
    reportList.append(currentStr)

    toListProjAndAnim(listOfLoc, reportList)

    #print(listOfLoc)

    global numOfEasy
    global numOfMedium
    global numOfHard
    global numOfEdit
    global numOfHo
    global numOfLoc

    numOfEasy = len(listOfEasy)
    numOfMedium = len(listOfMedium)
    numOfHard = len(listOfHard)
    numOfEdit = countAllEdits(listOfEdit)
    numOfHo = len(listOfHo)
    numOfLoc = len(listOfLoc)

    return reportList

def createInfoCheсkList():

    reportList = []

    currentStr = str(numOfHard) + "\t" + str(numOfMedium) + "\t" + str(numOfEasy) + "\t" + str(numOfEdit)
    reportList.append(currentStr)

    summNew = numOfEasy + numOfMedium + numOfHard
    summEdit = numOfEdit

    currentStr = str("Новые в дневном: " + str(numOfNewDaily) + " = " + str(summNew) + " :Новые посчитаны")
    reportList.append(currentStr)

    currentStr = str("Правки в дневном: " + str(numOfEditDaily)  + " = " + str(summEdit) + " :Правки посчитаны")
    reportList.append(currentStr)

    return reportList


def countPercentage(grade, hmeel):

    numOfHard = hmeel[0]
    numOfMedium = hmeel[1]
    numOfEasy = hmeel[2]
    numOfEdit = hmeel[3]
    numOfHo = hmeel[4]
    numOfLoc = hmeel[5]
    numOfOrg = hmeel[6]

    #numOfEasyHoLoc = numOfEasy + math.ceil(numOfHo/2) + round(numOfLoc/3)

    #print(numOfEasyHoLoc)

    coef = [[2, 4, 0, 1], [1.4, 2.8, 12, 0.7], [1, 2, 8, 0.5]] #Нормативы

    if grade == "J":
        coefOfEasy = coef[0][0]
        coefOfMedium = coef[0][1]
        coefOfHard = coef[0][2]
        coefOfEdit = coef[0][3]

    elif grade == "M":
        coefOfEasy = coef[1][0]
        coefOfMedium = coef[1][1]
        coefOfHard = coef[1][2]
        coefOfEdit = coef[1][3]
    elif grade == "S":
        coefOfEasy = coef[2][0]
        coefOfMedium = coef[2][1]
        coefOfHard = coef[2][2]
        coefOfEdit = coef[2][3]
    else:
        coefOfEasy = coef[2][0]
        coefOfMedium = coef[2][1]
        coefOfHard = coef[2][2]
        coefOfEdit = coef[2][3]

        #print(numOfEasy * coefOfEasy + numOfMedium * coefOfMedium + numOfHard * coefOfHard + numOfEdit * coefOfEdit + math.ceil(numOfHo/2) + math.ceil(numOfLoc/3))

    return  numOfEasy * coefOfEasy + numOfMedium * coefOfMedium + numOfHard * coefOfHard + numOfEdit * coefOfEdit + math.ceil(numOfHo/2) + math.ceil(numOfLoc/3) + numOfOrg

numOfNewDaily = 0
numOfEditDaily = 0

def countNewEditFromDaily(inputData):

    newCounter = 0
    editCounter = 0

    for i in inputData:
        if arrayInStr(["Новые", "Новое"], i):
            temp = re.findall(r'\d+', i)
            newCounter += int(temp[0])
            #print(newCounter)

        if arrayInStr(["Правки"], i):
            temp = re.findall(r'\d+', i)
            editCounter += int(temp[0])
            #print(editCounter)

    global numOfNewDaily
    global numOfEditDaily

    numOfNewDaily = newCounter
    numOfEditDaily = editCounter

    #print(newCounter, numOfNewDaily)

    return [newCounter, editCounter]

# countPercentage("J")
#
# with open('otchet 2.txt', 'r', encoding='utf-8') as f:
#     initial_report = f.read().splitlines()

#wordsToDelete = ["орг", "Правки"]
#getInputReport(initial_report, wordsToDelete)

# resList = createReportList(initial_report)
#
# for i in resList:
#      print(i)
