import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import rpui  # Это наш конвертированный файл дизайна
import report_creator
import new_zoom_check
import os
import unicodedata
import datetime

class ExampleApp(QtWidgets.QMainWindow, rpui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.createReportButton.clicked.connect(self.createReport)  # Выполнить функцию browse_folder
        # при нажатии кнопки
        # self.percentageButton.clicked.connect(self.countPercentage)
        self.checkNewZoomButton.clicked.connect(self.check_new_zoom)
        self.browseFolderButton.clicked.connect(self.browse_folder)
        self.percentageButton.clicked.connect(self.calculate_rate)
        self.percentageButtonHand.clicked.connect(self.calculate_rate_hand)

    def createReport(self):

        input_report = self.inputField.toPlainText()

        list01 = input_report.splitlines()

        resList = report_creator.createReportList(list01)

        self.outputField.clear()

        for i in resList:
            self.outputField.append(i)

        datetime.datetime.today()
        today = datetime.datetime.today().weekday()
        hours = (today + 1) * 8 #Считаем проценты для всех
        self.hours.setValue(hours)


        hmeehl = [report_creator.numOfHard, report_creator.numOfMedium, report_creator.numOfEasy,
                  report_creator.numOfEdit, report_creator.numOfHo, report_creator.numOfLoc, self.org.value()]

        hours = self.hours.value()

        self.j_perc_label.setText(
            "J% " + str(round((report_creator.countPercentage("J", hmeehl) / (hours)) * 100, 2)) + "%")
        self.m_perc_label.setText(
            "M% " + str(round((report_creator.countPercentage("M", hmeehl) / (hours)) * 100, 2)) + "%")
        self.s_perc_label.setText(
            "S% " + str(round((report_creator.countPercentage("S", hmeehl) / (hours)) * 100, 2)) + "%")
        self.l_perc_label.setText(
            "L% " + str(round((report_creator.countPercentage("L", hmeehl) / (hours)) * 100, 2)) + "%")

        self.outputCheckField.clear()
        resList2 = report_creator.createInfoCheсkList()
        #print(report_creator.createInfoCheсkList())
        for i in resList2:
             self.outputCheckField.append(i)

        #print(report_creator.createReportList())
        #print(inputReport)

    def browse_folder(self):
        #print("Тест")
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        content = os.listdir(directory)

        for i in content:
            self.inputZoomInFolder_2.append(i)

        #print(content)

    def check_new_zoom(self):

        # iy1 = "й"
        #
        # iy2 = "й"
        # print(len(iy1), len(iy2))
        #
        # iy2 = unicodedata.normalize('NFKC', iy2)
        # print(len(iy1), len(iy2))

        input_table_list = self.inputZoomInTable.toPlainText()
        list01 = input_table_list.splitlines()
        list01 = new_zoom_check.create_list_from_table(list01)

        for n, i in enumerate(list01, 0): #Сводим кодировки
            list01[n] = unicodedata.normalize('NFKC', i)

        #print(list01)

        #print(list01)

        input_folder_list = self.inputZoomInFolder_2.toPlainText()
        list02 = input_folder_list.splitlines()

        for n, i in enumerate(list02, 0):
            list02[n] = unicodedata.normalize('NFKC', i)

        #print(list01)

        res_list = new_zoom_check.find_new_zoom(list01, list02)

        self.outputNewZooms.clear()

        self.outputNewZooms.append("Новые: " + str(len(res_list)))

        for i in res_list:
             self.outputNewZooms.append(i)

        #print(res_list)

    def calculate_rate(self):

        hmeehl = [report_creator.numOfHard, report_creator.numOfMedium, report_creator.numOfEasy, report_creator.numOfEdit, report_creator.numOfHo, report_creator.numOfLoc, self.org.value()]

        hours = self.hours.value()

        self.j_perc_label.setText(
            "J% " + str(round((report_creator.countPercentage("J", hmeehl) / (hours)) * 100, 2)) + "%")
        self.m_perc_label.setText(
            "M% " + str(round((report_creator.countPercentage("M", hmeehl) / (hours)) * 100, 2)) + "%")
        self.s_perc_label.setText(
            "S% " + str(round((report_creator.countPercentage("S", hmeehl) / (hours)) * 100, 2)) + "%")
        self.l_perc_label.setText(
            "L% " + str(round((report_creator.countPercentage("L", hmeehl) / (hours)) * 100, 2)) + "%")

    def calculate_rate_hand(self):

        hmeehl = [self.numHardHand.value(), self.numMediumHand.value(), self.numEasyHand.value(),
                  self.numEditHand.value(), self.numHoHand.value(), self.numLocHand.value(), self.org.value()]

        hours = self.hours.value()

        self.j_perc_label.setText(
            "J% " + str(round((report_creator.countPercentage("J", hmeehl) / (hours)) * 100, 2)) + "%")
        self.m_perc_label.setText(
            "M% " + str(round((report_creator.countPercentage("M", hmeehl) / (hours)) * 100, 2)) + "%")
        self.s_perc_label.setText(
            "S% " + str(round((report_creator.countPercentage("S", hmeehl) / (hours)) * 100, 2)) + "%")
        self.l_perc_label.setText(
            "L% " + str(round((report_creator.countPercentage("L", hmeehl) / (hours)) * 100, 2)) + "%")

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()




