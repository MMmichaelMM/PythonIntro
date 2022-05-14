# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slider.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 338)
        self.verticalSlider1 = QtWidgets.QSlider(Form)
        self.verticalSlider1.setGeometry(QtCore.QRect(50, 90, 22, 160))
        self.verticalSlider1.setMaximum(5)
        self.verticalSlider1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider1.setObjectName("verticalSlider1")
        self.horizontalSlider1 = QtWidgets.QSlider(Form)
        self.horizontalSlider1.setGeometry(QtCore.QRect(150, 240, 160, 22))
        self.horizontalSlider1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider1.setObjectName("horizontalSlider1")
        self.labelForVerticalSlider = QtWidgets.QLabel(Form)
        self.labelForVerticalSlider.setGeometry(QtCore.QRect(40, 30, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelForVerticalSlider.setFont(font)
        self.labelForVerticalSlider.setObjectName("labelForVerticalSlider")
        self.labelForHorizontalSlider = QtWidgets.QLabel(Form)
        self.labelForHorizontalSlider.setGeometry(QtCore.QRect(350, 240, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelForHorizontalSlider.setFont(font)
        self.labelForHorizontalSlider.setObjectName("labelForHorizontalSlider")

        self.retranslateUi(Form)
        self.horizontalSlider1.valueChanged['int'].connect(self.labelForHorizontalSlider.setNum)
        self.verticalSlider1.valueChanged['int'].connect(self.labelForVerticalSlider.setNum)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelForVerticalSlider.setText(_translate("Form", "TextLabel"))
        self.labelForHorizontalSlider.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

