import os 
import pgzrun, random
from random import randint

WIDTH, HEIGHT = 800, 600
WHITE, VIOLET, BLUE = (255,255,255), (255, 182, 193), (0, 128, 255)

# Khai báo biến
diem = 0
ket_thuc = False

# Định dạng hình nền
background = Actor("nengame")

# Định dạng tank
tank = Actor('captain')
tank.x, tank.y = 100, 550

# Định dạng hộp quà
item = Actor('hopqua')
item.x, item.y = 200, 0

# Định dạng viên thiên thạch
rock = Actor('thienthach')
rock.x, rock.y = 400, 0

# Set up điểu khiển tank bằng chuột
def on_mouse_move(pos,rel,buttons):
    tank.x = pos[0]
    tank.y = pos[1]

sounds.nhacnen.play()
sounds.nhacnen.set_volume(0.5)

# Reset game
def reset_game():
    global diem, ket_thuc
    diem = 0
    ket_thuc = False
    tank.x, tank.y = 100, 550
    item.x, item.y = 200, 0
    rock.x, rock.y = 400, 0

