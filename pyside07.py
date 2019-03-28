# QFileSystemModel 的例子

from PySide2 import   QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.model  = QFileSystemModel()
        self.model.setRootPath(QDir.currentPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
    #   self.tree.setRootIndex(self.model.index(QDir.currentPath()))            把当前目录设为 首页

        self.list = QListView()
        self.list.setModel(self.model)

        self.layout = QGridLayout()

        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.list)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec_()





