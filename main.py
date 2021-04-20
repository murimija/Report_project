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

wordsToDelete = ["Новые", "орг", "Правки"]
wordsOfDifficulties = ["(л)", "(ср)", "(сл)"]

wordsOfEasy = ["(л)"]
wordsOfMedium = ["(ср)"]
wordOfHard = ["(сл)"]

wordsOfProject = ["SE", "CE"]

with open('otchet.txt', 'r', encoding='utf-8') as f:
    initial_report = f.read().splitlines()

for i in initial_report:  # Удаляем Новые и Орг
    if arrayInStr(wordsToDelete, i):
        initial_report.remove(i)

initial_report = [i for i in initial_report if i != ""]  # Удаляем оставшиеся пробелы

listOfAll = []
listOfAnimation = []
listOfEdit = []

listOfEasy = []
listOfMedium = []
listOfHard = []

currenProject = "КАКОЙ_ТО ПРОЕКТ"

for i in initial_report:
    if arrayInStr(wordsOfProject, i):
        currenProject = i
    else:
        anim = Anim(i, currenProject)
        listOfAll.append(anim)

for i in listOfAll:
    if arrayInStr(wordsOfDifficulties, i.name):
        listOfAnimation.append(i)
    else:
        listOfEdit.append(i)

for i in listOfAnimation:
    if arrayInStr(wordsOfEasy, i.name):
        listOfEasy.append(i)
    elif arrayInStr(wordsOfMedium, i.name):
        listOfMedium.append(i)
    else:
        listOfHard.append(i)

listOfEasyProject = []

testList = []

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

listOfEasy = sorted(listOfEasy, key=operator.attrgetter('project'))
listOfMedium = sorted(listOfMedium, key=operator.attrgetter('project'))
listOfHard = sorted(listOfHard, key=operator.attrgetter('project'))
listOfEdit = sorted(listOfEdit, key=operator.attrgetter('project'))

def countEdit(edit):
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

printOtchet()

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import rpui  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, rpui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.createReportButton.clicked.connect(self.createReport)  # Выполнить функцию browse_folder
        # при нажатии кнопки

    def createReport(self):
        print("Типа отчет!")
        self.repOutputLbl.setText("Типа отчет!")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()




