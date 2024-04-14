from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from gpiozero import LED
import time

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("LED Buttons")
        self.initUI()
        
    def initUI(self):
		#LED controller buttons 
        self.green_button = QtWidgets.QPushButton("GREEN", self)
        self.green_button.setGeometry(50, 50, 100, 50)
        self.green_button.clicked.connect(self.green_clicked) 
        
        self.blue_button = QtWidgets.QPushButton("BLUE", self)
        self.blue_button.setGeometry(50, 120, 100, 50)
        self.blue_button.clicked.connect(self.blue_clicked) 
     
        self.red_button = QtWidgets.QPushButton("RED", self)
        self.red_button.setGeometry(50, 190, 100, 50)
        self.red_button.clicked.connect(self.red_clicked)
        
        #Exit button
        self.exit_button = QtWidgets.QPushButton("EXIT", self)
        self.exit_button.setGeometry(150, 250, 100, 30)
        self.exit_button.clicked.connect(self.close)

#Button click to turn on corresponding LED for 1 second
    def green_clicked(self):
        print("TURN ON GREEN LED")
        Gled = LED(17)
        Gled.on()
        time.sleep(1)
        Gled.off()
        
    def blue_clicked(self):
        print("TURN ON BLUE LED") 
        Bled = LED(27)
        Bled.on()
        time.sleep(1)
        Bled.off()
        
    def red_clicked(self):
        print("TURN ON RED LED")
        Rled = LED(22)
        Rled.on()
        time.sleep(1)
        Rled.off()
        
        
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()  
    win.show()
    sys.exit(app.exec_())
    
window()
