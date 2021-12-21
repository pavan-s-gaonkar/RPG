from ASCII import ASCII
import random
import ctypes
import sys
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from Gui import Ui_MainWindow
import re
import pyperclip


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        self.ascii_data = ASCII('.\\artifact\\AsciiTable.txt')
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.set_current_time()

        self.timer = QtCore.QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.set_current_time)
        self.pushButton.clicked.connect(self.generate_button_clicked)
        self.copyButton.clicked.connect(self.copy_button_clicked)

    def set_current_time(self):
        self.timerLabel.setText(datetime.now().strftime("%H:%M:%S") + "  ")

    def copy_button_clicked(self):
        pyperclip.copy(self.resultTextObj.text())

    def generate_button_clicked(self):
        self.resultTextObj.clear()

        if 0 == len(self.numOfCharObj.text()):
            self.resultTextObj.setText("Error: Number of character for password has no empty")
        elif self.is_only_number(self.numOfCharObj.text()):
            self.resultTextObj.setText("Error: Number of character for password contains non digit characters")
        elif int(self.numOfCharObj.text()) < 2:
            self.resultTextObj.setText("Error: Number of character for pwd is less than 2")
        elif int(self.numOfCharObj.text()) > 31:
            self.resultTextObj.setText("Error: Number of character for pwd is greater than 31")
        elif (not self.numberCheckBox.isChecked()) and \
                (not self.alphaUpperCheckBox.isChecked()) and \
                (not self.alphaLowerCheckBox.isChecked()) and \
                (not self.symbolCheckBox.isChecked()):
            self.resultTextObj.setText("Error: No options selected")
        else:
            self.resultTextObj.setText(
                str(self.generate_password(int(self.numOfCharObj.text()),
                                           self.numberCheckBox.isChecked(),
                                           self.alphaUpperCheckBox.isChecked(),
                                           self.alphaLowerCheckBox.isChecked(),
                                           self.symbolCheckBox.isChecked(),
                                           self.avoidNumberAtExtremeCheckBox.isChecked(),
                                           self.avoidSymbolsAtExtremeCheckBox.isChecked())
                    ))

    @staticmethod
    def is_only_number(num_of_character_string):
        return bool(re.search(r'\D', num_of_character_string))

    def generate_password(self, length, is_num=True, is_upper_case=True, is_lower_case=True, is_symbol=True,
                          avoid_num_at_ext=False, avoid_sym_at_ext=False):
        return self.generate_generic_password(1, not avoid_num_at_ext, is_upper_case, is_lower_case,
                                              not avoid_sym_at_ext) + \
               self.generate_generic_password(length - 2, is_num, is_upper_case, is_lower_case, is_symbol) + \
               self.generate_generic_password(1, not avoid_num_at_ext, is_upper_case, is_lower_case,
                                              not avoid_sym_at_ext)

    def generate_generic_password(self, length, is_num=True, is_upper_case=True, is_lower_case=True, is_symbol=True):
        tmp_result = list()
        actual_length = 0
        while actual_length < length:
            list_selection = random.randint(1, 4)
            if list_selection == 1 and is_num:
                tmp_result.append(random.choice(self.ascii_data.number_set))
                actual_length = actual_length + 1
            elif list_selection == 2 and is_upper_case:
                tmp_result.append(random.choice(self.ascii_data.upper_case_char_set))
                actual_length = actual_length + 1
            elif list_selection == 3 and is_lower_case:
                tmp_result.append(random.choice(self.ascii_data.lower_case_char_set))
                actual_length = actual_length + 1
            elif list_selection == 4 and is_symbol:
                tmp_result.append(random.choice(self.ascii_data.symbol_set))
                actual_length = actual_length + 1
            else:
                pass

        result = ""
        for tmp_entry in tmp_result:
            result = result + tmp_entry
        return result


class RPG:
    def __init__(self):
        # Below 2 lines are needed to set the ICON of application on WINDOWS
        self.my_app_id = 'my_company.my_product.sub_product.version'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.my_app_id)
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.setWindowIcon(QtGui.QIcon('artifact\\password_key_icon123.png'))
        app.exec()


if __name__ == '__main__':
    RPG()

