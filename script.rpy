# The script of the game goes in this file.

#define narrator = Character(None, what_textalign=0,  what_size = 27,  what_font = "MotoyaLMaru.ttf", what_layout='greedy', window_background = None)

init python:
    config.gl_resize=False
    config.save_physical_size=False
    #style.window.left_margin = 0
    #style.window.background = Image("images/SMW11D.png", xalign=0.5, yalign=1.0)
    extension = "mkv"
    ogv_files = ["BG21A", "BG30" , "BG31" , "BG32"]
    def mov_path(m):
        if m in ogv_files:
            m = "images/movie/ogv/"+m+".ogv"
            return m
        else:
            m = "images/movie/"+extension+"/"+m+"."+extension
            return m

    def cut_scene(m):
        m = "images/movie/"+extension+"/"+m+"."+extension
        renpy.movie_cutscene(m)

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos 128 #gui.dialogue_xpos
    xsize 1024 #gui.dialogue_width
    ypos -160 #gui.dialogue_ypos
    ysize 0
    line_spacing 10
    adjust_spacing False
style window:
    xalign 0.5
    xfill True
    ypos 720
    yalign 0 #gui.textbox_yalign
    ysize gui.textbox_height
style say_dialogue is default
style window is default

define fade = Fade(1, 0.2, 1)
    
image bg21a =  Movie(play=mov_path("BG21A"))
#image bg30 =  Movie(play=mov_path("BG30"), loop=False)

image bg30:
    Movie(play=mov_path("BG30"), loop=False)
    pause 15.0           # A delay to get to the end of the movie
    Image("images/movie/BG30_omv.png")
    
image bg31 =  Movie(play=mov_path("BG31"))
image bg32 =  Movie(play=mov_path("BG32"))

image yumemi_pos1:
    Movie(play=mov_path("yumemi1"), loop=False)
    pause 6.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi1.png")
    
image yumemi_pos2:
    Movie(play=mov_path("yumemi2"), loop=False)
    pause 5.6            # A delay to get to the end of the movie
    Image("images/movie/yumemi2.png")

image yumemi_pos3:
    Movie(play=mov_path("yumemi3"), loop=False)
    pause 6.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi3.png")

image yumemi_pos4:
    Movie(play=mov_path("yumemi4"), loop=False)
    pause 5.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi4.png")

image yumemi_pos5:
    Movie(play=mov_path("yumemi5"), loop=False)
    pause 5.0          # A delay to get to the end of the movie
    Image("images/BG10.png")

image yumemi_pos6:
    Movie(play=mov_path("yumemi6"), loop=False)
    pause 3.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi6.png")

image yumemi_pos7:
    Movie(play=mov_path("yumemi7"), loop=False)
    pause 1.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi7.png")

image yumemi_pos8:
    Movie(play=mov_path("yumemi8"), loop=False)
    pause 1.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi8.png")

image yumemi_pos9:
    Movie(play=mov_path("yumemi9"), loop=False)
    pause 4.0            # A delay to get to the end of the movie
    Image("images/movie/yumemi9.png")

image bg22:
    Movie(play=mov_path("bg22_movie"), loop=False)
    pause 35.0            # A delay to get to the end of the movie
    Image("images/movie/bg22_movie.png")

image bg33:
    Movie(play=mov_path("BG33_movie"), loop=False)
    pause 54.0            # A delay to get to the end of the movie
    Image("images/movie/BG33_movie.png")

image ev01a_movie:
    Movie(play=mov_path("EV01A_movie"), loop=False)
    pause 4.0            # A delay to get to the end of the movie
    Image("images/movie/EV01A_movie.png")

label splashscreen:

    show warning:
        offset(0,0)
    with Dissolve(1.0)
    $ renpy.pause(2.0)
    hide warning with Dissolve(1.0)

    return


# The game starts here.

label start:

    
    ###0#------
    window hide                       
    #voice "ovk/z1000/13.ogg"
    narrator "{fast}「Than ôi ta đã biết rằng」"(interact=False)
    #voice "ovk/z1000/15.ogg"
    narrator "{fast}「Khó ai bì kịp chúng sinh Địa Cầu」"(interact=False)
    #voice "ovk/z1000/17.ogg"
    narrator "{fast}「Năm lần bảy lượt kiếm tìm」\n「Thánh thần không thấy thời người dựng nên」"(interact=False)
    narrator "{fast}Trích \"Địa Cầu nhìn từ Mặt Trăng\" / Kitahara Hakushu"(interact=False)
    
    $ cut_scene("quote")
    
    window show
    ###1#------
    jump chapter_1

label chapter_1 :
    scene bg01
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide bg34
    with fade
    play music "nwa/bgm02.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/25.ogg"
    narrator "{size=180}\n{/size}「Đào tạo người mới chẳng phải là công việc của em đó sao?」"
    ###2#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/27.ogg"
    narrator "{size=180}\n{/size}「Đúng vậy. Đúng là như thế, nhưng đó không phải là \"người\" mới.」"
    ###3#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/29.ogg"
    narrator "{size=180}\n{/size}「Đúng là người mới còn gì. Chính em là người yêu cầu tuyển thêm thuyết trình viên còn gì.」"
    ###4#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/31.ogg"
    narrator "{size=180}\n{/size}「Tôi đã đáp ứng rồi đấy. Em còn không hài lòng chuyện gì nữa?」"
    ###5#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/33.ogg"
    narrator "{size=180}\n{/size}「Đúng là em đã nói vậy, nhưng em cần người bình thường cơ...」"
    ###6#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/35.ogg"
    narrator "{size=180}\n{/size}「Con bé có bình thường hay không còn tùy thuộc em dạy dỗ như thế nào.」"
    ###7#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/37.ogg"
    narrator "{size=180}\n{/size}「Trên đời làm gì có cái phù hợp ngay từ đầu. Dù là giày da hay áo vét thì cũng phải đi nhiều mặc nhiều mới thấy hợp được.」"
    ###8#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/39.ogg"
    narrator "{size=180}\n{/size}「Nhưng mà giám đốc...」"
    ###9#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Ngay từ lần đầu nghe tin sẽ đưa cô bé đó vào biên chế, Satomi đã phản đối hàng trăm lần bằng đủ thứ cách."
    ###10#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nhưng giờ thì muốn thay đổi cũng muộn rồi."
    ###11#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/48.ogg"
    narrator "{size=180}\n{/size}(Biết rõ là vậy rồi, nhưng mà...)"
    ###12#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/49.ogg"
    narrator "{size=180}\n{/size}(Mình vẫn có trách nhiệm của một trưởng ban thuyết trình, cũng như lòng kiêu hãnh vốn có của một chuyên gia trong lĩnh vực này.)"
    ###13#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/54.ogg"
    narrator "{size=180}\n{/size}(Đâu thể nào chỉ \"À vậy ạ\" một cái là xong chuyện được.)"
    ###14#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/59.ogg"
    narrator "{size=180}\n{/size}「Hờ...」"
    ###15#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Giám đốc thở dài, áp mu bàn tay phải lên bờ trán rộng của mình, đoạn tiếp lời."
    ###16#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/63.ogg"
    narrator "{size=180}\n{/size}「Kurahashi Satomi-kun」"
    ###17#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Việc giám đốc gọi cả họ và tên cấp dưới đồng nghĩa với việc có tranh luận thêm cũng hoài công."
    ###18#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/67.ogg"
    narrator "{size=180}\n{/size}「Chúng ta không chỉ là nhân viên cung thiên văn, mà còn là nhân viên thời vụ của trung tâm bách hóa này.」"
    ###19#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/69.ogg"
    narrator "{size=180}\n{/size}「Nếu giúp cho thật nhiều người tận hưởng trời sao là sứ mệnh của chúng ta, thì cải thiện doanh thu cũng là sứ mệnh quan trọng chẳng kém. Em có hiểu không?」"
    ###20#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/72.ogg"
    narrator "{size=180}\n{/size}「.....」"
    ###21#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Giờ mà nói \"Em chẳng hiểu gì hết\" thì chắc da mặt cô phải dày lắm."
    ###22#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}『Làm việc tại đây khác với thuyết trình ở bảo tàng khoa học』. Đó là những lời đầu tiên cô nhận được trong buổi phỏng vấn xin việc thời niên thiếu."
    ###23#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Lúc đó, giám đốc bảo tàng hẳn vẫn còn tin tưởng vào triển vọng của dự án khai thác vũ trụ và cung thiên văn, và phần tóc hói của ông vẫn còn che giấu được dễ dàng bằng cách sử dụng keo xịt và loại lược gỗ chăm sóc tóc thần kỳ."
    ###24#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/78.ogg"
    narrator "{size=180}\n{/size}「Đến giờ họp giao ban rồi. Nhờ em dẫn con bé tới tập trung ở quầy lễ tân nhé.」"
    ###25#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se001_01.wav"
    play sound "nwa/se001_02.wav"
    narrator "{size=180}\n{/size}Khoác lên khuôn mặt của một cấp trên nghiêm khắc, ông nói, rồi cứ thế bước ra khỏi phòng giám đốc mà chẳng thèm ngoảnh lại."
    ###26#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Bỏ lại trưởng ban thuyết trình... hay nhân viên thời vụ Kurahashi Satomi một mình trong phòng."
    ###27#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không, để mà nói chính xác thì không phải \"một mình\"."
    ###28#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/84.ogg"
    narrator "{size=180}\n{/size}「...nhưng giám đốc ơi, con bé đâu phải con người cơ chứ?」"
    ###29#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không ai đáp lời cô cả."
    ###30#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/92.ogg"
    narrator "{size=180}\n{/size}(Có khác nào đang diễn hề đâu.)"
    ###31#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/93.ogg"
    narrator "{size=180}\n{/size}(À không... chính xác hơn thì phải là múa rối chứ nhỉ.)"
    ###32#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Vừa hay, chiếc đồng hồ treo tường chỉ đúng 9 giờ sáng."
    ###33#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play music "nwa/bgm12.wav" fadeout 0.5 fadein 0.5
    show yumemi_pos1:
        offset(128,22)
    play sound "nwa/se002.wav"
    narrator "{size=180}\n{/size}Ùng..."
    ###34#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se003.wav"
    extend "\nÂm thanh nho nhỏ của động cơ điện từ hao hao giống tiếng ong vo ve làm cô hơi nhột tai."
    ###35#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sâu trong phòng giám đốc, một thứ hình người khác ngoài Satomi bắt đầu di chuyển."
    ###36#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se004.wav"
    narrator "{size=180}\n{/size}Vừa thức dậy khỏi trạng thái tạm nghỉ, thứ đó từ từ nâng nửa thân trên dậy khỏi chiếc ghế dài, thật dễ khiến người ta liên tưởng tới hình ảnh một con quỷ hút máu bò ra khỏi quan tài."
    ###37#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/104.ogg"
    narrator "{size=180}\n{/size}(Giả như, con bé không có hình dạng thế này...)"
    ###38#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi lặp lại lời nghi vấn mà cô đã tự hỏi bản thân không biết bao nhiêu lần kể từ hồi mới nhìn thấy cô bé trong tập tài liệu."
    ###39#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/110.ogg"
    narrator "{size=180}\n{/size}(...thì liệu mình có thể đối xử với nó bình tĩnh hơn không? Hay mình sẽ còn ghét con bé hơn nữa?)"
    ###40#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    show yumemi_pos2:
        offset(128,22)
    narrator "{size=180}\n{/size}Bộ khung người thấp phỏng theo hình dạng cơ thể trung bình của một người con gái tầm 15-20 tuổi, được bao bọc trong bộ trang phục cách điệu dựa trên đồng phục lễ tân của Cửa hàng bách hóa Hanabishi."
    ###41#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos3:
        offset(128,22)
    narrator "{size=180}\n{/size}Hai đuôi tóc cô bé dài lắc lư, có tác dụng tản nhiệt và bảo vệ bộ phận xử lý dữ liệu phần đầu."
    ###42#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos4:
        offset(128,22)
    narrator "{size=180}\n{/size}Hai đầu dây cáp được nối với đầu cắm ở tai trái."
    ###43#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos5:
        offset(128,22)
    narrator "{size=180}\n{/size}Sau khi uốn xuống mặt sàn khoảng vài mét thì chúng được rút về cái thiết bị truyền tải thông tin trông khoa trương y như loại tủ rương làm từ gỗ hông."
    ###44#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trong vài tháng đầu, cô bé luôn phải ngồi đó kết nối dữ liệu gần như cả ngày để cung cấp cho nhà sản xuất những thông tin quý giá theo hợp đồng tiêu dùng."
    ###45#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nói đơn giản hơn thì công việc đó tựa hồ một loại \"của hồi môn\" để cô bé có thể được \"gả\" về nơi này với mức giá hời."
    ###46#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos6:
        offset(128,22)
    narrator "{size=180}\n{/size}Cuối cùng, cô bé đã hoàn toàn đứng dậy được."
    $ renpy.pause(3.0, hard=True)
    ###47#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos7:
        offset(128,22)
    extend "\nCùng một cử chỉ như đang quay trên bàn xoay gốm, cô bé bất giác hướng về phía Satomi."
    ###48#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Rồi thì, cô duỗi thẳng các ngón từ cả hai tay ― vốn là một bộ khung được chế tạo tinh xảo từ nhựa hữu cơ và hợp kim nhẹ bọc trong da nhân tạo."
    ###49#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    show yumemi_pos8:
        offset(128,22)
    voice "ovk/z1000/122.ogg"
    narrator "{size=180}\n{/size}「Buổi sáng tốt lành ạ.」"
    ###50#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé cất tiếng chào Satomi, với một chất giọng thiếu nữ hoàn hảo đến độ mất tự nhiên."
    ###51#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hình ảnh của Satomi phản chiếu trong con ngươi làm từ nhựa quang học kia."
    ###52#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chúng thay đổi độ cong khi tải điện áp yếu, thoáng thấy mờ mờ như màng dầu, khiến cô trông như đang mỉm cười."
    ###53#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kuroe with dissolve:
        offset(128,22)
    hide yumemi_pos1
    hide yumemi_pos2
    hide yumemi_pos3
    hide yumemi_pos4
    hide yumemi_pos5
    hide yumemi_pos6
    hide yumemi_pos7
    hide yumemi_pos8
    show bg10 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    hide kuroe

    show kr_b 00 zorder 2:
 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    show yu_b 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/131.ogg"
    narrator "{size=180}\n{/size}(Nếu có ai giới thiệu con bé này là con người, khéo có khi mình tin thật.)"
    ###54#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    hide kr_f
    hide kr_b
    with dissolve
    show yumemi_pos9:
        offset(128,22) 
    narrator "{size=180}\n{/size}Trên chiếc váy màu xanh biển rực rỡ có thêu một số chữ cái alphabet bằng chỉ phát quang."
    ###55#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}SC   PAGE5000Si/FL   CAPELII"
    ###56#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đó là tên của cô bé."
    ###57#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nÍt nhất, là trong thời điểm này."
    ###58#------
    scene kuros
    show kuroe :
        offset(128,22)
        anchor(0,0)
    hide bg10
    hide sbw00_3
    hide sbw00_4
    hide sbw01
    with fade
    stop music fadeout 1.0
    ###59#------
    $ cut_scene("title")
    jump chapter_2

label chapter_2:
    hide kuroe
    with dissolve
    $ cut_scene("10years")
    ###60#------
    scene bg01
    show bg22 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide kurob
    with fade
    play music "nwa/bgm04.wav" fadeout 0.5 fadein 0.5
    play sound "nwa/se005.wav"
    voice "ovk/z1000/152.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###61#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Giọng nói êm dịu vang vọng trong con ngõ vào một ngày đầu đông."
    ###62#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/156.ogg"
    narrator "{size=180}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###63#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Người người kéo cổ áo khoác lên mà lầm lũi vụt qua."
    ###64#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nKhông ai mảy may để ý đến cô người máy đồng hành lỗi thời ấy."
    ###65#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thứ duy nhất dừng lại chịu lắng nghe là chiếc xe đạp điện bị bỏ rơi nơi góc phố."
    ###66#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nDù vậy, cô vẫn vui vẻ lặp lại những câu từ nọ như ngân lên khúc ca."
    ###67#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/167.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn...」"
    ###68#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Theo như tốc độ di chuyển của Yumemi thì hẳn cô bé vẫn chưa đi quá xa, và nhờ vào thiết bị đầu cuối định vị mà Satomi có thể xác định vị trí hiện tại của cô bé."
    ###69#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se006.wav"
    voice "ovk/z1000/171.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan nè, chị hỏi chút được chứ?」"
    ###70#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Nghe tiếng gọi, cô bé dừng nói và quay sang Satomi mà không tỏ ra dù chỉ một chút ăn năn."
    ###71#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/175.ogg"
    narrator "{size=180}\n{/size}「Vâng, xin cứ tự nhiên hỏi tôi bất cứ điều gì.」"
    ###72#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/177.ogg"
    narrator "{size=180}\n{/size}「Công việc hôm nay của em là gì vậy nhỉ?」"
    ###73#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/179.ogg"
    narrator "{size=180}\n{/size}「Công việc của tôi là chào mời và chỉ dẫn cho khách tại quầy vé trong cung thiên văn.」"
    ###74#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/181.ogg"
    narrator "{size=180}\n{/size}「Biết thế thì sao em lại đứng cách vị trí làm việc những 3 km vậy hả?」"
    ###75#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/183.ogg"
    narrator "{size=180}\n{/size}「Vâng, kể ra thì đó là một câu chuyện dài...」"
    ###76#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sau đó cô bé kể với Satomi chi tiết làm thế nào mình đến được đây."
    ###77#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/187.ogg"
    narrator "{size=180}\n{/size}「...Chuyện đấy chị biết rồi. Chị muốn hỏi là, em đang làm gì ở một nơi như thế này vậy hả?」"
    ###78#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/190.ogg"
    narrator "{size=180}\n{/size}「...?」"
    ###79#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé khẽ nghiêng đầu trước câu hỏi nhấn nhá ngữ điệu của cấp trên."
    ###80#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Ngay cả khi con người đã mất hứng thú với thiên văn và cả bản thân cô bé, thì sắc thái thân thiện trong ánh mắt cô vẫn không hề phai nhạt."
    ###81#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sau vài giây trầm ngâm, cô bé ấy ― Hoshino Yumemi ― khẽ mỉm cười như đã ngộ ra tất cả và trả lời."
    ###82#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/196.ogg"
    narrator "{size=180}\n{/size}「Thành thật xin lỗi. Tôi không hiểu ý nghĩa câu hỏi cho lắm ạ.」"
    ###83#------
    jump chapter_3

