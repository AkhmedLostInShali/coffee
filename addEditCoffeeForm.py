# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 315)
        self.lineEdit_specie = QtWidgets.QLineEdit(Form)
        self.lineEdit_specie.setGeometry(QtCore.QRect(130, 20, 261, 31))
        self.lineEdit_specie.setObjectName("lineEdit_specie")
        self.lineEdit_grade = QtWidgets.QLineEdit(Form)
        self.lineEdit_grade.setGeometry(QtCore.QRect(130, 60, 261, 31))
        self.lineEdit_grade.setObjectName("lineEdit_grade")
        self.lineEdit_taste = QtWidgets.QLineEdit(Form)
        self.lineEdit_taste.setGeometry(QtCore.QRect(130, 140, 261, 31))
        self.lineEdit_taste.setObjectName("lineEdit_taste")
        self.label_specie = QtWidgets.QLabel(Form)
        self.label_specie.setGeometry(QtCore.QRect(40, 20, 101, 31))
        self.label_specie.setObjectName("label_specie")
        self.label_grade = QtWidgets.QLabel(Form)
        self.label_grade.setGeometry(QtCore.QRect(40, 60, 101, 31))
        self.label_grade.setObjectName("label_grade")
        self.label_grind = QtWidgets.QLabel(Form)
        self.label_grind.setGeometry(QtCore.QRect(40, 100, 101, 31))
        self.label_grind.setObjectName("label_grind")
        self.label_taste = QtWidgets.QLabel(Form)
        self.label_taste.setGeometry(QtCore.QRect(40, 140, 101, 31))
        self.label_taste.setObjectName("label_taste")
        self.pushBtn = QtWidgets.QPushButton(Form)
        self.pushBtn.setGeometry(QtCore.QRect(240, 270, 151, 41))
        self.pushBtn.setObjectName("pushBtn")
        self.label_error = QtWidgets.QLabel(Form)
        self.label_error.setGeometry(QtCore.QRect(20, 280, 201, 21))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        self.lineEdit_volume = QtWidgets.QLineEdit(Form)
        self.lineEdit_volume.setGeometry(QtCore.QRect(130, 220, 261, 31))
        self.lineEdit_volume.setObjectName("lineEdit_volume")
        self.lineEdit_price = QtWidgets.QLineEdit(Form)
        self.lineEdit_price.setGeometry(QtCore.QRect(130, 180, 261, 31))
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.label_price = QtWidgets.QLabel(Form)
        self.label_price.setGeometry(QtCore.QRect(40, 180, 101, 31))
        self.label_price.setObjectName("label_price")
        self.label_volume = QtWidgets.QLabel(Form)
        self.label_volume.setGeometry(QtCore.QRect(40, 220, 101, 31))
        self.label_volume.setObjectName("label_volume")
        self.comboBox_grind = QtWidgets.QComboBox(Form)
        self.comboBox_grind.setGeometry(QtCore.QRect(130, 100, 261, 31))
        self.comboBox_grind.setObjectName("comboBox_grind")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_specie.setText(_translate("Form", "Сорт"))
        self.label_grade.setText(_translate("Form", "Обжарка"))
        self.label_grind.setText(_translate("Form", "Форма выпуска"))
        self.label_taste.setText(_translate("Form", "Вкус"))
        self.pushBtn.setText(_translate("Form", "Добавить"))
        self.label_price.setText(_translate("Form", "Цена"))
        self.label_volume.setText(_translate("Form", "Объём"))
