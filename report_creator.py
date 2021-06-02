import operator

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

def getInputReport(initial_report_local, wordsToDelete): #Возврадает массив строк без "Новые", "Орг" и прочего ненужного

    # with open('otchet.txt', 'r', encoding='utf-8') as f:
    #     initial_report_local = f.read().splitlines()

    for i in initial_report_local:  # Удаляем Новые и Орг
        if arrayInStr(wordsToDelete, i):
            initial_report_local.remove(i)

    initial_report_local = [i for i in initial_report_local if i != ""]  # Удаляем оставшиеся пробелы
    return initial_report_local

def countEdit(edit): # Считает, сколько правок в одной записи
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
    currenProject = listOfAnim[0].getProj()
    print(currenProject)
    for i in listOfAnim:
        a = i.getProj()
        if a == currenProject:
            print(i.getName())
        else:
            print(a)
            currenProject = a
            print(i.getName())

def printOtchet():
    print("Отчет (ДАТА)")
    print()
    print("Новые (", len(listOfAnimation), ")")
    print()
    print("Легкие (", len(listOfEasy), ")")
    printProjAndAnim(listOfEasy)
    print()
    print("Средние (", len(listOfMedium), ")")
    printProjAndAnim(listOfMedium)
    print()
    print("Сложные (", len(listOfHard), ")")
    printProjAndAnim(listOfHard)
    print()
    a = countAllEdits(listOfEdit)
    print("Правки (", a, ")")
    printProjAndAnim(listOfEdit)

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

def createReportList(inputData):
    # Получили на вход ЧТО-ТО

    wordsToDelete = ["Новые", "орг", "Правки"]
    wordsOfDifficulties = ["(л)", "(ср)", "(сл)"]

    wordsOfEasy = ["(л)"]
    wordsOfMedium = ["(ср)"]
    wordOfHard = ["(сл)"]

    wordsOfProject = ["SE", "CE"]

    initial_report = []

    initial_report  = getInputReport(inputData, wordsToDelete) #Удаляем орг и пробелы

    listOfAll = []
    listOfAnimation = []
    listOfEdit = []

    listOfEasy = []
    listOfMedium = []
    listOfHard = []

    currenProject = "КАКОЙ_ТО ПРОЕКТ"

    for i in initial_report: # Переписываем исходный список в формате Аним-Проект (для этого есть отдельны тип)
        if arrayInStr(wordsOfProject, i):
            currenProject = i
        else:
            anim = Anim(i, currenProject)
            listOfAll.append(anim)

    for i in listOfAll: # Делим список на Аним и Правки
        if arrayInStr(wordsOfDifficulties, i.name):
            listOfAnimation.append(i)
        else:
            listOfEdit.append(i)

    for i in listOfAnimation: # Делим аним на три сложности
        if arrayInStr(wordsOfEasy, i.name):
            listOfEasy.append(i)
        elif arrayInStr(wordsOfMedium, i.name):
            listOfMedium.append(i)
        else:
            listOfHard.append(i)

    listOfEasyProject = []

    # Сортируем по Проектам списки с аним всех сложностей и правки

    listOfEasy = sorted(listOfEasy, key=operator.attrgetter('project'))
    listOfMedium = sorted(listOfMedium, key=operator.attrgetter('project'))
    listOfHard = sorted(listOfHard, key=operator.attrgetter('project'))
    listOfEdit = sorted(listOfEdit, key=operator.attrgetter('project'))

    # Формируем массив строк из всего, что получилось

    reportList = []

    currentStr = "Отчет " + "Дата"
    reportList.append(currentStr)

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

    return reportList

initial_report = ""

# with open('otchet 2.txt', 'r', encoding='utf-8') as f:
#          initial_report = f.read().splitlines()
#
# resList = createReportList(initial_report)
#
# for i in resList:
#      print(i)