label chapter_3:
    scene bg01
    show bg10 : 
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide bg22
    hide yu_f
    hide yu_a
    hide yu_b
    with fade
    play music "nwa/bgm05.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/202.ogg"
    narrator "{size=180}\n{/size}「Quả nhiên là bị hỏng hóc ở đâu rồi đấy nhỉ...」"
    ###84#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se007.wav"
    narrator "{size=180}\n{/size}Trút một tiếng thở dài, Satomi nâng cốc."
    ###85#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trong phòng máy tính này không được phép ăn uống, nhưng do chính giám đốc là người đã quyết định việc này lại luôn uống cà phê trong đó nên thành ra cô cũng chẳng ngại nữa."
    ###86#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chỉ có Yumemi là tuân thủ điều luật này."
    ###87#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/208.ogg"
    narrator "{size=180}\n{/size}「Chị thấy hương vị thế nào ạ?」"
    ###88#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi hỏi bằng giọng nhã nhặn, trong khi vẫn kết nối với thiết bị đầu cuối bằng cáp dữ liệu."
    ###89#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé này mới khi nãy còn đang vui vẻ bưng bê cà phê, giờ đây đã bị lệnh cho phải ngồi xuống ghế và chuyển sang chế độ sửa lỗi."
    ###90#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chẳng rõ cô ấy có hiểu được tính nguy cấp khi bị thẩm vấn về việc tự ý rời khỏi nơi làm việc không nữa..."
    ###91#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/216.ogg"
    narrator "{size=180}\n{/size}「.....」"
    ###92#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nhâm nhi ly cà phê."
    ###93#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nMùi vị vẫn như thường lệ."
    ###94#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cà phê rang kiểu Pháp thương mại được pha kỳ công, hai muỗng đường, không phần kem cho Satomi."
    ###95#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/225.ogg"
    narrator "{size=180}\n{/size}(Xem chừng không có vấn đề gì.)"
    ###96#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/227.ogg"
    narrator "{size=180}\n{/size}「Ngon lắm. Cảm ơn em.」"
    ###97#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 03 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/229.ogg"
    narrator "{size=180}\n{/size}「Thật vui khi được chị khen ngợi như vậy.」"
    ###98#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Yumemi mỉm cười, khẽ híp đôi mắt to tròn lại."
    ###99#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 02 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/233.ogg"
    narrator "{size=180}\n{/size}「Hôm nay, trời hơi trở lạnh, nên tôi đã lưu tâm đến nhiệt độ của nước.」"
    ###100#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/235.ogg"
    narrator "{size=180}\n{/size}「Giấy lọc cà phê vẫn còn khá nhiều trong kho, nhưng hạt cà phê thì chỉ còn một tuần nữa là hết hạn...」"
    ###101#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Vẫn như mọi khi, huyên thuyên đủ thứ chuyện."
    ###102#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/242.ogg"
    narrator "{size=180}\n{/size}(Quả nhiên là trông con bé không có gì bất thường...)"
    ###103#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    hide kr_f
    hide kr_b
    with dissolve
    narrator "{size=180}\n{/size}Ngồi cạnh cô ấy, đồng nghiệp Mikajima Gorou đang chăm chú nhìn màn hình kiểu cũ, tay cầm cốc mà bên trong hẳn là cà phê đen pha loãng."
    ###104#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mười năm trước, anh ta được điều chuyển công tác từ phía nhà sản xuất để giám hộ Yumemi ― lúc ấy hẵng còn chưa thạo việc, một người ngoài \"ở rể\" tại nơi này."
    ###105#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù năng lực của anh ta với tư cách kỹ sư robot là không thể phủ nhận, song lại hay có thói tin tưởng thái quá vào đối tượng cần bảo trì."
    ###106#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se008.wav"
    voice "ovk/z1000/248.ogg"
    narrator "{size=180}\n{/size}「Từ những triệu chứng chị vừa nói thì tôi nghĩ giờ lỗi sẽ không phát sinh nữa đâu.」"
    ###107#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Anh ta lẩm nhẩm vô nghĩa trong lúc lướt qua màn hình hiển thị báo cáo hoạt động chi tiết."
    ###108#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nHẳn phải có báo cáo về mô típ hành vi của Yumemi từ đêm qua."
    ###109#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/253.ogg"
    narrator "{size=180}\n{/size}「Vâng. Theo như tôi nhận thức được thì không hề có lỗi nào cả.」"
    ###110#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nở một nụ cười, Yumemi khẳng định mà chẳng hề có lấy một chút sức thuyết phục."
    ###111#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/257.ogg"
    narrator "{size=180}\n{/size}「Nào, ngày xưaaa chả có một vụ còn gì. Em chỉ đường cho một cụ bà xong rồi tự ý đi ra ngoài luôn ấy.」"
    ###112#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 06 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/259.ogg"
    narrator "{size=180}\n{/size}「Vâng. Khi ấy quả thật là khó khăn lắm thay.」"
    ###113#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/261.ogg"
    narrator "{size=180}\n{/size}「Vừa hay tôi đang đứng trước cửa chính mời chào khách và phân phát tờ rơi cho buổi triển lãm đặc biệt của trung tâm bách hóa Hanabishi...」"
    ###114#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/263.ogg"
    narrator "{size=180}\n{/size}「Tôi đã chứng minh là điều ấy chỉ xảy ra dưới những điều kiện vô cùng hạn chế, và hiện tại việc kiểm tra những hành vi bất thường cũng dần nghiêm ngặt hơn rồi nên...」"
    ###115#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/265.ogg"
    narrator "{size=180}\n{/size}「Không thế thì một cỗ máy bán độc lập thiếu bộ kiểm soát ý chí từ xa có lẽ đã bị crack Turing và bán bộ phận tại nơi nào đó ở Nam Mỹ rồi.」"
    ###116#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/267.ogg"
    narrator "{size=180}\n{/size}「Bớt nói gở đi hộ cái...」"
    ###117#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi biết, rằng những vụ trộm robot dân sinh gần đây xảy ra ngày càng thường xuyên hơn."
    ###118#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù vậy, Yumemi chắc không thể lọt vào tầm ngắm của lũ trộm được."
    ###119#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/272.ogg"
    narrator "{size=180}\n{/size}「Ừ thì, tôi không chắc có ai có ý định bắt cóc con bé không, cơ mà...」"
    ###120#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se009.wav"
    narrator "{size=180}\n{/size}Gorou nói, đoạn gõ bàn phím và mở một số video."
    ###121#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/276.ogg"
    narrator "{size=180}\n{/size}「Trên đường đi con bé đã chụp ngẫu nhiên sáu tấm ảnh đa chiều, nhưng chẳng có cái nào trông đáng ngờ cả. Tất cả đều đúng y như những gì được ghi chép lại.」"
    ###122#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/278.ogg"
    narrator "{size=180}\n{/size}「Danh sách mệnh lệnh vẫn được xử lý theo đúng quy trình, không thấy có dấu hiệu bị ngắt quãng bởi những hành động ngoài công việc. Cũng chẳng có mâu thuẫn nào giữa kho lưu trữ dữ liệu với bộ nhớ chính...」"
    ###123#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 22 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/280.ogg"
    narrator "{size=180}\n{/size}「Thưa, cho phép tôi được ngắt lời ạ.」"
    ###124#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thế rồi, đối tượng phân tích bắt đầu mở miệng, nghe đầy áy náy."
    ###125#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/284.ogg"
    narrator "{size=180}\n{/size}「Giờ đã là 3:40 chiều.」"
    ###126#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/286.ogg"
    narrator "{size=180}\n{/size}「Buổi thuyết trình hôm nay lúc 4 giờ do tôi đảm trách. Nếu không phiền, cho phép tôi trở lại với vị trí làm việc của mình ạ.」"
    ###127#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/288.ogg"
    narrator "{size=180}\n{/size}「À, phải rồi ha...」"
    ###128#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Satomi liếc đồng hồ treo tường rồi lại hướng về Yumemi."
    ###129#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé nhìn Satomi và Gorou bằng ánh mắt không thể dùng từ ngữ nào khác để miêu tả ngoài ngây thơ vô tội."
    ###130#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mặc dù vẫn hơi đáng dè chừng, nhưng chắc chắn cô bé sẽ không tấn công khách hàng."
    ###131#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/294.ogg"
    narrator "{size=180}\n{/size}「Được rồi, em trở lại với công việc đi.」"
    ###132#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 24 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/296.ogg"
    narrator "{size=180}\n{/size}「Vâng, tôi rõ rồi ạ.」"
    ###133#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    hide kr_f
    hide kr_b
    with dissolve
    play sound "nwa/se004.wav"
    narrator "{size=180}\n{/size}Cô nhẹ nhàng tháo dây cáp nối trên ngón tay và rời khỏi ghế."
    ###134#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/300.ogg"
    narrator "{size=180}\n{/size}「Giờ thì, tôi xin phép ạ.」"
    ###135#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play sound "nwa/se010.wav"
    narrator "{size=180}\n{/size}Cô cúi người lễ phép, rồi rời khỏi phòng máy tính."
    ###136#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se011.wav"
    voice "ovk/z1000/304.ogg"
    narrator "{size=180}\n{/size}「Tôi có nên nói lại chuyện này với giám đốc không?」"
    ###137#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou vừa hỏi vừa vươn vai trên chiếc ghế xoay cọt kẹt."
    ###138#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/308.ogg"
    narrator "{size=180}\n{/size}「Cứ theo dõi thêm một thời gian nữa đã. Chẳng mấy khi được đi nước ngoài như thế, tôi không muốn anh ta phải lo lắng nhiều.」"
    ###139#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/310.ogg"
    narrator "{size=180}\n{/size}「Vậy tức là, chị gà đây muốn vọc niêu tôm nhân lúc chủ nhà đi vắng chứ gì?」"
    ###140#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/312.ogg"
    narrator "{size=180}\n{/size}「Anh giai mà nói ngon nói ngọt với mấy ông lớn bên kia rồi mang một mẫu Zeiss mới về làm quà thì hay nhỉ.」"
    ###141#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/314.ogg"
    narrator "{size=180}\n{/size}「Được thế đã phúc. Tự cái giới kinh doanh này đã sống dở chết dở rồi.」"
    ###142#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/316.ogg"
    narrator "{size=180}\n{/size}「Tôi hiểu rồi...」"
    ###143#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hai người lại thở dài."
    ###144#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    extend "\nCửa sổ góc màn hình máy tính hiển thị doanh số hôm nay."
    ###145#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}0 suất đặt trước, 0 khách hàng trên tổng số 184 ghế ngồi."
    ###146#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Suất chiếu đầu tiên vào ngày thường sẽ luôn ít khách, và khi không có khách thì người mới có thể tận dụng thời gian ấy để luyện tập thuyết trình thủ công."
    ###147#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dẫu biết là chẳng còn cách nào khác, nhưng quả nhiên là cô cũng không giữ được bình tĩnh cho nổi."
    ###148#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nhớ về ngày xưa, khi cô nỗ lực trở thành người thuyết trình thiên văn."
    ###149#------
    scene black
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide bg10
    hide kr_f
    hide kr_b
    with fade
    play music "nwa/bgm07.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/338.ogg"
    narrator "{size=180}\n{/size}(Khoảnh khắc hào hứng, cuồng nhiệt khi con người lần đầu đặt chân lên Sao Hỏa.)"
    ###150#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/339.ogg"
    narrator "{size=180}\n{/size}(Khoảnh khắc nhân loại cùng đồng lòng hướng về vũ trụ.)"
    ###151#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/340.ogg"
    narrator "{size=180}\n{/size}(Thời kỳ kính viễn vọng và cung thiên văn tại gia bán đắt như tôm tươi.)"
    ###152#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/341.ogg"
    narrator "{size=180}\n{/size}(Thời kỳ mà con người có thể hồn nhiên mơ mộng, rằng bản thân đủ năng lực đi tới bất kỳ đâu.)"
    ###153#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/342.ogg"
    narrator "{size=180}\n{/size}(Cung thiên văn này được dựng lên giữa thời kỳ xô bồ ấy.)"
    ###154#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg30 :
        offset(128,22)
        anchor(0,0)
        ysize 704
        xsize 1024
        fit 'fill' 
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/343.ogg"
    narrator "{size=180}\n{/size}(Nhưng những năm tháng bùng nổ vũ trụ kia đã là quá khứ rồi.)"
    ###155#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide bg30
    with dissolve
    play music "nwa/bgm17.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/344.ogg"
    narrator "{size=180}\n{/size}(Khi phi hành đoàn trở về mặt đất, mọi người chuyển dần từ tán dương sang thất vọng.)"
    ###156#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/345.ogg"
    narrator "{size=180}\n{/size}(Người ta phát hiện ra rằng, trên đường trở về từ Sao Hỏa, đã có hai người thiệt mạng trong một sự cố chốt gió.)"
    ###157#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/346.ogg"
    narrator "{size=180}\n{/size}(Các thành viên khác cũng tổn thương não nghiêm trọng do tiếp xúc lâu dài với bức xạ vũ trụ...)"
    ###158#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/347.ogg"
    narrator "{size=180}\n{/size}(Cả Trái Đất như bị dội một gáo nước lạnh.)"
    ###159#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/348.ogg"
    narrator "{size=180}\n{/size}(Bóng tối của vực thẳm mà nhân loại vẫn chưa thể chạm tới, thật đen tối và đáng sợ...)"
    ###160#------
    scene bg01
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide kuroe
    with fade
    narrator "{size=180}\n{/size}Ngay cả chương trình thám hiểm không gian mà ai cũng thấy cần thiết vì là cứu cánh cuối cùng cho vấn nạn bùng nổ dân số và cạn kiệt tài nguyên cũng bị đình chỉ sau khi xây dựng hai thành phố trên Mặt Trăng."
    ###161#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tất cả những cuộc thám hiểm có người lái đều đã bị ngừng lại, và cả kế hoạch khai phá bên ngoài vũ trụ bằng máy bay không người lái cũng không có triển vọng mấy."
    ###162#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trên hết..."
    ###163#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/358.ogg"
    narrator "{size=180}\n{/size}(Những người có thể dành tình yêu cho các vì sao mô phỏng đâu cả rồi?)"
    ###164#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Ngay cả những bảo tàng khoa học đã lắp đặt máy chiếu thế hệ mới và chiếu lên loạt chương trình được trau chuốt tỉ mỉ cũng không tránh khỏi khó khăn."
    ###165#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thật kỳ diệu khi cung thiên văn thuần thương mại này vẫn có thể hoạt động mà không có khoản trợ cấp giáo dục nào."
    ###166#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Để thoát khỏi hoàn cảnh bế tắc, giám đốc đã cố gắng thực hiện một kế hoạch cải tử hoàn sinh, đó chính là robot thuyết trình viên tự hành đầu tiên trên thế giới ― Hoshino Yumemi, dù vậy..."
    ###167#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play music "nwa/bgm02.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/364.ogg"
    narrator "{size=180}\n{/size}「...Thôi không nên nghĩ nhiều về cái tình trạng này nữa. Khách hàng sẽ chạy mất dép cho coi.」"
    ###168#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/366.ogg"
    narrator "{size=180}\n{/size}「Tôi biết rồi.」"
    ###169#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hai người nhìn nhau và nói."
    ###170#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se012.wav"
    extend "\nSatomi vừa rời ghế, toan quay lại quầy tiếp tân, thì cửa phòng máy tính bỗng mở ra."
    ###171#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/371.ogg"
    narrator "{size=180}\n{/size}「Kurahashi-san! Em xin phép ạ!」"
    ###172#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Morimi Yuka, một thuyết trình viên, chạy đến."
    ###173#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô ấy đã vào công ty được hai năm, cũng đã quen dần với công việc rồi, thế mà lại đang mất bình tĩnh y như trong kỳ huấn luyện."
    ###174#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/376.ogg"
    narrator "{size=180}\n{/size}「Có chuyện gì thế?」"
    ###175#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/378.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan... mất tích rồi...」"
    ###176#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/380.ogg"
    narrator "{size=180}\n{/size}「Mất tích...?!」"
    ###177#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou và Satomi quay sang nhìn nhau."
    ###178#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nVà rồi, cuối cùng cả hai cũng hiểu tình hình."
    ###179#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se011.wav"
    narrator "{size=180}\n{/size}Anh kỹ sư ngay lập tức mở máy tính và thuyết trình viên trưởng bật ngay thiết bị định vị đầu cuối."
    ###180#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trên bản đồ chi tiết lấy cung thiên văn trên tầng thượng cửa hàng bách hóa Hanabishi làm trung tâm, đốm sáng chỉ vị trí hiện tại của Hoshino Yumemi đang di chuyển chậm rãi."
    ###181#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé vừa rời khỏi cửa chính và đi về phía nam với vận tốc 6 km/h hướng thẳng tới trạm xe buýt."
    ###182#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    extend "\nSatomi dùng cả hai tay ôm mặt..."
    ###183#------
    show bg10 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/393.ogg"
    narrator "{size=180}\n{/size}「Cái con bé nhân viên vụng thối này...」"
    ###184#------
    jump chapter_4

