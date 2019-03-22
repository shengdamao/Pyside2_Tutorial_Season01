import sys
from PySide2.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)                  # 调用 sys库的目的 是给Qapplication 参数
                                              # QApplication 是类的构造函数，
                                            # 有了这个类对象，相当于有了窗口，才能将QT 专属的东西添加上去。



label = QLabel("Hello World!")               #这里 创建一个 Label 标签，用来显示文本的组件， QLabel (stirng)
label.show()                                  # Label对象的方法函数，关于遇到其他对象，可查文档得知有哪些通用的方法
app.exec_()                                  # 这是 Qt 特有的函数， 是 让窗口 “执行”execute,
                                            # 会让它“一直”显示APP 窗口，而不是一闪而过，有点像死循环