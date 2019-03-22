# Layout 的 进阶使用
# 同时用到了 垂直布局(VBOXlayout)和水平布局(HBOXlayout， 并且完成了简单的嵌套。（大的水平布局装了2个小的垂直）

from PySide2 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.buttonA1 = QtWidgets.QPushButton("A1")
        self.buttonA2 = QtWidgets.QPushButton("A2")
        self.buttonA3 = QtWidgets.QPushButton("A3")
        self.buttonB1 = QtWidgets.QPushButton("B1")
        self.buttonB2 = QtWidgets.QPushButton("B2")
        self.buttonB3 = QtWidgets.QPushButton("B3")


        self.collunm1 = QtWidgets.QVBoxLayout()            # 建立一个VBOXLAYOUT 的一列    （垂直布局）
        self.collunm2 = QtWidgets.QVBoxLayout()            # 建立一个VBOXLAYOUT 的一列    （垂直布局）

        self.collunm1.addWidget(self.buttonA1)              # 在 collumn 1 中添加 A1,A2 按钮
        self.collunm1.addWidget(self.buttonA2)
        self.collunm1.addWidget(self.buttonA3)
        self.collunm2.addWidget(self.buttonB1)              # 在 collumn 2 中添加 B1, B2 按钮
        self.collunm2.addWidget(self.buttonB2)
        self.collunm2.addWidget(self.buttonB3)

        self.layout = QtWidgets.QHBoxLayout()               # 添加一个总的 水平布局，将之前的2个 垂直布局添加进去。

        self.layout.addLayout( self.collunm1)
        self.layout.addLayout(self.collunm2)
        self.setLayout(self.layout)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec_()