label chapter_4:
    scene bg02
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show smw00d zorder 100: 
        offset(97,550)
    hide bg10
    hide kr_f
    hide kr_b
    with fade
    play music "nwa/bgm04.wav" fadeout 0.5 fadein 0.5
    narrator "Người khổng lồ tốt bụng hiện đang gật gù như đang say ngủ."
    ###185#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nỞ chính giữa phòng trình chiếu, quả cầu định tính khoác trên người bộ áo đen thẫm đang nằm xuống vị trí bảo trì để kiểm tra bóng đèn."
    ###186#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nMáy chiếu vũ trụ 23/3 do Carl Zeiss Jena chế tạo."
    ###187#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nCó lẽ cách gọi cổ như \"mô hình vũ trụ\" sẽ phù hợp với cỗ máy này hơn."
    ###188#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Những ai lần đầu chứng kiến có lẽ sẽ bị choáng ngợp trước kích thước và hình dạng kỳ lạ của hai quả cầu được hai cánh tay nâng đỡ này."
    ###189#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nMột trong những cỗ máy từng được yêu thích nhất ở Bảo tàng khoa học Kansai suốt một thế kỷ, vốn dự tính sẽ được bảo tồn và trưng bày sau khi sử dụng xong."
    ###190#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Cung thiên văn trên tầng thượng cửa hàng bách hóa Hanabishi đã kế thừa cỗ máy này vào thời điểm khai trương và đến bây giờ nó vẫn được ưu tiên sử dụng hàng đầu."
    ###191#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Không thể phủ nhận rằng nó đã lỗi thời so với loại bóng đơn đang phổ biến, bất kể là loại chiếu quang học, chiếu kỹ thuật số hay loại tích hợp hoàn toàn không cần tới máy chiếu phụ."
    ###192#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nDù vậy thì, bầu trời sao chiếu ra thực sự được làm một cách thủ công."
    ###193#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nÁnh sáng bóng đèn dây tóc 1000 watt lớn chiếu qua lớp âm bản định tinh do những người thợ thủ công dệt nên một thế kỷ trước, được khuếch đại chính xác nhờ những thấu kính được đánh bóng tựa hồ đá quý và được chiếu lên màn trần hình cầu cách xa 10 mét."
    ###194#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Độ sắc nét cùng vẻ đẹp mê hoặc khó tả của bầu trời đầy sao này, chắc chắn không hề kém cạnh bất kỳ cỗ máy đời mới nào khác."
    ###195#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nGiám đốc và tất cả nhân viên đều tin tưởng như vậy, không chút hoài nghi."
    ###196#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nThế nhưng, sự thật không thể chối cãi là niềm hi vọng này không thu hút nổi khách hàng."
    ###197#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    hide bg13
    with dissolve
    voice "ovk/z1000/415.ogg"
    narrator "「Phù...」"
    ###198#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nTựa vào cây chổi lau nhà, Satomi thở dài một hơi."
    ###199#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    extend "\nCác thuyết trình viên cấp dưới của cô thì đang lau ghế khán phòng bằng khăn."
    ###200#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nNgay cả những cô gái chưa bao giờ bỏ lỡ cơ hội tán chuyện trong giờ làm cũng bắt đầu lộ rõ thái độ xuống tinh thần."
    ###201#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nSự cố xảy đến sau khi buổi chiếu cuối cùng diễn ra được 15 phút."
    ###202#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nMột khách hàng lỡ làm đổ nước ngọt, dẫn đến cãi vã với vị khách khác bên cạnh."
    ###203#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Dẫu có nhắc nhở là không được mang đồ ăn thức uống vào phòng trình chiếu bao nhiêu lần đi chăng nữa, lượng khách lỡ tay đem nước hộp vào phòng chẳng hề có dấu hiệu suy giảm."
    ###204#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nSau khi đèn tắt, cả phòng tối đến độ không nhìn thấy tay mình thì đã quá muộn để cất đồ uống rồi."
    ###205#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nBuổi trình diễn bị gián đoạn cho đến khi làm dịu được vị khách hàng nổi nóng và dẫn họ ra khỏi phòng chiếu."
    ###206#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Những lúc thế này, lượng khách ít ỏi quả là một điều đáng mừng."
    ###207#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/427.ogg"
    narrator "「A... em xin lỗi. Lúc ấy, em không làm được gì cả...」"
    ###208#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/429.ogg"
    extend "\n「Đừng để ý quá~. Những việc như này đôi khi vẫn xảy ra mà.」"
    ###209#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nKoga Akane đang ra sức động viên Morimi Yuka, nếu không cô sẽ tự trách bản thân mãi khôn nguôi mất."
    ###210#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nCông việc của Akane nhìn chung là khó nhọc, ấy nhưng những lúc thế này cô lại lạc quan đến lạ."
    ###211#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/434.ogg"
    narrator "「Vâng. Tôi tin rằng một lần thất bại không thể nói lên giá trị của con người.」"
    ###212#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nCô gái robot lạc quan không kém cũng bình thản lên tiếng."
    ###213#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/438.ogg"
    extend "\n「Nghe em nói vậy làm chị thấy hơi bối rối đấy, Yumemi-chan.」"
    ###214#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/440.ogg"
    extend "\n「Vâng? Tôi không hiểu ý chị cho lắm.」"
    ###215#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/442.ogg"
    narrator "「Ai đã bỏ bê công việc và chạy ra ngoài trong hai ngày liền hả?」"
    ###216#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/444.ogg"
    extend "\n「Vâng, chính là tôi ạ.」"
    ###217#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/447.ogg"
    extend "\n「.....」"
    ###218#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/449.ogg"
    extend "\n「...?」"
    ###219#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nSau khi trả lời thật nhiệt tình, cô bé chợt để ý thấy cái lườm lạnh lẽo từ Satomi và khẽ nghiêng đầu."
    ###220#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    narrator "Con ngươi to tròn vẫn mở rộng, Yumemi trầm ngâm một hồi..."
    ###221#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 06 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/454.ogg"
    extend "\n「Tôi thành thật xin lỗi!」"
    ###222#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 05 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/456.ogg"
    extend "\n「Giờ nghĩ lại, hành động của tôi đã vi phạm nghiêm trọng nguyên tắc công việc! Tôi thật sự... thật sự xin lỗi ạ!」"
    ###223#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nCô bé liên tục cúi đầu xin lỗi, trông chẳng khác nào con người... à không, chẳng khác động cơ của cô đã thay đổi 180 độ."
    ###224#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/460.ogg"
    narrator "「Hờ...」"
    ###225#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nDù đã thấy cảnh tượng này không biết bao nhiêu lần rồi, cô vẫn cảm nhận được có gì đó không đúng."
    ###226#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/464.ogg"
    narrator "「Nhưng mà nhé, em nghĩ là mình có thể hiểu được cảm giác của Yumemi-chan đấy.」"
    ###227#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nXem bộ đã chán cái bầu không khí u ám này (và cả việc dọn dẹp nữa), Akane hăng hái tham gia vào câu chuyện."
    ###228#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/468.ogg"
    extend "\n「Thật á? Chị đây làm việc cùng con bé được 10 năm rồi còn chẳng hiểu nó thật sự nghĩ gì nữa là.」"
    ###229#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/470.ogg"
    narrator "「Thì đó, suy nghĩ bình thường thì sẽ hiểu liền à~」"
    ###230#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/472.ogg"
    extend "\n「Nếu mọi người chỉ nuông chiều con bé lúc đầu còn lần sau thì chán chẳng thèm ngó lấy một cái, là em thì em nghỉ việc lâu rồi!」"
    ###231#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/474.ogg"
    extend "\n「Phải không nè, Yumemi-chan?」"
    ###232#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 22 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/476.ogg"
    extend "\n「Bạn định thôi việc sao?」"
    ###233#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 27 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/478.ogg"
    extend "\n「Điều đó quả thật là đáng tiếc.」"
    ###234#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/480.ogg"
    narrator "「Koga-san, mặc dù mới gặp gỡ chưa lâu, nhưng tôi chúc em sẽ tìm được niềm vui trong công việc mới.」"
    ###235#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/482.ogg"
    extend "\n「A, không phải thế! Không có! Không có! Em nào có định nghỉ đâu ạ!」"
    ###236#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    narrator "Những cuộc tán gẫu bình dị phản chiếu trên mái vòm, tràn ngập trong phòng trình chiếu."
    ###237#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/486.ogg"
    extend "\n「Akane-chan mà nghỉ việc thật thì mình chẳng biết phải làm sao nữa.」"
    ###238#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nThấy cô bạn đồng nghiệp cuối cùng cũng mỉm cười, Akane khẽ thì thầm vào tai cô."
    ###239#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/490.ogg"
    extend "\n「Nói thế chứ tớ muốn kết hôn xong nghỉ việc lắm đó nhaaa.」"
    ###240#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/492.ogg"
    extend "\n「Ừm... nghe cũng hay thật đấy.」"
    ###241#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/494.ogg"
    narrator "「...Hai cái đứa này, chị nghe thấy hết rồi nhé!」"
    ###242#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nKhi các đàn anh đàn chị từng dẫn dắt cô lần lượt rời công ty lập gia đình, Satomi hiện là thành viên kỳ cựu thứ hai chỉ sau giám đốc."
    ###243#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/502.ogg"
    extend "\n(Giờ mình đã hết thời mơ mộng rồi, nhưng mà...）"
    ###244#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/503.ogg"
    extend "\n(Mình vẫn còn bổn phận phải chỉ dạy cho mấy đứa này thông thạo công việc hơn.)"
    ###245#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/504.ogg"
    extend "\n(Để nếu như... chỉ nếu như thôi, một ngày nào đó mình rời khỏi chốn này, thì những gì mình học được, những gì mình cảm nhận được sẽ còn mãi lưu lại nơi đây.)"
    ###246#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "Yumemi vẫn đang nở nụ cười bên cạnh cô, đoạn khẽ nghiêng đầu 15 độ về bên phải."
    ###247#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/508.ogg"
    extend "\n「Xin lỗi, tôi có thể hỏi một điều được không ạ?」"
    ###248#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/510.ogg"
    extend "\n「Gì vậy? Cứ hỏi đi.」"
    ###249#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/512.ogg"
    extend "\n「Sau khi kết hôn thì buộc phải nghỉ việc sao?」"
    ###250#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/514.ogg"
    extend "\n「Bảo là bắt buộc thì cũng không phải... còn tùy từng người nữa.」"
    ###251#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nDù chẳng rõ tại sao cô bé lại hỏi như thế, Satomi vẫn đáp."
    ###252#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 03 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/518.ogg"
    narrator "「Là như vậy ạ. Tôi an tâm rồi.」"
    ###253#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nYumemi nói, đôi mắt làm bằng nhựa quang học của cô bé khẽ híp lại."
    ###254#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    extend "\nSatomi chợt nghĩ, biểu cảm trên khuôn mặt cô bé lúc ấy là trông \"con người\" nhất."
    ###255#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    hide kr_f
    hide kr_b
    with dissolve
    voice "ovk/z1000/523.ogg"
    narrator "「Em xin lỗi vì phải cắt ngang cuộc nói chuyện...」"
    ###256#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nTsuno Hidefumi là trưởng ban bảo trì, tay cầm cờ lê chạy đến gọi cô."
    ###257#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/527.ogg"
    extend "\n「Số lượng bóng đèn tồn kho cho máy chiếu chính sắp hết rồi, nên em yêu cầu nhập thêm được không ạ?」"
    ###258#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/529.ogg"
    extend "\n「Tiếc là chị phải từ chối rồi. Mấy cậu phải ráng tận dụng cho tới đầu năm thôi.」"
    ###259#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/531.ogg"
    extend "\n「Đừng nói với em, chị đi mà nói thẳng với Jena-san ấy...」"
    ###260#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "Anh chỉ ngón tay ra máy chiếu đằng sau cùng nụ cười gượng gạo."
    ###261#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nĐoạn, anh ta cũng xoa đầu Yumemi một cách thân thiện."
    ###262#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nAnh chàng nói cũng có lý, nhưng sao có thể đòi hỏi một thứ không tồn tại được."
    ###263#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nSatomi không còn cách nào khác ngoài chấp nhận."
    ###264#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/538.ogg"
    narrator "「Hết cách rồi, khách thì ít đến mà đồ cũng chẳng bán được...」"
    ###265#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/540.ogg"
    extend "\n「Gần đây doanh số bình đồ địa cầu í ẹ lắm. Phía phụ kiện thì thuận lợi hơn hẳn.」"
    ###266#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/542.ogg"
    extend "\n「Khi trời trở lạnh thì kiểu gì cũng thế.」"
    ###267#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/544.ogg"
    extend "\n「Cần phải có mặt hàng chủ lực. Nếu được thì là loại chỉ bán trong mùa đông thôi ấy.」"
    ###268#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nTrong khi Satomi và Yuka mải suy nghĩ, Akane phát biểu ý tưởng."
    ###269#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/548.ogg"
    extend "\n「Cầu tuyết thì sao nhỉ? Cái quả cầu thủy tinh có tuyết rơi bên trong ấy ạ.」"
    ###270#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/550.ogg"
    narrator "「Thứ đó thì liên quan gì đến cung thiên văn?」"
    ###271#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nSatomi điềm đạm hỏi."
    ###272#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/554.ogg"
    extend "\n「A... chị thấy đó, chúng tròn tròn này... trông gần giống như cung thiên văn mà ha~」"
    ###273#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "Trước câu trả lời chung chung thường thấy ở Akane, Satomi và Yuka cùng thở dài."
    ###274#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/558.ogg"
    narrator "「Ừm... vào mùa đông, người ta thường nghĩ về tuyết hơn là sao...」"
    ###275#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/560.ogg"
    extend "\n「Dù rằng sao trời đông chúng đẹp hơn hẳn...」"
    ###276#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/562.ogg"
    extend "\n「Sao ấy hả...」"
    ###277#------
    show bg12 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/567.ogg"
    extend "\n(Không biết có bao nhiêu người mua bình đồ địa cầu để được thấy sao trời hàng thật nhỉ?)"
    ###278#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    hide bg12
    hide kr_f
    hide kr_b
    with dissolve
    narrator "Cỗ máy trình chiếu 『Jena-san』 giữ nguyên vẻ tĩnh lặng đầy tinh tế."
    ###279#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    extend "\nVạn nhất nó mà nghe thấy nhân viên nói chuyện với nhau thế này thì chắc sẽ cạn lời lắm đây."
    ###280#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/575.ogg"
    extend "\n(...Cậu đừng có bỏ chạy đấy nhé.)"
    ###281#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    play sound "nwa/se035.wav"
    extend "\nKhẩn cầu cỗ máy như thế từ tận tâm can, Satomi vỗ hai tay lại và nói khẽ."
    ###282#------
    show bg13 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 505
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 505
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,534)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/579.ogg"
    narrator "「Được rồi, mười phút nữa chúng ta phải họp đấy, nên mọi người nhanh tay lên nào.」"
    ###283#------
    jump chapter_5

