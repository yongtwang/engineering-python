from card_gui import *
import time  # Used to simulate the progress in the progressbar
import numpy as np  # Used to generate a permutation

def signals(self):
    self.buttonGenerate.clicked.connect(self.generate)
    for i in range(30):
        statement_str = 'self.pushButton_'+str(i+1)+'.clicked.connect(self.pick)'
        eval(statement_str)

def generate(self):
    self.progressBar.setValue(0)
    n = int(self.lineEdit.text())  # You may add more code for input validation
    x = np.arange(1, n+1)  # Including 1 but not including n+1
    self.permutation = np.random.permutation(x)
    #print(self.permutation)  # For debugging
    for i in range(30):
        if i+1 <= n:
            eval('self.pushButton_'+str(i+1)+'.setEnabled(True)')
        else:
            eval('self.pushButton_'+str(i+1)+'.setEnabled(False)')
        eval('self.pushButton_'+str(i+1)+'.setText("?")')  # Reset the text of every button
        self.progressBar.setValue((i+1)/30*100)
        time.sleep(0.05)  # Pause for 0.05 seconds. Otherwise the progressbar is filled too fast

def pick(self):
    button_name = MainWindow.sender().objectName()  # Get the name of the button that sent the signal
    id = int(button_name.replace('pushButton_', ''))  # Get the button id
    #print(button_name, id, self.permutation[id-1])  # For debugging
    MainWindow.sender().setText(str(self.permutation[id-1]))
    
Ui_MainWindow.signals = signals
Ui_MainWindow.generate = generate
Ui_MainWindow.pick = pick

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())

