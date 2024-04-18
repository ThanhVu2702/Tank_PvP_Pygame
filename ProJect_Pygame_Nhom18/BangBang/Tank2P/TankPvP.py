import pygame
from pygame.locals import *
import random
import time
import socket
import threading
import time

pygame.init()


s = socket.socket()
host = "127.0.0.1"
port = 9999
playerOne = 1
playerTwo = 2
bottomMsg = ""
currentPlayer = 0
msg =""

Opt1 = 0
Opt2 = 0 

def create_thread(target):
    t = threading.Thread(target = target) #argument - target function
    t.daemon = True
    t.start()
    print("Created thread")

def receive_msg():
    global msg
    while True:
        try:
            recvData = s.recv(2048 * 10)
            msg = recvData.decode()
            print("Receive form "+str(currentPlayer)+" :", msg)
        except socket.error as e:
            print("Socket connection error:", e)
            break



################################################ SET UP BẢNG TÍNH ĐIỂM SAU TRẬN ĐẤU #########################################################################
def writeScorefile():
    # mô tả về việc tạo ra một tệp
    '''
   Để bắt đầu, nhóm sẽ kiểm tra xem có tệp điểm số nào tồn tại bằng cách thử mở nó. 
   Nếu không thể mở tệp, cho thấy tệp đó không tồn tại, nhóm sẽ tạo một tệp mới.
   Trong trường hợp này, tệp mới sẽ được tạo ra và được đặt tiêu đề như "Tên Người Chơi, Điểm Số". 
   Nếu tệp điểm số đã tồn tại, quá trình kiểm tra sẽ kết thúc.
    '''
    haveOne = False
    try:                                #Chương trình sẽ mở tệp tin này
        open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'r')
        haveOne = True
    finally:
        if not haveOne:                 #Nếu không có tệp tin, chương trình sẽ tạo một tệp mới
        
            scores = open('BangTinhDiem.txt', 'w')   
            scores.write('Player1: 0' + '\n')
            scores.write('Player2: 0' + '\n')
            scores.close()
            scoredata = {}
        ''' 
        Chương trình sẽ mở tệp 'BangTinhDiem.txt', sau đó ghi hai dòng vào tệp, mỗi dòng chứa số thứ tự và điểm số cách nhau bởi dấu phẩy. 
        Sau khi ghi, tệp sẽ được đóng và một từ điển rỗng có tên là scoredata sẽ được khởi tạo để lưu trữ dữ liệu.
        '''  
############################################## SET UP CHỈ SỐ TANK ####################################################################################################  
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
            data = "LEFT" + str(player.rect.left)
            s.sendall(data.encode('utf-8'))
           


    elif key[player.keys[1]]:
            player.rect.left += player.speed
            player.direction = 'right'
            player.image = player.pics[2]
            data = "RIGHT" + str(player.rect.left)
            s.sendall(data.encode('utf-8'))
    elif key[player.keys[2]]:
            player.rect.top -= player.speed
            player.direction = 'up'
            player.image = player.pics[0]
            data = "UP" + str(player.rect.top)
            s.sendall(data.encode('utf-8'))
            

    elif key[player.keys[3]]:
            player.rect.top += player.speed
            player.direction = 'down'
            player.image = player.pics[1]
            data = "DOWN" + str(player.rect.top)
            s.sendall(data.encode('utf-8'))

        

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



           
            
################################### SET UP VỊ TRÍ MÁU CỦA PLAYER TRONG TRẬN CHIẾN ###############################################################################
def drawPlayerHealth(player):
    #Hàm này cập nhật và in số máu của người chơi khi ở chế độ chiến đấu
    '''
    Sử dụng vòng lặp for dựa trên lượng máu còn lại của người chơi để in trái tim.
   - Vị trí của trái tim thay đổi tùy theo người chơi,
   - Nếu là người chơi 1, trái tim in ở góc dưới bên trái.
   - Nếu là người chơi 2, trái tim in ở góc dưới bên phải.
    '''
    healthimage = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/blood.png')
    
    p1healthpos = [60, 500]                                 #set up vị trí máu của Player1 trong trận chiến
    p1title = my_font4.render('P1', True, (0,0,0))           #tạo tiêu đề "chữ P1" với màu tương ứng
    p2healthpos = [520,500]
    p2title = my_font4.render('P2', True, (0,0,255))        
    
    screen.blit(p1title, (35, 500)) # vị trí chữ P1 (góc dưới bên trái màn hình)
    screen.blit(p2title, (495, 500)) # Khi giá trị của tọa độ x tăng, đối tượng di chuyển sang bên phải; tọa độ y tăng,di chuyển xuống dưới.

    #duyệt số lượng máu của người chơi và hiển thị nó trên màn hình tương ứng với vị trí của người chơi 1 hoặc người chơi 2
    #đồng thời cập nhật vị trí kế tiếp để hiển thị hình ảnh máu tiếp theo
    for c in range(player.health):
        if player == player1:
            screen.blit(healthimage,p1healthpos)
            p1healthpos[0] += 15
        else:
            screen.blit(healthimage, p2healthpos)
            p2healthpos[0] += 14
    '''
    Khi player là player1, máu được in tại vị trí p1healthpos trên màn hình.
    Việc tăng tọa độ x của p1healthpos lên 15 cho mỗi cục máu đảm bảo không có chồng lấn giữa các biểu tượng máu.
    '''

