import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton
from PySide2.QtWidgets import QVBoxLayout

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()                                        # 初始化 layout
        layout.addWidget(self.edit)                                   # 添加 edit, button
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)                                        # 将设置好得layout 赋值
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)                   # button 和 greetings 的信号槽

    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())