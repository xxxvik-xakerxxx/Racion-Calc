#!/usr/bin/python3
# -*- coding: utf-8 -*-
# TODO: Хоть и говнокод но работает, пока работает)
# TODO: перевести его в WEB стезю. Отказатся от django перейти на Flask
# (да я мазахист)
import sys
from PyQt5.QtWidgets import QComboBox, QLineEdit, QApplication, QWidget, QMainWindow, QFormLayout
from PyQt5 import QtCore
from res.ui2t import Ui_MainWindow
from res.base import Ui_Dialog2
import sqlite3



class BaseWind(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui2 = Ui_Dialog2()
        self.ui2.setupUi(self)


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calc)
        self.ui.pushButton_3.clicked.connect(self.show_basewind)
        self.ui.pushButton_4.clicked.connect(app.quit)
        self.ui.pushButton_5.clicked.connect(self.add_pol)

    def show_basewind(self):
        self.dialog1 = BaseWind()
        self.dialog1.show()

    def add_pol(self):
        self.komp_item = int(self.ui.lineEdit.text())
        v_pos = 40
        namber_com = 2
        component_list = [
            "None",
            "Пшеница",
            "Ячмень",
            "Кукуруза",
            "Рыбная",
            "Мясо/кос^",
            "Мясо/кос",
            "Яичная мука",
            "Жмых п-сол.",
            "Шрот соевый",
            "Масло раст.",
            "Мука трав.",
            "Ракушка",
            "Премикс8203",
            "Премикс8184",
            "Премикс8201"
        ]
        self.all_combox = []
        self.all_lineEd = []
        i = self.komp_item
        while (i > 0):

            """Создание combo_Box по количеству указанному в lineEdit"""

            combo_Box1 = 'comboBox_' + str(namber_com)
            line_Edit1 = 'LineEdit_' + str(namber_com)


            component_tab_FormLayout = i + 1 #нужен для сдвига компонентов на макете

            self.combo_Box = QComboBox(self.ui.verticalFrame_3)
            self.combo_Box.setObjectName('comboBox_'+str(namber_com))

            self.combo_Box.addItems(component_list)
            self.ui.formLayout.setWidget(component_tab_FormLayout, QFormLayout.LabelRole, self.combo_Box)
            self.combo_Box.show()
            self.line_Edit = QLineEdit(self.ui.verticalFrame_3)
            self.ui.formLayout.setWidget(component_tab_FormLayout, QFormLayout.FieldRole, self.line_Edit)
            self.line_Edit.show()
            self.all_combox.append(self.combo_Box)
            self.all_lineEd.append(self.line_Edit)


            v_pos += 30
            namber_com += 1
            i -= 1


    #def test(self):
    #    print(self.all_lineEd)
    #    print(self.all_combox)
    #    namber = int(self.ui.lineEdit.text()) - 1
    #    while namber >= 0:
    #        print("След цикл")
    #        combox = self.all_combox[namber]
    #        lineEd = self.all_lineEd[namber]
    #        namber -= 1
    #        index = combox.currentText()
    #        nam = lineEd.text()
    #        print(index, nam)

    def calc(self):

        tip_ptic = str(self.ui.comboBox.currentText())

        if tip_ptic == "X11 крос":
            ptic = "dackX11"
            self.normi(ptic)

        if tip_ptic == "22-47н.":
            ptic = "chikenb24"
            self.normi(ptic)

        if tip_ptic == "Перепела":
            ptic = "perep"
            self.normi(ptic)

        if tip_ptic == "1-7д.":
            ptic = "dack1-7d"
            self.normi(ptic)

    def sum_components(self):
        _translate = QtCore.QCoreApplication.translate

        self.komponents = [   ["None", 0],
            ["Пшеница", 0],
            ["Ячмень", 0],
            ["Кукуруза", 0],
            ["Рыбная", 0],
            ["Мясо/кос^", 0],
            ["Мясо/кос", 0],
            ["Яичная мука", 0],
            ["Жмых п-сол.", 0],
            ["Шрот соевый", 0],
            ["Масло раст.", 0],
            ["Мука трав.", 0],
            ["Ракушка", 0],
            ["Премикс8203", 0],
            ["Премикс8184", 0],
            ["Премикс8201", 0]]

        namber = int(self.komp_item) - 1
        #TODO: колхоз надо бы переделать
        while namber >= 0:
            combox = self.all_combox[namber]
            lineEd = self.all_lineEd[namber]
            index = combox.currentText()
            nam = float(lineEd.text())
            i = (len(self.komponents)) - 1

            while i >= 0:
                if index == self.komponents[i][0]:
                    self.komponents[i][1] = nam
                i -= 1
            namber -= 1

        end = 0
        komponent_buf = []
        i = (len(self.komponents)) - 1
        while i >= 0:
            if self.komponents[i][1] > 0:
                end = end + self.komponents[i][1]
                komponent_buf.append(self.komponents[i])
            i -= 1

        if end == 100:
            self.ui.label_12.setStyleSheet("color: rgb(0, 255, 60);")

            self.ui.label_12.setText(_translate("Dialog", str(end)))
        else:
            self.ui.label_12.setStyleSheet("color: rgb(255, 0, 0);")

            self.ui.label_12.setText(_translate("Dialog", str(end)))
        self.open_bd(komponent_buf)

    def calculate_equation(self, row, komponent_buf):

        row_buf = [
            ["Пшеница", 0],
            ["Ячмень",  1],
            ["Кукуруза", 2],
            ["Рыбная", 3],
            ["Мясо/кос^", 4],
            ["Мясо/кос",  5],
            ["Яичная мука", 6],
            ["Жмых п-сол.", 7],
            ["Шрот соевый", 8],
            ["Масло раст.", 9],
            ["Мука трав.", 10],
            ["Ракушка", 11],
            ["Премикс8203", 12],
            ["Премикс8184", 14],
            ["Премикс8201", 15]
        ]

        x =  (len(row_buf)) - 1
        pitat_wesch = 0
        while x >= 0:
            j =  (len(komponent_buf)) - 1
            while j >= 0:
                if row_buf[x][0] == komponent_buf[j][0]:
                    pitat_wesch += (float(row[int(row_buf[x][1])][0]) * float(komponent_buf[j][1]) )
                j -= 1
            x -= 1

        return (pitat_wesch) / 100

    def open_bd(self, komponent_buf):

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

        kdg = self.calculate_equation(row_kdg, komponent_buf)
        sp = self.calculate_equation(row_sp, komponent_buf)
        sk = self.calculate_equation(row_sk, komponent_buf)
        cal = self.calculate_equation(row_cal, komponent_buf)
        fos = self.calculate_equation(row_fos, komponent_buf)
        na = self.calculate_equation(row_na, komponent_buf)
        liz = self.calculate_equation(row_liz, komponent_buf)
        met = self.calculate_equation(row_met, komponent_buf)

        self.calc_end(kdg, sp, sk, cal, fos, na, liz, met)

    def normi(self, ptic):

        conn = sqlite3.connect('./data/data.db')
        c = conn.cursor()
        c.execute("SELECT  COUNT(Gv) FROM normy")
        st_col = c.fetchone()
        c.execute("SELECT  kdg FROM normy")
        row_kdg = c.fetchmany(st_col[0])

        c.execute("SELECT  sp FROM normy")
        row_sp = c.fetchmany(st_col[0])

        c.execute("SELECT  sk FROM normy")
        row_sk = c.fetchmany(st_col[0])

        c.execute("SELECT  cal FROM normy")
        row_cal = c.fetchmany(st_col[0])

        c.execute("SELECT  fos FROM normy")
        row_fos = c.fetchmany(st_col[0])

        c.execute("SELECT  na FROM normy")
        row_na = c.fetchmany(st_col[0])

        c.execute("SELECT liz FROM normy")
        row_liz = c.fetchmany(st_col[0])

        c.execute("SELECT met FROM normy")
        row_met = c.fetchmany(st_col[0])

        c.close()
        conn.close()

        if ('dackX11' in ptic):

            n = 1
            self.normi_viv(n, row_kdg, row_sp, row_sk, row_cal, row_fos,
                           row_na, row_liz, row_met)

        if ('perep' in ptic):
            n = 2
            self.normi_viv(n, row_kdg, row_sp, row_sk, row_cal, row_fos,
                           row_na, row_liz, row_met)

        if ('dack1-7d' in ptic):
            n = 3
            self.normi_viv(n, row_kdg, row_sp, row_sk, row_cal, row_fos,
                           row_na, row_liz, row_met)

    def normi_viv(self, n, row_kdg, row_sp, row_sk, row_cal, row_fos,
                  row_na, row_liz, row_met):
        _translate = QtCore.QCoreApplication.translate

        ptic_kdg = row_kdg[n][0]
        ptic_sp = row_sp[n][0]
        ptic_sk = row_sk[n][0]
        ptic_cal = row_cal[n][0]
        ptic_fos = row_fos[n][0]
        ptic_na = row_na[n][0]
        ptic_liz = row_liz[n][0]
        ptic_met = row_met[n][0]

        self.ui.label_26.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_kdg)))))
        self.ui.label_27.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_sp)))))
        self.ui.label_28.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_sk)))))
        self.ui.label_29.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_cal)))))
        self.ui.label_30.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_fos)))))
        self.ui.label_31.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_na)))))
        self.ui.label_49.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_liz)))))
        self.ui.label_50.setText(_translate("Dialog", str(float("{0:.3f}".format(ptic_met)))))

        self.sum_components()

    def calc_end(self, kdg, sp, sk, cal, fos, na, liz, met):
        _translate = QtCore.QCoreApplication.translate

        self.ui.label_20.setText(_translate("Dialog", str(float("{0:.3f}".format(kdg)))))
        self.ui.label_21.setText(_translate("Dialog", str(float("{0:.3f}".format(sp)))))
        self.ui.label_22.setText(_translate("Dialog", str(float("{0:.3f}".format(sk)))))
        self.ui.label_23.setText(_translate("Dialog", str(float("{0:.3f}".format(cal)))))
        self.ui.label_24.setText(_translate("Dialog", str(float("{0:.3f}".format(fos)))))
        self.ui.label_25.setText(_translate("Dialog", str(float("{0:.3f}".format(na)))))
        self.ui.label_47.setText(_translate("Dialog", str(float("{0:.3f}".format(liz)))))
        self.ui.label_48.setText(_translate("Dialog", str(float("{0:.3f}".format(met)))))

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
            self.ui.label_32.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_kdg)))))
        else:
            self.ui.label_32.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_32.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_kdg)))))

        otl_sp = norm_sp - sp
        if sp == norm_sp:
            self.ui.label_33.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_33.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_sp)))))
        else:
            self.ui.label_33.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_33.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_sp)))))

        otl_sk = norm_sk - sk
        if sk == norm_sk:
            self.ui.label_34.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_34.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_sk)))))
        else:
            self.ui.label_34.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_34.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_sk)))))

        otl_cal = norm_cal - cal
        if cal == norm_cal:
            self.ui.label_35.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_35.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_cal)))))
        else:
            self.ui.label_35.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_35.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_cal)))))

        otl_fos = norm_fos - fos
        if fos == norm_fos:
            self.ui.label_36.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_36.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_fos)))))
        else:
            self.ui.label_36.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_36.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_fos)))))

        otl_na = norm_na - na
        if na == norm_na:
            self.ui.label_37.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_37.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_na)))))
        else:
            self.ui.label_37.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_37.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_na)))))

        otl_liz = norm_liz - liz
        if liz == norm_liz:
            self.ui.label_51.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_51.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_liz)))))
        else:
            self.ui.label_51.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_51.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_liz)))))

        otl_met = norm_met - met
        if met == norm_met:
            self.ui.label_52.setStyleSheet("color: rgb(0, 255, 60);")
            self.ui.label_52.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_met)))))
        else:
            self.ui.label_52.setStyleSheet("color: rgb(255, 0, 0);")
            self.ui.label_52.setText(_translate("Dialog", str(float("{0:.3f}".format(otl_met)))))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec_())