############################################ SET UP ĐẠN ###############################################################       
def bullet(player):
    #Hàm tạo đạn, thiết lập kích thước, màu sắc, và vị trí của đạn.
    '''
    Hàm sẽ tạo ra đạn khi người chơi bắn, dựa vào người chơi là player 1 hoặc 2. Đạn sẽ được tạo ra và bay ra khỏi tank
    '''
    bullet = pygame.sprite.Sprite()

    bullet.image = pygame.Surface((5,5)) #kích thước viên đạn
    bullet.image.fill((255,0,0)) #màu viên đạn
    bullet.rect = pygame.Rect(bullet.image.get_rect()) #tạo hình (Rect) cho đối tượng bullet dựa trên kích thước của bullet.image, xác định vị trí và kích thước của đối tượng bullet
    bullet.direction = player.direction

    #set up vị trí của viên đạn sao cho khi bắn ra nó nằm ở giữa nòng súng tank
    if bullet.direction == 'up':                                                
        bullet.rect.x, bullet.rect.y = player.rect.x + 12, player.rect.y - 20   
    elif bullet.direction == 'down':
        bullet.rect.x, bullet.rect.y = player.rect.x + 12, player.rect.y + 24
    elif bullet.direction == 'left':
        bullet.rect.x, bullet.rect.y = player.rect.x - 20, player.rect.y + 12
    elif bullet.direction == 'right':
        bullet.rect.x, bullet.rect.y = player.rect.x + 24, player.rect.y + 12

    bulletgroup.add(bullet)

def bullet_update():
    #cập nhật vị trí của đạn
    '''
    viên đạn di chuyển theo hướng tương ứng với thuộc tính direction của nó khi viên đạn được bắn ra.
    '''
    for bullet in bulletgroup:
        if bullet.direction == 'left':
            bullet.rect.x -= 6
        elif bullet.direction == 'right':
            bullet.rect.x += 6
        elif bullet.direction == 'up': #Khi viên đạn di chuyển lên trên, nghĩa là nó đang đi ngược với trục y của màn hình, do đó để viên đạn di chuyển lên trên, giá trị của trục y cần phải giảm
            bullet.rect.y -= 6
        elif bullet.direction == 'down':
            bullet.rect.y += 6

