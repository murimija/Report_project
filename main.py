import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import rpui  # Это наш конвертированный файл дизайна
import report_creator

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
        inputReport = self.inputField.toPlainText()
        report_creator.initial_report = inputReport
        report_creator.setInitialReport(inputReport)
        report_creator.createReportList()
        print(report_creator.createReportList())
        #print(inputReport)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()




