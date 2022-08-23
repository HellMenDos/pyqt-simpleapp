from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QListWidget
from services.post import get_posts, get_posts_by_title

class PostsWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        MainWindow.setWindowTitle("UIToolTab")

        self.centralwidget = QWidget(MainWindow)

        self.listWidget = QListWidget(self.centralwidget)
        for item in get_posts():
            self.listWidget.addItem(item)
        self.listWidget.move(10, 10)
        self.listWidget.setGeometry(10, 10, 380, 200)
        
        self.input = QLineEdit(self.centralwidget)
        self.input.setGeometry(10, 220, 380, 20)
        self.input.textChanged.connect(self.input_text)

        self.button = QPushButton("back", self.centralwidget)
        self.button.setGeometry(10, 250, 380, 30)
        MainWindow.setCentralWidget(self.centralwidget)

    def input_text(self, text):
        posts = get_posts_by_title(text)
        self.listWidget.clear()

        for post in posts:
            self.listWidget.addItem(post)
