# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from components.LineEditDropSingleUrl import LineEditDropSingleUrl

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 332)
        Dialog.setAcceptDrops(False)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 541, 242))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)

        self.inputRemovePath = LineEditDropSingleUrl(self.verticalLayoutWidget)
        self.inputRemovePath.setObjectName(u"inputRemovePath")
        self.inputRemovePath.setDragEnabled(False)

        self.verticalLayout.addWidget(self.inputRemovePath)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.inputCaptionPath = LineEditDropSingleUrl(self.verticalLayoutWidget)
        self.inputCaptionPath.setObjectName(u"inputCaptionPath")

        self.verticalLayout.addWidget(self.inputCaptionPath)

        self.checkDeep = QCheckBox(self.verticalLayoutWidget)
        self.checkDeep.setObjectName(u"checkDeep")

        self.verticalLayout.addWidget(self.checkDeep)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.inputBackupExt = QLineEdit(self.verticalLayoutWidget)
        self.inputBackupExt.setObjectName(u"inputBackupExt")
        self.inputBackupExt.setAcceptDrops(False)

        self.verticalLayout.addWidget(self.inputBackupExt)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.btnStart = QPushButton(Dialog)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setGeometry(QRect(360, 261, 201, 51))
        self.btnStart.setMinimumSize(QSize(0, 50))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u524a\u9664\u30bf\u30b0\u3092\u8a18\u8ff0\u3057\u305f\u30d5\u30a1\u30a4\u30eb\u306e\u30d1\u30b9", None))
        self.inputRemovePath.setText("")
        self.inputRemovePath.setPlaceholderText(QCoreApplication.translate("Dialog", u"c:\u00a5remove_tag.txt", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u30ad\u30e3\u30d7\u30b7\u30e7\u30f3\u30d5\u30a1\u30a4\u30eb\u304c\u3042\u308b\u30d5\u30a9\u30eb\u30c0", None))
        self.inputCaptionPath.setPlaceholderText(QCoreApplication.translate("Dialog", u"c:\u00a5lora\u00a5train\u00a5", None))
        self.checkDeep.setText(QCoreApplication.translate("Dialog", u"\u4e0b\u5c64\u30d5\u30a9\u30eb\u30c0\u3082\u51e6\u7406\u3059\u308b", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u30d5\u30a1\u30a4\u30eb\u306e\u62e1\u5f35\u5b50", None))
        self.inputBackupExt.setText(QCoreApplication.translate("Dialog", u"bak", None))
        self.inputBackupExt.setPlaceholderText(QCoreApplication.translate("Dialog", u"c:\u00a5lora\u00a5train\u00a5", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u203b\u7a7a\u6b04\u306e\u6642\u306f\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u3092\u4f5c\u6210\u3057\u307e\u305b\u3093\u3002", None))
        self.btnStart.setText(QCoreApplication.translate("Dialog", u"\u5909\u63db\u958b\u59cb", None))
    # retranslateUi