######################################## SET UP MAP #######################################################################
def readMap():
    '''
    chọn một map từ tệp, đọc và phân tích từng dòng của nó, nơi mỗi ô trong tệp cách nhau bởi dấu phẩy,dấu chấm ('.') đại diện cho các tile (tường) 
    Khi đọc mỗi ô, phương pháp này gán hình ảnh tường cho mỗi ô và có thể tiến hành chỉnh sửa ô nếu cần thiết
    '''

  
    # Map = open(random.choice(maps), 'r') #Mở một file bản đồ ngẫu nhiên từ danh sách maps với quyền đọc ('r').
    Map = open(maps[0], 'r')
    x = 0 # kiểm soát vị trí x và y trên bản đồ khi đặt các tiles
    y = 0


    '''
    tạo ra một bức tường từ các tiles có kích thước 12x12 pixel, biểu diễn bởi các dấu chấm trong tệp đầu vào.
    '''
    for l in Map:   
        builtup = l.split(',') #Tách dòng hiện tại thành một list builtup bằng cách phân chia theo dấu phẩy
        builtup[-1] = builtup[-1].strip('\n')  # Loại bỏ ký tự xuống dòng ở cuối mỗi dòng trong list builtup.
        for D in builtup:
            if D == '.':
                tile = pygame.sprite.Sprite()
                tile.image = tiles
                tile.rect = pygame.Rect(x, y, 12, 12)       
                walls.add(tile)                    
                y += 12             #Tăng y sau mỗi tile và di chuyển để đặt tile tiếp theo theo chiều dọc.                 
            else:                # Nếu phần tử không phải là dấu chấm, chỉ tăng y và không tạo sprite
                y += 12
        x += 11                             
        y = 0
           
    Map.close()

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
    Title2 = my_font2.render('Online game', True, (255, 0, 0)) # set up tiêu đề game màu đỏ


    #tạo hình chữ nhật (text_rect) xung quanh Title, canh giữa theo chiều ngang ở trên màn hình dọc, làm Title nổi bật.
    text_rect = Title.get_rect(center=(screen.get_width() / 2, screen.get_height() / 4)) 
    # in dòng chữ lên màn hình
    screen.blit(Title, text_rect)

    Start_label = my_font2.render('Start Game', True, (212,212,212)) #Tạo surface chứa văn bản "Start Game", tham số True giúp hình ảnh rõ nét hơn
    Exit_label = my_font2.render('Exit Game', True, (212,212,212))

    text_rect1 = Start_label.get_rect(center=((screen.get_width() / 3)+150, (screen.get_height() / 4)+250))
    text_rect2 = Exit_label.get_rect(center=((screen.get_width() / 3)+150, (screen.get_height() / 4)+310))
    
        
    while thisStage:
            
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.mixer.music.stop() #khi đóng cửa sổ game thì hàm được gọi để stop nhạc nền của game
                    run = False
                    starting = False
                    selecting = False 
                    battling = False           #các biến cục bộ được trả về false để kết thúc các trạng thái
                    end = False                
                    thisStage = False
                elif ev.type == pygame.MOUSEMOTION:
                    # Kiểm tra nếu chuột nằm trong vùng chứa của title
                    if text_rect1.collidepoint(ev.pos):
                        Start_label = my_font2.render('Start Game', True, (255, 0, 0)) 
                    else:
                        Start_label = my_font2.render('Start Game', True, (212,212,212))  # Khôi phục màu văn bản khi chuột rời đi
                    if text_rect2.collidepoint(ev.pos):
                        Exit_label = my_font2.render('Exit Game', True, (255, 0, 0)) 
                    else:
                        Exit_label = my_font2.render('Exit Game', True, (212,212,212))  # Khôi phục màu văn bản khi chuột rời đi
                        
                    
                elif ev.type == MOUSEBUTTONDOWN: #kích hoạt event khi click chuột
                    if text_rect1.collidepoint(ev.pos):
                        pygame.mixer.music.stop()
                        starting = False      #nếu chọn Start game thì nhạc sẽ dừng, kiểm soát hiển thị trên màn và chuyển tiếp vào select tank
                        thisStage = False           
                    if text_rect2.collidepoint(ev.pos):
                        pygame.mixer.music.stop()
                        run = False
                        starting = False
                        selecting = False
                        battling = False #nếu chọn exit game thì nhạc cũng dừng lại và đóng cửa sổ, kết thúc mọi trạng thái
                        end = False
                        thisStage = False
                    
         
                
            my_font2.set_bold(False) #tắt hiệu ứng gạch dưới
            my_font2.set_underline(False)
         

            screen.blit(screenPIC, (0,0))
            screen.blit(Title,(screen.get_width() / 4, screen.get_height() / 4) )  # căn giữa Tank2
            screen.blit(Title2, (screen.get_width() / 4, (screen.get_height() / 4)-20) )  # căn giữa Tank2P


            screen.blit(Start_label, text_rect1 )                 #tọa độ chuỗi Start Game
            screen.blit(Exit_label, text_rect2 )            #blit: viết nội dung lên screen
            pygame.display.flip()                          #cập nhật nội dung trên screen
            
            


