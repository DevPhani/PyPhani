from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
import sys
from calculatorGUI import *

class DevPhani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pclear.clicked.connect(self.clear)
        self.ui.pdelete.clicked.connect(self.delete)

        self.ui.p1.clicked.connect(self.one)
        self.ui.p2.clicked.connect(self.two)
        self.ui.p3.clicked.connect(self.three)

        self.ui.p4.clicked.connect(self.four)
        self.ui.p5.clicked.connect(self.five)
        self.ui.p6.clicked.connect(self.six)

        self.ui.p7.clicked.connect(self.seven)
        self.ui.p8.clicked.connect(self.eight)
        self.ui.p9.clicked.connect(self.nine)

        self.ui.pp.clicked.connect(self.dot)
        self.ui.p0.clicked.connect(self.zero)
        self.ui.psq.clicked.connect(self.sqrt)

        self.ui.pplus.clicked.connect(self.plus)
        self.ui.pminus.clicked.connect(self.minus)
        self.ui.pmul.clicked.connect(self.mul)
        self.ui.pdiv.clicked.connect(self.div)
        self.ui.eqal.clicked.connect(self.equals)

    def one(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"1")
    def two(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"2")
    def three(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"3")
    def four(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"4")
    def five(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"5")
    def six(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"6")
    def seven(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"7")
    def eight(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"8")
    def nine(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"9")
    def zero(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"0")
    def dot(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+".")
    def sqrt(self):
        data = float(self.ui.label_5.text())
        self.ui.label_5.setText("{:.2f}".format(data**0.5))
    def plus(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"+")
    def minus(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"-")
    def mul(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"*")
    def div(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText(data+"/")
    def clear(self):
        self.ui.label_5.setText("0")
    def delete(self):
        data = self.ui.label_5.text()
        self.ui.label_5.setText("{}".format(data[:len(data)-1]))
    def equals(self):
        data = self.ui.label_5.text()
        try:
            ans = eval(data)
            self.ui.label_5.setText("{:.4f}".format(ans))
        except:
            self.ui.label_5.setText("Invalid Input")
        
                


if __name__=="__main__":
    app = QApplication(sys.argv)
    w = DevPhani()
    w.show()
    sys.exit(app.exec_())
