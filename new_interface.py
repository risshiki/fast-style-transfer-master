import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QProcess
import subprocess



# file_location = None
# check_location = None
original_colors = True


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT Interface for Video Style Transfer")

        

        
        openFile = QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        openCheckpoint = QtGui.QAction("&Open Checkpoint", self)
        openCheckpoint.setShortcut("Ctrl+J")
        openCheckpoint.setStatusTip('Open Checkpoint')
        openCheckpoint.triggered.connect(self.checkpoint)


        mainMenu = self.menuBar()
        
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(openCheckpoint)
        
        

        self.home()

    def home(self):

        self.label1 = QtGui.QLabel("File",self)
        self.label2 = QtGui.QLabel("Checkpoint",self)


        self.button = QtGui.QPushButton("Convert",self)
        self.textLine1 = QtGui.QLineEdit("File Path",self)
        self.textLine2 = QtGui.QLineEdit("Checkpoint Path",self)
        
        self.button.clicked.connect(self.executescript)

        self.label1.move(50,100)
        self.label2.move(50,150)
        
        self.textLine1.move(150,100)
        self.textLine2.move(150,150)
        self.button.move(50,200)


        

        
        self.show()

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        with file:
            file_location = name
            self.textLine1.setText(name) 

    def checkpoint(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name,'r')

        with file:
            check_location = name
            self.textLine2.setText(name)

    def executescript(self):
        self.button.setText("processing")
        script = "python transform_video.py --in-path " +  self.textLine1.text() + " " + "--checkpoint " + self.textLine2.text() + " " +  "--out-path video.mp4 " + "--batch-size 4"
        
        if original_colors == True:
            script = script + " --original_colors True"
        #print(script)
        subprocess.call(script, shell=True)
        self.button.setText("Done")



    

    


        
  
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()