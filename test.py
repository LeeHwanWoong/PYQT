import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        example = StartMenu(self)
        example.new_menu.clicked.connect(self.new_click)
        example.exit.clicked.connect(self.exit_click)
        self.central_widget.addWidget(example)

    def exit_click(self) :
        sys.exit(app.exec_())

    def new_click(self) :
        input_widget = Input(self)
        self.central_widget.addWidget(input_widget)
        self.central_widget.setCurrentWidget(input_widget)
        self.setGeometry(300, 300, 350, 300)

class Input(QWidget):
    def __init__(self,parent = None):
        super(Input,self).__init__(parent)

        grid = QGridLayout()
        self.dgrid = QGridLayout()
        box = QVBoxLayout()

        self.l_test1 = QLabel()
        self.l_test2 = QLabel()
        self.l_test3 = QLabel()
        self.l_test4 = QLabel()
        self.l_test5 = QLabel()
        self.text_box1 = QLineEdit()
        self.text_box2 = QLineEdit()
        self.text_box3 = QLineEdit()
        self.text_box4 = QLineEdit()
        self.text_box5 = QLineEdit()
        self.complete_button = QPushButton('complete')
        self.complete_button.clicked.connect(self.comp_click)
        # self.fare = QtGui.QProgressBar(self)

        self.l_test1.setText("No_aa")
        self.l_test2.setText("No_bb")
        self.l_test3.setText("Total")
        self.l_test4.setText("Value")
        self.l_test5.setText("Data")

        self.text_box1.setValidator(QIntValidator())
        self.text_box1.setMaxLength(4)
        self.text_box2.setValidator(QIntValidator())
        self.text_box2.setMaxLength(4)
        self.text_box3.setValidator(QIntValidator())
        self.text_box3.setMaxLength(4)
        self.text_box4.setValidator(QIntValidator())
        self.text_box4.setMaxLength(4)
        self.text_box5.setValidator(QIntValidator())
        self.text_box5.setMaxLength(4)

        grid.setSpacing(10)
        grid.addWidget(self.l_test1,1,0)
        grid.addWidget(self.l_test2,2,0)
        grid.addWidget(self.l_test3,3,0)
        grid.addWidget(self.l_test4,4,0)
        grid.addWidget(self.l_test5,5,0)
        grid.addWidget(self.text_box1,1,1,1,2)  #x,y,x_len,y_len
        grid.addWidget(self.text_box2,2,1,1,2)
        grid.addWidget(self.text_box3,3,1,1,2)
        grid.addWidget(self.text_box4,4,1,1,2)
        grid.addWidget(self.text_box5,5,1,1,2)
        grid.addWidget(self.complete_button,5,6)

        self.l_test6 = QLabel()
        self.l_test6.setText("Fare")

        self.dgrid.addWidget(self.l_test6,1,0)
        box.addLayout(grid)
        box.addLayout(self.dgrid)

        self.setLayout(box)
        self.setGeometry(300, 300, 350, 300)

    def comp_click(self):
        f = open("data.d",'w')
        test1 = "No_aa " + self.text_box1.text()+"\n"
        f.write(test1)
        test1 = "No_bb " + self.text_box2.text()+"\n"
        f.write(test1)
        test1 = "Total " + self.text_box3.text()+"\n"
        f.write(test1)
        test1 = "Value " + self.text_box4.text()+"\n"
        f.write(test1)
        test1 = "Data " + self.text_box5.text()+"\n"
        f.write(test1)
        f.close()

        self.temp_b = []
        mygroupbox = QGroupBox('ee')
        myform = QFormLayout()
        tgrid = []
        qgrid = []
        scroll = QScrollArea()
        for i in range(1,int(self.text_box2.text())+1):
            self.temp = QLabel()
            self.temp2 = QPushButton('change')
            self.temp_b.append(self.temp2)
            self.temp.setText(str(i))
            tgrid.append(self.temp)
            qgrid.append(self.temp_b[i-1])
            myform.addRow(tgrid[i-1],qgrid[i-1])
        mygroupbox.setLayout(myform)
        scroll.setWidget(mygroupbox)
        self.dgrid.addWidget(scroll,1,1,3,3)

class StartMenu(QWidget):
    def __init__(self,parent = None):
        super(StartMenu,self).__init__(parent)

        grid = QGridLayout()
        self.new_menu = QPushButton('New')
        self.exit = QPushButton('Exit')

        grid.setSpacing(10)    #interval between widget
        grid.addWidget(self.new_menu,1,0)
        grid.addWidget(self.exit,2,0)


        self.setLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

# from PyQt4 import QtCore, QtGui

# class MainWindow(QtGui.QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.central_widget = QtGui.QStackedWidget()
#         self.setCentralWidget(self.central_widget)
#         login_widget = LoginWidget(self)
#         login_widget.button.clicked.connect(self.login)
#         self.central_widget.addWidget(login_widget)
#     def login(self):
#         logged_in_widget = LoggedWidget(self)
#         self.central_widget.addWidget(logged_in_widget)
#         self.central_widget.setCurrentWidget(logged_in_widget)


# class LoginWidget(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(LoginWidget, self).__init__(parent)
#         layout = QtGui.QHBoxLayout()
#         self.button = QtGui.QPushButton('Login')
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#         # you might want to do self.button.click.connect(self.parent().login) here


# class LoggedWidget(QtGui.QWidget):
#     def __init__(self, parent=None):
#         super(LoggedWidget, self).__init__(parent)
#         layout = QtGui.QHBoxLayout()
#         self.label = QtGui.QLabel('logged in!')
#         layout.addWidget(self.label)
#         self.setLayout(layout)



# if __name__ == '__main__':
#     app = QtGui.QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()