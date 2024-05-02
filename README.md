Nhắc đến trò chơi điện tử (hay game), chắc chắn không ai xa lạ với thuật ngữ này, đây là thứ gắn liền với tuổi thơ của biết bao thế hệ, gắn bó với mọi người, chắc chắn ai cũng từng chơi qua một lần. Dạng sơ khai nhất của game chính là các trò chơi như cờ caro được chơi trên giấy, cờ vua, cờ tướng,... Hiện nay trò chơi đã được nâng lên một tầm cao mới, từ khi công nghệ cũng như internet phát triển, các lập trình viên đã mô hình hóa và đưa thành công nó lên các nền tảng thiết bị điện tử. Ngày nay trò chơi điện tử đã không ngừng được cải thiện lối chơi, đồ họa, các thể loại ngày càng hấp dẫn, thu hút đông đảo giới trẻ yêu thích. Khi nói đến game thì nhiều người thường nghĩ rằng nó là một thứ vô bổ, lãng phí thời gian, ảnh hưởng đến health và học tập. Và dĩ nhiên ở chiều ngược lại, các nhà khoa học đã chứng minh rằng, nếu chơi game điều độ, có chừng mực thì sẽ giúp nhóm em xả stress sau những giờ học tập và làm việc căng thẳng, và đối với một số tựa game như Minecraft, Lego còn khiến nhóm em rèn luyện khả năng tư duy sáng tạo cho trẻ.

Trong thế giới hỗn loạn và đầy cạnh tranh này, chào mừng bạn đến với đấu trường PvP hoành tráng, nơi kỹ năng, chiến lược và lòng dũng cảm sẽ được thử thách đến cùng cực. Hãy sẵn sàng đọ sức với những đối thủ ngang tài ngang sức, chứng minh bản lĩnh và vươn lên dẫn đầu bảng xếp hạng. Với nhiều chế độ chơi đa dạng, từ đấu đội 5v5 căng thẳng đến đấu đơn 1v1 gay cấn, tựa game tank  PvP của nhóm mình mang đến trải nxuấtệm chơi game đỉnh cao cho mọi game thủ. Tùy chỉnh nhân vật của bạn, trang bị cho họ những vũ khí và áo giáp mạnh mẽ nhất, và bước vào đấu trường để chiến đấu vì vinh quang và phần thưởng. Cho dù bạn là một chiến binh dày dạn kinh nxuấtệm hay một tân binh háo hức, đấu trường PvP luôn chào đón bạn. Hãy rèn luyện kỹ năng của mình, lập nhóm với bạn bè và chứng minh rằng bạn có những gì cần thiết để trở thành nhà vô địch tối thượng.

Tham gia ngay vào tựa game PvP của nhóm mình và trải nxuấtệm cảm giác hồi hộp khi chiến đấu với những người chơi khác trong thời gian thực. Vinh quang đang chờ đón những người dũng cảm nhất. Hãy sẵn sàng cho trận chiến và chứng minh sức mạnh của bạn!

Web Demo: https://thanhvu2702.github.io/web_intro_ProJ_Pygame/

Tài liệu & source LATEX: 

https://github.com/ThanhVu2702/Tank_PvP_Pygame/blob/main/ProJect_Pygame_Nhom18/BangBang/document/BaoCao_Nhom18.pdf

https://github.com/ThanhVu2702/Tank_PvP_Pygame/blob/main/ProJect_Pygame_Nhom18/BangBang/document/BaoCao_Nhom18.zip

 
Install instruction & extension for VSCode:

dowload VSCode: https://code.visualstudio.com/download

dowload python: https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe

Install pip in terminal for VSCode:
--------------------

pip install PyQt5

pip install pgzrun

pip install pygame

pip install pgzero

--------------------

Extension for VSCode:

--------------------

pygame (pygame Snippets)

python

pylance

python Debugger

---------------------

Nhóm quyết định phân chia từng phần của trò chơi thành các hàm riêng biệt do dự án có quy mô khá lớn. Phương pháp này giúp việc giải thích và ghi chú trở nên dễ dàng hơn. Dưới đây là một mô tả tổng quan về pseudocode của trò chơi của chúng tôi. Thông qua việc sử dụng pseudocode và phân chia trò chơi thành các hàm riêng biệt, chúng tôi hy vọng rằng việc hiểu và duy trì mã nguồn của trò chơi sẽ dễ dàng hơn, đồng thời cũng giúp tối ưu hóa quá trình phát triển.

