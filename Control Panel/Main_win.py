# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1113, 741)
        self.widget = QtWidgets.QWidget(Main)
        self.widget.setGeometry(QtCore.QRect(10, 0, 1091, 731))
        self.widget.setStyleSheet("background-color:rgb(33, 33, 33)")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 20, 511, 701))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet("background-color:rgb(44, 44, 44);\n"
"border-radius:25px")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(80, -10, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 421, 601))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-image: url(:/System Status/system_status.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/System Status/system_status.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(550, 20, 511, 291))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widget_3.setFont(font)
        self.widget_3.setStyleSheet("background-color:rgb(44, 44, 44);\n"
"border-radius:25px")
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(140, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 451, 581))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 471, 241))
        font = QtGui.QFont()
        font.setPointSize(3)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-image: url(:/Weather Analysis/weather_image.jpg);")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/Weather Analysis/weather_image.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(560, 340, 511, 371))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widget_4.setFont(font)
        self.widget_4.setStyleSheet("background-color:rgb(44, 44, 44);\n"
"border-radius:25px")
        self.widget_4.setObjectName("widget_4")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setGeometry(QtCore.QRect(140, 10, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 451, 581))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 451, 91))
        self.label_9.setStyleSheet("background-image: url(:/newPrefix/energy_levels_2.jpg);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/Energy Levels/energy_levels_2.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget_4)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 451, 91))
        self.label_10.setStyleSheet("background-image: url(:/newPrefix/energy_levels_2.jpg);")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/Energy Levels/energy_levels_3.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget_4)
        self.label_11.setGeometry(QtCore.QRect(20, 260, 451, 101))
        self.label_11.setStyleSheet("background-image: url(:/newPrefix/energy_levels_1.jpg);")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/Energy Levels/energy_levels_1.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.widget_4)
        self.label_12.setGeometry(QtCore.QRect(10, 140, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        self.label_13.setGeometry(QtCore.QRect(10, 240, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_4)
        self.label_14.setGeometry(QtCore.QRect(20, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Hanuman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.label.setText(_translate("Main", "System Status"))
        self.label_4.setText(_translate("Main", "Weather Analysis"))
        self.label_5.setText(_translate("Main", "Hi"))
        self.label_6.setText(_translate("Main", "Energy Analysis"))
        self.label_7.setText(_translate("Main", "Hi"))
        self.label_12.setText(_translate("Main", "Solar Energy"))
        self.label_13.setText(_translate("Main", "Wind Energy"))
        self.label_14.setText(_translate("Main", "Hydro Energy"))
import weather_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
