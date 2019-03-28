# 使用 Grid layout 网格 布局
from PySide2 import QtCore, QtWidgets, QtGui
class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.buttons = []

        self.strlist = ["Mon", "Tues", "Weds", "Thurs", "Fri", "Sat", "Sun"]

    #    self.btn1 = QtWidgets.QPushButton("Button1")
    #    self.buttons.append(self.btn1)

        for i in range(7):
            self.buttons.append(QtWidgets.QPushButton(self.strlist[i]))


        self.layout = QtWidgets.QGridLayout()

    #    self.layout.addWidget(self.buttons[0],0,0)
        self.layout.addWidget(self.buttons[0], 0, 0)             # 组件后面的参数，a, b, c, d
        self.layout.addWidget(self.buttons[1], 1, 0)             # 当只有 2个参数时，代表在几行几列
        self.layout.addWidget(self.buttons[2], 1, 1)
        self.layout.addWidget(self.buttons[3], 2, 2, 2, 4)       # 当有4个参数时。 a,b代表起始坐标。 c,d代表终止坐标。
        self.layout.addWidget(self.buttons[4], 3, 1, 3, 3)       #  就会变成 从a,b 坐标，到 c,d坐标的 合并结果。
        self.layout.addWidget(self.buttons[5], 4, 0, 4, 2)
        self.layout.addWidget(self.buttons[6], 5, 0, 5, 1)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    app.exec_()



