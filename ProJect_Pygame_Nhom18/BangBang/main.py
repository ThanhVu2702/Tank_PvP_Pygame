import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot
import subprocess
import pygame  # Thêm thư viện pygame để phát nhạc

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PROJECT PYGAME NHOM 18'
        self.left = 700
        self.top = 300
        self.width = 728
        self.height = 410
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Thiết lập logo cho cửa sổ chính
        icon = QIcon('ProJect_Pygame_Nhom18/BangBang/images/icon.png')
        self.setWindowIcon(icon)

        # Tạo label hiển thị ảnh nền
        label = QLabel(self)
        pixmap = QPixmap('ProJect_Pygame_Nhom18/BangBang/images/background.png')
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, self.width, self.height)
        
        # Phát nhạc nền khi mở game
        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/sounds/musicbg.wav')
        self.sound.set_volume(0.5) #set up độ lớn/nhỏ của nhạc
        self.sound.play()
        
        # Tạo 3 button
        btn1 = QPushButton('Tank PvP Online', self)
        btn1.move(90, 370)
        btn1.setStyleSheet("QPushButton:hover { background-color: red }") #đổi màu nền button
        btn1.clicked.connect(self.on_click_game)
        
        btn2 = QPushButton('Crazy Tank', self)
        btn2.move(300, 370)
        btn2.setStyleSheet("QPushButton:hover { background-color: yellow }")
        btn2.clicked.connect(self.on_click_game)
        
        btn3 = QPushButton('Tank PvP Offline', self)
        btn3.move(510, 370)
        btn3.clicked.connect(self.on_click_game)
        
        self.show()
    
    @pyqtSlot()
    def on_click_game(self):
        self.sound.stop()
        sender = self.sender()
        game_process = None
        if sender.text() == 'Tank PvP Online':
            game_process = subprocess.Popen(['python', 'ProJect_Pygame_Nhom18/BangBang/Tank2P/TankPvP.py'])
        if sender.text() == 'Crazy Tank':
            game_process = subprocess.Popen(['python', 'ProJect_Pygame_Nhom18/BangBang/CrazyTank.py'])
        elif sender.text() == 'Tank PvP Offline':
            game_process = subprocess.Popen(['python', 'ProJect_Pygame_Nhom18/BangBang/Tank2P_Offline/TankPvP.py'])
        
        game_process.wait()  # đợi ta thoát game
        self.sound.play()  # Phát lại nhạc nền

    @pyqtSlot()    
    def on_click_exit(self):
        self.sound.stop()
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
