"""
This module contains code for PasswordGeneratorGUI main class.
It is used to generating and saving passwords with GUI.
"""
import random
import sys
from string import ascii_letters, digits, punctuation

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

import password_generator.window as window


class PasswordGeneratorGUI(QMainWindow, window.Ui_MainWindow):
    """
    This is a class for GUI of the Password Generator.
    It provides window, buttons and functions to handle them.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_generate.clicked.connect(self.generate_password)
        self.action_save.triggered.connect(self.save_password)
        self.aplha = ''.join((ascii_letters, digits, punctuation))
        self.pass_len_box.setMaximum(len(self.aplha))

    def generate_password(self):
        """Generate password with required length"""
        p = ''.join(random.sample(self.aplha, int(self.pass_len_box.text())))
        self.display_password_area.setText(p)

    def save_password(self):
        """Save password to file"""
        save_path = QFileDialog.getSaveFileName(caption='Save to')[0]
        password = self.display_password_area.text()
        if save_path:
            with open(save_path, 'w') as f:
                f.write(password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_ = PasswordGeneratorGUI()
    window_.show()
    app.exec_()
