import sys
from PyQt5.QtWidgets import QMainWindow, QApplication 
from screens.posts import PostsWindow
from screens.index import IndexWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.posts = PostsWindow()
        self.index = IndexWindow()
        self.startPosts()

    def startIndex(self):
        self.index.setupUI(self)
        self.index.button.clicked.connect(self.startPosts)
        self.show()

    def startPosts(self):
        self.posts.setupUI(self)
        self.posts.button.clicked.connect(self.startIndex)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())