label chapter_5:
    scene bg01
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide bg13
    with fade
    play music "nwa/bgm06.wav" fadeout 0.5 fadein 0.5
    play sound "nwa/se005.wav"
    narrator "{size=180}\n{/size}Sau đó, Yumemi vẫn tiếp tục rời nơi làm việc."
    ###284#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nếu chỉ nhìn qua thì cô bé này chẳng có gì bất thường cả."
    ###285#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Miễn có đồng nghiệp xung quanh thì cô sẽ làm những công việc được giao như bình thường."
    ###286#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nhưng hễ đồng nghiệp rời mắt một chút thôi là cô sẽ lon ton chạy ngay ra khỏi sân thượng."
    ###287#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chừng như cô không có một điểm đến cố định."
    ###288#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Lang thang vô định khắp các con ngõ, dừng ngẫu nhiên ở một điểm nào đó để quay video ba chiều, rồi cố gắng mời chào khách... thật khó mà mường tượng được mục đích của những hành động này."
    ###289#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cho dù có khiến lịch làm việc dày hơn trước, cho dù có dùng lý do nhân viên lao lực để đưa ra mệnh lệnh ưu tiên, cho dù có ngắt ăng ten truyền tin một cách thủ công khi tính đến trường hợp nhiều khi cô bé đã nhận được tạp âm nào đó..."
    ###290#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg21a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tất cả những đối sách có thể nghĩ ra đều kết thúc trong bất lực."
    ###291#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    hide kuroe
    hide bg21a
    with dissolve
    play music "nwa/bgm03.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/596.ogg"
    narrator "{size=180}\n{/size}「Đây chẳng phải đường chui dưới cầu vượt quốc lộ sao?」"
    ###292#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/598.ogg"
    narrator "{size=180}\n{/size}「Lần này con bé đang chào mời khách. Địa điểm là... ở gần giao lộ trước tòa thị chính.」"
    ###293#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi và Gorou nhìn chăm chú vào các hình ảnh lần lượt hiển thị trên màn hình ống cực kỳ cổ."
    ###294#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chất lượng hình ảnh tệ và âm thanh khó nghe do hình ảnh được chụp ba chiều bị ép xuống còn hai chiều."
    ###295#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Giữa những khung cảnh phố thị bình thường, thỉnh thoảng lại có những cảnh mà ta phải nghiêng đầu mới thấy được."
    ###296#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Rác thải sinh hoạt thò ra từ thùng rác, rồi đến ánh mắt của lũ quạ đang bới móc chỗ rác ấy."
    ###297#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hàng dài những tấm áp phích bầu cử giống hệt nhau như thể chúng là tác phẩm nghệ thuật đương đại."
    ###298#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Graffiti nối đuôi graffiti trên tường nhà vệ sinh công cộng."
    ###299#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nMột xe cảnh sát với ánh đèn xanh đỏ quay vòng vòng chạy qua với tốc độ khủng khiếp."
    ###300#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/608.ogg"
    narrator "{size=180}\n{/size}「Tôi chẳng nghĩ ra nổi mấy thứ này liên quan chỗ nào...」"
    ###301#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/610.ogg"
    narrator "{size=180}\n{/size}「Thật là... con bé đang nghĩ cái quái gì vậy chứ?」"
    ###302#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cũng giống như việc mời chào khách, ngẫu nhiên chụp ảnh đa chiều là một phần nhiệm vụ của Yumemi."
    ###303#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù rằng liệu nhiệm vụ này có ẩn ý gì không thì, năm mươi-năm mươi."
    ###304#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nhớ lại quãng thời gian sau khi cô nhận nhiệm vụ đào tạo Yumemi từ giám đốc, và cả những lúc cô chưa thể kết thân với cô bé ấy."
    ###305#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/620.ogg"
    narrator "{size=180}\n{/size}(Liệu sự mâu thuẫn và biến dạng của thế giới sẽ trông như thế nào qua con mắt robot nhỉ?)"
    ###306#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/621.ogg"
    narrator "{size=180}\n{/size}(Liệu Yumemi đã cảm thấy điều gì, đã suy nghĩ những gì?)"
    ###307#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cho đến tận bây giờ, cô vẫn chưa tìm được câu trả lời."
    ###308#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/625.ogg"
    narrator "{size=180}\n{/size}「Tạm thời lúc này ta nên nghĩ cách đối phó hơn là cố tìm hiểu nguyên nhân. Thú thật, với trình độ của tôi thì đến cỡ này là giơ tay xin hàng rồi.」"
    ###309#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou nói, đoạn giơ hai tay khỏi bàn phím ra hiệu đầu hàng."
    ###310#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/629.ogg"
    narrator "{size=180}\n{/size}「Tôi đã lấy bit chẵn lẻ trên thẻ nhớ và kho lưu trữ rồi, giờ tôi mang dữ liệu sao lưu ra phòng lab để tiến hành gỡ lỗi thì chắc sẽ nghĩ ra được gì đó...」"
    ###311#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/631.ogg"
    narrator "{size=180}\n{/size}「Nhưng hiện tại ta khó mà loại trừ được khả năng có phần cứng bị trục trặc.」"
    ###312#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/633.ogg"
    narrator "{size=180}\n{/size}「Đại ý là, giờ ta phải cho con bé \"nhập viện\" hả...?」"
    ###313#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/638.ogg"
    narrator "{size=180}\n{/size}(...đã hết thời hạn bảo hành rồi.)"
    ###314#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Với tư cách một người quản lý thu chi, cô bắt đầu suy nghĩ về khía cạnh tiền nong."
    ###315#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nếu là cái người dính Yumemi như giám đốc thì chắc chắn anh ta sẽ không ngần ngại lệnh cho cấp dưới đưa cô bé đến nơi sản xuất, nhưng may mắn thay (hoặc không), chuyến khảo sát châu Âu của anh ta vẫn còn tới năm ngày nữa."
    ###316#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/644.ogg"
    narrator "{size=180}\n{/size}「Tôi hiểu rồi...」"
    ###317#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nghĩ tiếp."
    ###318#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/655.ogg"
    narrator "{size=180}\n{/size}(Theo như tờ hướng dẫn, có lẽ sẽ cần tắt nguồn chính và dừng hệ điều hành.)"
    ###319#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/656.ogg"
    narrator "{size=180}\n{/size}(Nhưng chúng ta thường xuyên thiếu nhân lực và một số vị khách đến chỉ để gặp Yumemi.)"
    ###320#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/657.ogg"
    narrator "{size=180}\n{/size}(Suy nghĩ đơn giản thì, chỉ cần có người để mắt đến Yumemi là sẽ chẳng còn vấn đề gì nữa.)"
    ###321#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/658.ogg"
    narrator "{size=180}\n{/size}(Kể cả có chạy đi, thì một cỗ máy hỗ trợ công việc như Yumemi sẽ không thể hoạt động được trong phạm vi ngoài 3 km từ nơi làm việc...)"
    ###322#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/659.ogg"
    narrator "{size=180}\n{/size}(Đó là nguyên tắc chung cho robot để đảm bảo chúng không làm hại con người mọi lúc.)"
    ###323#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/660.ogg"
    narrator "{size=180}\n{/size}(Với cả, đúng là khó mà nhờ mấy gian hàng tầng dưới bắt hộ con robot của mình nếu nó có đi qua thật...)"
    ###324#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/662.ogg"
    narrator "{size=180}\n{/size}「Mất thời gian chút cũng được, Gorou-kun tự làm một mình được chứ?」"
    ###325#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/664.ogg"
    narrator "{size=180}\n{/size}「Con bé cũng chưa phá phách gì cả. Cần thiết thì chị sẽ đến đưa nó về.」"
    ###326#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/666.ogg"
    narrator "{size=180}\n{/size}「Dù chị nói vậy thì...」"
    ###327#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg31 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide bg11
    hide kr_f
    hide kr_b
    with dissolve
    play music "nwa/bgm17.wav" fadeout 0.5 fadein 0.5
    play sound "nwa/se013.wav"
    narrator "{size=180}\n{/size}Gorou đáp, đoạn mở cửa sổ khác lên màn hình."
    ###328#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg31 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nNom như một cái video truyền hình vệ tinh trực tiếp."
    ###329#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg31 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một đám đông cầm panô ghi mớ tiếng Anh tệ hại đang hô vang khẩu hiệu gì đó."
    ###330#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg31 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một cột lửa trại được nhóm ngay giữa, và một gã đàn ông mặc áo sơ mi hình như có in mấy dòng chữ đang rưới vào đó một loại dầu quân dụng thời xưa."
    ###331#------
    show kuroe :
        offset(128,22)
        anchor(0,0)
    show bg31 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nằm giữa đống lửa đang bùng lên ấy, là những robot đồng hành xếp chồng chất lên nhau."
    ###332#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    hide kuroe
    hide bg31
    with dissolve
    voice "ovk/z1000/677.ogg"
    narrator "{size=180}\n{/size}「Uầy... sao họ có thể thản nhiên thiêu cháy một cỗ máy hình người như thế nhỉ...」"
    ###333#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi bất giác cau mày."
    ###334#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dẫu vốn biết đây chỉ là những bộ khung thế hệ cũ kiểu gì cũng bị vứt bỏ, và rằng đây chỉ là một cuộc biểu tình khác của đám người thất nghiệp, nhưng quả tình vẫn chẳng phải khung cảnh đáng xem gì cho cam."
    ###335#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/682.ogg"
    narrator "{size=180}\n{/size}「Có mang hình người hay không thì cũng đừng có đốt đi như vậy chứ. Không phân tách chúng đúng cách thì sẽ khó tái chế lắm.」"
    ###336#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/684.ogg"
    narrator "{size=180}\n{/size}「Vấn đề đâu có nằm ở đó chứ?」"
    ###337#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/686.ogg"
    narrator "{size=180}\n{/size}「Mà, chuyện này thuộc phạm trù tranh chấp thương mại hơn là vấn đề tuyển dụng.」"
    ###338#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/688.ogg"
    narrator "{size=180}\n{/size}「Cứ như thế này thì rồi sẽ lan tới cả cộng đồng những người có việc làm, tiếp đó trong tương lai gần, việc một phong trào bài trừ robot tương tự thế này xảy ra cũng không lạ.」"
    ###339#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/690.ogg"
    narrator "{size=180}\n{/size}「Quả thật, có nghĩ lạc quan thì vẫn thấy một robot lang thang ngoài đường đúng là rủi ro.」"
    ###340#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/695.ogg"
    narrator "{size=180}\n{/size}(Không có phong trào tẩy chay thì vấn đề cũng đã chất đống rồi.)"
    ###341#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play music "nwa/bgm03.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/697.ogg"
    narrator "{size=180}\n{/size}「Mà, chỉ cần chúng ta để mắt đến con bé thì mọi chuyện sẽ ổn thôi.」"
    ###342#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hiện tại, cả hai đang ngồi trên ghế nhựa trong khu tiếp tân."
    ###343#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cung thiên văn nằm trên tầng thượng của trung tâm bách hóa Hanabishi và chỉ có duy nhất một lối vào."
    ###344#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nói cách khác, nếu cô bé muốn xuống tầng thì chắc chắn sẽ phải đi qua khu vực này."
    ###345#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/703.ogg"
    narrator "{size=180}\n{/size}「Ngay từ đầu mình làm thế này có phải ngon rồi không.」"
    ###346#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/705.ogg"
    narrator "{size=180}\n{/size}「...Chị không thấy cách xử lý này vốn dĩ đã sai sai rồi à?」"
    ###347#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/707.ogg"
    narrator "{size=180}\n{/size}「Tình huống khẩn cấp mà, biết sao được. Thế Gorou-kun canh đến bốn giờ nhé, nhờ cậu đấy.」"
    ###348#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/709.ogg"
    narrator "{size=180}\n{/size}「Công việc của tôi cũng đang chất đống kia mà.」"
    ###349#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/711.ogg"
    narrator "{size=180}\n{/size}「Việc thì ngồi đây làm cũng được chứ gì? Ở đây cậu vẫn kết nối được với dữ liệu máy chủ đúng không?」"
    ###350#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou cạn lời khi nhìn vào con thiết bị đầu cuối quá mức lỗi thời đến độ gần như không thể sử dụng, còn Satomi thì biểu lộ một khuôn mặt sảng khoái hiếm thấy."
    ###351#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cho đến hiện tại thì buổi trình chiếu vẫn chưa có vấn đề gì."
    ###352#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thuyết trình viên hiện thời Mayuzumi Chihaya dù chỉ làm bán thời gian nhưng lại là một người vô cùng điềm tĩnh, nên cô cũng không cảm thấy quá lo lắng."
    ###353#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Akane đang giám sát Yumemi, người hiện đứng cạnh cửa thoát hiểm để đề phòng có khách rời khỏi chỗ trong lúc trình chiếu."
    ###354#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Phân chia công việc thế này rồi thì làm sao còn chuyện gì xảy ra được nữa."
    ###355#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nĐiều duy nhất khiến cô để tâm là lượng khách hàng vẫn ít ỏi như thường lệ."
    ###356#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se014.wav"
    voice "ovk/z1000/720.ogg"
    narrator "{size=180}\n{/size}「Thế thôi, tôi quay lại phòng chờ nhé...」"
    ###357#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Vừa dứt lời, cô chợt cảm thấy một sự hiện diện đáng lo ngại đằng sau quầy."
    ###358#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play music "nwa/bgm05.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/724.ogg"
    narrator "{size=180}\n{/size}「Bà cô ơi bà cô!」"
    ###359#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Rụt rè quay về phía giọng nói phát ra, cô chợt thấy hai cậu bé mang ba lô và khoác trên người bộ đồng phục từ một trường tiểu học công lập."
    ###360#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/728.ogg"
    narrator "{size=180}\n{/size}「Keita-kun... Yuusuke-kun...」"
    ###361#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không ai làm việc trong Bảo tàng cung thiên văn Hanabishi mà không biết tới sự khủng khiếp của bộ đôi này."
    ###362#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/732.ogg"
    narrator "{size=180}\n{/size}「Bà cô nè, Yumemi-chan có ở đây không?」"
    ###363#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thằng bé hỏi bằng năng lượng tràn trề, rõ là thiếu kiên nhẫn trong lúc đặt chiếc ba lô da bóng lộn của mình xuống."
    ###364#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/736.ogg"
    narrator "{size=180}\n{/size}「Bây giờ Yumemi-chan đang làm việc mất rồi. Hôm nay các em chơi cùng anh Gorou đây có được không?」"
    ###365#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô quay lại với một nụ cười méo xệch, chỉ để thấy chiếc ghế xếp bên cạnh đã trống rỗng tự lúc nào, dù vẫn còn hơi ấm người ngồi."
    ###366#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/740.ogg"
    narrator "{size=180}\n{/size}「Ặc, chạy mất rồi...」"
    ###367#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    narrator "{size=180}\n{/size}Dù là hiện tại hay quá khứ, thì trẻ em vẫn luôn là khách hàng yêu thích của cung thiên văn."
    ###368#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không như các cặp đôi nhiều khả năng chỉ tới xem một lần hoặc các nhân viên văn phòng ngay từ đầu đến chỉ để ngủ trưa, trẻ con rất nhiệt tình xem chương trình, và một khi đã thích thì chúng sẽ quay lại nhiều lần nữa."
    ###369#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù có là giá vé trẻ em thì một người vẫn là một người đấy, không đùa được đâu."
    ###370#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nNhưng trong số đó, vẫn có vài đứa cần phải đặc biệt chú ý."
    ###371#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đặc biệt, bộ đôi này thường trực tiếp chạy từ trường tiểu học tới để chơi đùa... hay nói đúng hơn, là để trêu chọc những thuyết trình viên ngây thơ."
    ###372#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chúng chắc chắn nằm trong tốp 10 đứa trẻ hư nhất mà Satomi tiếp xúc kể từ khi khai trương."
    ###373#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/749.ogg"
    narrator "{size=180}\n{/size}「Thế thì bà cô cũng được. Dạy bọn này học đi!」"
    ###374#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/751.ogg"
    narrator "{size=180}\n{/size}「Không phải \"Bà cô\", phải gọi là \"Chị\", nghe chưa.」"
    ###375#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/753.ogg"
    narrator "{size=180}\n{/size}「Nè nè, xem con robot này đi, ngầu phết nhờ? Chỉ cần bấm nút này là nó sẽ đấm một phát đấy!」"
    ###376#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/755.ogg"
    narrator "{size=180}\n{/size}「Thôi được rồi, chị sẽ giúp lần lượt, lần lượt―― khoan, đây chẳng phải câu hỏi môn thực hành xã hội à?」"
    ###377#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/757.ogg"
    narrator "{size=180}\n{/size}「Đã bảo chuyên môn của chị là thần thoại với trời sao cơ mà?」"
    ###378#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/759.ogg"
    narrator "{size=180}\n{/size}「Ơ kìa, bà cô không biết cái này hởở. Yumemi-chan thì cái gì cũng biết luôn đó.」"
    ###379#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/761.ogg"
    narrator "{size=180}\n{/size}「Chị biết rồi! Mà này, đừng gọi \"bà cô\" nữa, gọi \"chị\" nghe chưa!」"
    ###380#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/763.ogg"
    narrator "{size=180}\n{/size}「Ờ để xem nào... là thời Yayoi nên chắc đáp án 3 \"Trồng lúa\"... gượm đã, để chị làm hộ thì còn ý nghĩa gì nữa?」"
    ###381#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se015.wav"
    voice "ovk/z1000/765.ogg"
    narrator "{size=180}\n{/size}「Jet screw punch!」"
    ###382#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se016.wav"
    voice "ovk/z1000/767.ogg"
    narrator "{size=180}\n{/size}「Ái đau đau! Chị đầu hàng chị đầu hàng, đừng có đánh nữa!」"
    ###383#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trong khi đảm đương vai trò giáo viên phụ đạo và quái vật không gian cùng một lúc, Satomi tỏ ra quan ngại sâu sắc về sự khó khăn và phi lý của công việc thuyết trình viên tại cung thiên văn."
    ###384#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/774.ogg"
    narrator "{size=180}\n{/size}(Phải công nhận là tiếp đón những ngài khách bất kham kiểu này đúng là chuyên môn của Yumemi.)"
    ###385#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nghĩ vậy khiến cô thấy mình càng đáng thương hơn."
    ###386#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sau 15 phút vật lộn với lũ nhóc, cô đã chạm tới giới hạn, cả về mặt thể chất lẫn tinh thần."
    ###387#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/780.ogg"
    narrator "{size=180}\n{/size}「Này, buổi chiếu sắp xong rồi, chị gái phải quay lại công việc đây...」"
    ###388#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô nhìn ra cuối hành lang mà nói như van xin, đúng lúc ấy..."
    ###389#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se017.wav"
    narrator "{size=180}\n{/size}Mái tóc ngắn tung bay, Akane chạy tới chỗ cô."
    ###390#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Những tưởng trời cuối cùng cũng thương mình, thì chợt cô cảm thấy có gì đó không ổn."
    ###391#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/786.ogg"
    narrator "{size=180}\n{/size}「Em xin lỗi, cho em hỏi Yumemi-chan có qua đây không ạ~ mà hình như ở đây có vài vị khách không mời mà đến.」"
    ###392#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se015.wav"
    voice "ovk/z1000/788.ogg"
    narrator "{size=180}\n{/size}「Jet Buster Missile!」"
    ###393#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se016.wav"
    narrator "{size=180}\n{/size}Akane giật mình khi bị một đầu đạn bằng nhựa bay tới tấn công."
    ###394#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/792.ogg"
    narrator "{size=180}\n{/size}「...Yumemi-chan?」"
    ###395#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/794.ogg"
    narrator "{size=180}\n{/size}「Không có ở đấy á?」"
    ###396#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/796.ogg"
    narrator "{size=180}\n{/size}「Vâng, lúc em dẫn khách đi vệ sinh về thì đã không thấy con bé đâu rồi...」"
    ###397#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/798.ogg"
    narrator "{size=180}\n{/size}「Hảảảả?! Chị ở đây nãy giờ cơ mà?」"
    ###398#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cảm thấy bầu không khí có chút kỳ lạ, hai cậu bé đang thực hiện những hành vi bạo ngược tột cùng chợt dừng lại nhìn nhau."
    ###399#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/802.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan vừa đi ra ngoài xong nhờ~?」"
    ###400#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/804.ogg"
    narrator "{size=180}\n{/size}「Ờ, vừa đi xong.」"
    ###401#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/806.ogg"
    narrator "{size=180}\n{/size}「.....」"
    ###402#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/808.ogg"
    narrator "{size=180}\n{/size}「Ahahahaha...」"
    ###403#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi và Akane không khỏi bật cười thất thần."
    ###404#------
    jump chapter_6

