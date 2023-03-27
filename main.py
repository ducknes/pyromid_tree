from Form import *
import random
import sys
import numpy as np


class Tree(QtWidgets.QMainWindow):
    treeArray = [0] * 16
    current_size = 0
    resultArray = [] * 15

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit.clicked.connect(self.quit)
        self.ui.createQueue.clicked.connect(self.createArray)
        self.ui.clearQueue.clicked.connect(self.clearTable)
        self.ui.takeMax.clicked.connect(self.takeMax)
        self.ui.addNew.clicked.connect(self.add_new)
        self.ui.changePriority.clicked.connect(self.change_priority)

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
            self.ui.arrayView.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.treeArray[i + 1] if self.treeArray[i + 1] > 0 else " ")))

        for i in range(len(self.resultArray)):
            self.ui.resultView.setItem(0, i, QtWidgets.QTableWidgetItem(str(self.resultArray[i])))

        self.ui.treeView.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.treeArray[1] if self.treeArray[1] > 0 else " ")))
        self.ui.treeView.setItem(1, 3, QtWidgets.QTableWidgetItem(str(self.treeArray[2] if self.treeArray[2] > 0 else " ")))
        self.ui.treeView.setItem(1, 11, QtWidgets.QTableWidgetItem(str(self.treeArray[3] if self.treeArray[3] > 0 else " ")))
        self.ui.treeView.setItem(2, 1, QtWidgets.QTableWidgetItem(str(self.treeArray[4] if self.treeArray[4] > 0 else " ")))
        self.ui.treeView.setItem(2, 5, QtWidgets.QTableWidgetItem(str(self.treeArray[5] if self.treeArray[5] > 0 else " ")))
        self.ui.treeView.setItem(2, 9, QtWidgets.QTableWidgetItem(str(self.treeArray[6] if self.treeArray[6] > 0 else " ")))
        self.ui.treeView.setItem(2, 13, QtWidgets.QTableWidgetItem(str(self.treeArray[7] if self.treeArray[7] > 0 else " ")))
        self.ui.treeView.setItem(3, 0, QtWidgets.QTableWidgetItem(str(self.treeArray[8] if self.treeArray[8] > 0 else " ")))
        self.ui.treeView.setItem(3, 2, QtWidgets.QTableWidgetItem(str(self.treeArray[9] if self.treeArray[9] > 0 else " ")))
        self.ui.treeView.setItem(3, 4, QtWidgets.QTableWidgetItem(str(self.treeArray[10] if self.treeArray[10] > 0 else " ")))
        self.ui.treeView.setItem(3, 6, QtWidgets.QTableWidgetItem(str(self.treeArray[11] if self.treeArray[11] > 0 else " ")))
        self.ui.treeView.setItem(3, 8, QtWidgets.QTableWidgetItem(str(self.treeArray[12] if self.treeArray[12] > 0 else " ")))
        self.ui.treeView.setItem(3, 10, QtWidgets.QTableWidgetItem(str(self.treeArray[13] if self.treeArray[13] > 0 else " ")))
        self.ui.treeView.setItem(3, 12, QtWidgets.QTableWidgetItem(str(self.treeArray[14] if self.treeArray[14] > 0 else " ")))
        self.ui.treeView.setItem(3, 14, QtWidgets.QTableWidgetItem(str(self.treeArray[15] if self.treeArray[15] > 0 else " ")))

    def clearTable(self):
        if self.current_size == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь пуста")
            return

        self.current_size = 0
        self.ui.arrayView.clear()
        self.ui.treeView.clear()
        
        self.treeArray = [0 for x in range(len(self.treeArray))]

    def fixUp(self, k):
        while k > 1 and self.treeArray[int(k / 2)] < self.treeArray[k]:
            self.treeArray[k], self.treeArray[int(k / 2)] = self.treeArray[int(k / 2)], self.treeArray[k]
            k //= 2

    def fixDown(self, k):
        while 2 * k < len(self.treeArray):
            j = 2 * k
            if j < len(self.treeArray) and self.treeArray[j] < self.treeArray[j + 1]:
                j += 1
            if self.treeArray[k] > self.treeArray[j]:
                break
            self.treeArray[k], self.treeArray[j] = self.treeArray[j], self.treeArray[k]
            k = j

    def takeMax(self):
        if self.current_size == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь пуста")
            return
        
        tree_array_max = max(self.treeArray)
        self.resultArray.append(tree_array_max)
        self.treeArray[1] = 0
        self.fixDown(1)
        self.printArray()
        self.current_size -= 1

    def add_new(self):
        if self.current_size == 15:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь заполнена")

        for i in range(len(self.treeArray) - 1, 0, -1):
            if self.treeArray[i] == 0:
                self.treeArray[i] = self.ui.spinNew.value()
                self.current_size += 1
                self.fixUp(i)
                self.printArray()
                return

    def change_priority(self):
        if self.current_size == 0:
            QtWidgets.QMessageBox.about(self, "Ошибка!", "Очередь пуста")
            return

        for i in range(1, len(self.treeArray)):
            if self.treeArray[i] == self.ui.spinPrirFrom.value():
                self.treeArray[i] = self.ui.spinPrirTo.value()
                self.fixUp(i)
                self.fixDown(i)
                self.printArray()
                return

        QtWidgets.QMessageBox.about(self, "Ошибка!", "Невозможно изменить приоритет")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
