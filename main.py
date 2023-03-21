from Form import *
import random
import sys
import numpy as np


class Tree(QtWidgets.QMainWindow):
    treeArray = np.empty(16, dtype=np.int64)
    current_size = 0

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
        if self.current_size > 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь заполнена")
            return
        
        for i in range(1, 16):
            self.treeArray[i] = random.randint(10, 99)
            self.fixUp(i)
        self.current_size = 15
        self.printArray()
        
    def printArray(self):
        for i in range(len(self.treeArray) - 1):
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.treeArray[i + 1])))

        self.ui.treeView.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.treeArray[1])))
        self.ui.treeView.setItem(1, 3, QtWidgets.QTableWidgetItem(str(self.treeArray[2])))
        self.ui.treeView.setItem(1, 11, QtWidgets.QTableWidgetItem(str(self.treeArray[3])))
        self.ui.treeView.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.treeArray[4])))
        self.ui.treeView.setItem(2, 5, QtWidgets.QTableWidgetItem(str(self.treeArray[5])))
        self.ui.treeView.setItem(2, 9, QtWidgets.QTableWidgetItem(str(self.treeArray[6])))
        self.ui.treeView.setItem(2, 13, QtWidgets.QTableWidgetItem(str(self.treeArray[7])))
        self.ui.treeView.setItem(3, 0, QtWidgets.QTableWidgetItem(str(self.treeArray[8])))
        self.ui.treeView.setItem(3, 2, QtWidgets.QTableWidgetItem(str(self.treeArray[9])))
        self.ui.treeView.setItem(3, 4, QtWidgets.QTableWidgetItem(str(self.treeArray[10])))
        self.ui.treeView.setItem(3, 6, QtWidgets.QTableWidgetItem(str(self.treeArray[11])))
        self.ui.treeView.setItem(3, 8, QtWidgets.QTableWidgetItem(str(self.treeArray[12])))
        self.ui.treeView.setItem(3, 10, QtWidgets.QTableWidgetItem(str(self.treeArray[13])))
        self.ui.treeView.setItem(3, 12, QtWidgets.QTableWidgetItem(str(self.treeArray[14])))
        self.ui.treeView.setItem(3, 14, QtWidgets.QTableWidgetItem(str(self.treeArray[15])))

    def clearTable(self):
        if self.current_size == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь пуста")
            return

        self.current_size = 0
        self.ui.arrayView.clear()
        self.ui.treeView.clear()
        
        np.delete(self.treeArray, 0)

    def fixUp(self, k):
        while k > 1 and self.treeArray[int(k / 2)] < self.treeArray[k]:
            self.treeArray[k], self.treeArray[int(k / 2)] = self.treeArray[int(k / 2)], self.treeArray[k]
            k //= 2
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