Quá trình chuẩn bị cho trò chơi bắt đầu bằng việc import thư viện pygame, khởi động Pygame, thiết lập Pygame Mixer cho âm thanh, khởi tạo màu sắc và biến font. Sau đó, tạo cửa sổ trò chơi, thiết kế hình nền, nạp âm thanh, hình ảnh bản đồ và xe tăng, đặt điểm xuất hiện xe tăng, tạo nhóm người chơi, nhân vật, thêm xe tăng, quản lý tường và viên đạn, và cuối cùng đặt biến điều khiển cho hàm và vòng lặp trong trò chơi.

Sẽ ghi điểm vào file điểm khi có, thiết lập số khung hình trên giây để chạy mượt mà, gọi hàm menu để hiển thị giao diện người chơi và xử lý sự kiện chuột. Khi người dùng chọn "chơi trò chơi", hàm menu sẽ kết thúc và dừng phát nhạc nền. Khi chọn "thoát trò chơi", hàm menu sẽ kết thúc, đặt giá trị false cho biến điều khiển và dừng phát nhạc.

Tải và phát nhạc nền khi call màn hình lựa chọn xe tăng, hiển thị tên các mục lựa chọn và hình ảnh, yêu cầu người chơi sử dụng phím điều khiển để chuyển đổi xe tăng. Khi người chơi nhấn Enter, xác nhận xe tăng được chọn và cập nhật thông số. Sau đó, chọn bản đồ và kết thúc hàm lựa chọn. Nếu người chơi thoát, hàm sẽ kết thúc và dừng phát nhạc.

Hẹn giờ cho việc bắn đạn khi màn hình chiến đấu được kích hoạt, sau đó nạp và phát nhạc nền. Trong vòng lặp, họ di chuyển người chơi, xử lý việc bắn đạn và đóng cửa sổ trò chơi. Duyệt qua đạn để xử lý va chạm và hiển thị trạng thái trên màn hình. Khi sức khỏe của người chơi giảm về 0, kết thúc trò chơi và dừng nhạc nền.

Sẽ tải và phát nhạc nền khi hàm kết thúc trò chơi được gọi, sau đó cập nhật điểm số từ tệp và xác định người chiến thắng. Người chiến thắng sẽ được cộng thêm một điểm và điểm số mới sẽ được ghi lại. Tiêu đề kết quả sẽ được hiển thị trên màn hình và trong vòng lặp, điểm số sẽ được hiển thị và xử lý sự kiện như dừng phát nhạc, thiết lập lại điểm số hoặc kết thúc trò chơi sẽ được thực hiện.

Cụ thể như sau:

*******************************************************************************************************************************
Import các thư viện cần thiết:
Đầu tiên, chúng ta sẽ bắt đầu bằng việc import các thư viện cần thiết cho trò chơi, bao gồm pygame, random, và time.

Khởi động Pygame:
Sau đó, chúng ta cần khởi động Pygame để chuẩn bị cho việc chạy trò chơi.

Thiết lập Pygame Mixer:
Chúng ta cần thiết lập Pygame Mixer để có thể phát âm thanh và nhạc nền trong trò chơi.
Khởi tạo màu sắc:

Tiếp theo, chúng ta sẽ khởi tạo các biến để chứa màu sắc, giúp cho việc thiết kế giao diện trở nên đẹp mắt hơn.
Tạo biến font:

Để vẽ chữ trên màn hình, chúng ta cần tạo một biến font sử dụng trong trò chơi.

Tạo cửa sổ hiển thị trò chơi:
Chúng ta cần tạo một cửa sổ hiển thị cho trò chơi, nơi mà tất cả các hành động sẽ diễn ra.

Thiết kế hình nền:
Hãy thiết kế một hình nền hấp dẫn để tạo nên không gian trò chơi sống động.
Nạp tệp âm thanh và đặt chúng vào danh sách:

Tiếp theo, chúng ta sẽ nạp các tệp âm thanh như tiếng súng, tiếng nổ vào trong trò chơi và đặt chúng vào danh sách để sử dụng sau này.
Nạp ảnh bản đồ và tạo một danh sách bản đồ:

Chúng ta cần nạp các hình ảnh bản đồ khác nhau và tạo một danh sách để chọn lựa trong quá trình chơi.
Nạp hình ảnh xe tăng và xếp chúng vào danh sách:

Tiếp theo, chúng ta cần nạp các hình ảnh của các loại xe tăng và sắp xếp chúng vào danh sách để sử dụng.

Tạo điểm xuất hiện của xe tăng:
Chúng ta cần đặt các điểm xuất hiện của các xe tăng trong trò chơi để chúng xuất hiện một cách tự nhiên.

Tạo nhóm người chơi:
Tạo một nhóm chứa các nhân vật người chơi để quản lý và điều khiển chúng trong trò chơi.
Tạo nhân vật và đặc tính cố định:

Tiếp theo, chúng ta cần tạo các nhân vật trong trò chơi cùng với các đặc tính cố định như hướng di chuyển, điều khiển và hình dạng.
Thêm xe tăng vào nhóm người chơi:
Sau đó, chúng ta thêm các xe tăng vào nhóm người chơi để chúng tham gia vào trò chơi.
Tạo các nhóm cho tường và viên đạn:

Cuối cùng, chúng ta cần tạo các nhóm để quản lý tường và set up bullet trong trò chơi, giúp việc xử lý và va chạm trở nên dễ dàng hơn.

Đặt các biến điều khiển:
Cuối cùng, hãy đặt các biến cần thiết để điều khiển các hàm và vòng lặp trong trò chơi, giúp cho quá trình phát triển và kiểm soát trở nên thuận tiện hơn.

*******************************************************************************************************************************************************
Nếu có lưu điểm, chúng ta sẽ ghi vào file điểm.
Trong khi vòng lặp chính của trò chơi đang chạy:

Thiết lập số khung hình trên giây (30fps):
Trước tiên, chúng ta cần thiết lập số khung hình trên giây để đảm bảo trò chơi chạy mượt mà.

Gọi hàm menu của trò chơi:
Khi đó, chúng ta sẽ gọi hàm menu để hiển thị giao diện người dùng cho người chơi.
Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Tải và phát nhạc nền phù hợp từ danh sách nhạc đã chuẩn bị.
Hiển thị tiêu đề trên màn hình.
Bắt đầu một vòng lặp không giới hạn để xử lý các sự kiện của người chơi.
Trong vòng lặp này, chúng ta sẽ:
Hiển thị hình ảnh và tiêu đề cho menu.
Theo dõi vị trí của con chuột và lưu vào biến.
Xử lý mọi sự kiện diễn ra, bao gồm:
Đánh dấu tiêu đề "chơi trò chơi" nếu con chuột di chuyển đến đó.
Đánh dấu tiêu đề "thoát trò chơi" nếu con chuột di chuyển đến đó.

Khi người dùng nhấn vào tiêu đề "chơi trò chơi":
Kết thúc hàm menu.
Dừng phát nhạc nền.
Khi người dùng chọn "thoát trò chơi" hoặc đóng cửa sổ trò chơi:
Kết thúc hàm menu và đặt giá trị false cho tất cả các biến điều khiển các hàm và vòng lặp chính.
Dừng phát nhạc.

********************************************************************************************************************************************************
Khi call màn hình lựa chọn xe tăng:

Tải và phát nhạc nền:
Trước tiên, chúng ta cần tải và phát nhạc nền để tạo không khí soi dong cho màn hình lựa chọn.

Hiển thị tên các mục lựa chọn lên màn hình:
Sau đó, chúng ta sẽ hiển thị tên các mục lựa chọn như xe tăng để người chơi có thể chọn.
Trong một vòng lặp:

Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Hiển thị hình ảnh và tên của các mục lựa chọn, tức là các loại xe tăng.
Yêu cầu người chơi sử dụng phím điều khiển trái và phải để di chuyển qua lại giữa các xe tăng.
Nếu người chơi nhấn phím trái hoặc phải:
Thay đổi hình ảnh và thông số kỹ thuật của xe tăng hiện tại  (health, speed, reload)

