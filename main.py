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
        if len(self.treeArray) >= 1:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже создана")
            return
        
        self.treeArray = [random.randint(10, 99) for number in range(15)]
        self.printArray()
        

    def printArray(self):
        for i in range(len(self.treeArray)):
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.treeArray[i])))

        position = int(len(self.treeArray) / 2)
        i = 0
        rows = 0
        maxEleminRow = 1
        while rows < self.ui.treeView.rowCount():
            j = 0
            firstElemInRow = position
            while maxEleminRow > j and i < len(self.treeArray):
                self.ui.treeView.setItem(rows, firstElemInRow, QtWidgets.QTableWidgetItem(str(self.treeArray[i])))
                i += 1
                firstElemInRow += position * 2 + 2
                j += 1
            position //= 2
            maxEleminRow *= 2
            rows += 1

        
    def clearTable(self):
        if len(self.treeArray) == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже очищена")
            return

        self.ui.arrayView.clear()
        self.ui.treeView.clear()
        
        self.treeArray.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