label chapter_6:
    scene bg02
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide bg11
    hide kr_f
    hide kr_b
    with fade
    play music "nwa/bgm10.wav" fadeout 0.5 fadein 0.5
    play sound "nwa/se018.wav"
    narrator "{size=180}\n{/size}Với bộ đồng phục thuyết trình viên cùng áo choàng trên người, Satomi bước ra ngoài cửa chính."
    ###405#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nKhông cần vội quá mà làm gì. "
    ###406#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Theo như tốc độ di chuyển của Yumemi thì hẳn cô bé vẫn chưa đi quá xa, và nhờ vào thiết bị đầu cuối định vị"
    ###407#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hơn nữa hệ thống có cả chìa khóa và phím bấm để phát tín hiệu dừng trong trường hợp khẩn cấp."
    ###408#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/825.ogg"
    narrator "{size=180}\n{/size}(...Cứ tưởng cuối cùng cũng được nghỉ xả hơi, mà thôi kệ vậy...)"
    ###409#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trước những bước chân hối hả đầy bực dọc của Satomi, người trên đường chỉ còn biết né sang bên."
    ###410#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi hiểu rõ hơn ai hết rằng sẽ thật vô nghĩa khi nổi nóng với Yumemi."
    ###411#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù vậy, nỗi thất vọng vẫn ngự trị trong cô."
    ###412#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/840.ogg"
    narrator "{size=180}\n{/size}(Yumemi chắc chắn sẽ không bỏ đi.)"
    ###413#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/841.ogg"
    narrator "{size=180}\n{/size}(Cho dù điều kiện công việc có tồi tệ đến mức nào, con bé nhất định sẽ không phàn nàn.)"
    ###414#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/842.ogg"
    narrator "{size=180}\n{/size}(Yumemi vốn được tạo ra như vậy mà.)"
    ###415#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/843.ogg"
    narrator "{size=180}\n{/size}(Ngoại trừ yêu cầu làm hại con người, thì robot không có quyền từ chối mệnh lệnh nào cả.)"
    ###416#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/844.ogg"
    narrator "{size=180}\n{/size}(Dù có là mệnh lệnh lố bịch đến mức nào, thì robot cũng không thể lý giải hay đánh giá được.)"
    ###417#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/845.ogg"
    narrator "{size=180}\n{/size}(Nếu vậy thì bây giờ, mình đang đuổi theo thứ gì đây?)"
    ###418#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/846.ogg"
    narrator "{size=180}\n{/size}(Nếu không phải chán ghét, thì tại sao mình lại không mừng vui chút nào?)"
    ###419#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi không hiểu."
    ###420#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    narrator "{size=180}\n{/size}Bỗng, cô trông thấy bóng lưng quen thuộc."
    ###421#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    play sound "nwa/se019.wav"
    narrator "{size=180}\n{/size}Qua ánh đèn đầy bụi, Yumemi đang lang thang trên vỉa hè lát gạch trong buổi chiều tà."
    ###422#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tà váy của cô bé ― vốn đóng vai trò như khe tản nhiệt ― được xẻ thành năm phần, để lộ đôi chân quyến rũ."
    ###423#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mái tóc dài rủ xuống hai bên, nhẹ nhàng đong đưa theo từng nhịp bước."
    ###424#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nNom như cô không hề lạc lối trong nơi mình cần đi, hay việc mình phải làm."
    ###425#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    voice "ovk/z1000/854.ogg"
    narrator "{size=180}\n{/size}「Yume...」"
    ###426#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi toan gọi Yumemi, nhưng vì lý do nào đó mà cô ngừng lại."
    ###427#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/861.ogg"
    narrator "{size=180}\n{/size}(Thử đi theo con bé xem sao.)"
    ###428#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô đi chậm lại và giữ nhịp thở của mình nhẹ hơn."
    ###429#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nếu chú ý quan sát hành động, thì biết đâu sẽ tìm ra được nguyên nhân khiến cô bé cứ \"mất tích\" không chừng."
    ###430#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô tự biện hộ như vậy."
    ###431#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/871.ogg"
    narrator "{size=180}\n{/size}(Thật ra, có thể là mình đang sợ hãi.)"
    ###432#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/872.ogg"
    narrator "{size=180}\n{/size}(Sợ rằng Yumemi sẽ rời xa nơi làm việc... rời xa mình mà chẳng màng ngoảnh lại.)"
    ###433#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    hide kr_f
    hide kr_b
    with dissolve
    play sound "nwa/se019.wav"
    narrator "{size=180}\n{/size}Như muốn đi ngược lại với dòng người hướng về phía nhà ga, Yumemi rảo bước theo hướng tây bắc trên con đường chỉ cách khu phồn hoa một con phố."
    ###434#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trước mặt tiền của một cửa hàng đồ điện lớn, những mẫu robot đồng hành thế hệ mới nhất khoác lên mình nhiều bộ trang phục diễm lệ đang quảng cáo một thiết bị truyền hình đa chiều độ nét cực cao."
    ###435#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Màn hình demo đang chiếu tin tức về những phi thuyền không gian bắt đầu khai thác lộ trình đến cảng Mặt Trăng đầu tiên."
    ###436#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Các tiếp viên mặc đồng phục đang đứng tươi cười dọc lối đi cho khách cũng là những robot đồng hành được chế tác tại cùng một nơi với chỗ phi thuyền đó."
    ###437#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    voice "ovk/z1000/883.ogg"
    narrator "{size=180}\n{/size}(Quả thật, vũ trụ đang ngày càng gần chúng ta hơn.)"
    ###438#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/884.ogg"
    narrator "{size=180}\n{/size}(Nhất là với một bộ phận người giàu, kỹ sư thuộc địa và quân nhân.)"
    ###439#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    narrator "{size=180}\n{/size}Một cậu nhân viên văn phòng băng qua đường mà không thèm nhìn đèn tín hiệu."
    ###440#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,24)
        zoom 1
        ease .06 xoffset -830+24
        ease .06 xoffset -830+-24
        ease .05 xoffset -830+20
        ease .05 xoffset -830+-20
        ease .04 xoffset -830+16
        ease .04 xoffset -830+-16
        ease .03 xoffset -830+12
        ease .03 xoffset -830+-12
        ease .02 xoffset -830+8
        ease .02 xoffset -830+-8
        ease .01 xoffset -830+4
        ease .01 xoffset -830+-4
        ease .01 xoffset -830+0
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
        ease .06 xoffset -830+24
        ease .06 xoffset -830+-24
        ease .05 xoffset -830+20
        ease .05 xoffset -830+-20
        ease .04 xoffset -830+16
        ease .04 xoffset -830+-16
        ease .03 xoffset -830+12
        ease .03 xoffset -830+-12
        ease .02 xoffset -830+8
        ease .02 xoffset -830+-8
        ease .01 xoffset -830+4
        ease .01 xoffset -830+-4
        ease .01 xoffset -830+0
    show yu_f 22 zorder 4: 
        offset(-830,24)
        zoom 1
        ease .06 xoffset -830+24
        ease .06 xoffset -830+-24
        ease .05 xoffset -830+20
        ease .05 xoffset -830+-20
        ease .04 xoffset -830+16
        ease .04 xoffset -830+-16
        ease .03 xoffset -830+12
        ease .03 xoffset -830+-12
        ease .02 xoffset -830+8
        ease .02 xoffset -830+-8
        ease .01 xoffset -830+4
        ease .01 xoffset -830+-4
        ease .01 xoffset -830+0
    with dissolve
    play sound "nwa/se021.wav"
    narrator "{size=180}\n{/size}Anh ta định bước lên lề đường qua khoảng trống giữa thanh chắn, để rồi vai lại chạm vào Yumemi đang đi trên mép lề."
    ###441#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/889.ogg"
    narrator "{size=180}\n{/size}「...muốn gì?」"
    ###442#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/891.ogg"
    narrator "{size=180}\n{/size}「Tôi thật sự xin lỗi, anh có sao không ạ?」"
    ###443#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi ngay lập tức dừng lại và cúi thấp đầu một cách không cần thiết."
    ###444#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se022.wav"
    narrator "{size=180}\n{/size}Khi nhận ra mình vừa va phải robot, mặt anh chàng lộ rõ vẻ lúng túng và nhanh chóng bỏ đi."
    ###445#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/896.ogg"
    narrator "{size=180}\n{/size}「Thật mừng vì anh không sao cả.」"
    ###446#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/898.ogg"
    narrator "{size=180}\n{/size}「Giờ thì, tôi xin phép ạ.」"
    ###447#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play sound "nwa/se019.wav"
    narrator "{size=180}\n{/size}Yumemi nói với khoảng không rồi tiếp tục cất bước."
    ###448#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\n――và đột nhiên khựng lại."
    ###449#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi suýt nữa vấp chân, vội vã náu mình đằng sau biển hiệu của quán rượu."
    ###450#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô lo lắng, chẳng lẽ mình đã bị phát hiện rồi sao."
    ###451#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi tôn kính cúi chào hai bên trái phải, rồi đặt lòng bàn tay này lên mu bàn tay kia."
    ###452#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    play music "nwa/bgm16.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/906.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###453#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/908.ogg"
    narrator "{size=180}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###454#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Với nụ cười mơ màng, cô bé mời gọi những người qua đường."
    ###455#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nNgay từ lần đầu nhận việc, cô gái này đã thu hút được một đám đông lớn."
    ###456#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Robot tiếp tân loại người máy thực tiễn tiên phong được chế tạo hoàn toàn dựa trên cơ sở Luật Cơ bản về việc vận hành những cỗ máy tự động mô phỏng con người, hay thường được gọi là \"Luật Robot\"."
    ###457#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cả người lớn và trẻ em đều dõi theo nhất cử nhất động của Yumemi, không giấu được sự tò mò và phấn khích."
    ###458#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hẳn mọi người đều mường tượng ra biết bao viễn cảnh tương lai thông qua cô robot dạng thiếu nữ trông chẳng khác nào con người này."
    ###459#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thấm thoát mười năm trôi qua, robot giờ đây đã trở nên phổ biến."
    ###460#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Họ vừa là thành phần thiết yếu trong xã hội, nhưng đồng thời họ cũng gây ra đủ loại vấn đề."
    ###461#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù vậy, ấy là lẽ tất yếu."
    ###462#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nLà điều không thể tránh khỏi."
    ###463#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Những con người sáng mắt lên khi lần đầu tiên chạm vào xe ô tô chắc chẳng bao giờ ngờ tới vấn đề ô nhiễm hay tai nạn giao thông mà nó đem lại."
    ###464#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/921.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?...」"
    ###465#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Sau khi lặp lại bài văn hai lần, Yumemi dừng cử động một lúc, vẫn giữ nguyên nụ cười thiên thần."
    ###466#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một khi xác định được người quan tâm tới mình, cô bé sẽ in tờ rơi chương trình của ngày hôm nay, kéo ra khỏi khe thẻ ở tai trái và đưa chúng cho họ."
    ###467#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đương nhiên, không ai đến gần cô cả."
    ###468#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play sound "nwa/se019.wav"
    narrator "{size=180}\n{/size}Yumemi tiếp bước."
    ###469#------
    show bg21b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nSatomi đi theo."
    ###470#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    hide bg21b
    with dissolve
    play music "nwa/bgm11.wav" fadeout 0.5 fadein 0.5
    narrator "{size=180}\n{/size}Vụ bám đuôi lạ lùng đột ngột kết thúc."
    ###471#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCách xa con phố nhộn nhịp khoảng 2 km về phía tây bắc, là một khu phố với hàng dài những căn chung cư cũ xếp san sát nhau."
    ###472#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Lúc này đây, Satomi mới đâm lo rằng nơi này đã cách quá xa chỗ làm việc."
    ###473#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nĐột nhiên, Yumemi dừng bước."
    ###474#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé di chuyển phần trên cổ, nhìn xung quanh như đang tìm kiếm gì đó."
    ###475#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCử chỉ này vô cùng quen thuộc."
    ###476#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cái hồi mà đến những hành vi cơ bản vẫn còn vụng về, mỗi lần pin yếu Yumemi sẽ đứng yên bất động, giữ nguyên tư thế chờ, làm cho mọi người ai cũng hoảng hồn."
    ###477#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Do đó Satomi đã dặn dò cô bé."
    ###478#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Rằng 『Khi nào pin yếu hoặc chuẩn bị vào chế độ ngủ thì ráng tìm chỗ nào mà ngồi xuống.』"
    ###479#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    narrator "{size=180}\n{/size}Ở cuối ngã ba có một công viên nhỏ."
    ###480#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se023.wav"
    narrator "{size=180}\n{/size}Đứng trước lối vào, Yumemi nhìn chằm chằm hai thanh chắn xe xếp song song nhau, chừng như đang phán đoán xem nó có đỡ được trọng lượng của mình không, rồi như đã quyết định, cô bé tới đó, ngồi xuống và ngừng cử động."
    ###481#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chẳng khác nào một vở kịch câm của nghệ sĩ đường phố."
    ###482#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/955.ogg"
    narrator "{size=180}\n{/size}「Hết pin mất rồi à, chết thật...」"
    ###483#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi lẩm bẩm."
    ###484#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/963.ogg"
    narrator "{size=180}\n{/size}(Dạo gần đây xô bồ quá nên mình quên mất không để ý lượng pin còn lại...)"
    ###485#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/964.ogg"
    narrator "{size=180}\n{/size}(Huống hồ mình biết thừa việc liên tục tự động đi bộ sẽ rất hao pin rồi mà...)"
    ###486#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chắc vẫn có thể giao tiếp và truyền tin, song Yumemi lại không có khả năng tự mình gọi dịch vụ sạc điện."
    ###487#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trong chế độ tiết kiệm pin, cô bé thậm chí còn chẳng thể đi bộ, nên nếu cứ để yên thì cô sẽ ngồi đó vĩnh viễn mất."
    ###488#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/970.ogg"
    narrator "{size=180}\n{/size}「Hờ...」"
    ###489#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kr_f
    hide kr_b
    with dissolve
    narrator "{size=180}\n{/size}Sau khi thở dài lần thứ bao nhiêu chẳng rõ, Satomi toan tiếp cận cô bé."
    ###490#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se024.wav"
    extend "\nThì chợt, một bé gái chạy lon ton ra khỏi công viên."
    ###491#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé đi giày đỏ, đội mũ đỏ và mặc chiếc áo khoác xinh xắn làm từ len nhân tạo vốn từng là mốt một thời."
    ###492#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thấy Yumemi không cử động gì, cô bé tỏ vẻ lo lắng."
    ###493#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 11 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/977.ogg"
    narrator "{size=180}\n{/size}「Chị ơi, chị có sao không?」"
    ###494#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/979.ogg"
    narrator "{size=180}\n{/size}「Vâng, do tình trạng thiếu hụt năng lượng mà một vài chức năng đã bị giới hạn, nhưng tôi không dò ra được bộ phận nào bị hỏng hay trục trặc cả.」"
    ###495#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi trả lời một cách nghiêm túc."
    ###496#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nBiểu cảm của cô trông cứ đơ đơ sao đó."
    ###497#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/984.ogg"
    narrator "{size=180}\n{/size}「Tôi xin lỗi vì đã để em phải lo lắng.」"
    ###498#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Vẫn trong tư thế ngồi, cô cúi đầu và bày tỏ niềm tiếc nuối sâu sắc."
    ###499#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/988.ogg"
    narrator "{size=180}\n{/size}「？？」"
    ###500#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nét mặt của cô bé cho thấy em chẳng hiểu mô tê gì cả."
    ###501#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nSatomi chạy đến cạnh em, quỳ xuống cho ngang chiều cao của em rồi từ tốn nói."
    ###502#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/993.ogg"
    narrator "{size=180}\n{/size}「Em không phải lo đâu, chị gái này là robot mà.」"
    ###503#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/995.ogg"
    narrator "{size=180}\n{/size}「Chị ấy... là robot ư?」"
    ###504#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé tròn mắt và nhìn chằm chằm vào Yumemi."
    ###505#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/999.ogg"
    narrator "{size=180}\n{/size}「Vâng. Tôi là một robot.」"
    ###506#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi trông yếu ớt hơn mọi khi, song vẫn nở nụ cười đầy tự hào."
    ###507#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCô bé kiễng chân, giơ nắm đấm nhỏ xíu của mình lên trời..."
    ###508#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se025.wav"
    voice "ovk/z1000/1004.ogg"
    narrator "{size=180}\n{/size}「Hây!」"
    ###509#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Rồi đánh vào đầu Yumemi/"
    ###510#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nTrong một khoảnh khắc, Satomi không hiểu chuyện gì đang xảy ra."
    ###511#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se026.wav"
    voice "ovk/z1000/1009.ogg"
    narrator "{size=180}\n{/size}「Hây! Hây! Hây!...」"
    ###512#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hai lần, ba lần, bốn lần, cô bé đánh Yumemi không ngừng nghỉ."
    ###513#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi ngây người ra, chẳng rõ phải phản ứng thế nào."
    ###514#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Thấy không ăn thua, cô bé giơ cánh tay cao hơn."
    ###515#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play music "nwa/bgm06.wav" fadeout 0.5 fadein 0.5
    play sound "nwa/se027.wav"
    voice "ovk/z1000/1015.ogg"
    narrator "{size=180}\n{/size}「Đừng...」"
    ###516#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi bừng tỉnh, lập tức can thiệp."
    ###517#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mặc dù bị bao phủ trong các sợi trao đổi nhiệt được mô phỏng lại giống như tóc, nhưng khung bên trong vẫn được tạo thành từ hợp kim titan và magiê."
    ###518#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù chỉ là lực đánh của một đứa trẻ, thì đánh liên tục như thế cũng không thể nào bình an vô sự được."
    ###519#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1021.ogg"
    narrator "{size=180}\n{/size}「Đưa tay chị xem nào? Em không bị thương chứ?」"
    ###520#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô mở bàn tay phải nắm chặt của cô bé ra và kiểm tra."
    ###521#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nMột bàn tay xinh xắn, tựa hồ chiếc lá thu gấp theo kiểu origami."
    ###522#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đầu ngón tay của em đã ửng đỏ."
    ###523#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nBé gái chực khóc."
    ###524#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Song lại không khóc."
    ###525#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCô bé đang quyết liệt kìm nén cảm xúc."
    ###526#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1030.ogg"
    narrator "{size=180}\n{/size}「Cha bảo...」"
    ###527#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chừng như em đang giận dữ."
    ###528#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nBằng tông giọng yếu ớt, em lên tiếng với Satomi."
    ###529#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1035.ogg"
    narrator "{size=180}\n{/size}「Cha nói, tất cả chỉ vì robot... mà cha bị mất việc...」"
    ###530#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đôi mắt vẫn nhìn thẳng vào Satomi, lệ từ từ đọng trên khóe mi em."
    ###531#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1039.ogg"
    narrator "{size=180}\n{/size}「Yukino-chan, dừng lại đi con!」"
    ###532#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một người phụ nữ khoác theo túi mua đồ bằng vải kéo cô bé ra khỏi Satomi như muốn lôi em đi."
    ###533#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Hẳn là mẹ của cô bé ấy."
    ###534#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    extend "\nCô nhìn về phía Satomi ― vẫn đang quỳ gối ― ra chiều muốn cầu xin gì đó, rồi khẽ cúi đầu."
    ###535#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se028.wav"
    narrator "{size=180}\n{/size}Sau đó cô kéo tay bé gái và rời khỏi công viên."
    ###536#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trước khi rẽ vào con hẻm, người mẹ một lần nữa nhìn về phía này và cúi đầu xin lỗi."
    ###537#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Khi thân ảnh cô đã khuất khỏi tầm nhìn, Satomi vẫn chìm trong suy tư."
    ###538#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1052.ogg"
    narrator "{size=180}\n{/size}(Nếu cô bé kia lẫn người mẹ mà thái quá hơn rồi ra sức khiển trách mình và Yumemi...)"
    ###539#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1054.ogg"
    narrator "{size=180}\n{/size}(...thì có lẽ cảm xúc của mình đã không phức tạp thế này.)"
    ###540#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 24 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Yumemi vẫn đang ngồi trên thanh chắn xe như thể chưa có chuyện gì xảy ra."
    ###541#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1058.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan, em có đau không?」"
    ###542#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 23 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1060.ogg"
    narrator "{size=180}\n{/size}「Không ạ, xin chớ lo lắng. Tôi là một robot, vậy nên tôi không thể cảm thấy đau đớn được.」"
    ###543#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé nở nụ cười thanh nhã, như đang quan tâm tới Satomi."
    ###544#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1069.ogg"
    narrator "{size=180}\n{/size}(Yumemi hẳn là không hề biết.)"
    ###545#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1070.ogg"
    narrator "{size=180}\n{/size}(Rằng nỗi đau em ấy đáng ra phải nhận, đều đã được những người liên quan đến em ấy hứng chịu cả rồi.)"
    ###546#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1071.ogg"
    narrator "{size=180}\n{/size}(Để những người yêu quý robot, và những người chán ghét chúng đều được bình đẳng.)"
    ###547#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1073.ogg"
    narrator "{size=180}\n{/size}「Thôi thì, trước hết mình phải về cái đã.」"
    ###548#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1075.ogg"
    narrator "{size=180}\n{/size}「À mà, em không sạc điện thì sao mà đi được nhỉ.」"
    ###549#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1077.ogg"
    narrator "{size=180}\n{/size}「Vâng, tôi thành thật xin lỗi. Pin dự phòng cũng sắp cạn, nên tôi không thể nào đi lại được nữa.」"
    ###550#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1079.ogg"
    narrator "{size=180}\n{/size}「Vậy là coi như liệt toàn thân rồi còn gì. Hết chuyện này tới chuyện khác, gì cũng đến tay mình...」"
    ###551#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Việc kiểm tra và thay thế nguồn điện dự phòng là bắt buộc, nhưng chính Satomi đã quyết định để yên như thế do ngân sách không cho phép."
    ###552#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Rồi chuyện này xảy ra, và Satomi chẳng thể nào một mình mang cô bé ra trạm sạc được, thật chẳng có cách nào diễn tả tốt hơn bằng \"tự làm tự chịu\"."
    ###553#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se029.wav"
    voice "ovk/z1000/1084.ogg"
    narrator "{size=180}\n{/size}「...Giờ đâu phải lúc để phàn nàn chứ. Để chị gọi xe, em ngồi chờ chút nhé.」"
    ###554#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 11 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Cô nói, đoạn rút điện thoại di động ra khỏi túi áo khoác."
    ###555#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không có tiếng đáp lại."
    ###556#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1089.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan?」"
    ###557#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mặc cho cô gọi tên thì Yumemi cũng không cử động nữa."
    ###558#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nVẫn với biểu cảm như mọi khi trên khuôn mặt, cô bé đóng băng theo đúng nghĩa đen."
    ###559#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Có vẻ như pin đã hoàn toàn cạn rồi."
    ###560#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Bình thường cô bé sẽ cảnh báo đếm ngược 100 giây trước khi hết pin, nhưng lần này có vẻ như đến thời gian để làm vậy còn không có."
    ###561#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Bất kể có hiểu cho cảm nhận của Satomi hay không, thì cô robot rắc rối kia cứ thế trở lại thành một vật thể vô tri cỡ người thật, mặc kệ sự đời có ra sao."
    ###562#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1097.ogg"
    narrator "{size=180}\n{/size}「Trời ạ...」"
    ###563#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi đấm nhẹ vào cái đầu đá kia."
    ###564#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nQuả nhiên là có hơi đau một chút."
    ###565#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi cất điện thoại đi."
    ###566#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    hide kr_f
    hide kr_b
    with dissolve
    extend "\nCô kéo áo khoác lên, rồi ngồi xuống thanh chắn xe bên cạnh Yumemi."
    ###567#------
    scene black
    show ev01a_movie :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide bg20
    with fade
    play music "nwa/bgm12.wav" fadeout 0.5 fadein 0.5
    narrator "{size=180}\n{/size}Thời khắc chạng vạng đang đến gần."
    ###568#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô cảm nhận cái lạnh mơn trớn bờ má mình."
    ###569#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1115.ogg"
    narrator "{size=180}\n{/size}(Chắc mấy đứa nó đang chuẩn bị cho buổi chiếu cuối trong ngày nhỉ?)"
    ###570#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Những đồng nghiệp đứng ở quầy lễ tân, căn phòng hình cầu chưa được lấp đầy ghế bao nhiêu năm rồi chẳng rõ."
    ###571#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1119.ogg"
    narrator "{size=180}\n{/size}(Một nơi làm việc đáng ra phải được xác định là sự nghiệp cả đời...)"
    ###572#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1120.ogg"
    narrator "{size=180}\n{/size}(Vậy mà chỉ có mình mình và Yumemi là đang ngồi cách xa cái khuôn khổ thường nhật đó.)"
    ###573#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01a_movie
    with Dissolve(2.0)
    narrator "{size=180}\n{/size}Cô khẽ nghiêng tầm nhìn."
    ###574#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Bầu trời đô thị nhàn nhạt trầm buồn, khó mà gọi là mang sắc xanh, xuất hiện giữa khe hở những tòa chung cư cũ."
    ###575#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Khi cô còn nhỏ, cảm giác như nó trông rực rỡ và có nhiều gam màu sắc nét hơn hẳn."
    ###576#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1126.ogg"
    narrator "{size=180}\n{/size}「Có lẽ mình đã quên đi mục tiêu ban đầu mất rồi...」"
    ###577#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi lẩm bẩm."
    ###578#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1136.ogg"
    narrator "{size=180}\n{/size}(Sẽ là nói dối nếu bảo mình không có động cơ âm thầm, mong muốn tự mình tăng doanh thu trong lúc giám đốc đi vắng.)"
    ###579#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1137.ogg"
    narrator "{size=180}\n{/size}(Tìm cách bóc tách từng vấn đề và cải thiện chúng theo cảm tính, cốt để chốn sinh nhai này và bọn mình không bị bỏ rơi...)"
    ###580#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1138.ogg"
    narrator "{size=180}\n{/size}(Xem như đây là một dịp tốt để nhìn nhận lại vậy.)"
    ###581#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1139.ogg"
    narrator "{size=180}\n{/size}(...Là bọn mình... phải không nhỉ?)"
    ###582#------
    show bg35b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1140.ogg"
    narrator "{size=180}\n{/size}(Hay nói đúng ra, là chỉ mỗi mình mình?)"
    ###583#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide bg35b
    with dissolve
    voice "ovk/z1000/1142.ogg"
    narrator "{size=180}\n{/size}「Nè, Yumemi-chan.」"
    ###584#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi bắt chuyện với Yumemi trong lúc ngắm nhìn bầu trời tối dần."
    ###585#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1146.ogg"
    narrator "{size=180}\n{/size}「Em có mệt mỏi với công việc không?」"
    ###586#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không lời hồi đáp."
    ###587#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1150.ogg"
    narrator "{size=180}\n{/size}「Em không thích làm việc cùng bọn chị nữa sao?」"
    ###588#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù biết thừa rằng mình sẽ không nhận được câu trả lời, Satomi vẫn tiếp lời."
    ###589#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1154.ogg"
    narrator "{size=180}\n{/size}「Chị ấy nhé, chị từng tin rằng mình sẽ không bao giờ thay đổi.」"
    ###590#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1156.ogg"
    narrator "{size=180}\n{/size}「Chị đã luôn nghĩ, rằng vì mình thích những vì sao, vì mình thích cung thiên văn, nên mới có thể tiếp tục được công việc này.」"
    ###591#------
    show ev01b :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô nhắm mắt lại và hồi tưởng."
    ###592#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg33 :
        offset(128,22)
        anchor(0,0)
    hide ev01b
    hide sbw00_3
    hide sbw00_4
    hide sbw01
    with dissolve
    voice "ovk/z1000/1168.ogg"
    narrator "{size=180}\n{/size}(Hồi lên sáu, ba mẹ đã tặng mình một cuốn sách tranh về Thần thoại Hy Lạp làm quà sinh nhật.)"
    ###593#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1169.ogg"
    narrator "{size=180}\n{/size}(Hồi 11 tuổi, mình từng làm một cung thiên văn bằng giấy trong kỳ nghỉ hè và lần đầu tiên chiếu nó lên trần phòng.)"
    ###594#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1170.ogg"
    narrator "{size=180}\n{/size}(15 tuổi, ba mẹ đưa mình về quê tránh nóng, và đấy cũng là lần đầu tiên mình được thấy bầu trời sao đúng nghĩa.)"
    ###595#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1171.ogg"
    narrator "{size=180}\n{/size}(Năm 18 tuổi, nghe rằng có một cung thiên văn đang xây dựng trên sân thượng cửa hàng bách hóa địa phương và hiện tuyển chọn thuyết trình viên, nên dù hồi hộp quá chừng, mình vẫn gọi điện cho họ.)"
    ###596#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1172.ogg"
    narrator "{size=180}\n{/size}(Những bối rối, dằn vặt, và cả mâu thuẫn khi còn là lính mới.)"
    ###597#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1173.ogg"
    narrator "{size=180}\n{/size}(Nỗi căng thẳng khi lần đầu tiên được giao cho công việc thuyết trình một mình.)"
    ###598#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1174.ogg"
    narrator "{size=180}\n{/size}(Và cả cái ngày mà giám đốc lệnh cho mình giám sát cô bé robot đồng hành này nữa...)"
    ###599#------
    show ev01a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kuros
    hide bg33
    with dissolve
    narrator "{size=180}\n{/size}Cô mở mắt, và khẽ ngắm Yumemi."
    ###600#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tại nơi ngoại ô thành phố này, tại chốn ven đường lộng gió này, dẫu cho bản thân không thể tự mình cử động, thì cô bé ấy... cô bé ấy vẫn là người duy nhất mang vẻ vô tư, dịu dàng, trong sáng và hạnh phúc."
    ###601#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1179.ogg"
    narrator "{size=180}\n{/size}「Nhưng Yumemi-chan này, đừng bao giờ thay đổi em nhé.」"
    ###602#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nhẹ nhàng nói với khuôn mặt trông nghiêng đã cứng đờ lại kia."
    ###603#------
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1183.ogg"
    narrator "{size=180}\n{/size}「Dẫu cho một ngày nào đó chị phải rời đi, thì Yumemi-chan cũng đừng bao giờ thay đổi nhé.」"
    ###604#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01a
    with dissolve
    voice "ovk/z1000/1185.ogg"
    narrator "{size=180}\n{/size}「Xin thứ lỗi cho tôi, chị định rời công ty sao?」"
    ###605#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1187.ogg"
    narrator "{size=180}\n{/size}「Chị không có, nhưng mà...」"
    ###606#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sau câu trả lời, cô chợt nhận ra."
    ###607#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nYumemi đang nở nụ cười như chưa hề xảy ra chuyện gì."
    ###608#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01d
    with dissolve
    voice "ovk/z1000/1192.ogg"
    narrator "{size=180}\n{/size}「Oái, Yumemi-chan?!」"
    ###609#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1194.ogg"
    narrator "{size=180}\n{/size}「Tôi sẽ không bao giờ thay đổi, tôi sẽ mãi mãi làm việc ở đây, cùng với Satomi-san và mọi người.」"
    ###610#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đôi mắt nhựa của cô chuyển sang màu như vết dầu loang, thấu kính bên trong được lấy nét, và quan sát Satomi đang bối rối một cách điệu đà."
    ###611#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cứ như vừa bị lừa vậy."
    ###612#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1199.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan... không phải em vừa hết pin à?」"
    ###613#------
    show ev01f :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1201.ogg"
    narrator "{size=180}\n{/size}「Vâng. Nói chính xác thì, tôi có thể kéo dài khả năng hoạt động thêm 800 giây nữa trong chế độ tiết kiệm pin.」"
    ###614#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01f
    with dissolve
    voice "ovk/z1000/1203.ogg"
    narrator "{size=180}\n{/size}「Thế có nghĩa là em đã nói dối chị? Em có thể làm được việc đó ư?」"
    ###615#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1205.ogg"
    narrator "{size=180}\n{/size}「Thưa không. Tôi là một robot, nên tôi không thể nói dối.」"
    ###616#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô trả lời, quả quyết và kiên định."
    ###617#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1209.ogg"
    narrator "{size=180}\n{/size}「Hôm qua mọi người đã nói với tôi rằng, \"Thỉnh thoảng em nên lắng nghe Satomi-san than thở một chút nhé.\"」"
    ###618#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1211.ogg"
    narrator "{size=180}\n{/size}「Than thở?」"
    ###619#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1213.ogg"
    narrator "{size=180}\n{/size}「Vâng, mọi người bảo, \"Có những chuyện mà con người sẽ chỉ nói với robot, vì vậy nếu em ở một mình cùng Satomi-san, hãy giữ yên lặng và lắng nghe chị ấy than thở.\"」"
    ###620#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1215.ogg"
    narrator "{size=180}\n{/size}「Mọi người... nói vậy sao?」"
    ###621#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1217.ogg"
    narrator "{size=180}\n{/size}「Vâng, tôi xác định đây là một chỉ thị có liên quan mật thiết đến sức khỏe của Satomi-san, nên tôi đã đăng ký chuyện này là nhiệm vụ ưu tiên.」"
    ###622#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trước lời giải thích lưu loát của Yumemi, Satomi không khỏi ngạc nhiên song cũng thấy xấu hổ."
    ###623#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nếu biết cách sử dụng các mệnh lệnh ưu tiên, ta có thể điều khiển hành vi của Yumemi ― vốn không hề linh hoạt ― đến một mức độ nào đó."
    ###624#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đó là điều Satomi đã dạy các hậu bối của mình."
    ###625#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nNhưng cô chưa bao giờ nghĩ bọn họ sẽ áp dụng theo cách này."
    ###626#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01d
    with dissolve
    narrator "{size=180}\n{/size}Cô tưởng tượng ra những nét mặt tinh quái của đồng nghiệp tại nơi làm việc."
    ###627#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1228.ogg"
    narrator "{size=180}\n{/size}(Họ đều quan tâm tới mình trong khi mình thì chẳng làm được gì...)"
    ###628#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nghĩ đến đây, bất giác cô nhớ ra."
    ###629#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01e
    with dissolve
    voice "ovk/z1000/1232.ogg"
    narrator "{size=180}\n{/size}「Lẽ nào, việc em tự ý chạy ra ngoài thế này là để làm như vậy hả?」"
    ###630#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1234.ogg"
    narrator "{size=180}\n{/size}「Vâng?」"
    ###631#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Vẫn là cái cử chỉ khẽ nghiêng đầu như mọi khi."
    ###632#------
    show ev01d :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nRồi, cơ hồ vừa nghĩ ra gì đó..."
    ###633#------
    show ev01g :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01d
    with dissolve
    voice "ovk/z1000/1239.ogg"
    narrator "{size=180}\n{/size}「Tôi thành thật xin lỗi!」"
    ###634#------
    show ev01g :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1241.ogg"
    narrator "{size=180}\n{/size}「Giờ nghĩ lại, hành động của tôi đã vi phạm nghiêm trọng nguyên tắc công việc! Tôi thật sự... thật sự xin lỗi ạ!」"
    ###635#------
    show ev01g :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé khẩn khoản cúi đầu."
    ###636#------
    show ev01g :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Do chế độ tiết kiệm pin mà hành động của cô bé thiếu đi sự sắc sảo, nhưng cái cách cô đột ngột thay đổi thái độ vẫn luôn ngoạn mục như vậy."
    ###637#------
    show ev01h :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01g
    with dissolve
    narrator "{size=180}\n{/size}Không còn sốc và giận nữa, Satomi bật cười."
    ###638#------
    show ev01h :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1251.ogg"
    narrator "{size=180}\n{/size}(Thôi kệ vậy.)"
    ###639#------
    show ev01h :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1253.ogg"
    narrator "{size=180}\n{/size}(Làm gì có con người nào không có khuyết điểm kia chứ.)"
    ###640#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide ev01h
    with dissolve
    voice "ovk/z1000/1255.ogg"
    narrator "{size=180}\n{/size}「Chuyện này em nhớ giữ bí mật với mọi người nhé.」"
    ###641#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi ghé miệng vào tai ― dù rằng đương nhiên cô biết đó không phải tai mà là thiết bị thu sóng ― của người bạn thâm niên là robot và thì thầm."
    ###642#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1259.ogg"
    narrator "{size=180}\n{/size}「Nếu chị là con trai... nhất định chị sẽ cầu hôn Yumemi-chan đấy.」"
    ###643#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô duỗi tay phải ra, dịu dàng vuốt tóc Yumemi."
    ###644#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nChắc chỉ là nhầm tưởng thôi."
    ###645#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nhưng có cảm giác như cô bé ấy sẽ hạnh phúc khi cô làm vậy."
    ###646#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1265.ogg"
    narrator "{size=180}\n{/size}「Nhưng mà nhé, dù mình có kết hôn thì chị cũng sẽ không để Yumemi-chan phải nghỉ việc đâu.」"
    ###647#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1267.ogg"
    narrator "{size=180}\n{/size}「Đôi ta sẽ mãi làm việc trong cung thiên văn, cùng với nhau.」"
    ###648#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nói đoạn, cô chợt cảm thấy ngượng ngùng."
    ###649#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi thấu cảm điều ấy từ sâu thẳm con tim."
    ###650#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1275.ogg"
    narrator "{size=180}\n{/size}(Được mà như thế thì tuyệt thật.)"
    ###651#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi nhìn chằm chằm vào Satomi bằng vẻ mặt của một thiếu nữ ngây thơ."
    ###652#------
    show ev01e :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nSau đó, cô bé trả lời."
    ###653#------
    scene bg02
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide ev01e
    with fade
    voice "ovk/z1000/1280.ogg"
    narrator "{size=180}\n{/size}「Thành thật xin lỗi, tôi đã có hôn ước rồi ạ.」"
    ###654#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 06 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1282.ogg"
    narrator "{size=180}\n{/size}「Yumemi-chan...? Em vừa nói gì vậy?」"
    ###655#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1284.ogg"
    narrator "{size=180}\n{/size}「Vâng, tôi vừa nói, \"Thành thật xin lỗi, tôi đã có hôn ước rồi ạ.\"」"
    ###656#------
    show bg20 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé nhắc lại với khuôn mặt không thể nghiêm túc hơn."
    ###657#------
    jump chapter_7