Nếu người chơi nhấn phím Enter:
Xác nhận mẫu xe tăng được hiển thị là lựa chọn của người chơi.
Cập nhật các thuộc tính có thể thay đổi cho xe tăng như sức khỏe, tốc độ di chuyển, thời gian nạp đạn.
Lựa chọn một bản đồ từ danh sách các bản đồ đã chuẩn bị sẵn.
Kết thúc hàm lựa chọn và ngừng phát nhạc nền.

Nếu người chơi thoát khỏi trò chơi:
Kết thúc hàm và đặt giá trị sai cho tất cả các biến điều khiển chức năng và vòng lặp chính.
Ngừng phát nhạc.

**********************************************************************************************************************************************************
Khi màn hình chiến đấu được kích hoạt:

Hẹn giờ cho việc bắn đạn:
Đầu tiên, chúng ta cần hẹn giờ cho việc bắn đạn để đảm bảo rằng người chơi không thể bắn đạn liên tục.

Nạp và phát nhạc nền:
Sau đó, chúng ta cần nạp và phát nhạc nền để tạo không khí kịch tính trong trận đấu.

Bắt đầu vòng lặp liên tục:

Trong quá trình này, chúng ta sẽ thực hiện các hành động sau:
Gọi hàm để di chuyển người chơi.
Xử lý các sự kiện đang diễn ra:
Nếu người chơi bắn ra đạn:
Tạo một đạn mới và thêm vào nhóm đạn.
Phát ra âm thanh của việc bắn đạn.

Nếu người chơi đóng cửa sổ trò chơi:
Kết thúc hàm và đặt giá trị 'sai' cho các biến điều khiển các hàm và vòng lặp khác.
Dừng phát nhạc nền.
Kết thúc trò chơi.

Duyệt qua từng viên đạn trong nhóm đạn:
Nếu đạn trúng người chơi:
Phát âm thanh vụ nổ.
Giảm sức khỏe của người chơi.
Xác định vị trí xuất hiện lại của người chơi.

Nếu đạn va chạm vào đạn khác:
Loại bỏ cả hai viên đạn ra khỏi trò chơi.
Phát âm thanh vụ nổ.

Nếu đạn bắn trúng tường:
Loại bỏ viên đạn đó.
Phát âm thanh vụ nổ.

Hiển thị nền, bản đồ, người chơi và đạn lên màn hình.
Nếu sức khỏe của một người chơi giảm về 0:
Kết thúc hàm này.
Gọi hàm kết thúc trò chơi.
Ngừng phát nhạc nền.

*********************************************************************************************************
Khi hàm kết thúc trò chơi được gọi:

Tải và phát nhạc nền:
Đầu tiên, chúng ta cần tải và phát nhạc nền để tạo không khí phù hợp cho màn hình kết thúc trò chơi.

update điểm số từ tệp:
Sau đó, chúng ta sẽ đọc điểm số từ tệp và lưu trữ vào một từ điển để dễ quản lý.

Kiểm tra và xác định người chiến thắng:
Chúng ta cần kiểm tra và xác định người chiến thắng dựa trên điểm số của họ.
Cộng điểm cho người thắng cuộc:

Người thắng cuộc sẽ được cộng thêm một điểm vào điểm số hiện có của họ.

Ghi lại điểm số mới vào tệp và cập nhật từ điển:
Chúng ta cần ghi lại điểm số mới vào tệp và cập nhật từ điển để lưu trữ thông tin mới nhất.
Hiển thị tiêu đề lên màn hình:

Sau đó, chúng ta sẽ hiển thị tiêu đề lên màn hình để thông báo kết quả của trận đấu.
Tiếp tục trong một vòng lặp không kết thúc:

Trong vòng lặp này, chúng ta sẽ thực hiện các hành động sau:
Hiển thị điểm số của các người chơi.
Hiển thị hình nền, tiêu đề và điểm số lên màn hình.
Xử lý các sự kiện đang diễn ra:
Nếu người chơi nhấn phím Enter:
Dừng phát nhạc nền.
Kết thúc hàm và làm mới các biến và thống kê cuối cùng của hàm, và viết lại điểm số.
Nếu người chơi nhấn phím R:
Thiết lập lại điểm số.
Nếu người chơi đóng chương trình:
Dừng phát nhạc nền.
Kết thúc hàm và trò chơi kết thúc.

*********************************************************************************************************
