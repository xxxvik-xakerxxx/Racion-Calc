#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QLabel, QLineEdit, QRadioButton, QPushButton, QMainWindow, QApplication, QWidget, qApp
from PyQt5 import QtCore
from res.ui import Ui_Dialog
import sqlite3


class MyApp(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calc)
        self.ui.pushButton_4.clicked.connect(qApp.quit)

    def calc(self):
        _translate = QtCore.QCoreApplication.translate
        if self.ui.radioButton.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1173"))
            self.ui.label_27.setText(_translate("Dialog", "17.1"))
            self.ui.label_28.setText(_translate("Dialog", "5.5"))
            self.ui.label_29.setText(_translate("Dialog", "2.5"))
            self.ui.label_30.setText(_translate("Dialog", "0.84"))
            self.ui.label_31.setText(_translate("Dialog", "0.45"))
            self.ui.label_49.setText(_translate("Dialog", "0.74"))
            self.ui.label_50.setText(_translate("Dialog", "0.34"))

        if self.ui.radioButton_2.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1130"))
            self.ui.label_27.setText(_translate("Dialog", "17"))
            self.ui.label_28.setText(_translate("Dialog", "5.5"))
            self.ui.label_29.setText(_translate("Dialog", "3.1"))
            self.ui.label_30.setText(_translate("Dialog", "0.7"))
            self.ui.label_31.setText(_translate("Dialog", "0.3"))
            self.ui.label_49.setText(_translate("Dialog", "0.75"))
            self.ui.label_50.setText(_translate("Dialog", "0.32"))

        if self.ui.radioButton_3.isChecked():
            self.ui.label_26.setText(_translate("Dialog", "1290"))
            self.ui.label_27.setText(_translate("Dialog", "20.5"))
            self.ui.label_28.setText(_translate("Dialog", "5"))
            self.ui.label_29.setText(_translate("Dialog", "1"))
            self.ui.label_30.setText(_translate("Dialog", "0.8"))
            self.ui.label_31.setText(_translate("Dialog", "0.3"))
            self.ui.label_49.setText(_translate("Dialog", "1"))
            self.ui.label_50.setText(_translate("Dialog", "0.43"))
        self.sum_components()

    def sum_components(self):
        _translate = QtCore.QCoreApplication.translate
        phen = float(self.ui.lineEdit.text())
        yach = float(self.ui.lineEdit_2.text())
        kuk = float(self.ui.lineEdit_3.text())
        m_k = float(self.ui.lineEdit_4.text())
        fish = float(self.ui.lineEdit_5.text())
        prem_8184 = float(self.ui.lineEdit_6.text())
        gmih = float(self.ui.lineEdit_7.text())
        shr = float(self.ui.lineEdit_8.text())
        mk2 = float(self.ui.lineEdit_9.text())
        yam = float(self.ui.lineEdit_10.text())
        trm = float(self.ui.lineEdit_11.text())
        msrs = float(self.ui.lineEdit_12.text())
        r_k = float(self.ui.lineEdit_13.text())
        prem_8203 = float(self.ui.lineEdit_14.text())
        end = (phen + yach + kuk + m_k + fish + prem_8184 + gmih +
               shr + mk2 + yam + trm + msrs + r_k + prem_8203)

        if end == 100:
            self.ui.label_12.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        else:
            self.ui.label_12.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_12.setText(_translate("Dialog", str(end)))
        self.open_bd(phen, yach, kuk, m_k, fish, prem_8184,
                     gmih, shr, mk2, yam, trm, msrs, r_k, prem_8203)

    def calculate_equation(self, row, defaults):
        val_phen = row[0][0]
        val_yach = row[1][0]
        val_kuk = row[2][0]
        val_fish = row[3][0]
        val_mk2 = row[4][0]
        val_m_k = row[5][0]
        val_yam = row[6][0]
        val_gmih = row[7][0]
        val_shr = row[8][0]
        val_msrs = row[9][0]
        val_trm = row[10][0]
        val_r_k = row[11][0]
        val_prem_8203 = row[12][0]
        val_prem_8184 = row[13][0]

        (phen,
         yach,
         kuk,
         fish,
         mk2,
         m_k,
         yam,
         gmih,
         shr,
         msrs,
         trm,
         r_k,
         prem_8203,
         prem_8184) = defaults

        return ((val_phen * phen) +
                (val_yach * yach) +
                (val_kuk * kuk) +
                (val_m_k * m_k) +
                (val_fish * fish) +
                (val_prem_8184 * prem_8184) +
                (val_prem_8203 * prem_8203) +
                (val_gmih * gmih) +
                (val_shr * shr) +
                (val_mk2 * mk2) +
                (val_yam * yam) +
                (val_trm * trm) +
                (val_msrs * msrs) +
                (val_r_k * r_k)) / 100

    def open_bd(self, phen, yach, kuk, m_k, fish, prem_8184,
                gmih, shr, mk2, yam, trm, msrs, r_k, prem_8203):

        defaults = (
            phen,
            yach,
            kuk,
            fish,
            mk2,
            m_k,
            yam,
            gmih,
            shr,
            msrs,
            trm,
            r_k,
            prem_8203,
            prem_8184
        )

        conn = sqlite3.connect('./data/data.db')
        c = conn.cursor()
        c.execute("SELECT  COUNT(post_id) FROM komponents")
        st_col = c.fetchone()
        c.execute("SELECT  kdg FROM komponents")
        row_kdg = c.fetchmany(st_col[0])

        c.execute("SELECT  sp FROM komponents")
        row_sp = c.fetchmany(st_col[0])

        c.execute("SELECT  sk FROM komponents")
        row_sk = c.fetchmany(st_col[0])

        c.execute("SELECT  cal FROM komponents")
        row_cal = c.fetchmany(st_col[0])

        c.execute("SELECT  fos FROM komponents")
        row_fos = c.fetchmany(st_col[0])

        c.execute("SELECT  na FROM komponents")
        row_na = c.fetchmany(st_col[0])

        c.execute("SELECT liz FROM komponents")
        row_liz = c.fetchmany(st_col[0])

        c.execute("SELECT met FROM komponents")
        row_met = c.fetchmany(st_col[0])

        c.close()
        conn.close()

        kdg = self.calculate_equation(row_kdg, defaults)
        sp = self.calculate_equation(row_sp, defaults)
        sk = self.calculate_equation(row_sk, defaults)
        cal = self.calculate_equation(row_cal, defaults)
        fos = self.calculate_equation(row_fos, defaults)
        na = self.calculate_equation(row_na, defaults)
        liz = self.calculate_equation(row_liz, defaults)
        met = self.calculate_equation(row_met, defaults)

        self.calc_end(kdg, sp, sk, cal, fos, na, liz, met)

    def calc_end(self, kdg, sp, sk, cal, fos, na, liz, met):
        _translate = QtCore.QCoreApplication.translate

        self.ui.label_20.setText(_translate("Dialog", str(kdg)))
        self.ui.label_21.setText(_translate("Dialog", str(sp)))
        self.ui.label_22.setText(_translate("Dialog", str(sk)))
        self.ui.label_23.setText(_translate("Dialog", str(cal)))
        self.ui.label_24.setText(_translate("Dialog", str(fos)))
        self.ui.label_25.setText(_translate("Dialog", str(na)))
        self.ui.label_47.setText(_translate("Dialog", str(liz)))
        self.ui.label_48.setText(_translate("Dialog", str(met)))

        norm_kdg = float(self.ui.label_26.text())
        norm_sp = float(self.ui.label_27.text())
        norm_sk = float(self.ui.label_28.text())
        norm_cal = float(self.ui.label_29.text())
        norm_fos = float(self.ui.label_30.text())
        norm_na = float(self.ui.label_31.text())
        norm_liz = float(self.ui.label_49.text())
        norm_met = float(self.ui.label_50.text())

        otl_kdg = norm_kdg - kdg
        if kdg == norm_kdg:
            self.ui.label_32.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_32.setText(_translate("Dialog", str(otl_kdg)))
        else:
            self.ui.label_32.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_32.setText(_translate("Dialog", str(otl_kdg)))

        otl_sp = norm_sp - sp
        if sp == norm_sp:
            self.ui.label_33.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_33.setText(_translate("Dialog", str(otl_sp)))
        else:
            self.ui.label_33.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_33.setText(_translate("Dialog", str(otl_sp)))

        otl_sk = norm_sk - sk
        if sk == norm_sk:
            self.ui.label_34.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_34.setText(_translate("Dialog", str(otl_sk)))
        else:
            self.ui.label_34.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_34.setText(_translate("Dialog", str(otl_sk)))

        otl_cal = norm_cal - cal
        if cal == norm_cal:
            self.ui.label_35.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_35.setText(_translate("Dialog", str(otl_cal)))
        else:
            self.ui.label_35.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_35.setText(_translate("Dialog", str(otl_cal)))

        otl_fos = norm_fos - fos
        if fos == norm_fos:
            self.ui.label_36.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_36.setText(_translate("Dialog", str(otl_fos)))
        else:
            self.ui.label_36.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_36.setText(_translate("Dialog", str(otl_fos)))

        otl_na = norm_na - na
        if na == norm_na:
            self.ui.label_37.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_37.setText(_translate("Dialog", str(otl_na)))
        else:
            self.ui.label_37.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_37.setText(_translate("Dialog", str(otl_na)))

        otl_liz = norm_liz - liz
        if liz == norm_liz:
            self.ui.label_51.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_51.setText(_translate("Dialog", str(otl_liz)))
        else:
            self.ui.label_51.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_51.setText(_translate("Dialog", str(otl_liz)))

        otl_met = norm_met - met
        if met == norm_met:
            self.ui.label_52.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_52.setText(_translate("Dialog", str(otl_met)))
        else:
            self.ui.label_52.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_52.setText(_translate("Dialog", str(otl_met)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
