"""
GUI
"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QApplication, QMessageBox
from PyQt5.QtGui import QDoubleValidator, QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QLine, QSize

class TextMood(QWidget):
    def __init__(self):
        super(TextMood, self).__init__()
        self.header = QLabel("Text Mood Analysis")
        self.header.setFont(QFont("Times",24, weight=QFont.Bold))
        self.input_box = QTextEdit()
        self.submit = QPushButton("PREDICT")
        self.sad = QPushButton()
        self.enthu = QPushButton()
        self.neutral = QPushButton()
        self.happy = QPushButton()
        self.love = QPushButton()
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()
        self.init_UI()
    
    def init_UI(self):
        """initializes the gui """
        self.header.setAlignment(Qt.AlignTop)
        self.submit.setFixedWidth(100)
        self.v_box.addWidget(self.header)
        self.input_box.setFixedSize(400, 100)
        self.v_box.addWidget(self.input_box)
        self.v_box.setSpacing(10)
        #self.h_box.addSpacing(30)
        self.v_box.addWidget(self.submit)
        self.sad.setFixedSize(80,80) 
        self.sad.setIcon(QIcon("icons/frown.png"))
        self.sad.setIconSize(QSize(70,70))
        self.enthu.setFixedSize(80,80) 
        self.enthu.setIcon(QIcon("icons/surprised.png"))
        self.enthu.setIconSize(QSize(70,70))
        self.neutral.setFixedSize(80,80) 
        self.neutral.setIcon(QIcon("icons/silent1.png"))
        self.neutral.setIconSize(QSize(70,70))
        self.happy.setFixedSize(80,80) 
        self.happy.setIcon(QIcon("icons/happiness.png"))
        self.happy.setIconSize(QSize(70,70))
        self.love.setFixedSize(80,80)
        self.love.setIcon(QIcon("icons/in-love3.png"))
        self.love.setIconSize(QSize(70,70))
        self.h_box.addWidget(self.sad)
        self.h_box.addWidget(self.enthu)
        self.h_box.addWidget(self.neutral)
        self.h_box.addWidget(self.happy)
        self.h_box.addWidget(self.love)
        self.v_box.addLayout(self.h_box)
        self.v_box.addStretch(1)
        self.setLayout(self.v_box)

    def mwindow(self) -> None:
        """ window features are set here and application is loaded into display"""
        self.setWindowTitle("Text emotion analysis")
        self.show()


if __name__=="__main__":
    app = QApplication(sys.argv)
    a_window = TextMood()
    a_window.mwindow()
    sys.exit(app.exec_())