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


# set up các vật thể & tính điểm, cộng điểm khi nhặt được hộp quà
def update():
    global diem, ket_thuc
    if ket_thuc:  # Không cập nhật nếu game đã kết thúc
        return
    # Tăng tốc độ rơi của thiên thạch dựa vào điểm mà player đang có
    item.y = item.y + 2 + diem / 4
    rock.y = rock.y + 2 + diem / 4

    # Set up giới hạn của màn hình
    if item.y > 600:
        item.y = 0
    
    # Thiên thạch này rơi xong thì random lại thiên thạch rơi tiếp
    if rock.y > 600:
        rock.y = 0
        rock.x = random.randint(20,780)
        

    # item và thiên thạch không được xuất hiện ngẫu nhiên cùng một chỗ
    while rock.colliderect(item):
        rock.x = random.randint(20,780)
        item.x = random.randint(20,780)

    # Xe tăng nhặt hộp quà
    if item.colliderect(tank):
        item.x = random.randint(20,780)
        item.y = 0
        diem += 1
        
    # Thiên thạch rơi trúng xe tăng
    if rock.colliderect(tank):
        ket_thuc = True
        sounds.bum.play()
        sounds.nhacnen.stop()

# Đưa các đối tượng và thông báo ra màn hình
def draw():
    background.draw()
    if ket_thuc:
        screen.draw.text('You Lose',(210,200), color = WHITE, fontsize=60)
        screen.draw.text('Total Score: '+ str(diem),(210,250), color = VIOLET, fontsize=80)
        screen.draw.text('(Press G to play again)',(210,330), color = BLUE, fontsize=40)
        if keyboard.G:
            reset_game()
            sounds.nhacnen.play()
            sounds.nhacnen.set_volume(0.5)
    else:
      screen.draw.text('Score: '+ str(diem),(10,15), color = WHITE, fontsize=60)
      tank.draw()
      item.draw()
      rock.draw()

# Trước khi chạy game, set up vị trí cho cửa sổ lúc nó hiện lên sẽ nằm phía trên và ở giữa
window_position = "{},{}".format(
    (os.get_terminal_size().columns - WIDTH) // 2,
    (os.get_terminal_size().lines - HEIGHT) // 2
)

os.environ['SDL_VIDEO_CENTERED'] = '1'
os.environ['SDL_VIDEO_WINDOW_POS'] = window_position

pgzrun.go()