def selectionScreen(thisStage):
    global currentPlayer
    global msg
    #shows menu, cửa sổ màn hình đầu tiên khi vào gaem
    '''
    Đoạn mã cần kiểm tra biến 'thisStage' trước khi thực thi một số chức năng như cập nhật lớp của "player tank" và gọi hàm readMap()
    để chuẩn bị cho trận chiến.
    '''
    global run, selecting, battling, end                    #biến toàn cục cho phép thay đổi trong phạm vi cục bộ của hàm
                                                            
    pygame.mixer.music.load(musicList[1])    # chỉ số [1] cho biết rằng nó đang tải bản nhạc thứ hai trong danh sách
    pygame.mixer.music.set_volume(0.4)      #mức âm lượng được set up ở mức 40%
    pygame.mixer.music.play(-1)              #phát nhạc mãi mãi, nếu hết nhạc thì phát lại tiếp
    
    global Opt1,Opt2                                  #Opt1 - Opt2 các cài đặt của player1 - player2
    
    

    
    Title = my_font3.render('Select Tank', True, (9,255,242))
    Title2 = my_font_title.render('Waiting for player', True, (9,255,242))

    # text_rect1 = Start_label.get_rect(center=((screen.get_width() / 3)+150, (screen.get_height() / 4)+250))

    # Lấy hình chữ nhật bao quanh văn bản
    Title_rect = Title.get_rect(center=((screen.get_width() / 2), (screen.get_height() / 4)))
    # Canh lề giữa cho văn bản
    # in văn bản lên màn hình
    screen.blit(Title, Title_rect)

    Guide1 = my_font_title2.render('Use W, A, S, D keys to move your tank', True,  (9,255,242))
    Guide2 = my_font_title2.render('W: Move Up', True,  (9,255,242))
    Guide3 = my_font_title2.render('A: Move Left', True,  (9,255,242))
    Guide4 = my_font_title2.render('S: Move Down', True,  (9,255,242))
    Guide5 = my_font_title2.render('D: Move Right', True,  (9,255,242))
    Guide6 = my_font_title2.render('Press R to shoot bullets towards your opponent.', True,  (9,255,242))



    p1Title = my_font_title2.render('Player 1', True, (255,255,0)) #chữ màu vàng nền trong suốt
    p2Title = my_font_title2.render('Player 2', True, (255,255,0))
    
    instruction = my_font4.render('Use your A or D controls to switch between tanks.', True, (255,255,0))
    instruction2 = my_font4.render('Press ENTER to start the battle !!!', True, (255,255,0))

    options = [imageUp_v1_2,imageUp_v2_2]                  #tạo danh sách chứa các ảnh của 2 phiên bản tank 
    stats = {0:['3', '6', '3'], 1:['6','3','1']}
    
    

   
            

    try:
        s.connect((host, port))
        print("Connected to :", host, ":", port)
        recvData = s.recv(2048 * 10)
        print("Receive from server: ", recvData.decode())
        bottomMsg = recvData.decode()
        if "1" in bottomMsg:
            currentPlayer = 1
            print( "You are player 1")
            Title2 = my_font_title.render('You are player 1', True, (255,255,0))
            screen.blit(Title2, (170, 120)) # tọa độ dòng chữ Select Tank

        else:
            currentPlayer =2
            print( "You are player 2")
            Title2 = my_font_title.render('You are player 2', True, (255,255,0))
            screen.blit(Title2, (170, 120)) # tọa độ dòng chữ Select Tank

            # s.close()
    except socket.error as e:
        Title2 = my_font_title.render('server error', True, (255,255,0))
        screen.blit(Title2, (170, 120)) # tọa độ dòng chữ Select Tank 

    create_thread(receive_msg)


    DisplaySurf = pygame.Surface((120,120))
    if currentPlayer == 1:
        DisplaySurf.fill((255,255,0))
    else:
        DisplaySurf.fill((255,212,255))                 #tạo ô nền cho tank
    DisplaySurf2 = pygame.Surface((120,120))
    if currentPlayer == 2:
        DisplaySurf2.fill((255,255,0))
    else:
        DisplaySurf2.fill((255,212,255))

    

    while thisStage:
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                selecting = False
                battling = False
                end = False
                thisStage = False
            elif ev.type == KEYDOWN:
                if ev.key == K_RETURN: #Khi nhấn phím ENTER, dừng âm nhạc, gọi hàm readMap() để tải bản đồ, sau đó gọi hàm player_classes() với Opt1 và player1, rồi Opt2 và player2; thiết lập selecting và thisStage thành False để chuyển sang giai đoạn khác.
                    pygame.mixer.music.stop()
                    readMap()
                    player_classes(Opt1, player1)
                    player_classes(Opt2, player2)
                    s.sendall("Play".encode('utf-8'))
                    selecting = False
                    thisStage = False

                if currentPlayer == 1:
                    if ev.key == K_a:
                        data = "A"+str(currentPlayer)
                        print("A")
                        # đối với player1 sử dụng phím A or D để lựa chọn tank
                        if Opt1 == 0:
                            Opt1 = 1                                   
                        else:
                            Opt1 -= 1
                        s.sendall(data.encode('utf-8'))
                    elif ev.key == K_d:
                        print("D")
                        
                        data = "D"+str(currentPlayer)
                        if Opt1 == 1:
                            Opt1 = 0
                        else:
                            Opt1 += 1
                        s.sendall(data.encode('utf-8'))
                else :
                    if ev.key == K_a:
                        print("A")
                        data = "A"+str(currentPlayer)
                        # đối với player2 sử dụng phím A or D để lựa chọn tank
                        if Opt2 == 0:
                            Opt2 = 1                                   
                        else:
                            Opt2 -= 1
                        s.sendall(data.encode('utf-8'))
                    elif ev.key == K_d:
                        print("D")
                        data = "D"+str(currentPlayer)
                        if Opt2 == 1:
                            Opt2 = 0
                        else:
                            Opt2 += 1
                        s.sendall(data.encode('utf-8'))

            
        if "A" in msg:
                if currentPlayer == 1:
                    print("Player "+ str(currentPlayer)+" di chuyen ",msg )
                    if Opt2 == 0:
                            Opt2 = 1                                   
                    else:
                        Opt2 -= 1
                    msg = ""
                else:
                    print("Player "+ str(currentPlayer)+" di chuyen ",msg )
                    if Opt1 == 0:
                            Opt1 = 1                                   
                    else:
                        Opt1 -= 1
                    msg = ""
        if "D" in msg:
                if currentPlayer == 1:
                    print("Player "+ str(currentPlayer)+" di chuyen ",msg )
                    if Opt2 == 1:
                            Opt2 = 0
                    else:
                        Opt2 += 1
                    msg = ""
                else:
                    print("Player "+ str(currentPlayer)+" di chuyen ",msg )
                    if Opt1 == 1:
                            Opt1 = 0
                    else:
                        Opt1 += 1
                    msg = ""
        if "Play" in msg:
                pygame.mixer.music.stop()
                readMap()
                player_classes(Opt1, player1)
                player_classes(Opt2, player2)
                selecting = False
                thisStage = False

                
                


        
        p1statsHealth = my_font_title2.render('Health: ' + stats[Opt1][0], True, (255,212,212))
        p1statsSpeed = my_font_title2.render('Speed: ' + stats[Opt1][1],True, (255,212,212))
        p1statsReload = my_font_title2.render('Reload: ' + stats[Opt1][2], True, (255,212,212))   #these renders needs to be in the loop because as users switch
        p2statsHealth = my_font_title2.render('Health: ' + stats[Opt2][0], True, (255,212,212))   #between tanks, the stats info needs to update
        p2statsSpeed = my_font_title2.render('Speed: ' + stats[Opt2][1],True, (255,212,212))
        p2statsReload = my_font_title2.render('Reload: ' + stats[Opt2][2], True, (255,212,212))
        
        screen.blit(screenPIC, (0,0))
        screen.blit(Title, (370, 70)) # tọa độ dòng chữ Select Tank
        screen.blit(Title2, (370, 120)) # tọa độ dòng chữ Select Tank

        screen.blit(p1Title, (330, 170))
        screen.blit(p2Title, (590, 170))

        screen.blit(p1statsHealth, (225,220)) 
        screen.blit(p1statsSpeed, (225,240))  
        screen.blit(p1statsReload, (225,260)) 

        screen.blit(p2statsHealth, (750,220)) #tọa độ chỉ số máu của player2
        screen.blit(p2statsSpeed, (750,240)) #tọa độ chỉ tốc độ của player2
        screen.blit(p2statsReload, (750,260)) #tọa độ chỉ số tốc độ bắn của player2

        screen.blit(DisplaySurf, (335, 209))  #tọa độ ô trắng
        screen.blit(DisplaySurf2, (590, 209))
        screen.blit(options[Opt1], (370, 240)) # tọa độ hình tank trong ô màu trắng
        screen.blit(options[Opt2], (625, 240))

        # screen.blit(instructionP1, (270, 310))
        # screen.blit(instructionP2, (530, 310))
        screen.blit(Guide1, (330, 350))
        screen.blit(Guide2, (360, 370))
        screen.blit(Guide3, (360, 390))
        screen.blit(Guide4, (360, 410))
        screen.blit(Guide5, (360, 430))
        screen.blit(Guide6, (330, 450))





        screen.blit(instruction, (300, 520)) #tọa độ của dòng chữ "Use your left and right controls..."
        screen.blit(instruction2, (370, 540))
        pygame.display.flip()

