
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from pyqtgraph import PlotWidget
import pyqtgraph as pg

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(793, 326)
        self.horizontalSlider1 = QtWidgets.QSlider(Form)
        self.horizontalSlider1.setGeometry(QtCore.QRect(150, 240, 561, 22))
        self.horizontalSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider1.setObjectName("horizontalSlider1")
        self.labelForHorizontalSlider = QtWidgets.QLabel(Form)
        self.labelForHorizontalSlider.setGeometry(QtCore.QRect(400, 270, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelForHorizontalSlider.setFont(font)
        self.labelForHorizontalSlider.setObjectName("labelForHorizontalSlider")

        self.setGraphicsView()

        self.retranslateUi(Form)
        self.horizontalSlider1.valueChanged['int'].connect(self.labelForHorizontalSlider.setNum)
        self.horizontalSlider1.valueChanged['int'].connect(lambda: self.build_graph())

        QtCore.QMetaObject.connectSlotsByName(Form)

    def build_graph(self):
        self.graphicsView.clear()
        self.t = self.horizontalSlider1.value()

        x = np.linspace(0, 2 * np.pi, 100) - float(self.t)
        y = 2 * np.cos(x)
        pen = pg.mkPen(color=(0, 0, 255))
        self.graphicsView.plot(x, y, pen=pen)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelForHorizontalSlider.setText(_translate("Form", "TextLabel"))

    def setGraphicsView(self):
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget) #Add a new set of data to an existing plot widget
        self.graphicsView.setBackground('w')
        self.graphicsView.setGeometry(QtCore.QRect(150, 30, 571, 192))
        self.graphicsView.setObjectName("graphicsView")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