label chapter_7:
    scene bg01
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide bg20
    hide kr_f
    hide kr_b
    with fade
    play music "nwa/bgm01.wav" fadeout 0.5 fadein 0.5
    voice "ovk/z1000/1293.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###658#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cung thiên văn trên tầng thượng của trụ sở chính trung tâm bách hóa Hanabishi, trước máy bán vé tại quầy lễ tân."
    ###659#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi vẫn đang mời gọi khách như thường lệ."
    ###660#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1298.ogg"
    narrator "{size=180}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###661#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Sau khi lặp lại câu nói nhiều lần, hành vi của Yumemi dần trở nên lóng ngóng."
    ###662#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé di chuyển phần trên cổ và quan sát xung quanh để đảm bảo rằng không có đồng nghiệp nào đang nhìn mình."
    ###663#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    narrator "{size=180}\n{/size}Đoạn, cô bé khẽ khàng rời khỏi chỗ chiếc máy bán vé."
    ###664#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nĐó là tật xấu mới đây của cô: rời bỏ nơi làm việc."
    ###665#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se031.wav"
    play sound "nwa/se032.wav"
    narrator "{size=180}\n{/size}Đúng lúc đó, khách hàng mới đẩy cửa kính và bước vào."
    ###666#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nTrông hai người như một cặp đôi cấp ba, hoặc đại học."
    ###667#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chàng trai có thân hình mảnh khảnh cùng mái tóc thẳng, và dù diện mạo của cậu không hẳn là lý tưởng, nhưng cậu lại có một cô bạn gái vừa trông đã toát lên vẻ mạnh mẽ."
    ###668#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cách ăn mặc của hai người có thể gọi là hợp thời trang."
    ###669#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cậu bạn trai vận chiếc áo khoác da quân đội theo lối cổ điển, còn bạn gái mặc váy ngắn cùng kiểu tóc sử dụng keo xịt màu trông như những người nổi tiếng sành điệu trên TV và đeo vòng bạc trên cổ tay."
    ###670#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Không ai trong hai người trông mong buổi chiếu, mặc dù họ đến cung thiên văn cùng nhau."
    ###671#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1311.ogg"
    narrator "{size=180}\n{/size}「Tôi đã luôn chờ bạn.」"
    ###672#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi cất lời vô cùng tự nhiên, và mỉm cười với cậu bạn trai."
    ###673#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCậu ta hình như định nói gì đó, nhưng lại chẳng thốt nên lời."
    ###674#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Trông cậu ta cứ như vừa tìm thấy con ma hư cấu mà bản thân từng tán phét với đám bạn từ cái thời hỉ mũi chưa sạch vậy."
    ###675#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1317.ogg"
    narrator "{size=180}\n{/size}「...À, ừm... chị vẫn nhớ tôi sao?」"
    ###676#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 02 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1319.ogg"
    narrator "{size=180}\n{/size}「Vâng, tất nhiên rồi.」"
    ###677#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1321.ogg"
    narrator "{size=180}\n{/size}「Đã lâu không thấy bạn tới đây, nên tôi cứ lo rằng phải chăng bạn đã gặp vấn đề sức khỏe nào đó.」"
    ###678#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Cô bé khẽ nghiêng đầu, và nhìn thẳng vào cậu ta."
    ###679#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô gái đi cùng cậu ta trưng ra một biểu cảm còn thiếu sức sống hơn cả cô robot đứng trước mặt hai người."
    ###680#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cuối cùng, cơ hồ vừa quyết định điều gì đó, cậu ta lên tiếng."
    ###681#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1327.ogg"
    narrator "{size=180}\n{/size}「Tôi ấy, từng... ờ, cầu hôn Yumemi-chan, chuyện đấy... quả nhiên là chị nhớ hả?」"
    ###682#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1329.ogg"
    narrator "{size=180}\n{/size}「Vâng, tôi nhớ. Vì tôi là một robot nên ghi nhớ là thế mạnh của tôi.」"
    ###683#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi mỉm cười, không vương chút tà tâm."
    ###684#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1333.ogg"
    narrator "{size=180}\n{/size}「Giờ... tôi muốn rút lại lời cầu hôn ấy.」"
    ###685#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Xem chừng đã chấp nhận sự lố bịch trong lời lẽ của mình, cậu ta ấp úng nói tiếp."
    ###686#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1337.ogg"
    narrator "{size=180}\n{/size}「Vì... giờ... tôi thích nhỏ này.」"
    ###687#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cậu ta hất cằm về phía cô bạn gái."
    ###688#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCô ta không giấu được vẻ khó chịu khi vòng tay ôm lấy tay bạn trai."
    ###689#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô liếc cậu ta bằng ánh nhìn thoáng vẻ khinh khi, và chu đôi môi đỏ lòm của mình lên."
    ###690#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi một lần nữa mỉm cười."
    ###691#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1344.ogg"
    narrator "{size=180}\n{/size}「Tôi hiểu rồi. Tôi đã ghi nhận rằng hôn ước giữa chúng ta đã bị hủy bỏ.」"
    ###692#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé nói bằng giọng của một nhân viên quản lý việc đặt hàng từ xa vừa chấp nhận hủy đơn hàng."
    ###693#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,72.0)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(0,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1348.ogg"
    narrator "{size=180}\n{/size}「Chúc hai bạn mãi hạnh phúc bên nhau.」"
    ###694#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô bé cúi nhẹ đầu và tươi tỉnh nói, dù chẳng biết cô có hiểu tình hình hay không."
    ###695#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se033.wav"
    narrator "{size=180}\n{/size}Sau khi đã nhận lời chúc từ tận đáy lòng ấy, cặp đôi trẻ nhanh chóng rời khỏi cung thiên văn."
    ###696#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    voice "ovk/z1000/1353.ogg"
    narrator "{size=180}\n{/size}「Đã mất công gửi vé miễn phí cho rồi thì ở lại xem cả buổi chiếu đi chứ... tôi mà nghĩ thế thì có bị coi là keo kiệt không nhỉ?」"
    ###697#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou, người đang ngồi trên ghế lễ tân vừa quan sát sự việc diễn ra, nói."
    ###698#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1357.ogg"
    narrator "{size=180}\n{/size}「Thì chắc tại thằng bé hết hứng thú với cung thiên văn rồi chứ gì.」"
    ###699#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi ngồi ghế bên cạnh đáp lại."
    ###700#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1361.ogg"
    narrator "{size=180}\n{/size}「Nói sao thì nói chứ, nhóc Susumu ấy...」"
    ###701#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1363.ogg"
    narrator "{size=180}\n{/size}「Thật tình. Nói sao giờ nhỉ... tôi vẫn tưởng thằng nhóc là người chất phác lắm kia.」"
    ###702#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1365.ogg"
    narrator "{size=180}\n{/size}「Ngày nay thì đấy đã là chất phác rồi. Mỗi thời mỗi khác mà chị.」"
    ###703#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1367.ogg"
    narrator "{size=180}\n{/size}「Gorou-kun nói chuyện cứ như ông già ấy.」"
    ###704#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nhóc Susumu, hay chính xác hơn là Akino Susumu, từng là khách quen của cung thiên văn vào đúng 10 năm trước."
    ###705#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đương nhiên là cậu bé thích thiên văn rồi, nhưng trên hết, cậu ta cũng thích việc chăm sóc Yumemi ― khi ấy vừa mới nhận việc ― đến mức thái quá, gây ra rất nhiều rắc rối cho dàn nhân sự lúc bấy giờ."
    ###706#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Đến một ngày nọ, cậu bé đột ngột ngừng ghé qua."
    ###707#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Mọi người đều quên béng đi mất, bởi học sinh tiểu học vốn là như thế."
    ###708#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tuy vậy, Satomi vẫn nhớ cảm giác nhẹ nhõm khi ấy, song hành cùng chút buồn bã nữa."
    ###709#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1375.ogg"
    narrator "{size=180}\n{/size}「...Thật tình, thằng bé cứ thế chuyển đi, chẳng nói với chúng ta một lời, rồi còn tinh tướng đi kiếm bạn gái nữa.」"
    ###710#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1377.ogg"
    narrator "{size=180}\n{/size}「Bạn gái hay gì là cách cậu ta khẳng định giá trị bản thân, nên tôi xin phép miễn bình luận...」"
    ###711#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se009.wav"
    narrator "{size=180}\n{/size}Gorou nói trong lúc thao tác với chiếc bàn phím hàng cổ một cách thuần thục."
    ###712#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1381.ogg"
    narrator "{size=180}\n{/size}「Nhưng thứ tôi không hiểu là cái mệnh lệnh ưu tiên bị bỏ lại suốt tận 10 năm này này.」"
    ###713#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou làu bàu khi nhìn vào cửa sổ trạng thái ở giữa màn hình, thứ được dành riêng cho việc bảo trì Yumemi trong vài ngày qua."
    ###714#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một cửa sổ với tiêu đề \"COMMANDSTACK\" đang chạy."
    ###715#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một dòng số 0 ― thứ đáng ra không thể tồn tại ― chứa đầy các mã thập lục phân."
    ###716#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Nói đơn giản, thì đây giống như một dòng thần chú ma thuật ẩn nấp trong trí nhớ Yumemi suốt 10 năm trời và gây ra hiện tượng \"rời bỏ nơi làm việc\" của cô bé."
    ###717#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1388.ogg"
    narrator "{size=180}\n{/size}「Mà, khi ấy chúng ta hãy còn đang điều chỉnh con bé, cả hệ thống học tập nữa ha.」"
    ###718#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1390.ogg"
    narrator "{size=180}\n{/size}「Có hàng tá lỗi nghiêm trọng đã được sửa lại rồi. Cả cái này, nguyên nhân chính cũng là do việc xử lý ngoại lệ thôi, cơ mà...」"
    ###719#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    play sound "nwa/se034.wav"
    narrator "{size=180}\n{/size}Anh ta tiếp tục nhấp vào màn hình bằng chiếc bút mực có kèm chức năng của một cây bút cảm ứng."
    ###720#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1394.ogg"
    narrator "{size=180}\n{/size}「Vì được bảo là phải giữ bí mật mà con bé có thể thực hiện một hành vi phức tạp như hook chính quá trình gỡ lỗi hàng ngày và làm cho danh sách mệnh lệnh bị ẩn đi, chuyện này chính tôi cũng chẳng tin nổi.」"
    ###721#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1396.ogg"
    narrator "{size=180}\n{/size}「Hay ngược lại, tôi còn thấy phục con bé.」"
    ###722#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1398.ogg"
    narrator "{size=180}\n{/size}「Nhưng dù không biết về mệnh lệnh đó, thì nếu xem video từ lúc đầu, cậu vẫn sẽ tìm được khởi điểm chứ?」"
    ###723#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1400.ogg"
    narrator "{size=180}\n{/size}「Ý chị là kiểm tra toàn diện xuyên 10 năm ấy hả? Xét về mặt vật chất thì chuyện đó là bất khả thi đấy.」"
    ###724#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 09 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1402.ogg"
    narrator "{size=180}\n{/size}「Cũng phải...」"
    ###725#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cũng có thể Satomi đã từng thấy rồi, nhưng sau đó cô lại quên đi mất."
    ###726#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Phát không ngừng ở góc phải màn hình máy tính là một video đa chiều do Yumemi quay lại được nén xuống còn hai chiều."
    ###727#------
    scene black
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    hide bg11
    hide sbw00_3
    hide sbw00_4
    hide sbw01
    hide kr_f
    hide kr_b
    with fade
    play music "nwa/bgm13.wav" fadeout 0.5 fadein 0.5
    narrator "{size=180}\n{/size}Ngày quay là 10 năm và 8 ngày trước."
    ###728#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tại quầy lễ tân của cung thiên văn, trước máy bán vé tự động, một cậu bé đang nhìn chằm chằm vào Yumemi từ chính diện."
    ###729#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Khuôn mặt cậu lộ rõ vẻ tinh nghịch, mái tóc ngắn lòa xòa và đôi mắt như sắp khóc tới nơi."
    ###730#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1413.ogg"
    narrator "{size=180}\n{/size}『Yumemi-chan, chị em mình cưới nhau đi!』"
    ###731#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một lời cầu hôn hết lòng hết dạ và tha thiết đến từ phía cậu bé."
    ###732#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1417.ogg"
    narrator "{size=180}\n{/size}『Mai em phải chuyển nhà rồi... Vì thế chúng ta sẽ không thể gặp nhau được nữa.』"
    ###733#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1419.ogg"
    narrator "{size=180}\n{/size}『Nhưng tôi là một robot, nên tôi không thể cưới bạn được.』"
    ###734#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1421.ogg"
    narrator "{size=180}\n{/size}『Làm gì có chuyện đấy! Yêu nhau là cưới nhau được mà!』"
    ###735#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1423.ogg"
    narrator "{size=180}\n{/size}『Mẹ em dạy như vậy đó. Chỉ cần yêu là có thể thành thân được rồi.』"
    ###736#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1425.ogg"
    narrator "{size=180}\n{/size}『Thật sự xin lỗi, nhưng tôi không tìm thấy bất cứ dữ liệu nào trong cơ sở dữ liệu để khẳng định những điều bạn vừa nói.』"
    ###737#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cậu bé tỏ ra thất vọng vì cuộc trò chuyện không đúng hướng như dự kiến."
    ###738#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1429.ogg"
    narrator "{size=180}\n{/size}『Nếu không cưới được Yumemi-chan... chắc em chết mất...』"
    ###739#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Màn hình hơi chếch đi một chút."
    ###740#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    extend "\nCó lẽ Yumemi đang nghiêng đầu nghĩ ngợi gì đó."
    ###741#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1434.ogg"
    narrator "{size=180}\n{/size}『Thật thất lễ quá, nhưng tôi có thể biết quý khách Susumu năm nay bao nhiêu tuổi được không?』"
    ###742#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1436.ogg"
    narrator "{size=180}\n{/size}『Em chín tuổi.』"
    ###743#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1438.ogg"
    narrator "{size=180}\n{/size}『Nếu là như vậy thì thật đáng tiếc, nhưng ở độ tuổi này bạn chưa được phép kết hôn.』"
    ###744#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một thoáng lặng im."
    ###745#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1442.ogg"
    narrator "{size=180}\n{/size}『Yumemi-chan, đợi em 10 năm nữa nhé! 10 năm nữa em sẽ đến đón chị!』"
    ###746#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1444.ogg"
    narrator "{size=180}\n{/size}『Em sẽ cố gắng giữ mình cho đến lúc đó, nên khi ấy mình kết hôn đi!』"
    ###747#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1446.ogg"
    narrator "{size=180}\n{/size}『Đây... là thứ gọi là hôn ước phải không ạ?』"
    ###748#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1448.ogg"
    narrator "{size=180}\n{/size}『Đúng, là hôn ước đó!』"
    ###749#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1450.ogg"
    narrator "{size=180}\n{/size}『Nhưng... tôi còn phải làm việc.』"
    ###750#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1452.ogg"
    narrator "{size=180}\n{/size}『Khi không ai thấy thì chị cứ ra ngoài cũng có sao đâu, giả vờ như đang làm việc là được.』"
    ###751#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1454.ogg"
    narrator "{size=180}\n{/size}『Khi ấy em sẽ đến đón chị. Nhất định, nhất định em sẽ đến...』"
    ###752#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sau khi lưỡng lự đôi chút, Yumemi lên tiếng trả lời dứt khoát."
    ###753#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1458.ogg"
    narrator "{size=180}\n{/size}『Xin nhận lệnh, đã đăng ký mệnh lệnh này ở mức ưu tiên cao hơn.』"
    ###754#------
    show kuros :
        offset(0,0)
        anchor(0,0)
    show bg32 :
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1460.ogg"
    narrator "{size=180}\n{/size}『Ừm! Chị nhớ giữ bí mật nhé. Lời hứa bí mật của đôi ta...』"
    ###755#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    hide kuros
    hide bg32
    with dissolve
    play music "nwa/bgm08.wav" fadeout 0.5 fadein 0.5
    narrator "{size=180}\n{/size}Video ghi lại dừng ở đó và quay lại cảnh đầu tiên."
    ###756#------
    show bg35a_movie :
        offset(128,22)
        anchor(0,0)
        Movie(play=mov_path("snow_start_movie"), loop=False)
        pause 10.0
        Movie(play=mov_path("snow_movie"), loop=True)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Một lời hứa ngây ngô và trong sáng giữa cô gái ấy và một cậu chàng bé nhỏ."
    ###757#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Lời hứa nhảy múa vòng quanh không ngừng tựa như bông tuyết chứa trong quả cầu tuyết."
    ###758#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Dù cho cậu bé ấy đã quên đi mọi chuyện."
    ###759#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi không ngừng suy nghĩ."
    ###760#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1473.ogg"
    narrator "{size=180}\n{/size}(Con người luôn quên đi, và Yumemi không thể quên...)"
    ###761#------
    show bg35a :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1475.ogg"
    narrator "{size=180}\n{/size}(Liệu bên nào mới hạnh phúc đây?)"
    ###762#------
    scene bg01
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide bg35a
    with fade
    play sound "nwa/se011.wav"
    voice "ovk/z1000/1477.ogg"
    narrator "{size=180}\n{/size}「Phù...」"
    ###763#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi vươn vai trên ghế như thể đang dối lừa những cảm xúc đương trào dâng."
    ###764#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1481.ogg"
    narrator "{size=180}\n{/size}「Để tôi đoán chị đang nghĩ gì nhé?」"
    ###765#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Gorou lên tiếng."
    ###766#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1485.ogg"
    narrator "{size=180}\n{/size}「Gì hở?」"
    ###767#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1487.ogg"
    narrator "{size=180}\n{/size}「Làm sao để tính phí vé đi-về của hai đứa kia đúng không?」"
    ###768#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Anh ta chỉ ra cùng một vẻ tự tin."
    ###769#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1491.ogg"
    narrator "{size=180}\n{/size}「Chán cậu lắm Gorou-kun ạ.」"
    ###770#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Xen lẫn với một tiếng thở dài, Satomi đáp."
    ###771#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    narrator "{size=180}\n{/size}Giờ đây nguyên nhân đã được xác định, tất cả những gì họ cần làm chỉ đơn giản là viết lại danh sách mệnh lệnh mà thôi, nhưng không một ai ― bao gồm cả Gorou là người đề xuất ý tưởng này ― đồng ý làm thế."
    ###772#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Để đề phòng trường hợp khai man danh tính, những robot đồng hành như Yumemi sử dụng rất nhiều lớp quét sinh trắc học nhằm định dạng một cá thể, vậy nên việc nhờ chính chủ từng xác nhận mệnh lệnh ưu tiên tới để \"hủy bỏ hôn ước\" là điều tối cần thiết."
    ###773#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Kết quả sinh ra từ những dữ kiện này là một màn kịch nhỏ với đương sự làm vai chính."
    ###774#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Tất nhiên ta không thể bỏ qua những công sức và phí tổn của bọn họ trong việc tìm kiếm địa chỉ hiện tại của cậu bé Susumu ngày nào từ danh sách khách hàng thời đó, đi giải thích tình hình rồi lại yêu cầu cậu ta tới gặp Yumemi ngay lập tức."
    ###775#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1502.ogg"
    narrator "{size=180}\n{/size}(Thật tình, cái chỗ làm việc gì mà rặt một đám nhân viên vô dụng đi thấu cảm cho một robot.)"
    ###776#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Cô không biết nhóc Susumu và cô bạn gái sẽ đi đâu."
    ###777#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1509.ogg"
    narrator "{size=180}\n{/size}(Liệu hai đứa nó sẽ đi thăm thú thành phố nơi bạn trai từng sống, hay sẽ đi vào quán cà phê, trung tâm trò chơi hay thậm chí là rạp chiếu phim 3D...)"
    ###778#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Quả nhiên là cô vẫn thấy bực khi cung thiên văn không nằm trong kế hoạch hò hẹn ấy."
    ###779#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1513.ogg"
    narrator "{size=180}\n{/size}「Thôi thì, xin được chúc cho những cặp yêu nhau một tương lai xán lạn.」"
    ###780#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1515.ogg"
    narrator "{size=180}\n{/size}「...Nghe câu đậm mùi cà khịa.」"
    ###781#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 04 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1517.ogg"
    narrator "{size=180}\n{/size}「Cậu thấy thế thì thế.」"
    ###782#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1519.ogg"
    narrator "{size=180}\n{/size}「Đã cho Yumemi dễ thương nhà mình ăn bơ vậy rồi mà còn không đến gặp con bé thì tôi sẽ cho thằng nhóc đó một bài học. Như 10 năm trước vậy.」"
    ###783#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1521.ogg"
    narrator "{size=180}\n{/size}「Thế giờ ta làm gì đây? Nguyên nhân thì xác định được rồi, và tôi có thể tự tin đảm bảo là bây giờ lỗi sẽ không xuất hiện nữa đâu...」"
    ###784#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1523.ogg"
    narrator "{size=180}\n{/size}「Nhưng nếu lỗi ở cấp độ này vẫn còn lưu lại thì khi giám đốc trở về, có lẽ tôi sẽ phải đề xuất một lần cập nhật lại hệ thống cho con bé.」"
    ###785#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 03 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1525.ogg"
    narrator "{size=180}\n{/size}「Nhưng làm vậy thì tính cách em nó cũng sẽ thay đổi theo chứ gì? Kệ đi, cứ để thế này cũng được mà.」"
    ###786#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1529.ogg"
    narrator "{size=180}\n{/size}(Ai mà chẳng phải có một hai bí mật muốn giấu người khác chứ.)"
    ###787#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,72.0)
        zoom 1
    hide kr_f
    hide kr_b
    with dissolve
    voice "ovk/z1000/1531.ogg"
    narrator "{size=180}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###788#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1533.ogg"
    narrator "{size=180}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận...」"
    ###789#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Yumemi quay trở lại vị trí thường ngày, liên tục mời chào khách không biết mệt mỏi."
    ###790#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Làn gió đầu đông luồn qua khe cửa kính làm cho mái tóc chẻ hai đuôi lỗi mốt của cô bé khẽ dao động."
    ###791#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Sắc diện của cô trông như yêu kiều nữ tính hơn, tràn đầy sức sống hơn bình thường."
    ###792#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1539.ogg"
    narrator "{size=180}\n{/size}「Nè, Yumemi-chan, sao em không thử thay đổi kiểu tóc nhỉ?」"
    ###793#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1542.ogg"
    narrator "{size=180}\n{/size}「...?」"
    ###794#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Bất ngờ được gọi, cô bé nhìn Satomi với một vẻ ngây ngô."
    ###795#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show yu_b 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,72.0)
        zoom 1
    with dissolve
    voice "ovk/z1000/1546.ogg"
    narrator "{size=180}\n{/size}「Mái tóc của tôi đóng vai trò như bộ tản nhiệt từ bộ phận tính toán trên đầu, nên không được phép uốn hoặc buộc lại.」"
    ###796#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1548.ogg"
    narrator "{size=180}\n{/size}「Ra thế, chị hiểu rồi...」"
    ###797#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi liếc mắt lên đồng hồ treo tường trong lúc nghe cô bé trả lời."
    ###798#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Ở trong phòng trình chiếu, nhạc nền đã chuyển, đã sắp đến lúc buổi chiếu lúc bình minh bắt đầu."
    ###799#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Chuẩn bị có thêm một lượt khách tới xem."
    ###800#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    extend "\nCô cần phải trở về vị trí của mình."
    ###801#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play sound "nwa/se051.wav"
    narrator "{size=180}\n{/size}Satomi thì thầm vào tai Gorou trong khi anh đứng dậy khỏi chiếc ghế xếp."
    ###802#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 01 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1556.ogg"
    narrator "{size=180}\n{/size}「Nè, cậu nghĩ đeo thêm phụ kiện tóc cho Yumemi có ổn không?」"
    ###803#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1558.ogg"
    narrator "{size=180}\n{/size}「Nếu ta chuẩn bị một thứ dành cho máy móc dòng cao cấp thì tôi nghĩ sẽ chẳng sao đâu. Tất nhiên, ngân sách đâu ra thì lại là một chuyện khác nhé.」"
    ###804#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    show kr_b 00 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 02 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1560.ogg"
    narrator "{size=180}\n{/size}「Chỉ còn cách làm việc quần quật để kiếm chác thôi ha.」"
    ###805#------
    show bg11 :
        offset(128,22)
        anchor(0,0)
    show sbw00_3 :
        offset(115,35)
        anchor(0,0)
        ysize 697
        xsize 13
        fit 'fill' 
    show sbw00_4 :
        offset(1152,35)
        anchor(0,0)
        ysize 697
        xsize 12
        fit 'fill' 
    show sbw01 :
        offset(128,726)
        anchor(0,0)
    with dissolve
    narrator "{size=180}\n{/size}Satomi nói và mỉm cười."
    ###806#------
    scene black
    with dissolve
    jump chapter_8

label chapter_8:
    scene black
    $ cut_scene("staff")
    
    play music "nwa/se040.ogg" fadeout 0.5 fadein 1.0
    
    image pre_epilogue:
        Movie(play=mov_path("pre_epilogue"), loop=False)
    show pre_epilogue:
        offset(0,0)
    $ renpy.pause(10.0, hard=True)
    $ renpy.pause(9.0)
    stop music
        
    image epilogue:
        Movie(play=mov_path("epilogue"), loop=False)
    show epilogue:
        offset(0,0)
    $ renpy.pause(10.0, hard=True)
    $ renpy.pause(10.0)
    
    play sound "nwa/se036.wav"
    
    $ renpy.pause(6.0, hard=True)

    ###807#------
    return