################################# SET UP TRẬN ĐẤU ########################################################################
import math
# Hàm tính khoảng cách giữa hai điểm
def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def battleScreen(thisStage):

    '''
    quản lý màn hình chiến đấu trong game bằng cách xử lý các sự kiện, di chuyển, 
    cập nhật trạng thái đạn, xử lý va chạm, và hiển thị các đối tượng trên màn hình, kết thúc trò chơi khi người chơi hết máu.
    '''
    global run, end         #biến cục bộ sẽ update các thay đổi của function
    pygame.mixer.music.load(musicList[2])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

    p1 = my_font_title2.render('Player 1', True,  (9,255,242))
    p2 = my_font_title2.render('Player 2', True,  (9,255,242))


    
    global msg
    timer = 0  #Khởi tạo biến đếm để điều chỉnh thời gian nghỉ giữa các lần bắn của người chơi
    timer2 = 0
    msg = ""

    def updatePlayer(player):
        global msg
        if msg =="": return
        if "LEFT" in msg:
            data = msg.split("LEFT")
            for i in range(len(data)-1):
                player.rect.left -= player.speed# Di chuyển sprite sang trái theo tốc độ đã định
                player.direction = 'left' # Cập nhật hướng di chuyển của sprite
                player.image = player.pics[3] # Cập nhật hình ảnh của sprite khi người chơi hướng di chuyển sang trái
                players.draw(screen)
                pygame.display.update()
            if data[len(data)-1].isdigit():
                if player.rect.left!= int(data[len(data)-1]):
                    player.rect.left = int(data[len(data)-1])
               
            msg = ""
            players.draw(screen)
            pygame.display.update()

        elif "RIGHT" in msg:
            data = msg.split("RIGHT")
            for i in range(len(data)-1):
                player.rect.left += player.speed
                player.direction = 'right'
                player.image = player.pics[2]
                
            if data[len(data)-1].isdigit():
                if player.rect.left!= int(data[len(data)-1]):
                    player.rect.left = int(data[len(data)-1])
            msg = ""
            players.draw(screen)
            pygame.display.update()
           

        elif "UP" in msg:
            data = msg.split("UP")
            for i in range(len(data)-1):
                player.rect.top -= player.speed
                player.direction = 'up'
                player.image = player.pics[0]
                players.draw(screen)
            if data[len(data)-1].isdigit():
                print("Top" + str(player.rect.top))
                if player.rect.top!= int(data[len(data)-1]):
                    player.rect.top = int(data[len(data)-1])
            msg = ""
            players.draw(screen)
            pygame.display.update()
        elif "DOWN" in msg:
            data = msg.split("DOWN")
            for i in range(len(data)-1):
                player.rect.top += player.speed
                player.direction = 'down'
                player.image = player.pics[1]
                players.draw(screen)
                pygame.display.update()
            if data[len(data)-1].isdigit():
                print("Top" + str(player.rect.top))
                if player.rect.top!= int(data[len(data)-1]):
                    player.rect.top = int(data[len(data)-1])
            msg = ""
            players.draw(screen)
            pygame.display.update()


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
   

    while thisStage:
        fps = clock.tick(30)  #điều chỉnh fps giúp game mượt hơn      
        timer += 1  #Mỗi vòng lặp, timer và timer2 tăng lên 1, giúp đếm số lần lặp xảy ra và có thể dùng để kiểm soát thời gian nghỉ giữa các lần bắn
        timer2 += 1
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                s.close()

                battling = False
                thisStage = False
                end = False

    
       

        if currentPlayer == 1:
            movement(player1)
        else:
            movement(player2)

        # xử lý di chuyển, va chạm (p1-p2-tường)
        # movement(player2) 
        bullet_update()
        key = pygame.key.get_pressed() #kiêmr tra các phím được nhấn


        #Khi người chơi nhấn phím bắn sau hết thời gian cooldown của lần bắn trước, hệ thống sẽ phát âm thanh bắn và tạo viên đạn mới cho người chơi đó
        #Bộ đếm thời gian (timer cho người chơi 1 và timer2 cho người chơi 2) sẽ được đặt lại về 0 để chuẩn bị cho lần bắn tiếp theo

        if currentPlayer == 1:
            if key[player1.keys[4]]:
                if timer >= player1.cooldown:  
                    shoot.play()
                    bullet(player1)
                    timer = 0
                    s.sendall("SHOT".encode('utf-8'))
           
        else:
            if key[player2.keys[4]]:
                if timer2 >= player2.cooldown:
                    shoot.play()
                    bullet(player2)
                    timer2 = 0
                    s.sendall("SHOT".encode('utf-8'))
            



        # if key[player2.keys[4]]:
        #     if timer2 >= player2.cooldown:
        #         shoot.play()
        #         bullet(player2)
        #         timer2 = 0
                
        

        for bullets in bulletgroup: 
            
            if pygame.sprite.collide_rect(bullets,player1): #check viên đạn có trúng p1 không
                bulletgroup.remove(bullets)
                player1.health -= 1
                explode.play() #phát âm thanh vuno
                screen.blit(explosion, player1.rect) #in hình ảnh vuno tại vị trí p1
                pygame.display.flip() #update screen để hiển thị hình ảnh vuno
                time.sleep(1) 

                # Tìm vị trí respawn cách xa player2 nhất, để lúc random lại vị trí nó không đứng gần player cũ
                farthest_point = max(spawnpoints, key=lambda point: distance(point, player2.rect.center))
                player1.rect.center = farthest_point
        
                
            if pygame.sprite.collide_rect(bullets,player2):
                bulletgroup.remove(bullets)
                player2.health -= 1
                explode.play()
                screen.blit(explosion, player2.rect)
                pygame.display.flip()
                time.sleep(1)

                # Tìm vị trí respawn cách xa player1 nhất
                farthest_point = max(spawnpoints, key=lambda point: distance(point, player1.rect.center))
                player2.rect.center = farthest_point

            if pygame.sprite.spritecollide(bullets,walls,False):
                explode.play()
                bulletgroup.remove(bullets)
            if len(pygame.sprite.spritecollide(bullets,bulletgroup, False))>1:
                pygame.sprite.spritecollide(bullets,bulletgroup, True)


        if currentPlayer ==1: updatePlayer(player2)
        else: updatePlayer(player1)
        if "SHOT" in msg:
            if currentPlayer == 1:
                msg = ""
                shoot.play()
                bullet(player2)
                timer2 = 0
            else:
                msg = ""
                shoot.play()
                bullet(player1)
                timer1 = 0
            
        
        screen.blit(background, (0,0)) #in background đè lên toàn bộ screen
        screen.blit(p1, (700, 80))
        screen.blit(p2, (700, 250))
        if Opt1 == 0:
            screen.blit(imageUp_v1_2, (700, 110))
        else :
            screen.blit(imageUp_v2_2, (700, 110))
        if Opt2 == 0:
            screen.blit(imageUp_v1_2, (700, 280))
        else :
            screen.blit(imageUp_v2_2, (700, 280))

        walls.draw(screen)
        players.draw(screen)
        bulletgroup.draw(screen) #các viên đạn được bắn ra
        drawPlayerHealth(player1)
        drawPlayerHealth(player2)
        pygame.display.flip()
        pygame.display.update()
        
        if player1.health == 0 or player2.health == 0: #nếu 1 trong 2 player hết sạch máu thì kết thúc trò chơi,màn hình kết thúc sẽ hiển thị kết quả tỉ số
            pygame.mixer.music.stop()
            battling = False
            thisStage = False
            endScreen(end)
            

