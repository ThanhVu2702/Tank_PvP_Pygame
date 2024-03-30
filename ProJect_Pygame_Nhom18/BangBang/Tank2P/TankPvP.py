import pygame
from pygame.locals import *
import random
import time
import socket
import threading

pygame.init()


s = socket.socket()
host = "127.0.0.1"
port = 9999
playerOne = 1
playerTwo = 2
bottomMsg = ""
currentPlayer = 0
msg =""



def player_classes(option,player):
    '''
    Để thêm thuộc tính vào player.sprite dựa trên loại xe tăng mà người dùng đã chọn (player1 hoặc player2), 
    chương trình sẽ kiểm tra loại xe tăng đó và thêm các thuộc tính tương ứng. 
    Điều này sẽ giúp xác định các đặc điểm cụ thể của từng loại xe tăng và áp dụng chúng vào sprite của người chơi.
    '''
    if option == 0: #tank 1 có tốc độ bắn và di chuyển nhanh hơn, nhưng có lượng máu thấp hơn

        player.cooldown = 30 #Giảm cooldown để bắn nhanh hơn
        player.health = 3  
        player.speed = 5
        player.pics = ver1 # ảnh dùng cho xe tăng loại 1
        player.image = ver1[0] # Ảnh hiển thị đầu tiên cho xe tăng loại 1

    elif option == 1: #tank 2 có tốc độ bắn và di chuyển chậm, nhưng nhiều máu 
        player.cooldown = 45
        player.health = 6
        player.speed = 3
        player.pics = ver2
        player.image = ver2[0]

############### SET UP DI CHUYỂN CỦA TANK #######################
def movement(player):
    
    '''
   di chuyển trong trò chơi phụ thuộc vào phím được bấm
   xử lý đầu vào từ bàn phím để di chuyển tank theo các hướng, ngăn tank đi xuyên tường, đi xuyên player khác
    '''
    key = pygame.key.get_pressed()
    #tạo ra một cơ chế di chuyển liên tục cho sprite mà không bị gián đoạn khi người chơi giữ phím 
    #đồng thời đề cập đến cách xử lý va chạm để ngăn sprite không di chuyển qua các vật thể khác.


    if key[player.keys[0]]:
        player.rect.left -= player.speed # Di chuyển sprite sang trái theo tốc độ đã định
        player.direction = 'left' # Cập nhật hướng di chuyển của sprite
        player.image = player.pics[3] # Cập nhật hình ảnh của sprite khi người chơi hướng di chuyển sang trái


    elif key[player.keys[1]]:
        player.rect.left += player.speed
        player.direction = 'right'
        player.image = player.pics[2]

    elif key[player.keys[2]]:
        player.rect.top -= player.speed
        player.direction = 'up'
        player.image = player.pics[0]

    elif key[player.keys[3]]:
        player.rect.top += player.speed
        player.direction = 'down'
        player.image = player.pics[1]


    if len(pygame.sprite.spritecollide(player,players,False))> 1 or pygame.sprite.spritecollide(player,walls,False):
    #Trong trường hợp "player" nằm trong nhóm sprite "players", chúng ta cần kiểm tra xem có va chạm với đối tượng khác trong nhóm hay không bằng cách xem độ dài của danh sách va chạm có lớn hơn 1 không. Nếu độ dài này lớn hơn 1, điều này có nghĩa là đã có va chạm với một "player" khác.
    #Hàm collidelist sẽ trả về -1 nếu không có va chạm nào. Vì vậy, nếu giá trị trả về khác -1, điều đó cho biết "player" đã va chạm vào 1 khối tuong.
    

        if player.direction == 'left':
            player.rect.left += player.speed
        if player.direction == 'right':
            player.rect.left -= player.speed
        if player.direction == 'up':
            player.rect.top += player.speed
        if player.direction == 'down':
            player.rect.top -= player.speed


