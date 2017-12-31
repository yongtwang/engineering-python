from calculator_gui import *

def signals(self):
    self.buttonCalc.clicked.connect(self.calc)  # Connect buttonCalc clicked signal to the calc function

def calc(self):  # Do the calculation
    a = self.lineEdit1.text()
    b = self.lineEdit2.text()
    operator = self.comboBox.currentText()
    try:
        c = eval(a + operator + b)  # e.g., eval('2 * 4')
        self.lineEdit3.setText(str(c))
    except:  # In case an error occurs
        QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Invalid inputs!', QtWidgets.QMessageBox.Ok)

Ui_MainWindow.signals = signals  # Add new attributes to Ui_MainWindow
Ui_MainWindow.calc = calc

if __name__ == "__main__":  # A library or a stand-alone program
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Must create a QApplication object
                                            # sys.argv allows passing parameters in command line
    MainWindow = QtWidgets.QMainWindow()  # Create a main window instance.
    ui = Ui_MainWindow()  # Create a Ui_MainWindow instance
    ui.setupUi(MainWindow)  # Add widgets to the main window
    ui.signals()  # Connect signals with the appropriate functions
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # If a termination signal is captured, exit the program.