########################### SET UP MÀN HÌNH CUỐI - KHI TRẬN CHIẾN KẾT THÚC  ###########################################################            
def endScreen(thisStage): 
    '''
    xác định người chiến thắng, tính điểm, hiển thị màn hình kết thúc và kết thúc trò chơi. 
    '''
    global run, starting, selecting

    pygame.mixer.music.load(musicList[3])    
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    bulletgroup.empty()     
    walls.empty()               
    
    #đọc từng dòng của tệp tin và tách dữ liệu bằng dấu phẩy (,) để lấy ra thông tin điểm số
    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'r')
    for l in scores:
        dataFields = l.split(':')
        dataFields[-1] = dataFields[-1].strip('\n')
        scoredata[dataFields[0]] = int(dataFields[1]) #dictionary chứa các điểm số, key là thông tin được đọc từ tệp và value được chuyển thành số nguyên              
    scores.close()
    
    winner = max(player1.health,player2.health)   #người chơi nào hết sạch máu sau trận chiến thì người đó thua
    if winner == player1.health:
            WinnerTitle =  my_font2.render('PLAYER 1 WINS', True, (255,255,0))
            scoredata['Player1'] +=1                    # =1 điểm cho người chơi thắng                              
    else:
            WinnerTitle = my_font2.render('PLAYER 2 WINS', True, (255,255,0))
            scoredata['Player2'] +=1

    # mở tệp trong chế độ ghi (mode 'w': write), ghi điểm số được cập nhật của cả hai người chơi và sau đó đóng tệp.
    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'w')
    scores.write('Player1,' + str(scoredata['Player1']) + '\n')         
    scores.write('Player2,' + str(scoredata['Player2']) + '\n')
    scores.close()
            
    Title = my_font3.render('END OF THE MATCH', True, (255,0,0))
    scoreTitle = my_font2.render('Scores', True, (255,212,255))
    instruction = my_font4.render('Press R to reset scores!', True, (255,255,0))
    instruction2 = my_font4.render('Press ENTER to return to game menu.', True, (255,255,0))

    while thisStage:
        p1Scores = my_font2.render('Player 1: ' +str(scoredata['Player1']), True, (9,255,212))
        p2Scores = my_font2.render('Player 2: '+ str(scoredata['Player2']), True, (9,255,212))
        #set up tọa độ vị trí căn lề cho các text
        screen.blit(screenPIC, (0,0))
        screen.blit(Title, (60,50))
        screen.blit(WinnerTitle, (145,200))
        screen.blit(scoreTitle, (240,280))
        screen.blit(p1Scores, (50,340))
        screen.blit(p2Scores, (340,340))
        screen.blit(instruction, (210, 480))
        screen.blit(instruction2, (150,500))
        pygame.display.flip()
        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.mixer.music.stop()
                run = False
                end = False
                thisStage = False
            elif ev.type == KEYDOWN:
                if ev.key == K_RETURN:
                    pygame.mixer.music.stop()
                    thisStage = False
                elif ev.key == K_r:
                    scoredata['Player1'] = 0        #nhấn phím R để reset bảng điểm
                    scoredata['Player2'] = 0

    scores = open('ProJect_Pygame_Nhom18/BangBang/Tank2P/BangTinhDiem.txt', 'w')
    scores.write('Player1: ' + str(scoredata['Player1']) + '\n')
    scores.write('Player2: ' + str(scoredata['Player2']) + '\n')         #update kết quả trong fie txt
    scores.close()
        
    starting = True
    selecting = True
    
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048) #set up chất lựơng âm thanh
clock = pygame.time.Clock() #điều chỉnh tốc độ của trò chơi, thời gian chờ,...

