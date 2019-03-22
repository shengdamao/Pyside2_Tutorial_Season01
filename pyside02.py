import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import *

@Slot()                                                         #这是添加槽函数的特殊语法，用在def 前
def say_hello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)
button = QPushButton("Click me")                                # 创建一个 Button 按钮， 按钮上显示字符串
button.clicked.connect(say_hello)                               #  链接 Button 的 （" clicked" ) 信号，
                                                                # 即 一按下按钮， 就会发出"clicked "信号，
                                                                # Clicked 信号 连接上了 （ say_hello) 函数
                                                                # 这是  Qt 最重要的 信号槽 机制， clicked 是信号，
                                                                # (say_hello )函数 是 槽函数。
                                                                # 连接他们的是这个connect 函数

# Show the button
button.show()
# Run the main Qt loop
app.exec_()