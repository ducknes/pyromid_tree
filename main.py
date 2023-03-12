from Form import *
import random
import sys

class Tree(QtWidgets.QMainWindow):
    queueCreated = False

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit.clicked.connect(self.quit)
        self.ui.createQueue.clicked.connect(self.createArray)

    def quit(self):
        self.ui.quit.clicked.connect(QtWidgets.QApplication.instance().quit)
    
    def createArray(self):
        if self.queueCreated:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже создана")
            return
        
        array = [random.randint(10, 99) for number in range(15)]
        self.queueCreated = True
        for i in range(len(array)):
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str(array[i])))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
