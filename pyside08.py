
from PySide2 import   QtGui
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.model  = QStringListModel()

        txt = ['line1','line2']


        self.model.setStringList(txt)

        self.listview = QListView()
        self.listview.setModel(self.model)

        self.layout = QGridLayout()


        self.layout.addWidget(self.listview)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec_()