colours = pygame.color.THECOLORS # dictionary chứa màu sắc tiêu chuẩn của Pygame
my_font = pygame.font.SysFont('Verdana', 100)
my_font2 = pygame.font.SysFont('moolboran', 66)
my_font3 = pygame.font.SysFont('andalus', 72)      #setup Font chữ
my_font4 = pygame.font.SysFont('candara', 20)
my_font5 = pygame.font.SysFont('arial', 16)

my_font_title = pygame.font.SysFont('moolboran', 50)
my_font_title2 = pygame.font.SysFont('moolboran', 30)



size = (960, 600) #kích thước cửa sổ game
screen = pygame.display.set_mode(size)
screenPIC = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/anhnen.png')
screenPIC = pygame.transform.scale(screenPIC, size)
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
imageUp_v1 = pygame.transform.scale(imageUp_v1, (30, 30))
imageUp_v1_2 = pygame.transform.scale(imageUp_v1, (50, 50))

imageDown_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 down.png')
imageDown_v1 = pygame.transform.scale(imageDown_v1, (30, 30))
imageRight_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 right.png')
imageRight_v1 = pygame.transform.scale(imageRight_v1, (30, 30))
     #load ảnh khi tank thay đổi hướng khi di chuyển
imageLeft_v1 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank1 left.png')
imageLeft_v1 = pygame.transform.scale(imageLeft_v1, (30, 30))


