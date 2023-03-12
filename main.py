from Form import *
import sys

class Tree(QtWidgets.QMainWindow):
    queueCreated = False

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.quit.clicked.connect(self.quit)

    def quit(self):
        self.ui.quit.clicked.connect(QtWidgets.QApplication.instance().quit)
    
    def createArray(self):



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Tree()
    myapp.show()
    sys.exit(app.exec())