################################## SET UP MENU GAME #############################################################################   
def gameMenu(thisStage):
    '''
    cải thiện menu game bằng cách đặt nền nhạc, và hiển thị tiêu đề cùng với hai lựa chọn:
    "Start Game" và "Exit Game". Khi người chơi di chuyển chuột qua các label lựa chọn, chúng sẽ được làm nổi bật với màu sắc và dấu gạch dưới.
    Phản ứng của label được cập nhật trực tiếp trên màn hình.
    Sự kiện chuột được quản lý để xử lý việc bắt đầu game hoặc thoát khỏi game phụ thuộc vào label mà người dùng chọn.
    '''
    global run, selecting, battling, end                                                
    pygame.mixer.music.load(musicList[0])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    
    Title = my_font.render('Tank PvP', True, (255, 0, 0)) # set up tiêu đề game màu đỏ

    #tạo hình chữ nhật (text_rect) xung quanh Title, canh giữa theo chiều ngang ở trên màn hình dọc, làm Title nổi bật.
    text_rect = Title.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4)) 
    # in dòng chữ lên màn hình
    screen.blit(Title, text_rect)

    Start_label = my_font2.render('Start Game', True, (212,212,212)) #Tạo surface chứa văn bản "Start Game", tham số True giúp hình ảnh rõ nét hơn
    Exit_label = my_font2.render('Exit Game', True, (212,212,212))
    
    Srect = Rect(210,280,421,339)         #hiệu ứng khi trỏ chuột vào
    Erect = Rect(245,340,380,430)
        
    while thisStage:
            
            x, y = pygame.mouse.get_pos()        #định vị trí của chuột trên màn hình
            Opt = 0                                            
            '''
            Nếu vị trí chuột (x, y) nằm trong phạm vi của hình chữ nhật Srect
            tức là vùng mà label "Start Game", "Exit Game"
            '''
            if Srect[0] < x <Srect[2] and Srect[1] < y < Srect[3]: 
                my_font2.set_underline(True)
                Start_label = my_font2.render('Start Game', True, (255,255,0)) # nháy màu vàng, phần gạch chân cũng vậy
                screen.blit(Start_label, (183,280))
                pygame.display.flip()

                Opt = 1 #biến Opt được đặt thành 1, label "Start Game" đang được chọn. Khi người chơi nhấp chuột, có thể sẽ có sự kiện diễn ra tùy vào giá trị của Opt.                                                      
                                                                                 
            elif Erect[0] < x < Erect[2] and Erect[1] < y < Erect[3]:           

                my_font2.set_bold(True)
                Exit_label = my_font2.render('Exit Game', True, (255,0,0))
                screen.blit(Exit_label, (170, 340))
                pygame.display.flip()
                
                Opt = 2
                
            my_font2.set_bold(False) #tắt hiệu ứng gạch dưới
            my_font2.set_underline(False)
            Start_label = my_font2.render('Start Game', True, (212,212,212)) #set up màu cho label Star Game
            Exit_label = my_font2.render('Exit Game', True, (212,212,212))

            screen.blit(screenPIC, (0,0))
            screen.blit(Title, (90,120))  # căn giữa Tank2P
            screen.blit(Start_label, (180,280))                 #tọa độ chuỗi Start Game
            screen.blit(Exit_label, (180, 340))            #blit: viết nội dung lên screen
            pygame.display.flip()                          #cập nhật nội dung trên screen
            
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.mixer.music.stop() #khi đóng cửa sổ game thì hàm được gọi để stop nhạc nền của game
                    run = False
                    starting = False
                    selecting = False 
                    battling = False           #các biến cục bộ được trả về false để kết thúc các trạng thái
                    end = False                
                    thisStage = False
                    
                elif ev.type == MOUSEBUTTONDOWN: #kích hoạt event khi click chuột
                    if Opt == 1:
                        pygame.mixer.music.stop()
                        starting = False      #nếu chọn Start game thì nhạc sẽ dừng, kiểm soát hiển thị trên màn và chuyển tiếp vào select tank
                        thisStage = False
                    elif Opt == 2:
                        pygame.mixer.music.stop()
                        run = False
                        starting = False
                        selecting = False
                        battling = False #nếu chọn exit game thì nhạc cũng dừng lại và đóng cửa sổ, kết thúc mọi trạng thái
                        end = False
                        thisStage = False



pygame.init()
pygame.mixer.init(44100, -16, 2, 2048) #set up chất lựơng âm thanh
clock = pygame.time.Clock() #điều chỉnh tốc độ của trò chơi, thời gian chờ,...

