from PyQt5.QtWidgets import QWidget, QPushButton,QLineEdit, QLabel
from services.anogram import anogram

class IndexWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIWindow")
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.button = QPushButton('to other window', self.centralwidget)
        self.button.setGeometry(0, 50, 390, 30)


        self.input = QLineEdit(self.centralwidget)
        self.input.setGeometry(10, 120, 380, 20)
        self.input.textChanged.connect(self.input_text)

        self.label = QLabel(self.centralwidget)
        self.label.adjustSize()
        self.label.setGeometry(10, 10, 380, 40)
        self.label.setText("GUI application with PyQt5")
    
    def input_text(self, text):
        anogramed_text = anogram(text)
        self.label.setText(anogramed_text)
