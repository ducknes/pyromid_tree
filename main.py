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

        self.ui.treeView.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.treeArray[0])))
        self.ui.treeView.setItem(1, 3, QtWidgets.QTableWidgetItem(str(self.treeArray[1])))
        self.ui.treeView.setItem(1, 11, QtWidgets.QTableWidgetItem(str(self.treeArray[2])))
        self.ui.treeView.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.treeArray[3])))
        self.ui.treeView.setItem(2, 5, QtWidgets.QTableWidgetItem(str(self.treeArray[4])))
        self.ui.treeView.setItem(2, 9, QtWidgets.QTableWidgetItem(str(self.treeArray[5])))
        self.ui.treeView.setItem(2, 13, QtWidgets.QTableWidgetItem(str(self.treeArray[6])))
        self.ui.treeView.setItem(3, 0, QtWidgets.QTableWidgetItem(str(self.treeArray[7])))
        self.ui.treeView.setItem(3, 2, QtWidgets.QTableWidgetItem(str(self.treeArray[8])))
        self.ui.treeView.setItem(3, 4, QtWidgets.QTableWidgetItem(str(self.treeArray[9])))
        self.ui.treeView.setItem(3, 6, QtWidgets.QTableWidgetItem(str(self.treeArray[10])))
        self.ui.treeView.setItem(3, 8, QtWidgets.QTableWidgetItem(str(self.treeArray[11])))
        self.ui.treeView.setItem(3, 10, QtWidgets.QTableWidgetItem(str(self.treeArray[12])))
        self.ui.treeView.setItem(3, 12, QtWidgets.QTableWidgetItem(str(self.treeArray[13])))
        self.ui.treeView.setItem(3, 14, QtWidgets.QTableWidgetItem(str(self.treeArray[14])))

        
    def clearTable(self):
        if len(self.treeArray) == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь уже очищена")
            return

        self.ui.arrayView.clear()
        self.ui.treeView.clear()
        
        self.treeArray.clear()

    def fixUp(self):
        k = len(self.treeArray)
        while k > 1 and self.treeArray[k / 2] < self.treeArray[k]:
            self.treeArray[k], self.treeArray[k / 2] = self.treeArray[k / 2], self.treeArray[k]
            k //= 2
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
