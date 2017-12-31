from editor_gui import *

def signals(self):
    self.actionOpen.triggered.connect(self.file_open)
    self.actionSave.triggered.connect(self.file_save)
    self.actionQuit.triggered.connect(self.file_quit)
    self.actionFont.triggered.connect(self.edit_font)
    self.actionColor.triggered.connect(self.edit_color)        
    self.checkBox.stateChanged.connect(self.enlarge_window)
    
def file_open(self):
    name = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File')  # Returns a tuple
    #print(name)  # For debugging
    if len(name[0]) > 0:
        with open(name[0], 'r') as file:
            text = file.read()
            self.textEdit.setText(text)
        
def file_save(self):
    name = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save File')  # Returns a tuple
    #print(name)  # For debugging
    if len(name[0]) > 0:        
        with open(name[0], 'w') as file:
            #text = self.textEdit.toPlainText()  # Plain text without formatting
            text = self.textEdit.toHtml()  # Rich text with formatting (font, color, etc.)
            file.write(text)
            
def file_quit(self):
    decision = QtWidgets.QMessageBox.question(MainWindow, 'Question',
                   'Sure to quit?',
                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    if decision == QtWidgets.QMessageBox.Yes:
        sys.exit()

def edit_font(self):  # Applies on all text
    font = self.textEdit.font()  # Get the currently used font
    newfont, valid = QtWidgets.QFontDialog.getFont(font)
    if valid:
        self.textEdit.setFont(newfont)

def edit_color(self):  # Applies on selected text only
    color = self.textEdit.textColor()
    newcolor = QtWidgets.QColorDialog.getColor(color)
    if newcolor.isValid():
        self.textEdit.setTextColor(newcolor)

def enlarge_window(self):
    if self.checkBox.isChecked():
        MainWindow.setGeometry(100, 100, 600, 400)
    else:
        MainWindow.setGeometry(100, 100, 400, 300)

Ui_MainWindow.signals = signals
Ui_MainWindow.file_open = file_open
Ui_MainWindow.file_save = file_save
Ui_MainWindow.file_quit = file_quit
Ui_MainWindow.edit_font = edit_font
Ui_MainWindow.edit_color = edit_color
Ui_MainWindow.enlarge_window = enlarge_window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())

