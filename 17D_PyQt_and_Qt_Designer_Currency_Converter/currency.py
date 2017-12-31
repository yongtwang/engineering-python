from currency_gui import *
import urllib3  # An HTTP client. Installed with Anaconda.
urllib3.disable_warnings()

def signals(self):
    self.actionDownload_Rates.triggered.connect(self.download)
    self.lineEdit_1.textEdited['QString'].connect(self.edit1_change)
    self.lineEdit_2.textEdited['QString'].connect(self.edit2_change)
    self.comboBox_1.activated[str].connect(self.edit1_change)
    self.comboBox_2.activated[str].connect(self.edit2_change)
    
def download(self):
    http = urllib3.PoolManager()  # A PoolManager handles all of the details of connection pooling
    try:
        r = http.request('GET', 'https://api.fixer.io/latest?base=USD', retries=False)  # Rates are quoted against the base (USD).
        #print(r.data)  # For debugging
        data = r.data.decode('ascii')
        #print()  # For debugging
        #print(data)  # For debugging
        #print('Download Successfully!')  # For debugging
        self.actionDownload_Rates.setEnabled(False)  # Disable this menu to avoid downloading again
        r.close()

        data = eval(data)  # To be safer, you may use: import ast; ast.literal_eval(data)
        self.rates = data['rates']
        self.rates['USD'] = 1.0
        #print(self.rates)  # For debugging
        for key, value in self.rates.items():
            self.comboBox_1.addItem(key)
            self.comboBox_2.addItem(key)
    except urllib3.exceptions.NewConnectionError:
        QtWidgets.QMessageBox.critical(MainWindow, 'Error', 'Download failed!', QtWidgets.QMessageBox.Ok)

def edit1_change(self):
    key1 = self.comboBox_1.currentText()
    key2 = self.comboBox_2.currentText()
    rate = self.rates[key2]/self.rates[key1]
    amount = float(self.lineEdit_1.text()) * rate
    self.lineEdit_2.setText('{:.2f}'.format(amount))

def edit2_change(self):
    key1 = self.comboBox_1.currentText()
    key2 = self.comboBox_2.currentText()
    rate = self.rates[key1]/self.rates[key2]
    amount = float(self.lineEdit_2.text()) * rate
    self.lineEdit_1.setText('{:.2f}'.format(amount))

Ui_MainWindow.signals = signals
Ui_MainWindow.download = download
Ui_MainWindow.edit1_change = edit1_change
Ui_MainWindow.edit2_change = edit2_change

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())