colours = pygame.color.THECOLORS # dictionary chứa màu sắc tiêu chuẩn của Pygame
my_font = pygame.font.SysFont('Verdana', 100)
my_font2 = pygame.font.SysFont('moolboran', 66)
my_font3 = pygame.font.SysFont('andalus', 72)      #setup Font chữ
my_font4 = pygame.font.SysFont('candara', 20)
my_font5 = pygame.font.SysFont('arial', 16)

size = (605, 540) #kích thước cửa sổ game
screen = pygame.display.set_mode(size)
screenPIC = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/anhnen.png')
pygame.display.set_caption("Tank Moba PvP")              #đặt tiêu đề cửa sổ game
background = pygame.Surface(size) # tạo một đối tượng Surface để làm nền, sau đó "convert" nó để cải thiện hiệu suất hiển thị trên màn hình.
background = background.convert()
background.fill(colours['grey']) #màu nền của map trong game

explode = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/Tank2P/bum.ogg')
shoot = pygame.mixer.Sound('ProJect_Pygame_Nhom18/BangBang/Tank2P/music/fireMusic.mp3')          
musicList = ['ProJect_Pygame_Nhom18/BangBang/Tank2P/music/endMusic.mp3','ProJect_Pygame_Nhom18/BangBang/Tank2P/music/selectSong.mp3','ProJect_Pygame_Nhom18/BangBang/Tank2P/mbattle.ogg','ProJect_Pygame_Nhom18/BangBang/Tank2P/music/endMusic.mp3']

maps = ['ProJect_Pygame_Nhom18/BangBang/Tank2P/map1.txt', 'ProJect_Pygame_Nhom18/BangBang/Tank2P/map2.txt', 'ProJect_Pygame_Nhom18/BangBang/Tank2P/map3.txt']
tiles = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tuong.png')

explosion = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/vuno.png')
imageUp_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 up.png')
imageDown_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 down.png')
imageRight_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 right.png')     #load ảnh khi tank thay đổi hướng khi di chuyển
imageLeft_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 left.png')

imageUp_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 up.png')
imageDown_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 down.png')
imageRight_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 right.png')
imageLeft_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 left.png')

#Hai danh sách chứa hình ảnh đại diện cho các version khác nhau của người chơi và các nhiều hướng khác nhau
ver1 = [imageUp_v1,imageDown_v1,imageRight_v1,imageLeft_v1]
ver2 = [imageUp_v2,imageDown_v2,imageRight_v2,imageLeft_v2]
spawnpoints = [(30,30),(40,390),(560,130),(560,390)]  #List chứa các cặp tuple, mỗi tuple là một điểm xuất phát của viên đạn trên màn hình.              


players = pygame.sprite.Group()
#Tạo hai đối tượng người chơi là các sprite có hình chữ nhật xác định vị trí và kích thước, hướng di chuyển trên màn hình
player1 = pygame.sprite.Sprite()
player1.rect = pygame.Rect((20, 20),(24,24))                        
player1.direction = 'up'                                            
player1.keys = (K_a, K_d, K_w, K_s,K_4)    # Player 1 sử dụng phím W A S D để di chuyển và phím bắn đạn là phím 4                   

player2 = pygame.sprite.Sprite()
player2.rect = pygame.Rect((560, 390), (24,24))
player2.direction = 'up'
player2.keys = (K_LEFT, K_RIGHT, K_UP, K_DOWN,K_l) # Player 2 sử dụng phím LEFT RIGHT UP DOWN để di chuyển và phím bắn đạn là phím l

players.add(player1) #phương thức add thêm player 1 & 2 vào nhóm player
players.add(player2)

bulletgroup = pygame.sprite.Group()
walls = pygame.sprite.Group()                       

            
run = True
starting = True                     
selecting = True
battling = True
end = True


while run:
    fps = clock.tick(30)

    gameMenu(starting) # hàm hiển thị menu trò chơi khi trò chơi bắt đầu
    # selectionScreen(selecting) #hiển thị màn hình chọn tank 
    # battleScreen(battling)
    
   

pygame.display.quit()
quit()
