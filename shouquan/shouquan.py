# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shouquan.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(335, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 5, 1, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 8, 1, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout.addWidget(self.checkBox_1, 1, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 4, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 35))
        self.textEdit.setMaximumSize(QtCore.QSize(16777205, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_send_sbar = QtWidgets.QScrollBar()
        self.textEdit_send_sbar.setStyleSheet("""
                                       QScrollBar:horizontal {
                                          border-height: 0px;
                                          border: none;
                                          background:rgba(64, 65, 79, 0);
                                          height:6px;
                                          margin: 0px 0px 0px 0px;
                                      }
                                      QScrollBar::handle:horizontal {
                                          background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                          stop: 0 #aaaaff, stop: 0.5 #aaaaff, stop:1 #aaaaff);
                                          min-width: 20px;
                                          max-width: 20px;
                                          margin: 0 0px 0 0px;
                                          border-radius: 3px;
                                      }
                                      QScrollBar::add-line:horizontal {
                                          background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                          stop: 0 rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                          width: 0px;
                                          border: none;
                                          subcontrol-position: right;
                                          subcontrol-origin: margin;
                                      }
                                      QScrollBar::sub-line:horizontal {
                                          background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                          stop: 0  rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                          width: 0 px;
                                          border: none;
                                          subcontrol-position: left;
                                          subcontrol-origin: margin;
                                      }
                                      QScrollBar::sub-page:horizontal {
                                      background: rgba(64, 65, 79, 0);
                                      }

                                      QScrollBar::add-page:horizontal {
                                      background: rgba(64, 65, 79, 0);
                                      }
                                      """)

        # self.textEdit.setVerticalScrollBar(self.textEdit_send_sbar)
        self.textEdit.setHorizontalScrollBar(self.textEdit_send_sbar)

        self.gridLayout.addWidget(self.textEdit, 11, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 12, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 6, 1, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 7, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setMinimumSize(QtCore.QSize(0, 200))
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 200))


        self.textEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_send_sbar_2 = QtWidgets.QScrollBar()

        # 2.给这个滚动条添加属性
        self.textEdit_send_sbar_2.setStyleSheet("""
                             QScrollBar:vertical {
                                  border-width: 0px;
                                  border: none;
                                  background:rgba(64, 65, 79, 0);
                                  width:6px;
                                  margin: 0px 0px 0px 0px;
                              }
                              QScrollBar::handle:vertical {
                                  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                  stop: 0 #aaaaff, stop: 0.5 #aaaaff, stop:1 #aaaaff);
                                  min-height: 20px;
                                  max-height: 20px;
                                  margin: 0 0px 0 0px;
                                  border-radius: 3px;
                              }
                              QScrollBar::add-line:vertical {
                                  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                  stop: 0 rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                  height: 0px;
                                  border: none;
                                  subcontrol-position: bottom;
                                  subcontrol-origin: margin;
                              }
                              QScrollBar::sub-line:vertical {
                                  background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                  stop: 0  rgba(64, 65, 79, 0), stop: 0.5 rgba(64, 65, 79, 0),  stop:1 rgba(64, 65, 79, 0));
                                  height: 0 px;
                                  border: none;
                                  subcontrol-position: top;
                                  subcontrol-origin: margin;
                              }
                              QScrollBar::sub-page:vertical {
                              background: rgba(64, 65, 79, 0);
                              }

                              QScrollBar::add-page:vertical {
                              background: rgba(64, 65, 79, 0);
                              }
                              """)

        # 3.把这个textEdit_send_sbar当作属性附加到textEdit控件上
        self.textEdit_2.setVerticalScrollBar(self.textEdit_send_sbar_2)


        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 14, 0, 1, 2)
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBox_10.setFont(font)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout.addWidget(self.checkBox_10, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 15, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "授权管理"))
        self.label.setText(_translate("MainWindow", "设备："))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.pushButton.setText(_translate("MainWindow", "授 权"))
        self.label_3.setText(_translate("MainWindow", "*多个IP用“;”隔开"))
        self.checkBox_6.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_9.setText(_translate("MainWindow", "CheckBox"))
        self.label_2.setText(_translate("MainWindow", "IP："))
        self.checkBox_10.setText(_translate("MainWindow", "CheckBox"))