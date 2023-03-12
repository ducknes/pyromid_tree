from Form import *
import random
import sys

class Tree(QtWidgets.QMainWindow):
    treeArray = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit.clicked.connect(self.quit)
        self.ui.createQueue.clicked.connect(self.createArray)
        self.ui.clearQueue.clicked.connect(self.clearTable)

    def quit(self):
        self.ui.quit.clicked.connect(QtWidgets.QApplication.instance().quit)
    
    def createArray(self):
        if len(self.treeArray) != 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже создана")
            return
        
        self.treeArray = [random.randint(10, 99) for number in range(15)]
        for i in range(len(self.treeArray)):
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.treeArray[i])))

    def clearTable(self):
        if len(self.treeArray) == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже очищена")
            return
        
        for i in range(len(self.treeArray)):
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str("")))
        
        self.treeArray.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