imageUp_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 up.png')
imageUp_v2 = pygame.transform.scale(imageUp_v2, (30, 30))
imageUp_v2_2 = pygame.transform.scale(imageUp_v2, (50, 50))

imageDown_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 down.png')
imageDown_v2 = pygame.transform.scale(imageDown_v2, (30, 30))
imageRight_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 right.png')
imageRight_v2 = pygame.transform.scale(imageRight_v2, (30, 30))
imageLeft_v2 = pygame.image.load('ProJect_Pygame_Nhom18/BangBang/Tank2P/picture/tank2 left.png')
imageLeft_v2 = pygame.transform.scale(imageLeft_v2, (30, 30))


#Hai danh sách chứa hình ảnh đại diện cho các version khác nhau của người chơi và các nhiều hướng khác nhau
ver1 = [imageUp_v1,imageDown_v1,imageRight_v1,imageLeft_v1]
ver2 = [imageUp_v2,imageDown_v2,imageRight_v2,imageLeft_v2]
spawnpoints = [(30,30),(40,390),(560,130),(560,390)]  #List chứa các cặp tuple, mỗi tuple là một điểm xuất phát của viên đạn trên màn hình.              


players = pygame.sprite.Group()
#Tạo hai đối tượng người chơi là các sprite có hình chữ nhật xác định vị trí và kích thước, hướng di chuyển trên màn hình
player1 = pygame.sprite.Sprite()
player1.rect = pygame.Rect((20, 20),(24,24))                        
player1.direction = 'up'                                            
player1.keys = (K_a, K_d, K_w, K_s,K_r)    # Player 1 sử dụng phím W A S D để di chuyển và phím bắn đạn là phím 4                   

player2 = pygame.sprite.Sprite()
player2.rect = pygame.Rect((560, 390), (24,24))
player2.direction = 'up'
player2.keys = (K_a, K_d, K_w, K_s,K_r) # Player 2 sử dụng phím LEFT RIGHT UP DOWN để di chuyển và phím bắn đạn là phím l

players.add(player1) #phương thức add thêm player 1 & 2 vào nhóm player
players.add(player2)

bulletgroup = pygame.sprite.Group()
walls = pygame.sprite.Group()                       

            
run = True
starting = True                     
selecting = True
battling = True
end = True


writeScorefile() #ghi điểm số ra tệp txt
scoredata = {} #Khởi tạo một dictionary rỗng để ưu trữ dữ liệu điểm số

while run:
    fps = clock.tick(30)

    gameMenu(starting) # hàm hiển thị menu trò chơi khi trò chơi bắt đầu
    selectionScreen(selecting) #hiển thị màn hình chọn tank 
    battleScreen(battling)
    
   

pygame.display.quit()
quit()

