# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define fade = Fade(1, 0.2, 1)

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 128 #gui.dialogue_xpos
    xsize 1024 #gui.dialogue_width
    ypos -250 #gui.dialogue_ypos
    ysize 200

    adjust_spacing False

style say_dialogue is default

init python:
    config.gl_resize=False
    config.save_physical_size=False
    style.default.font = "kiloji.ttf"
    style.default.language = "eastasian"
    #style.window.left_margin = 0
    #style.window.right_margin = 0
    #style.window.top_margin = 550

    ## Padding is space inside the window, where the background is
    ## drawn.

    #style.window.left_padding = 6
    #style.window.right_padding = 6
    #style.window.top_padding = 6
    #style.window.bottom_padding = 0
    #style.window.background = Image("images/SMW11D.png", xalign=0.5, yalign=1.0)

# The game starts here.

label start:

    with dissolve
    "雪圏球はじめから"
    ###------
    show bg34 : 
        offset(0,0)
        anchor(0,0)
    show smw01d zorder 100: 
        offset(97,742)
    with dissolve
    play music "nwa/bgm01.wav"
    voice "ovk/z1000/13.ogg"
    voice "ovk/z1000/15.ogg"
    voice "ovk/z1000/17.ogg"
    "{size=192}\n{/size}"
    ###------
    scene bg01
    with fade
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
    with dissolve
    play music "nwa/bgm02.wav"
    voice "ovk/z1000/25.ogg"
    "{size=192}\n{/size}「Đào tạo người mới chẳng phải là công việc của em đó sao?」"
    ###------
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
    "{size=192}\n{/size}「Đúng vậy. Đúng là như thế, nhưng đó không phải là \"người\" mới.」"
    ###------
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
    "{size=192}\n{/size}「Đúng là người mới còn gì. Chính em là người yêu cầu tuyển thêm thuyết trình viên còn gì.」"
    ###------
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
    "{size=192}\n{/size}「Tôi đã đáp ứng rồi đấy. Em còn không hài lòng chuyện gì nữa?」"
    ###------
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
    "{size=192}\n{/size}「Đúng là em đã nói vậy, nhưng em cần người bình thường cơ...」"
    ###------
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
    "{size=192}\n{/size}「Con bé có bình thường hay không còn tùy thuộc em dạy dỗ như thế nào.」"
    ###------
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
    "{size=192}\n{/size}「Trên đời làm gì có cái phù hợp ngay từ đầu. Dù là giày da hay áo vét thì cũng phải đi nhiều mặc nhiều mới thấy hợp được.」"
    ###------
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
    "{size=192}\n{/size}「Nhưng mà giám đốc...」"
    ###------
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
    "{size=192}\n{/size}Ngay từ lần đầu nghe tin sẽ đưa cô bé đó vào biên chế, Satomi đã phản đối hàng trăm lần bằng đủ thứ cách."
    ###------
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
    "{size=192}\n{/size}Nhưng giờ thì muốn thay đổi cũng muộn rồi."
    ###------
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
    "{size=192}\n{/size}里美(Biết rõ là vậy rồi, nhưng mà...)"
    ###------
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
    "{size=192}\n{/size}里美(Mình vẫn có trách nhiệm của một trưởng ban thuyết trình, cũng như lòng kiêu hãnh vốn có của một chuyên gia trong lĩnh vực này.)"
    ###------
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
    "{size=192}\n{/size}里美(Đâu thể nào chỉ \"À vậy ạ\" một cái là xong chuyện được.)"
    ###------
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
    "{size=192}\n{/size}「Hờ...」"
    ###------
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
    "{size=192}\n{/size}Giám đốc thở dài, áp mu bàn tay phải lên bờ trán rộng của mình, đoạn tiếp lời."
    ###------
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
    "{size=192}\n{/size}「Kurahashi Satomi-kun」"
    ###------
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
    "{size=192}\n{/size}Việc giám đốc gọi cả họ và tên cấp dưới đồng nghĩa với việc có tranh luận thêm cũng hoài công."
    ###------
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
    "{size=192}\n{/size}「Chúng ta không chỉ là nhân viên cung thiên văn, mà còn là nhân viên thời vụ của trung tâm bách hóa này.」"
    ###------
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
    "{size=192}\n{/size}「Nếu giúp cho thật nhiều người tận hưởng trời sao là sứ mệnh của chúng ta, thì cải thiện doanh thu cũng là sứ mệnh quan trọng chẳng kém. Em có hiểu không?」"
    ###------
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
    "{size=192}\n{/size}「.....」"
    ###------
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
    "{size=192}\n{/size}Giờ mà nói \"Em chẳng hiểu gì hết\" thì chắc da mặt cô phải dày lắm."
    ###------
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
    "{size=192}\n{/size}『Làm việc tại đây khác với thuyết trình ở bảo tàng khoa học』. Đó là những lời đầu tiên cô nhận được trong buổi phỏng vấn xin việc thời niên thiếu."
    ###------
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
    "{size=192}\n{/size}Lúc đó, giám đốc bảo tàng hẳn vẫn còn tin tưởng vào triển vọng của dự án khai thác vũ trụ và cung thiên văn, và phần tóc hói của ông vẫn còn che giấu được dễ dàng bằng cách sử dụng keo xịt và loại lược gỗ chăm sóc tóc thần kỳ."
    ###------
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
    "{size=192}\n{/size}「Đến giờ họp giao ban rồi. Nhờ em dẫn con bé tới tập trung ở quầy lễ tân nhé.」"
    ###------
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
    "{size=192}\n{/size}Khoác lên khuôn mặt của một cấp trên nghiêm khắc, ông nói, rồi cứ thế bước ra khỏi phòng giám đốc mà chẳng thèm ngoảnh lại."
    ###------
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
    "{size=192}\n{/size}Bỏ lại trưởng ban thuyết trình... hay nhân viên thời vụ Kurahashi Satomi một mình trong phòng."
    ###------
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
    "{size=192}\n{/size}Không, để mà nói chính xác thì không phải \"một mình\"."
    ###------
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
    "{size=192}\n{/size}「...nhưng giám đốc ơi, con bé đâu phải con người cơ chứ?」"
    ###------
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
    "{size=192}\n{/size}Không ai đáp lời cô cả."
    ###------
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
    "{size=192}\n{/size}里美(Có khác nào đang diễn hề đâu.)"
    ###------
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
    "{size=192}\n{/size}里美(À không... chính xác hơn thì phải là múa rối chứ nhỉ.)"
    ###------
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
    "{size=192}\n{/size}Vừa hay, chiếc đồng hồ treo tường chỉ đúng 9 giờ sáng."
    ###------
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
    play music "nwa/bgm12.wav"
    play sound "nwa/se002.wav"
    "{size=192}\n{/size}Ùng..."
    ###------
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
    "{size=192}\n{/size}Âm thanh nho nhỏ của động cơ điện từ hao hao giống tiếng ong vo ve làm cô hơi nhột tai."
    ###------
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
    "{size=192}\n{/size}Sâu trong phòng giám đốc, một thứ hình người khác ngoài Satomi bắt đầu di chuyển."
    ###------
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
    "{size=192}\n{/size}サスペンドVừa thức dậy khỏi trạng thái tạm nghỉ, thứ đó từ từ nâng nửa thân trên dậy khỏi chiếc ghế dài, thật dễ khiến người ta liên tưởng tới hình ảnh một con quỷ hút máu bò ra khỏi quan tài."
    ###------
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
    "{size=192}\n{/size}里美(Giả như, con bé không có hình dạng thế này...)"
    ###------
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
    "{size=192}\n{/size}Satomi lặp lại lời nghi vấn mà cô đã tự hỏi bản thân không biết bao nhiêu lần kể từ hồi mới nhìn thấy cô bé trong tập tài liệu."
    ###------
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
    "{size=192}\n{/size}里美(...thì liệu mình có thể đối xử với nó bình tĩnh hơn không? Hay mình sẽ còn ghét con bé hơn nữa?)"
    ###------
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
    "{size=192}\n{/size}１０代後半女性の平均的体型を模したというＦＬ低身長型の筐体は、花菱デパートの受付制服を元にした特注のコスチュームに包まれている。"
    ###------
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
    "{size=192}\n{/size}Hai đuôi tóc cô bé dài lắc lư, có tác dụng tản nhiệt và bảo vệ bộ phận xử lý dữ liệu phần đầu."
    ###------
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
    "{size=192}\n{/size}Hai đầu dây cáp được nối với đầu cắm ở tai trái."
    ###------
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
    "{size=192}\n{/size}床を何メートルかのたくった後、それは桐箪笥のように大げさなテレ情報送メーター信装置に吸い込まれる。"
    ###------
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
    "{size=192}\n{/size}Trong vài tháng đầu, cô bé luôn phải ngồi đó kết nối dữ liệu gần như cả ngày để cung cấp cho nhà sản xuất những thông tin quý giá theo hợp đồng tiêu dùng."
    ###------
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
    "{size=192}\n{/size}Nói đơn giản hơn thì công việc đó tựa hồ một loại \"của hồi môn\" để cô bé có thể được \"gả\" về nơi này với mức giá hời."
    ###------
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
    "{size=192}\n{/size}Cuối cùng, cô bé đã hoàn toàn đứng dậy được."
    ###------
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
    "{size=192}\n{/size}Cùng một cử chỉ như đang quay trên bàn xoay gốm, cô bé bất giác hướng về phía Satomi."
    ###------
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
    "{size=192}\n{/size}それから、両手の指――有機樹脂と軽合金の骨格を人工皮膚でコーティングしたマニピュレーター精密義指――をぴんと伸ばし揃えた。"
    ###------
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
    voice "ovk/z1000/122.ogg"
    "{size=192}\n{/size}「Buổi sáng tốt lành ạ.」"
    ###------
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
    "{size=192}\n{/size}Cô bé cất tiếng chào Satomi, với một chất giọng thiếu nữ hoàn hảo đến độ mất tự nhiên."
    ###------
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
    "{size=192}\n{/size}Hình ảnh của Satomi phản chiếu trong con ngươi làm từ nhựa quang học kia."
    ###------
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
    "{size=192}\n{/size}Chúng thay đổi độ cong khi tải điện áp yếu, thoáng thấy mờ mờ như màng dầu, khiến cô trông như đang mỉm cười."
    ###------
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
    show yu_b 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/131.ogg"
    "{size=192}\n{/size}里美(Nếu có ai giới thiệu con bé này là con người, khéo có khi mình tin thật.)"
    ###------
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
    "{size=192}\n{/size}Trên chiếc váy màu xanh biển rực rỡ có thêu một số chữ cái alphabet bằng chỉ phát quang."
    ###------
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
    "{size=192}\n{/size}	 "
    ###------
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
    "{size=192}\n{/size}Đó là tên của cô bé."
    ###------
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
    "{size=192}\n{/size}Ít nhất, là trong thời điểm này."
    ###------
    scene kuros
    with fade
    show kuroe : 
        offset(128,22)
        anchor(0,0)
    hide bg10
    hide sbw00_3
    hide sbw00_4
    hide sbw01
    with dissolve
    play music "nwa/bgm08.wav"
    ""
    ###------
    show kurob : 
        offset(128,22)
        anchor(0,0)
    hide kuroe
    with dissolve
    "雪圏球第２章"
    ###------
    scene bg01
    with fade
    show bg22 : 
        offset(78,22)
        anchor(0,0)
        ysize 704
        xsize 1074
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
    with dissolve
    play music "nwa/bgm04.wav"
    play sound "nwa/se005.wav"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###------
    show bg22 : 
        offset(-247,22)
        anchor(0,0)
        ysize 704
        xsize 1399
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
    voice "ovk/z1000/152.ogg"
    "{size=192}\n{/size}Giọng nói êm dịu vang vọng trong con ngõ vào một ngày đầu đông."
    ###------
    show bg22 : 
        offset(-573,22)
        anchor(0,0)
        ysize 704
        xsize 1725
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
    voice "ovk/z1000/156.ogg"
    "{size=192}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###------
    show bg22 : 
        offset(-896,22)
        anchor(0,0)
        ysize 704
        xsize 2048
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
    "{size=192}\n{/size}Người người kéo cổ áo khoác lên mà lầm lũi vụt qua."
    ###------
    show bg22 : 
        offset(-896,22)
        anchor(0,0)
        ysize 704
        xsize 2048
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
    "{size=192}\n{/size}Không ai mảy may để ý đến cô người máy đồng hành lỗi thời ấy."
    ###------
    show bg22 : 
        offset(-896,22)
        anchor(0,0)
        ysize 704
        xsize 2048
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
    "{size=192}\n{/size}Thứ duy nhất dừng lại chịu lắng nghe là chiếc xe đạp điện bị bỏ rơi nơi góc phố."
    ###------
    show bg22 : 
        offset(-896,22)
        anchor(0,0)
        ysize 704
        xsize 2048
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
    "{size=192}\n{/size}Dù vậy, cô vẫn vui vẻ lặp lại những câu từ nọ như ngân lên khúc ca."
    ###------
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
    show yu_b 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/167.ogg"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn...」"
    ###------
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
    with dissolve
    "{size=192}\n{/size}イーポスTheo như tốc độ di chuyển của Yumemi thì hẳn cô bé vẫn chưa đi quá xa, và nhờ vào thiết bị đầu cuối định vị mà Satomi có thể xác định vị trí hiện tại của cô bé."
    ###------
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
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 00 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    play sound "nwa/se006.wav"
    voice "ovk/z1000/171.ogg"
    "{size=192}\n{/size}「Yumemi-chan nè, chị hỏi chút được chứ?」"
    ###------
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
    show yu_b 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Nghe tiếng gọi, cô bé dừng nói và quay sang Satomi mà không tỏ ra dù chỉ một chút ăn năn."
    ###------
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
    show yu_b 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/175.ogg"
    "{size=192}\n{/size}「Vâng, xin cứ tự nhiên hỏi tôi bất cứ điều gì.」"
    ###------
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
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 07 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/177.ogg"
    "{size=192}\n{/size}「Công việc hôm nay của em là gì vậy nhỉ?」"
    ###------
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
    show yu_b 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/179.ogg"
    "{size=192}\n{/size}「Công việc của tôi là chào mời và chỉ dẫn cho khách tại quầy vé trong cung thiên văn.」"
    ###------
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
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 08 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/181.ogg"
    "{size=192}\n{/size}「Biết thế thì sao em lại đứng cách vị trí làm việc những 3 km vậy hả?」"
    ###------
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
    show yu_b 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/183.ogg"
    "{size=192}\n{/size}「Vâng, kể ra thì đó là một câu chuyện dài...」"
    ###------
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
    with dissolve
    "{size=192}\n{/size}Sau đó cô bé kể với Satomi chi tiết làm thế nào mình đến được đây."
    ###------
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
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 10 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/187.ogg"
    "{size=192}\n{/size}「...Chuyện đấy chị biết rồi. Chị muốn hỏi là, em đang làm gì ở một nơi như thế này vậy hả?」"
    ###------
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
    show yu_b 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/190.ogg"
    "{size=192}\n{/size}「...?」"
    ###------
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
    with dissolve
    "{size=192}\n{/size}Cô bé khẽ nghiêng đầu trước câu hỏi nhấn nhá ngữ điệu của cấp trên."
    ###------
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
    show kr_b 01 zorder 2: 
        offset(0,24)
        zoom 1
    show kr_f 05 zorder 2: 
        offset(0,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Ngay cả khi con người đã mất hứng thú với thiên văn và cả bản thân cô bé, thì sắc thái thân thiện trong ánh mắt cô vẫn không hề phai nhạt."
    ###------
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
    with dissolve
    "{size=192}\n{/size}Sau vài giây trầm ngâm, cô bé ấy ― Hoshino Yumemi ― khẽ mỉm cười như đã ngộ ra tất cả và trả lời."
    ###------
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
    show yu_b 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/196.ogg"
    "{size=192}\n{/size}「Thành thật xin lỗi. Tôi không hiểu ý nghĩa câu hỏi cho lắm ạ.」"
    ###------
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
    hide bg22
    hide yu_f
    hide yu_a
    hide yu_b
    with dissolve
    play music "nwa/bgm05.wav"
    voice "ovk/z1000/202.ogg"
    "{size=192}\n{/size}「Quả nhiên là bị hỏng hóc ở đâu rồi đấy nhỉ...」"
    ###------
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
    "{size=192}\n{/size}Trút một tiếng thở dài, Satomi nâng cốc."
    ###------
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
    "{size=192}\n{/size}Trong phòng máy tính này không được phép ăn uống, nhưng do chính giám đốc là người đã quyết định việc này lại luôn uống cà phê trong đó nên thành ra cô cũng chẳng ngại nữa."
    ###------
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
    "{size=192}\n{/size}Chỉ có Yumemi là tuân thủ điều luật này."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/208.ogg"
    "{size=192}\n{/size}「Chị thấy hương vị thế nào ạ?」"
    ###------
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
    "{size=192}\n{/size}Yumemi hỏi bằng giọng nhã nhặn, trong khi vẫn kết nối với thiết bị đầu cuối bằng cáp dữ liệu."
    ###------
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
    "{size=192}\n{/size}Cô bé này mới khi nãy còn đang vui vẻ bưng bê cà phê, giờ đây đã bị lệnh cho phải ngồi xuống ghế và chuyển sang chế độ sửa lỗi."
    ###------
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
    "{size=192}\n{/size}Chẳng rõ cô ấy có hiểu được tính nguy cấp khi bị thẩm vấn về việc tự ý rời khỏi nơi làm việc không nữa..."
    ###------
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
    "{size=192}\n{/size}「.....」"
    ###------
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
    "{size=192}\n{/size}Satomi nhâm nhi ly cà phê."
    ###------
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
    "{size=192}\n{/size}Mùi vị vẫn như thường lệ."
    ###------
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
    "{size=192}\n{/size}Cà phê rang kiểu Pháp thương mại được pha kỳ công, hai muỗng đường, không phần kem cho Satomi."
    ###------
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
    "{size=192}\n{/size}里美(Xem chừng không có vấn đề gì.)"
    ###------
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
    "{size=192}\n{/size}「Ngon lắm. Cảm ơn em.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 03 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/229.ogg"
    "{size=192}\n{/size}「Thật vui khi được chị khen ngợi như vậy.」"
    ###------
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
    "{size=192}\n{/size}Yumemi mỉm cười, khẽ híp đôi mắt to tròn lại."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 02 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/233.ogg"
    "{size=192}\n{/size}「Hôm nay, trời hơi trở lạnh, nên tôi đã lưu tâm đến nhiệt độ của nước.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/235.ogg"
    "{size=192}\n{/size}「Giấy lọc cà phê vẫn còn khá nhiều trong kho, nhưng hạt cà phê thì chỉ còn một tuần nữa là hết hạn...」"
    ###------
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
    "{size=192}\n{/size}Vẫn như mọi khi, huyên thuyên đủ thứ chuyện."
    ###------
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
    "{size=192}\n{/size}里美(Quả nhiên là trông con bé không có gì bất thường...)"
    ###------
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
    "{size=192}\n{/size}Ngồi cạnh cô ấy, đồng nghiệp Mikajima Gorou đang chăm chú nhìn màn hình kiểu cũ, tay cầm cốc mà bên trong hẳn là cà phê đen pha loãng."
    ###------
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
    "{size=192}\n{/size}Mười năm trước, anh ta được điều chuyển công tác từ phía nhà sản xuất để giám hộ Yumemi ― lúc ấy hẵng còn chưa thạo việc, một người ngoài \"ở rể\" tại nơi này."
    ###------
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
    "{size=192}\n{/size}Dù năng lực của anh ta với tư cách kỹ sư robot là không thể phủ nhận, song lại hay có thói tin tưởng thái quá vào đối tượng cần bảo trì."
    ###------
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
    "{size=192}\n{/size}「Từ những triệu chứng chị vừa nói thì tôi nghĩ giờ lỗi sẽ không phát sinh nữa đâu.」"
    ###------
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
    "{size=192}\n{/size}Anh ta lẩm nhẩm vô nghĩa trong lúc lướt qua màn hình hiển thị báo cáo hoạt động chi tiết."
    ###------
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
    "{size=192}\n{/size}Hẳn phải có báo cáo về mô típ hành vi của Yumemi từ đêm qua."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/253.ogg"
    "{size=192}\n{/size}「Vâng. Theo như tôi nhận thức được thì không hề có lỗi nào cả.」"
    ###------
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
    "{size=192}\n{/size}Nở một nụ cười, Yumemi khẳng định mà chẳng hề có lấy một chút sức thuyết phục."
    ###------
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
    "{size=192}\n{/size}「Nào, ngày xưaaa chả có một vụ còn gì. Em chỉ đường cho một cụ bà xong rồi tự ý đi ra ngoài luôn ấy.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 06 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/259.ogg"
    "{size=192}\n{/size}「Vâng. Khi ấy quả thật là khó khăn lắm thay.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/261.ogg"
    "{size=192}\n{/size}「Vừa hay tôi đang đứng trước cửa chính mời chào khách và phân phát tờ rơi cho buổi triển lãm đặc biệt của trung tâm bách hóa Hanabishi...」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/263.ogg"
    "{size=192}\n{/size}「Tôi đã chứng minh là điều ấy chỉ xảy ra dưới những điều kiện vô cùng hạn chế, và hiện tại việc kiểm tra những hành vi bất thường cũng dần nghiêm ngặt hơn rồi nên...」"
    ###------
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
    "{size=192}\n{/size}「Không thế thì một cỗ máy bán độc lập thiếu bộ kiểm soát ý chí từ xa có lẽ đã bị crack Turing và bán bộ phận tại nơi nào đó ở Nam Mỹ rồi.」"
    ###------
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
    "{size=192}\n{/size}「Bớt nói gở đi hộ cái...」"
    ###------
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
    "{size=192}\n{/size}Satomi biết, rằng những vụ trộm robot dân sinh gần đây xảy ra ngày càng thường xuyên hơn."
    ###------
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
    "{size=192}\n{/size}Dù vậy, Yumemi chắc không thể lọt vào tầm ngắm của lũ trộm được."
    ###------
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
    "{size=192}\n{/size}「Ừ thì, tôi không chắc có ai có ý định bắt cóc con bé không, cơ mà...」"
    ###------
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
    "{size=192}\n{/size}Gorou nói, đoạn gõ bàn phím và mở một số video."
    ###------
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
    "{size=192}\n{/size}「Trên đường đi con bé đã chụp ngẫu nhiên sáu tấm ảnh đa chiều, nhưng chẳng có cái nào trông đáng ngờ cả. Tất cả đều đúng y như những gì được ghi chép lại.」"
    ###------
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
    "{size=192}\n{/size}「Danh sách mệnh lệnh vẫn được xử lý theo đúng quy trình, không thấy có dấu hiệu bị ngắt quãng bởi những hành động ngoài công việc. Cũng chẳng có mâu thuẫn nào giữa kho lưu trữ dữ liệu với bộ nhớ chính...」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 22 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/280.ogg"
    "{size=192}\n{/size}「Thưa, cho phép tôi được ngắt lời ạ.」"
    ###------
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
    "{size=192}\n{/size}Thế rồi, đối tượng phân tích bắt đầu mở miệng, nghe đầy áy náy."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/284.ogg"
    "{size=192}\n{/size}「Giờ đã là 3:40 chiều.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/286.ogg"
    "{size=192}\n{/size}「Buổi thuyết trình hôm nay lúc 4 giờ do tôi đảm trách. Nếu không phiền, cho phép tôi trở lại với vị trí làm việc của mình ạ.」"
    ###------
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
    "{size=192}\n{/size}「À, phải rồi ha...」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 20 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Satomi liếc đồng hồ treo tường rồi lại hướng về Yumemi."
    ###------
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
    "{size=192}\n{/size}Cô bé nhìn Satomi và Gorou bằng ánh mắt không thể dùng từ ngữ nào khác để miêu tả ngoài ngây thơ vô tội."
    ###------
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
    "{size=192}\n{/size}Mặc dù vẫn hơi đáng dè chừng, nhưng chắc chắn cô bé sẽ không tấn công khách hàng."
    ###------
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
    "{size=192}\n{/size}「Được rồi, em trở lại với công việc đi.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 24 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/296.ogg"
    "{size=192}\n{/size}「Vâng, tôi rõ rồi ạ.」"
    ###------
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
    "{size=192}\n{/size}Cô nhẹ nhàng tháo dây cáp nối trên ngón tay và rời khỏi ghế."
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/300.ogg"
    "{size=192}\n{/size}「Giờ thì, tôi xin phép ạ.」"
    ###------
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
    "{size=192}\n{/size}Cô cúi người lễ phép, rồi rời khỏi phòng máy tính."
    ###------
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
    "{size=192}\n{/size}「Tôi có nên nói lại chuyện này với giám đốc không?」"
    ###------
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
    "{size=192}\n{/size}Gorou vừa hỏi vừa vươn vai trên chiếc ghế xoay cọt kẹt."
    ###------
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
    "{size=192}\n{/size}「Cứ theo dõi thêm một thời gian nữa đã. Chẳng mấy khi được đi nước ngoài như thế, tôi không muốn anh ta phải lo lắng nhiều.」"
    ###------
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
    "{size=192}\n{/size}「Vậy tức là, chị gà đây muốn vọc niêu tôm nhân lúc chủ nhà đi vắng chứ gì?」"
    ###------
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
    "{size=192}\n{/size}「Anh giai mà nói ngon nói ngọt với mấy ông lớn bên kia rồi mang một mẫu Zeiss mới về làm quà thì hay nhỉ.」"
    ###------
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
    "{size=192}\n{/size}「Được thế đã phúc. Tự cái giới kinh doanh này đã sống dở chết dở rồi.」"
    ###------
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
    "{size=192}\n{/size}「Tôi hiểu rồi...」"
    ###------
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
    "{size=192}\n{/size}Hai người lại thở dài."
    ###------
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
    "{size=192}\n{/size}Cửa sổ góc màn hình máy tính hiển thị doanh số hôm nay."
    ###------
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
    "{size=192}\n{/size}0 suất đặt trước, 0 khách hàng trên tổng số 184 ghế ngồi."
    ###------
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
    "{size=192}\n{/size}Suất chiếu đầu tiên vào ngày thường sẽ luôn ít khách, và khi không có khách thì người mới có thể tận dụng thời gian ấy để luyện tập thuyết trình thủ công."
    ###------
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
    "{size=192}\n{/size}Dẫu biết là chẳng còn cách nào khác, nhưng quả nhiên là cô cũng không giữ được bình tĩnh cho nổi."
    ###------
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
    "{size=192}\n{/size}Satomi nhớ về ngày xưa, khi cô nỗ lực trở thành người thuyết trình thiên văn."
    ###------
    scene black
    with fade
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
    with dissolve
    play music "nwa/bgm07.wav"
    voice "ovk/z1000/338.ogg"
    "{size=192}\n{/size}里美(Khoảnh khắc hào hứng, cuồng nhiệt khi con người lần đầu đặt chân lên Sao Hỏa.)"
    ###------
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
    "{size=192}\n{/size}里美(Khoảnh khắc nhân loại cùng đồng lòng hướng về vũ trụ.)"
    ###------
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
    "{size=192}\n{/size}里美(Thời kỳ kính viễn vọng và cung thiên văn tại gia bán đắt như tôm tươi.)"
    ###------
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
    "{size=192}\n{/size}里美(Thời kỳ mà con người có thể hồn nhiên mơ mộng, rằng bản thân đủ năng lực đi tới bất kỳ đâu.)"
    ###------
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
    "{size=192}\n{/size}里美(Cung thiên văn này được dựng lên giữa thời kỳ xô bồ ấy.)"
    ###------
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
    "{size=192}\n{/size}里美(Nhưng những năm tháng bùng nổ vũ trụ kia đã là quá khứ rồi.)"
    ###------
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
    play music "nwa/bgm17.wav"
    voice "ovk/z1000/344.ogg"
    "{size=192}\n{/size}里美(Khi phi hành đoàn trở về mặt đất, mọi người chuyển dần từ tán dương sang thất vọng.)"
    ###------
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
    "{size=192}\n{/size}里美(Người ta phát hiện ra rằng, trên đường trở về từ Sao Hỏa, đã có hai người thiệt mạng trong một sự cố chốt gió.)"
    ###------
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
    "{size=192}\n{/size}里美(Các thành viên khác cũng tổn thương não nghiêm trọng do tiếp xúc lâu dài với bức xạ vũ trụ...)"
    ###------
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
    "{size=192}\n{/size}里美(Cả Trái Đất như bị dội một gáo nước lạnh.)"
    ###------
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
    "{size=192}\n{/size}里美(Bóng tối của vực thẳm mà nhân loại vẫn chưa thể chạm tới, thật đen tối và đáng sợ...)"
    ###------
    scene bg01
    with fade
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
    with dissolve
    "{size=192}\n{/size}Ngay cả chương trình thám hiểm không gian mà ai cũng thấy cần thiết vì là cứu cánh cuối cùng cho vấn nạn bùng nổ dân số và cạn kiệt tài nguyên cũng bị đình chỉ sau khi xây dựng hai thành phố trên Mặt Trăng."
    ###------
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
    "{size=192}\n{/size}Tất cả những cuộc thám hiểm có người lái đều đã bị ngừng lại, và cả kế hoạch khai phá bên ngoài vũ trụ bằng máy bay không người lái cũng không có triển vọng mấy."
    ###------
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
    "{size=192}\n{/size}Trên hết..."
    ###------
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
    "{size=192}\n{/size}里美(Những người có thể dành tình yêu cho các vì sao mô phỏng đâu cả rồi?)"
    ###------
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
    "{size=192}\n{/size}Ngay cả những bảo tàng khoa học đã lắp đặt máy chiếu thế hệ mới và chiếu lên loạt chương trình được trau chuốt tỉ mỉ cũng không tránh khỏi khó khăn."
    ###------
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
    "{size=192}\n{/size}Thật kỳ diệu khi cung thiên văn thuần thương mại này vẫn có thể hoạt động mà không có khoản trợ cấp giáo dục nào."
    ###------
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
    "{size=192}\n{/size}Để thoát khỏi hoàn cảnh bế tắc, giám đốc đã cố gắng thực hiện một kế hoạch cải tử hoàn sinh, đó chính là robot thuyết trình viên tự hành đầu tiên trên thế giới ― Hoshino Yumemi, dù vậy..."
    ###------
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
    play music "nwa/bgm02.wav"
    voice "ovk/z1000/364.ogg"
    "{size=192}\n{/size}「...Thôi không nên nghĩ nhiều về cái tình trạng này nữa. Khách hàng sẽ chạy mất dép cho coi.」"
    ###------
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
    "{size=192}\n{/size}「Tôi biết rồi.」"
    ###------
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
    "{size=192}\n{/size}Hai người nhìn nhau và nói."
    ###------
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
    "{size=192}\n{/size}Satomi vừa rời ghế, toan quay lại quầy tiếp tân, thì cửa phòng máy tính bỗng mở ra."
    ###------
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
    "{size=192}\n{/size}「Kurahashi-san! Em xin phép ạ!」"
    ###------
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
    "{size=192}\n{/size}Morimi Yuka, một thuyết trình viên, chạy đến."
    ###------
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
    "{size=192}\n{/size}Cô ấy đã vào công ty được hai năm, cũng đã quen dần với công việc rồi, thế mà lại đang mất bình tĩnh y như trong kỳ huấn luyện."
    ###------
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
    "{size=192}\n{/size}「Có chuyện gì thế?」"
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan... mất tích rồi...」"
    ###------
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
    "{size=192}\n{/size}「Mất tích...?!」"
    ###------
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
    "{size=192}\n{/size}Gorou và Satomi quay sang nhìn nhau."
    ###------
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
    "{size=192}\n{/size}Và rồi, cuối cùng cả hai cũng hiểu tình hình."
    ###------
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
    "{size=192}\n{/size}Anh kỹ sư ngay lập tức mở máy tính và thuyết trình viên trưởng bật ngay thiết bị định vị đầu cuối."
    ###------
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
    "{size=192}\n{/size}Trên bản đồ chi tiết lấy cung thiên văn trên tầng thượng cửa hàng bách hóa Hanabishi làm trung tâm, đốm sáng chỉ vị trí hiện tại của Hoshino Yumemi đang di chuyển chậm rãi."
    ###------
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
    "{size=192}\n{/size}Cô bé vừa rời khỏi cửa chính và đi về phía nam với vận tốc 6 km/h hướng thẳng tới trạm xe buýt."
    ###------
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
    "{size=192}\n{/size}Satomi dùng cả hai tay ôm mặt..."
    ###------
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
    "{size=192}\n{/size}「Cái con bé nhân viên vụng thối này...」"
    ###------
    scene bg02
    with fade
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
    with dissolve
    play music "nwa/bgm04.wav"
    "雪圏球第４章Người khổng lồ tốt bụng hiện đang gật gù như đang say ngủ."
    ###------
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
    "Ở chính giữa phòng trình chiếu, quả cầu định tính khoác trên người bộ áo đen thẫm đang nằm xuống vị trí bảo trì để kiểm tra bóng đèn."
    ###------
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
    "Máy chiếu vũ trụ 23/3 do Carl Zeiss Jena chế tạo."
    ###------
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
    "Có lẽ cách gọi cổ như \"mô hình vũ trụ\" sẽ phù hợp với cỗ máy này hơn."
    ###------
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
    "Những ai lần đầu chứng kiến có lẽ sẽ bị choáng ngợp trước kích thước và hình dạng kỳ lạ của hai quả cầu được hai cánh tay nâng đỡ này."
    ###------
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
    "Một trong những cỗ máy từng được yêu thích nhất ở Bảo tàng khoa học Kansai suốt một thế kỷ, vốn dự tính sẽ được bảo tồn và trưng bày sau khi sử dụng xong."
    ###------
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
    "Cung thiên văn trên tầng thượng cửa hàng bách hóa Hanabishi đã kế thừa cỗ máy này vào thời điểm khai trương và đến bây giờ nó vẫn được ưu tiên sử dụng hàng đầu."
    ###------
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
    "Không thể phủ nhận rằng nó đã lỗi thời so với loại bóng đơn đang phổ biến, bất kể là loại chiếu quang học, chiếu kỹ thuật số hay loại tích hợp hoàn toàn không cần tới máy chiếu phụ."
    ###------
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
    "Dù vậy thì, bầu trời sao chiếu ra thực sự được làm một cách thủ công."
    ###------
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
    "Ánh sáng bóng đèn dây tóc 1000 watt lớn chiếu qua lớp âm bản định tinh do những người thợ thủ công dệt nên một thế kỷ trước, được khuếch đại chính xác nhờ những thấu kính được đánh bóng tựa hồ đá quý và được chiếu lên màn trần hình cầu cách xa 10 mét."
    ###------
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
    "Độ sắc nét cùng vẻ đẹp mê hoặc khó tả của bầu trời đầy sao này, chắc chắn không hề kém cạnh bất kỳ cỗ máy đời mới nào khác."
    ###------
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
    "Giám đốc và tất cả nhân viên đều tin tưởng như vậy, không chút hoài nghi."
    ###------
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
    "Thế nhưng, sự thật không thể chối cãi là niềm hi vọng này không thu hút nổi khách hàng."
    ###------
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
    "「Phù...」"
    ###------
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
    "Tựa vào cây chổi lau nhà, Satomi thở dài một hơi."
    ###------
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
    "Các thuyết trình viên cấp dưới của cô thì đang lau ghế khán phòng bằng khăn."
    ###------
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
    "Ngay cả những cô gái chưa bao giờ bỏ lỡ cơ hội tán chuyện trong giờ làm cũng bắt đầu lộ rõ thái độ xuống tinh thần."
    ###------
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
    "Sự cố xảy đến sau khi buổi chiếu cuối cùng diễn ra được 15 phút."
    ###------
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
    "Một khách hàng lỡ làm đổ nước ngọt, dẫn đến cãi vã với vị khách khác bên cạnh."
    ###------
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
    "Dẫu có nhắc nhở là không được mang đồ ăn thức uống vào phòng trình chiếu bao nhiêu lần đi chăng nữa, lượng khách lỡ tay đem nước hộp vào phòng chẳng hề có dấu hiệu suy giảm."
    ###------
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
    "Sau khi đèn tắt, cả phòng tối đến độ không nhìn thấy tay mình thì đã quá muộn để cất đồ uống rồi."
    ###------
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
    "Buổi trình diễn bị gián đoạn cho đến khi làm dịu được vị khách hàng nổi nóng và dẫn họ ra khỏi phòng chiếu."
    ###------
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
    "Những lúc thế này, lượng khách ít ỏi quả là một điều đáng mừng."
    ###------
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
    "「A... em xin lỗi. Lúc ấy, em không làm được gì cả...」"
    ###------
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
    "「Đừng để ý quá~. Những việc như này đôi khi vẫn xảy ra mà.」"
    ###------
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
    "Koga Akane đang ra sức động viên Morimi Yuka, nếu không cô sẽ tự trách bản thân mãi khôn nguôi mất."
    ###------
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
    "Công việc của Akane nhìn chung là khó nhọc, ấy nhưng những lúc thế này cô lại lạc quan đến lạ."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/434.ogg"
    "「Vâng. Tôi tin rằng một lần thất bại không thể nói lên giá trị của con người.」"
    ###------
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
    "Cô gái robot lạc quan không kém cũng bình thản lên tiếng."
    ###------
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
    "「Nghe em nói vậy làm chị thấy hơi bối rối đấy, Yumemi-chan.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/440.ogg"
    "「Vâng? Tôi không hiểu ý chị cho lắm.」"
    ###------
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
    "「Ai đã bỏ bê công việc và chạy ra ngoài trong hai ngày liền hả?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/444.ogg"
    "「Vâng, chính là tôi ạ.」"
    ###------
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
    "「.....」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/449.ogg"
    "「...?」"
    ###------
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
    "Sau khi trả lời thật nhiệt tình, cô bé chợt để ý thấy cái lườm lạnh lẽo từ Satomi và khẽ nghiêng đầu."
    ###------
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
    "Con ngươi to tròn vẫn mở rộng, Yumemi trầm ngâm một hồi..."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 06 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/454.ogg"
    "ゆめみ「申し訳ありませんっ！"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 05 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/456.ogg"
    "ゆめみ　今、こうして思い返してみますと、わたしの行為は重大な職務規程違反です、本当に本当に申し訳ありません！」"
    ###------
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
    "Cô bé liên tục cúi đầu xin lỗi, trông chẳng khác nào con người... à không, chẳng khác động cơ của cô đã thay đổi 180 độ."
    ###------
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
    "「Hờ...」"
    ###------
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
    "Dù đã thấy cảnh tượng này không biết bao nhiêu lần rồi, cô vẫn cảm nhận được có gì đó không đúng."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/464.ogg"
    "「Nhưng mà nhé, em nghĩ là mình có thể hiểu được cảm giác của Yumemi-chan đấy.」"
    ###------
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
    "Xem bộ đã chán cái bầu không khí u ám này (và cả việc dọn dẹp nữa), Akane hăng hái tham gia vào câu chuyện."
    ###------
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
    "「Thật á? Chị đây làm việc cùng con bé được 10 năm rồi còn chẳng hiểu nó thật sự nghĩ gì nữa là.」"
    ###------
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
    "茜「だって、普通に考えたらわかりますよー。"
    ###------
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
    "茜　最初だけみんなでチヤホヤしといて飽きたら見向きもしないなんて、わたしならぜったい辞めちゃいますもん。"
    ###------
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
    "茜　ねー？　ゆめみちゃん」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 22 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/476.ogg"
    "ゆめみ「お辞めになるのですか？"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 27 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/478.ogg"
    "ゆめみ　それはとても残念です」"
    ###------
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
    "「Koga-san, mặc dù mới gặp gỡ chưa lâu, nhưng tôi chúc em sẽ tìm được niềm vui trong công việc mới.」"
    ###------
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
    "「A, không phải thế! Không có! Không có! Em nào có định nghỉ đâu ạ!」"
    ###------
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
    "Những cuộc tán gẫu bình dị phản chiếu trên mái vòm, tràn ngập trong phòng trình chiếu."
    ###------
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
    "「Akane-chan mà nghỉ việc thật thì mình chẳng biết phải làm sao nữa.」"
    ###------
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
    "Thấy cô bạn đồng nghiệp cuối cùng cũng mỉm cười, Akane khẽ thì thầm vào tai cô."
    ###------
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
    "「Nói thế chứ tớ muốn kết hôn xong nghỉ việc lắm đó nhaaa.」"
    ###------
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
    "「Ừm... nghe cũng hay thật đấy.」"
    ###------
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
    "「...Hai cái đứa này, chị nghe thấy hết rồi nhé!」"
    ###------
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
    "Khi các đàn anh đàn chị từng dẫn dắt cô lần lượt rời công ty lập gia đình, Satomi hiện là thành viên kỳ cựu thứ hai chỉ sau giám đốc."
    ###------
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
    "里美（今さら甘い夢は見てないけど……"
    ###------
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
    "里美　せめて彼女たちが独り立ちできるまで教えるのは、わたしの責務だもの。"
    ###------
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
    "里美　もし……もしいつか、この職場がなくなったとしても、わたしがここで学んだこと、感じたことの種を残すために）"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "Yumemi vẫn đang nở nụ cười bên cạnh cô, đoạn khẽ nghiêng đầu 15 độ về bên phải."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/508.ogg"
    "「Xin lỗi, tôi có thể hỏi một điều được không ạ?」"
    ###------
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
    "「Gì vậy?　Cứ hỏi đi.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/512.ogg"
    "「Sau khi kết hôn thì buộc phải nghỉ việc sao?」"
    ###------
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
    "「Bảo là bắt buộc thì cũng không phải... còn tùy từng người nữa.」"
    ###------
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
    "Dù chẳng rõ tại sao cô bé lại hỏi như thế, Satomi vẫn đáp."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 03 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/518.ogg"
    "「Là như vậy ạ. Tôi an tâm rồi.」"
    ###------
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
    "Yumemi nói, đôi mắt làm bằng nhựa quang học của cô bé khẽ híp lại."
    ###------
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
    "Satomi chợt nghĩ, biểu cảm trên khuôn mặt cô bé lúc ấy là trông \"con người\" nhất."
    ###------
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
    "「Em xin lỗi vì phải cắt ngang cuộc nói chuyện...」"
    ###------
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
    "Tsuno Hidefumi là trưởng ban bảo trì, tay cầm cờ lê chạy đến gọi cô."
    ###------
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
    "「Số lượng bóng đèn tồn kho cho máy chiếu chính sắp hết rồi, nên em yêu cầu nhập thêm được không ạ?」"
    ###------
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
    "「Tiếc là chị phải từ chối rồi. Mấy cậu phải ráng tận dụng cho tới đầu năm thôi.」"
    ###------
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
    "「Đừng nói với em, chị đi mà nói thẳng với Jena-san ấy...」"
    ###------
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
    "Anh chỉ ngón tay ra máy chiếu đằng sau cùng nụ cười gượng gạo."
    ###------
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
    "Đoạn, anh ta cũng xoa đầu Yumemi một cách thân thiện."
    ###------
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
    "Anh chàng nói cũng có lý, nhưng sao có thể đòi hỏi một thứ không tồn tại được."
    ###------
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
    "Satomi không còn cách nào khác ngoài chấp nhận."
    ###------
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
    "「Hết cách rồi, khách thì ít đến mà đồ cũng chẳng bán được...」"
    ###------
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
    "「Gần đây doanh số bình đồ địa cầu í ẹ lắm. Phía phụ kiện thì thuận lợi hơn hẳn.」"
    ###------
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
    "「Khi trời trở lạnh thì kiểu gì cũng thế.」"
    ###------
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
    "「Cần phải có mặt hàng chủ lực. Nếu được thì là loại chỉ bán trong mùa đông thôi ấy.」"
    ###------
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
    "Trong khi Satomi và Yuka mải suy nghĩ, Akane phát biểu ý tưởng."
    ###------
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
    "「Cầu tuyết thì sao nhỉ?　Cái quả cầu thủy tinh có tuyết rơi bên trong ấy ạ.」"
    ###------
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
    "「Thứ đó thì liên quan gì đến cung thiên văn?」"
    ###------
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
    "Satomi điềm đạm hỏi."
    ###------
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
    "「A... chị thấy đó, chúng tròn tròn này... trông gần giống như cung thiên văn mà ha~」"
    ###------
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
    "Trước câu trả lời chung chung thường thấy ở Akane, Satomi và Yuka cùng thở dài."
    ###------
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
    "「Ừm... vào mùa đông, người ta thường nghĩ về tuyết hơn là sao...」"
    ###------
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
    "「Dù rằng sao trời đông chúng đẹp hơn hẳn...」"
    ###------
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
    "「Sao ấy hả...」"
    ###------
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
    "里美(Không biết có bao nhiêu người mua bình đồ địa cầu để được thấy sao trời hàng thật nhỉ?)"
    ###------
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
    "Cỗ máy trình chiếu 『Jena-san』 giữ nguyên vẻ tĩnh lặng đầy tinh tế."
    ###------
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
    "Vạn nhất nó mà nghe thấy nhân viên nói chuyện với nhau thế này thì chắc sẽ cạn lời lắm đây."
    ###------
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
    "里美(...Cậu đừng có bỏ chạy đấy nhé.)"
    ###------
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
    "Khẩn cầu cỗ máy như thế từ tận tâm can, Satomi vỗ hai tay lại và nói khẽ."
    ###------
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
    "「Được rồi, mười phút nữa chúng ta phải họp đấy, nên mọi người nhanh tay lên nào.」"
    ###------
    scene bg01
    with fade
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
    with dissolve
    play music "nwa/bgm06.wav"
    play sound "nwa/se005.wav"
    "{size=192}\n{/size}雪圏球第５章Sau đó, Yumemi vẫn tiếp tục rời nơi làm việc."
    ###------
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
    "{size=192}\n{/size}Nếu chỉ nhìn qua thì cô bé này chẳng có gì bất thường cả."
    ###------
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
    "{size=192}\n{/size}Miễn có đồng nghiệp xung quanh thì cô sẽ làm những công việc được giao như bình thường."
    ###------
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
    "{size=192}\n{/size}Nhưng hễ đồng nghiệp rời mắt một chút thôi là cô sẽ lon ton chạy ngay ra khỏi sân thượng."
    ###------
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
    "{size=192}\n{/size}Chừng như cô không có một điểm đến cố định."
    ###------
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
    "{size=192}\n{/size}Lang thang vô định khắp các con ngõ, dừng ngẫu nhiên ở một điểm nào đó để quay video ba chiều, rồi cố gắng mời chào khách... thật khó mà mường tượng được mục đích của những hành động này."
    ###------
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
    "{size=192}\n{/size}Cho dù có khiến lịch làm việc dày hơn trước, cho dù có dùng lý do nhân viên lao lực để đưa ra mệnh lệnh ưu tiên, cho dù có ngắt ăng ten truyền tin một cách thủ công khi tính đến trường hợp nhiều khi cô bé đã nhận được tạp âm nào đó..."
    ###------
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
    "{size=192}\n{/size}Tất cả những đối sách có thể nghĩ ra đều kết thúc trong bất lực."
    ###------
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
    play music "nwa/bgm03.wav"
    voice "ovk/z1000/596.ogg"
    "{size=192}\n{/size}「Đây chẳng phải đường chui dưới cầu vượt quốc lộ sao?」"
    ###------
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
    "{size=192}\n{/size}「Lần này con bé đang chào mời khách. Địa điểm là... ở gần giao lộ trước tòa thị chính.」"
    ###------
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
    "{size=192}\n{/size}Satomi và Gorou nhìn chăm chú vào các hình ảnh lần lượt hiển thị trên màn hình ống cực kỳ cổ."
    ###------
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
    "{size=192}\n{/size}Chất lượng hình ảnh tệ và âm thanh khó nghe do hình ảnh được chụp ba chiều bị ép xuống còn hai chiều."
    ###------
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
    "{size=192}\n{/size}Giữa những khung cảnh phố thị bình thường, thỉnh thoảng lại có những cảnh mà ta phải nghiêng đầu mới thấy được."
    ###------
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
    "{size=192}\n{/size}Rác thải sinh hoạt thò ra từ thùng rác, rồi đến ánh mắt của lũ quạ đang bới móc chỗ rác ấy."
    ###------
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
    "{size=192}\n{/size}Hàng dài những tấm áp phích bầu cử giống hệt nhau như thể chúng là tác phẩm nghệ thuật đương đại."
    ###------
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
    "{size=192}\n{/size}Graffiti nối đuôi graffiti trên tường nhà vệ sinh công cộng."
    ###------
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
    "{size=192}\n{/size}Một xe cảnh sát với ánh đèn xanh đỏ quay vòng vòng chạy qua với tốc độ khủng khiếp."
    ###------
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
    "{size=192}\n{/size}「Tôi chẳng nghĩ ra nổi mấy thứ này liên quan chỗ nào...」"
    ###------
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
    "{size=192}\n{/size}「Thật là... con bé đang nghĩ cái quái gì vậy chứ?」"
    ###------
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
    "{size=192}\n{/size}Cũng giống như việc mời chào khách, ngẫu nhiên chụp ảnh đa chiều là một phần nhiệm vụ của Yumemi."
    ###------
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
    "{size=192}\n{/size}Dù rằng liệu nhiệm vụ này có ẩn ý gì không thì, năm mươi-năm mươi."
    ###------
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
    "{size=192}\n{/size}Satomi nhớ lại quãng thời gian sau khi cô nhận nhiệm vụ đào tạo Yumemi từ giám đốc, và cả những lúc cô chưa thể kết thân với cô bé ấy."
    ###------
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
    "{size=192}\n{/size}里美(Liệu sự mâu thuẫn và biến dạng của thế giới sẽ trông như thế nào qua con mắt robot nhỉ?)"
    ###------
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
    "{size=192}\n{/size}里美(Liệu Yumemi đã cảm thấy điều gì, đã suy nghĩ những gì?)"
    ###------
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
    "{size=192}\n{/size}Cho đến tận bây giờ, cô vẫn chưa tìm được câu trả lời."
    ###------
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
    "{size=192}\n{/size}「Tạm thời lúc này ta nên nghĩ cách đối phó hơn là cố tìm hiểu nguyên nhân. Thú thật, với trình độ của tôi thì đến cỡ này là giơ tay xin hàng rồi.」"
    ###------
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
    "{size=192}\n{/size}Gorou nói, đoạn giơ hai tay khỏi bàn phím ra hiệu đầu hàng."
    ###------
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
    "{size=192}\n{/size}「Tôi đã lấy bit chẵn lẻ trên thẻ nhớ và kho lưu trữ rồi, giờ tôi mang dữ liệu sao lưu ra phòng lab để tiến hành gỡ lỗi thì chắc sẽ nghĩ ra được gì đó...」"
    ###------
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
    "{size=192}\n{/size}「Nhưng hiện tại ta khó mà loại trừ được khả năng có phần cứng bị trục trặc.」"
    ###------
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
    "{size=192}\n{/size}「Đại ý là, giờ ta phải cho con bé \"nhập viện\" hả...?」"
    ###------
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
    "{size=192}\n{/size}里美(...đã hết thời hạn bảo hành rồi.)"
    ###------
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
    "{size=192}\n{/size}Với tư cách một người quản lý thu chi, cô bắt đầu suy nghĩ về khía cạnh tiền nong."
    ###------
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
    "{size=192}\n{/size}Nếu là cái người dính Yumemi như giám đốc thì chắc chắn anh ta sẽ không ngần ngại lệnh cho cấp dưới đưa cô bé đến nơi sản xuất, nhưng may mắn thay (hoặc không), chuyến khảo sát châu Âu của anh ta vẫn còn tới năm ngày nữa."
    ###------
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
    "{size=192}\n{/size}「Tôi hiểu rồi...」"
    ###------
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
    "{size=192}\n{/size}Satomi nghĩ tiếp."
    ###------
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
    "{size=192}\n{/size}里美(Theo như tờ hướng dẫn, có lẽ sẽ cần tắt nguồn chính và dừng hệ điều hành.)"
    ###------
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
    "{size=192}\n{/size}里美(Nhưng chúng ta thường xuyên thiếu nhân lực và một số vị khách đến chỉ để gặp Yumemi.)"
    ###------
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
    "{size=192}\n{/size}里美(Suy nghĩ đơn giản thì, chỉ cần có người để mắt đến Yumemi là sẽ chẳng còn vấn đề gì nữa.)"
    ###------
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
    "{size=192}\n{/size}里美(Kể cả có chạy đi, thì một cỗ máy hỗ trợ công việc như Yumemi sẽ không thể hoạt động được trong phạm vi ngoài 3 km từ nơi làm việc...)"
    ###------
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
    "{size=192}\n{/size}里美(Đó là nguyên tắc chung cho robot để đảm bảo chúng không làm hại con người mọi lúc.)"
    ###------
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
    "{size=192}\n{/size}里美(Với cả, đúng là khó mà nhờ mấy gian hàng tầng dưới bắt hộ con robot của mình nếu nó có đi qua thật...)"
    ###------
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
    "{size=192}\n{/size}「Mất thời gian chút cũng được, Gorou-kun tự làm một mình được chứ?」"
    ###------
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
    "{size=192}\n{/size}「Con bé cũng chưa phá phách gì cả. Cần thiết thì chị sẽ đến đưa nó về.」"
    ###------
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
    "{size=192}\n{/size}「Dù chị nói vậy thì...」"
    ###------
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
    play music "nwa/bgm17.wav"
    play sound "nwa/se013.wav"
    "{size=192}\n{/size}Gorou đáp, đoạn mở cửa sổ khác lên màn hình."
    ###------
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
    "{size=192}\n{/size}Nom như một cái video truyền hình vệ tinh trực tiếp."
    ###------
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
    "{size=192}\n{/size}Một đám đông cầm panô ghi mớ tiếng Anh tệ hại đang hô vang khẩu hiệu gì đó."
    ###------
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
    "{size=192}\n{/size}Một cột lửa trại được nhóm ngay giữa, và một gã đàn ông mặc áo sơ mi hình như có in mấy dòng chữ đang rưới vào đó một loại dầu quân dụng thời xưa."
    ###------
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
    "{size=192}\n{/size}Nằm giữa đống lửa đang bùng lên ấy, là những robot đồng hành xếp chồng chất lên nhau."
    ###------
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
    "{size=192}\n{/size}「Uầy... sao họ có thể thản nhiên thiêu cháy một cỗ máy hình người như thế nhỉ...」"
    ###------
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
    "{size=192}\n{/size}Satomi bất giác cau mày."
    ###------
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
    "{size=192}\n{/size}Dẫu vốn biết đây chỉ là những bộ khung thế hệ cũ kiểu gì cũng bị vứt bỏ, và rằng đây chỉ là một cuộc biểu tình khác của đám người thất nghiệp, nhưng quả tình vẫn chẳng phải khung cảnh đáng xem gì cho cam."
    ###------
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
    "{size=192}\n{/size}「Có mang hình người hay không thì cũng đừng có đốt đi như vậy chứ. Không phân tách chúng đúng cách thì sẽ khó tái chế lắm.」"
    ###------
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
    "{size=192}\n{/size}「Vấn đề đâu có nằm ở đó chứ?」"
    ###------
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
    "{size=192}\n{/size}「Mà, chuyện này thuộc phạm trù tranh chấp thương mại hơn là vấn đề tuyển dụng.」"
    ###------
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
    "{size=192}\n{/size}「Cứ như thế này thì rồi sẽ lan tới cả cộng đồng những người có việc làm, tiếp đó trong tương lai gần, việc một phong trào bài trừ robot tương tự thế này xảy ra cũng không lạ.」"
    ###------
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
    "{size=192}\n{/size}「Quả thật, có nghĩ lạc quan thì vẫn thấy một robot lang thang ngoài đường đúng là rủi ro.」"
    ###------
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
    "{size=192}\n{/size}里美(Không có phong trào tẩy chay thì vấn đề cũng đã chất đống rồi.)"
    ###------
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
    play music "nwa/bgm03.wav"
    voice "ovk/z1000/697.ogg"
    "{size=192}\n{/size}「Mà, chỉ cần chúng ta để mắt đến con bé thì mọi chuyện sẽ ổn thôi.」"
    ###------
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
    "{size=192}\n{/size}Hiện tại, cả hai đang ngồi trên ghế nhựa trong khu tiếp tân."
    ###------
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
    "{size=192}\n{/size}Cung thiên văn nằm trên tầng thượng của trung tâm bách hóa Hanabishi và chỉ có duy nhất một lối vào."
    ###------
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
    "{size=192}\n{/size}Nói cách khác, nếu cô bé muốn xuống tầng thì chắc chắn sẽ phải đi qua khu vực này."
    ###------
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
    "{size=192}\n{/size}「Ngay từ đầu mình làm thế này có phải ngon rồi không.」"
    ###------
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
    "{size=192}\n{/size}「...Chị không thấy cách xử lý này vốn dĩ đã sai sai rồi à?」"
    ###------
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
    "{size=192}\n{/size}「Tình huống khẩn cấp mà, biết sao được. Thế Gorou-kun canh đến bốn giờ nhé, nhờ cậu đấy.」"
    ###------
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
    "{size=192}\n{/size}「Công việc của tôi cũng đang chất đống kia mà.」"
    ###------
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
    "{size=192}\n{/size}「Việc thì ngồi đây làm cũng được chứ gì? Ở đây cậu vẫn kết nối được với dữ liệu máy chủ đúng không?」"
    ###------
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
    "{size=192}\n{/size}Gorou cạn lời khi nhìn vào con thiết bị đầu cuối quá mức lỗi thời đến độ gần như không thể sử dụng, còn Satomi thì biểu lộ một khuôn mặt sảng khoái hiếm thấy."
    ###------
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
    "{size=192}\n{/size}Cho đến hiện tại thì buổi trình chiếu vẫn chưa có vấn đề gì."
    ###------
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
    "{size=192}\n{/size}Thuyết trình viên hiện thời Mayuzumi Chihaya dù chỉ làm bán thời gian nhưng lại là một người vô cùng điềm tĩnh, nên cô cũng không cảm thấy quá lo lắng."
    ###------
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
    "{size=192}\n{/size}Akane đang giám sát Yumemi, người hiện đứng cạnh cửa thoát hiểm để đề phòng có khách rời khỏi chỗ trong lúc trình chiếu."
    ###------
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
    "{size=192}\n{/size}Phân chia công việc thế này rồi thì làm sao còn chuyện gì xảy ra được nữa."
    ###------
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
    "{size=192}\n{/size}Điều duy nhất khiến cô để tâm là lượng khách hàng vẫn ít ỏi như thường lệ."
    ###------
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
    "{size=192}\n{/size}「Thế thôi, tôi quay lại phòng chờ nhé...」"
    ###------
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
    "{size=192}\n{/size}Vừa dứt lời, cô chợt cảm thấy một sự hiện diện đáng lo ngại đằng sau quầy."
    ###------
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
    play music "nwa/bgm05.wav"
    voice "ovk/z1000/724.ogg"
    "{size=192}\n{/size}「Bà cô ơi bà cô!」"
    ###------
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
    "{size=192}\n{/size}Rụt rè quay về phía giọng nói phát ra, cô chợt thấy hai cậu bé mang ba lô và khoác trên người bộ đồng phục từ một trường tiểu học công lập."
    ###------
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
    "{size=192}\n{/size}「Keita-kun... Yuusuke-kun...」"
    ###------
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
    "{size=192}\n{/size}Không ai làm việc trong Bảo tàng cung thiên văn Hanabishi mà không biết tới sự khủng khiếp của bộ đôi này."
    ###------
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
    "{size=192}\n{/size}「Bà cô nè, Yumemi-chan có ở đây không?」"
    ###------
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
    "{size=192}\n{/size}Thằng bé hỏi bằng năng lượng tràn trề, rõ là thiếu kiên nhẫn trong lúc đặt chiếc ba lô da bóng lộn của mình xuống."
    ###------
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
    "{size=192}\n{/size}「Bây giờ Yumemi-chan đang làm việc mất rồi. Hôm nay các em chơi cùng anh Gorou đây có được không?」"
    ###------
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
    "{size=192}\n{/size}Cô quay lại với một nụ cười méo xệch, chỉ để thấy chiếc ghế xếp bên cạnh đã trống rỗng tự lúc nào, dù vẫn còn hơi ấm người ngồi."
    ###------
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
    "{size=192}\n{/size}「Ặc, chạy mất rồi...」"
    ###------
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
    "{size=192}\n{/size}Dù là hiện tại hay quá khứ, thì trẻ em vẫn luôn là khách hàng yêu thích của cung thiên văn."
    ###------
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
    "{size=192}\n{/size}Không như các cặp đôi nhiều khả năng chỉ tới xem một lần hoặc các nhân viên văn phòng ngay từ đầu đến chỉ để ngủ trưa, trẻ con rất nhiệt tình xem chương trình, và một khi đã thích thì chúng sẽ quay lại nhiều lần nữa."
    ###------
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
    "{size=192}\n{/size}Dù có là giá vé trẻ em thì một người vẫn là một người đấy, không đùa được đâu."
    ###------
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
    "{size=192}\n{/size}Nhưng trong số đó, vẫn có vài đứa cần phải đặc biệt chú ý."
    ###------
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
    "{size=192}\n{/size}Đặc biệt, bộ đôi này thường trực tiếp chạy từ trường tiểu học tới để chơi đùa... hay nói đúng hơn, là để trêu chọc những thuyết trình viên ngây thơ."
    ###------
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
    "{size=192}\n{/size}Chúng chắc chắn nằm trong tốp 10 đứa trẻ hư nhất mà Satomi tiếp xúc kể từ khi khai trương."
    ###------
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
    "{size=192}\n{/size}「Thế thì bà cô cũng được. Dạy bọn này học đi!」"
    ###------
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
    "{size=192}\n{/size}「Không phải \"Bà cô\", phải gọi là \"Chị\", nghe chưa.」"
    ###------
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
    "{size=192}\n{/size}「Nè nè, xem con robot này đi, ngầu phết nhờ? Chỉ cần bấm nút này là nó sẽ đấm một phát đấy!」"
    ###------
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
    "{size=192}\n{/size}「Thôi được rồi, chị sẽ giúp lần lượt, lần lượt―― khoan, đây chẳng phải câu hỏi môn thực hành xã hội à?」"
    ###------
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
    "{size=192}\n{/size}「Đã bảo chuyên môn của chị là thần thoại với trời sao cơ mà?」"
    ###------
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
    "{size=192}\n{/size}「Ơ kìa, bà cô không biết cái này hởở. Yumemi-chan thì cái gì cũng biết luôn đó.」"
    ###------
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
    "{size=192}\n{/size}「Chị biết rồi!　Mà này, đừng gọi \"bà cô\" nữa, gọi \"chị\" nghe chưa!」"
    ###------
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
    "{size=192}\n{/size}「Ờ để xem nào... là thời Yayoi nên chắc đáp án 3 \"Trồng lúa\"... gượm đã, để chị làm hộ thì còn ý nghĩa gì nữa?」"
    ###------
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
    "{size=192}\n{/size}「Jet screw punch!」"
    ###------
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
    "{size=192}\n{/size}「Ái đau đau! Chị đầu hàng chị đầu hàng, đừng có đánh nữa!」"
    ###------
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
    "{size=192}\n{/size}Trong khi đảm đương vai trò giáo viên phụ đạo và quái vật không gian cùng một lúc, Satomi tỏ ra quan ngại sâu sắc về sự khó khăn và phi lý của công việc thuyết trình viên tại cung thiên văn."
    ###------
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
    "{size=192}\n{/size}里美(Phải công nhận là tiếp đón những ngài khách bất kham kiểu này đúng là chuyên môn của Yumemi.)"
    ###------
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
    "{size=192}\n{/size}Nghĩ vậy khiến cô thấy mình càng đáng thương hơn."
    ###------
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
    "{size=192}\n{/size}Sau 15 phút vật lộn với lũ nhóc, cô đã chạm tới giới hạn, cả về mặt thể chất lẫn tinh thần."
    ###------
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
    "{size=192}\n{/size}「Này, buổi chiếu sắp xong rồi, chị gái phải quay lại công việc đây...」"
    ###------
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
    "{size=192}\n{/size}Cô nhìn ra cuối hành lang mà nói như van xin, đúng lúc ấy..."
    ###------
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
    "{size=192}\n{/size}Mái tóc ngắn tung bay, Akane chạy tới chỗ cô."
    ###------
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
    "{size=192}\n{/size}Những tưởng trời cuối cùng cũng thương mình, thì chợt cô cảm thấy có gì đó không ổn."
    ###------
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
    "{size=192}\n{/size}「Em xin lỗi, cho em hỏi Yumemi-chan có qua đây không ạ~ mà hình như ở đây có vài vị khách không mời mà đến.」"
    ###------
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
    "{size=192}\n{/size}「Jet Buster Missile!」"
    ###------
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
    "{size=192}\n{/size}Akane giật mình khi bị một đầu đạn bằng nhựa bay tới tấn công."
    ###------
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
    "{size=192}\n{/size}「...Yumemi-chan?」"
    ###------
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
    "{size=192}\n{/size}「Không có ở đấy á?」"
    ###------
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
    "{size=192}\n{/size}「Vâng, lúc em dẫn khách đi vệ sinh về thì đã không thấy con bé đâu rồi...」"
    ###------
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
    "{size=192}\n{/size}「Hảảảả?! Chị ở đây nãy giờ cơ mà?」"
    ###------
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
    "{size=192}\n{/size}Cảm thấy bầu không khí có chút kỳ lạ, hai cậu bé đang thực hiện những hành vi bạo ngược tột cùng chợt dừng lại nhìn nhau."
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan vừa đi ra ngoài xong nhờ~?」"
    ###------
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
    "{size=192}\n{/size}「Ờ, vừa đi xong.」"
    ###------
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
    "{size=192}\n{/size}「.....」"
    ###------
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
    "{size=192}\n{/size}「Ahahahaha...」"
    ###------
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
    "{size=192}\n{/size}Satomi và Akane không khỏi bật cười thất thần."
    ###------
    scene bg02
    with fade
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
    with dissolve
    play music "nwa/bgm10.wav"
    play sound "nwa/se018.wav"
    "{size=192}\n{/size}雪圏球第６章Với bộ đồng phục thuyết trình viên cùng áo choàng trên người, Satomi bước ra ngoài cửa chính."
    ###------
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
    "{size=192}\n{/size}Không cần vội quá mà làm gì. "
    ###------
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
    "{size=192}\n{/size}ゆめみの歩行速度ではそう遠くまでは行き着けないし、イーポス位置把握端末のおかげで現在位置も筒抜けだ。"
    ###------
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
    "{size=192}\n{/size}Hơn nữa hệ thống có cả chìa khóa và phím bấm để phát tín hiệu dừng trong trường hợp khẩn cấp."
    ###------
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
    "{size=192}\n{/size}里美(...Cứ tưởng cuối cùng cũng được nghỉ xả hơi, mà thôi kệ vậy...)"
    ###------
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
    "{size=192}\n{/size}Trước những bước chân hối hả đầy bực dọc của Satomi, người trên đường chỉ còn biết né sang bên."
    ###------
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
    "{size=192}\n{/size}Satomi hiểu rõ hơn ai hết rằng sẽ thật vô nghĩa khi nổi nóng với Yumemi."
    ###------
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
    "{size=192}\n{/size}Dù vậy, nỗi thất vọng vẫn ngự trị trong cô."
    ###------
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
    "{size=192}\n{/size}里美(Yumemi chắc chắn sẽ không bỏ đi.)"
    ###------
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
    "{size=192}\n{/size}里美(Cho dù điều kiện công việc có tồi tệ đến mức nào, con bé nhất định sẽ không phàn nàn.)"
    ###------
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
    "{size=192}\n{/size}里美(Yumemi vốn được tạo ra như vậy mà.)"
    ###------
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
    "{size=192}\n{/size}里美(Ngoại trừ yêu cầu làm hại con người, thì robot không có quyền từ chối mệnh lệnh nào cả.)"
    ###------
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
    "{size=192}\n{/size}里美(Dù có là mệnh lệnh lố bịch đến mức nào, thì robot cũng không thể lý giải hay đánh giá được.)"
    ###------
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
    "{size=192}\n{/size}里美(Nếu vậy thì bây giờ, mình đang đuổi theo thứ gì đây?)"
    ###------
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
    "{size=192}\n{/size}里美(Nếu không phải chán ghét, thì tại sao mình lại không mừng vui chút nào?)"
    ###------
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
    "{size=192}\n{/size}Satomi không hiểu."
    ###------
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
    "{size=192}\n{/size}Bỗng, cô trông thấy bóng lưng quen thuộc."
    ###------
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
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    play sound "nwa/se019.wav"
    "{size=192}\n{/size}Qua ánh đèn đầy bụi, Yumemi đang lang thang trên vỉa hè lát gạch trong buổi chiều tà."
    ###------
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
    "{size=192}\n{/size}Tà váy của cô bé ― vốn đóng vai trò như khe tản nhiệt ― được xẻ thành năm phần, để lộ đôi chân quyến rũ."
    ###------
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
    "{size=192}\n{/size}Mái tóc dài rủ xuống hai bên, nhẹ nhàng đong đưa theo từng nhịp bước."
    ###------
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
    "{size=192}\n{/size}Nom như cô không hề lạc lối trong nơi mình cần đi, hay việc mình phải làm."
    ###------
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
    "{size=192}\n{/size}「Yume...」"
    ###------
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
    "{size=192}\n{/size}Satomi toan gọi Yumemi, nhưng vì lý do nào đó mà cô ngừng lại."
    ###------
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
    "{size=192}\n{/size}里美(Thử đi theo con bé xem sao.)"
    ###------
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
    "{size=192}\n{/size}歩調をゆるめ、小さく息を吐いた。"
    ###------
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
    "{size=192}\n{/size}Nếu chú ý quan sát hành động, thì biết đâu sẽ tìm ra được nguyên nhân khiến cô bé cứ \"mất tích\" không chừng."
    ###------
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
    "{size=192}\n{/size}Cô tự biện hộ như vậy."
    ###------
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
    "{size=192}\n{/size}里美(Thật ra, có thể là mình đang sợ hãi.)"
    ###------
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
    "{size=192}\n{/size}里美(Sợ rằng Yumemi sẽ rời xa nơi làm việc... rời xa mình mà chẳng màng ngoảnh lại.)"
    ###------
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
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    hide kr_f
    hide kr_b
    with dissolve
    play sound "nwa/se019.wav"
    "{size=192}\n{/size}Như muốn đi ngược lại với dòng người hướng về phía nhà ga, Yumemi rảo bước theo hướng tây bắc trên con đường chỉ cách khu phồn hoa một con phố."
    ###------
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
    "{size=192}\n{/size}大型電器店の店頭、流麗なコスチュームに身を包んだ最新型のコンパニオンロボットたちが、リアルビジョン超高精細立体受像器の実演をしている。"
    ###------
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
    "{size=192}\n{/size}Màn hình demo đang chiếu tin tức về những phi thuyền không gian bắt đầu khai thác lộ trình đến cảng Mặt Trăng đầu tiên."
    ###------
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
    "{size=192}\n{/size}Các tiếp viên mặc đồng phục đang đứng tươi cười dọc lối đi cho khách cũng là những robot đồng hành được chế tác tại cùng một nơi với chỗ phi thuyền đó."
    ###------
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
    "{size=192}\n{/size}里美(Quả thật, vũ trụ đang ngày càng gần chúng ta hơn.)"
    ###------
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
    "{size=192}\n{/size}里美(Nhất là với một bộ phận người giàu, kỹ sư thuộc địa và quân nhân.)"
    ###------
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
    "{size=192}\n{/size}Một cậu nhân viên văn phòng băng qua đường mà không thèm nhìn đèn tín hiệu."
    ###------
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
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 22 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    play sound "nwa/se021.wav"
    "{size=192}\n{/size}Anh ta định bước lên lề đường qua khoảng trống giữa thanh chắn, để rồi vai lại chạm vào Yumemi đang đi trên mép lề."
    ###------
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
    "{size=192}\n{/size}「...muốn gì?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 07 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/891.ogg"
    "{size=192}\n{/size}「Tôi thật sự xin lỗi, anh có sao không ạ?」"
    ###------
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
    "{size=192}\n{/size}Yumemi ngay lập tức dừng lại và cúi thấp đầu một cách không cần thiết."
    ###------
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
    "{size=192}\n{/size}Khi nhận ra mình vừa va phải robot, mặt anh chàng lộ rõ vẻ lúng túng và nhanh chóng bỏ đi."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/896.ogg"
    "{size=192}\n{/size}「Thật mừng vì anh không sao cả.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/898.ogg"
    "{size=192}\n{/size}「Giờ thì, tôi xin phép ạ.」"
    ###------
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
    "{size=192}\n{/size}Yumemi nói với khoảng không rồi tiếp tục cất bước."
    ###------
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
    "{size=192}\n{/size}――và đột nhiên khựng lại."
    ###------
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
    "{size=192}\n{/size}Satomi suýt nữa vấp chân, vội vã náu mình đằng sau biển hiệu của quán rượu."
    ###------
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
    "{size=192}\n{/size}Cô lo lắng, chẳng lẽ mình đã bị phát hiện rồi sao."
    ###------
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
    "{size=192}\n{/size}Yumemi tôn kính cúi chào hai bên trái phải, rồi đặt lòng bàn tay này lên mu bàn tay kia."
    ###------
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
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    play music "nwa/bgm16.wav"
    voice "ovk/z1000/906.ogg"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###------
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
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/908.ogg"
    "{size=192}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###------
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
    "{size=192}\n{/size}Với nụ cười mơ màng, cô bé mời gọi những người qua đường."
    ###------
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
    "{size=192}\n{/size}Ngay từ lần đầu nhận việc, cô gái này đã thu hút được một đám đông lớn."
    ###------
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
    "{size=192}\n{/size}Robot tiếp tân loại người máy thực tiễn tiên phong được chế tạo hoàn toàn dựa trên cơ sở Luật Cơ bản về việc vận hành những cỗ máy tự động mô phỏng con người, hay thường được gọi là \"Luật Robot\"."
    ###------
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
    "{size=192}\n{/size}Cả người lớn và trẻ em đều dõi theo nhất cử nhất động của Yumemi, không giấu được sự tò mò và phấn khích."
    ###------
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
    "{size=192}\n{/size}Hẳn mọi người đều mường tượng ra biết bao viễn cảnh tương lai thông qua cô robot dạng thiếu nữ trông chẳng khác nào con người này."
    ###------
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
    "{size=192}\n{/size}Thấm thoát mười năm trôi qua, robot giờ đây đã trở nên phổ biến."
    ###------
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
    "{size=192}\n{/size}Họ vừa là thành phần thiết yếu trong xã hội, nhưng đồng thời họ cũng gây ra đủ loại vấn đề."
    ###------
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
    "{size=192}\n{/size}Dù vậy, ấy là lẽ tất yếu."
    ###------
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
    "{size=192}\n{/size}Là điều không thể tránh khỏi."
    ###------
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
    "{size=192}\n{/size}Những con người sáng mắt lên khi lần đầu tiên chạm vào xe ô tô chắc chẳng bao giờ ngờ tới vấn đề ô nhiễm hay tai nạn giao thông mà nó đem lại."
    ###------
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
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/921.ogg"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?...」"
    ###------
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
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Sau khi lặp lại bài văn hai lần, Yumemi dừng cử động một lúc, vẫn giữ nguyên nụ cười thiên thần."
    ###------
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
    "{size=192}\n{/size}Một khi xác định được người quan tâm tới mình, cô bé sẽ in tờ rơi chương trình của ngày hôm nay, kéo ra khỏi khe thẻ ở tai trái và đưa chúng cho họ."
    ###------
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
    "{size=192}\n{/size}Đương nhiên, không ai đến gần cô cả."
    ###------
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
    "{size=192}\n{/size}Yumemi tiếp bước."
    ###------
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
    "{size=192}\n{/size}Satomi đi theo."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    hide bg21b
    with dissolve
    play music "nwa/bgm11.wav"
    "{size=192}\n{/size}Vụ bám đuôi lạ lùng đột ngột kết thúc."
    ###------
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
    "{size=192}\n{/size}Cách xa con phố nhộn nhịp khoảng 2 km về phía tây bắc, là một khu phố với hàng dài những căn chung cư cũ xếp san sát nhau."
    ###------
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
    "{size=192}\n{/size}Lúc này đây, Satomi mới đâm lo rằng nơi này đã cách quá xa chỗ làm việc."
    ###------
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
    "{size=192}\n{/size}Đột nhiên, Yumemi dừng bước."
    ###------
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
    "{size=192}\n{/size}Cô bé di chuyển phần trên cổ, nhìn xung quanh như đang tìm kiếm gì đó."
    ###------
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
    "{size=192}\n{/size}Cử chỉ này vô cùng quen thuộc."
    ###------
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
    "{size=192}\n{/size}Cái hồi mà đến những hành vi cơ bản vẫn còn vụng về, mỗi lần pin yếu Yumemi sẽ đứng yên bất động, giữ nguyên tư thế chờ, làm cho mọi người ai cũng hoảng hồn."
    ###------
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
    "{size=192}\n{/size}Do đó Satomi đã dặn dò cô bé."
    ###------
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
    "{size=192}\n{/size}Rằng 『Khi nào pin yếu hoặc chuẩn bị vào chế độ ngủ thì ráng tìm chỗ nào mà ngồi xuống.』"
    ###------
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
    "{size=192}\n{/size}Ở cuối ngã ba có một công viên nhỏ."
    ###------
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
    "{size=192}\n{/size}Đứng trước lối vào, Yumemi nhìn chằm chằm hai thanh chắn xe xếp song song nhau, chừng như đang phán đoán xem nó có đỡ được trọng lượng của mình không, rồi như đã quyết định, cô bé tới đó, ngồi xuống và ngừng cử động."
    ###------
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
    "{size=192}\n{/size}Chẳng khác nào một vở kịch câm của nghệ sĩ đường phố."
    ###------
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
    "{size=192}\n{/size}「Hết pin mất rồi à, chết thật...」"
    ###------
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
    "{size=192}\n{/size}Satomi lẩm bẩm."
    ###------
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
    "{size=192}\n{/size}里美(Dạo gần đây xô bồ quá nên mình quên mất không để ý lượng pin còn lại...)"
    ###------
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
    "{size=192}\n{/size}里美(Huống hồ mình biết thừa việc liên tục tự động đi bộ sẽ rất hao pin rồi mà...)"
    ###------
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
    "{size=192}\n{/size}Chắc vẫn có thể giao tiếp và truyền tin, song Yumemi lại không có khả năng tự mình gọi dịch vụ sạc điện."
    ###------
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
    "{size=192}\n{/size}Trong chế độ tiết kiệm pin, cô bé thậm chí còn chẳng thể đi bộ, nên nếu cứ để yên thì cô sẽ ngồi đó vĩnh viễn mất."
    ###------
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
    "{size=192}\n{/size}「Hờ...」"
    ###------
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
    "{size=192}\n{/size}Sau khi thở dài lần thứ bao nhiêu chẳng rõ, Satomi toan tiếp cận cô bé."
    ###------
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
    "{size=192}\n{/size}Thì chợt, một bé gái chạy lon ton ra khỏi công viên."
    ###------
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
    "{size=192}\n{/size}赤い靴に赤い帽子、少し前に流行したポーラーヤーン人造毛糸の可愛らしいコートを着ている。"
    ###------
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
    "{size=192}\n{/size}Thấy Yumemi không cử động gì, cô bé tỏ vẻ lo lắng."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 11 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/977.ogg"
    "{size=192}\n{/size}「Chị ơi, chị có sao không?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/979.ogg"
    "{size=192}\n{/size}「Vâng, do tình trạng thiếu hụt năng lượng mà một vài chức năng đã bị giới hạn, nhưng tôi không dò ra được bộ phận nào bị hỏng hay trục trặc cả.」"
    ###------
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
    "{size=192}\n{/size}Yumemi trả lời một cách nghiêm túc."
    ###------
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
    "{size=192}\n{/size}Biểu cảm của cô trông cứ đơ đơ sao đó."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/984.ogg"
    "{size=192}\n{/size}「Tôi xin lỗi vì đã để em phải lo lắng.」"
    ###------
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
    "{size=192}\n{/size}Vẫn trong tư thế ngồi, cô cúi đầu và bày tỏ niềm tiếc nuối sâu sắc."
    ###------
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
    "{size=192}\n{/size}「？？」"
    ###------
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
    "{size=192}\n{/size}Nét mặt của cô bé cho thấy em chẳng hiểu mô tê gì cả."
    ###------
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
    "{size=192}\n{/size}Satomi chạy đến cạnh em, quỳ xuống cho ngang chiều cao của em rồi từ tốn nói."
    ###------
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
    "{size=192}\n{/size}「Em không phải lo đâu, chị gái này là robot mà.」"
    ###------
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
    "{size=192}\n{/size}「Chị ấy... là robot ư?」"
    ###------
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
    "{size=192}\n{/size}Cô bé tròn mắt và nhìn chằm chằm vào Yumemi."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/999.ogg"
    "{size=192}\n{/size}「Vâng. Tôi là một robot.」"
    ###------
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
    "{size=192}\n{/size}Yumemi trông yếu ớt hơn mọi khi, song vẫn nở nụ cười đầy tự hào."
    ###------
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
    "{size=192}\n{/size}女の子は背伸びをし、ちいさな拳を振り上げて……"
    ###------
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
    "{size=192}\n{/size}「Hây!」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Rồi đánh vào đầu Yumemi/"
    ###------
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
    "{size=192}\n{/size}Trong một khoảnh khắc, Satomi không hiểu chuyện gì đang xảy ra."
    ###------
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
    "{size=192}\n{/size}「Hây! Hây! Hây!...」"
    ###------
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
    "{size=192}\n{/size}Hai lần, ba lần, bốn lần, cô bé đánh Yumemi không ngừng nghỉ."
    ###------
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
    "{size=192}\n{/size}Yumemi ngây người ra, chẳng rõ phải phản ứng thế nào."
    ###------
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
    "{size=192}\n{/size}Thấy không ăn thua, cô bé giơ cánh tay cao hơn."
    ###------
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
    play music "nwa/bgm06.wav"
    play sound "nwa/se027.wav"
    voice "ovk/z1000/1015.ogg"
    "{size=192}\n{/size}「Đừng...」"
    ###------
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
    "{size=192}\n{/size}Satomi bừng tỉnh, lập tức can thiệp."
    ###------
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
    "{size=192}\n{/size}Mặc dù bị bao phủ trong các sợi trao đổi nhiệt được mô phỏng lại giống như tóc, nhưng khung bên trong vẫn được tạo thành từ hợp kim titan và magiê."
    ###------
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
    "{size=192}\n{/size}Dù chỉ là lực đánh của một đứa trẻ, thì đánh liên tục như thế cũng không thể nào bình an vô sự được."
    ###------
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
    "{size=192}\n{/size}「Đưa tay chị xem nào? Em không bị thương chứ?」"
    ###------
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
    "{size=192}\n{/size}Cô mở bàn tay phải nắm chặt của cô bé ra và kiểm tra."
    ###------
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
    "{size=192}\n{/size}Một bàn tay xinh xắn, tựa hồ chiếc lá thu gấp theo kiểu origami."
    ###------
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
    "{size=192}\n{/size}Đầu ngón tay của em đã ửng đỏ."
    ###------
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
    "{size=192}\n{/size}Bé gái chực khóc."
    ###------
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
    "{size=192}\n{/size}Song lại không khóc."
    ###------
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
    "{size=192}\n{/size}Cô bé đang quyết liệt kìm nén cảm xúc."
    ###------
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
    "{size=192}\n{/size}「Cha bảo...」"
    ###------
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
    "{size=192}\n{/size}Chừng như em đang giận dữ."
    ###------
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
    "{size=192}\n{/size}Bằng tông giọng yếu ớt, em lên tiếng với Satomi."
    ###------
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
    "{size=192}\n{/size}「Cha nói, tất cả chỉ vì robot... mà cha bị mất việc...」"
    ###------
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
    "{size=192}\n{/size}Đôi mắt vẫn nhìn thẳng vào Satomi, lệ từ từ đọng trên khóe mi em."
    ###------
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
    "{size=192}\n{/size}「Yukino-chan, dừng lại đi con!」"
    ###------
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
    "{size=192}\n{/size}Một người phụ nữ khoác theo túi mua đồ bằng vải kéo cô bé ra khỏi Satomi như muốn lôi em đi."
    ###------
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
    "{size=192}\n{/size}Hẳn là mẹ của cô bé ấy."
    ###------
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
    "{size=192}\n{/size}Cô nhìn về phía Satomi ― vẫn đang quỳ gối ― ra chiều muốn cầu xin gì đó, rồi khẽ cúi đầu."
    ###------
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
    "{size=192}\n{/size}Sau đó cô kéo tay bé gái và rời khỏi công viên."
    ###------
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
    "{size=192}\n{/size}Trước khi rẽ vào con hẻm, người mẹ một lần nữa nhìn về phía này và cúi đầu xin lỗi."
    ###------
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
    "{size=192}\n{/size}Khi thân ảnh cô đã khuất khỏi tầm nhìn, Satomi vẫn chìm trong suy tư."
    ###------
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
    "{size=192}\n{/size}里美(Nếu cô bé kia lẫn người mẹ mà thái quá hơn rồi ra sức khiển trách mình và Yumemi...)"
    ###------
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
    "{size=192}\n{/size}里美(...thì có lẽ cảm xúc của mình đã không phức tạp thế này.)"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 24 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Yumemi vẫn đang ngồi trên thanh chắn xe như thể chưa có chuyện gì xảy ra."
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan, em có đau không?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 23 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1060.ogg"
    "{size=192}\n{/size}「Không ạ, xin chớ lo lắng. Tôi là một robot, vậy nên tôi không thể cảm thấy đau đớn được.」"
    ###------
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
    "{size=192}\n{/size}Cô bé nở nụ cười thanh nhã, như đang quan tâm tới Satomi."
    ###------
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
    "{size=192}\n{/size}里美(Yumemi hẳn là không hề biết.)"
    ###------
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
    "{size=192}\n{/size}里美(Rằng nỗi đau em ấy đáng ra phải nhận, đều đã được những người liên quan đến em ấy hứng chịu cả rồi.)"
    ###------
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
    "{size=192}\n{/size}里美(Để những người yêu quý robot, và những người chán ghét chúng đều được bình đẳng.)"
    ###------
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
    "{size=192}\n{/size}「Thôi thì, trước hết mình phải về cái đã.」"
    ###------
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
    "{size=192}\n{/size}「À mà, em không sạc điện thì sao mà đi được nhỉ.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 04 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1077.ogg"
    "{size=192}\n{/size}「Vâng, tôi thành thật xin lỗi. Pin dự phòng cũng sắp cạn, nên tôi không thể nào đi lại được nữa.」"
    ###------
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
    "{size=192}\n{/size}「Vậy là coi như liệt toàn thân rồi còn gì. Hết chuyện này tới chuyện khác, gì cũng đến tay mình...」"
    ###------
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
    "{size=192}\n{/size}Việc kiểm tra và thay thế nguồn điện dự phòng là bắt buộc, nhưng chính Satomi đã quyết định để yên như thế do ngân sách không cho phép."
    ###------
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
    "{size=192}\n{/size}Rồi chuyện này xảy ra, và Satomi chẳng thể nào một mình mang cô bé ra trạm sạc được, thật chẳng có cách nào diễn tả tốt hơn bằng \"tự làm tự chịu\"."
    ###------
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
    "{size=192}\n{/size}「...Giờ đâu phải lúc để phàn nàn chứ. Để chị gọi xe, em ngồi chờ chút nhé.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 11 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Cô nói, đoạn rút điện thoại di động ra khỏi túi áo khoác."
    ###------
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
    "{size=192}\n{/size}Không có tiếng đáp lại."
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan?」"
    ###------
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
    "{size=192}\n{/size}Mặc cho cô gọi tên thì Yumemi cũng không cử động nữa."
    ###------
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
    "{size=192}\n{/size}Vẫn với biểu cảm như mọi khi trên khuôn mặt, cô bé đóng băng theo đúng nghĩa đen."
    ###------
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
    "{size=192}\n{/size}Có vẻ như pin đã hoàn toàn cạn rồi."
    ###------
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
    "{size=192}\n{/size}Bình thường cô bé sẽ cảnh báo đếm ngược 100 giây trước khi hết pin, nhưng lần này có vẻ như đến thời gian để làm vậy còn không có."
    ###------
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
    "{size=192}\n{/size}Bất kể có hiểu cho cảm nhận của Satomi hay không, thì cô robot rắc rối kia cứ thế trở lại thành một vật thể vô tri cỡ người thật, mặc kệ sự đời có ra sao."
    ###------
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
    "{size=192}\n{/size}「Trời ạ...」"
    ###------
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
    "{size=192}\n{/size}Satomi đấm nhẹ vào cái đầu đá kia."
    ###------
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
    "{size=192}\n{/size}Quả nhiên là có hơi đau một chút."
    ###------
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
    "{size=192}\n{/size}Satomi cất điện thoại đi."
    ###------
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
    "{size=192}\n{/size}Cô kéo áo khoác lên, rồi ngồi xuống thanh chắn xe bên cạnh Yumemi."
    ###------
    scene black
    with fade
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
    show smw01d zorder 100: 
        offset(97,742)
    hide bg20
    with dissolve
    play music "nwa/bgm12.wav"
    "{size=192}\n{/size}Thời khắc chạng vạng đang đến gần."
    ###------
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
    with dissolve
    "{size=192}\n{/size}Cô cảm nhận cái lạnh mơn trớn bờ má mình."
    ###------
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
    with dissolve
    voice "ovk/z1000/1115.ogg"
    "{size=192}\n{/size}里美(Chắc mấy đứa nó đang chuẩn bị cho buổi chiếu cuối trong ngày nhỉ?)"
    ###------
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
    with dissolve
    "{size=192}\n{/size}Những đồng nghiệp đứng ở quầy lễ tân, căn phòng hình cầu chưa được lấp đầy ghế bao nhiêu năm rồi chẳng rõ."
    ###------
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
    with dissolve
    voice "ovk/z1000/1119.ogg"
    "{size=192}\n{/size}里美(Một nơi làm việc đáng ra phải được xác định là sự nghiệp cả đời...)"
    ###------
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
    with dissolve
    voice "ovk/z1000/1120.ogg"
    "{size=192}\n{/size}里美(Vậy mà chỉ có mình mình và Yumemi là đang ngồi cách xa cái khuôn khổ thường nhật đó.)"
    ###------
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
    hide ev01a
    with dissolve
    "{size=192}\n{/size}Cô khẽ nghiêng tầm nhìn."
    ###------
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
    "{size=192}\n{/size}Bầu trời đô thị nhàn nhạt trầm buồn, khó mà gọi là mang sắc xanh, xuất hiện giữa khe hở những tòa chung cư cũ."
    ###------
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
    "{size=192}\n{/size}Khi cô còn nhỏ, cảm giác như nó trông rực rỡ và có nhiều gam màu sắc nét hơn hẳn."
    ###------
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
    "{size=192}\n{/size}「Có lẽ mình đã quên đi mục tiêu ban đầu mất rồi...」"
    ###------
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
    "{size=192}\n{/size}Satomi lẩm bẩm."
    ###------
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
    "{size=192}\n{/size}里美(Sẽ là nói dối nếu bảo mình không có động cơ âm thầm, mong muốn tự mình tăng doanh thu trong lúc giám đốc đi vắng.)"
    ###------
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
    "{size=192}\n{/size}里美(Tìm cách bóc tách từng vấn đề và cải thiện chúng theo cảm tính, cốt để chốn sinh nhai này và bọn mình không bị bỏ rơi...)"
    ###------
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
    "{size=192}\n{/size}里美(Xem như đây là một dịp tốt để nhìn nhận lại vậy.)"
    ###------
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
    "{size=192}\n{/size}里美(...Là bọn mình... phải không nhỉ?)"
    ###------
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
    "{size=192}\n{/size}里美(Hay nói đúng ra, là chỉ mỗi mình mình?)"
    ###------
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
    "{size=192}\n{/size}「Nè, Yumemi-chan.」"
    ###------
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
    "{size=192}\n{/size}Satomi bắt chuyện với Yumemi trong lúc ngắm nhìn bầu trời tối dần."
    ###------
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
    "{size=192}\n{/size}「Em có mệt mỏi với công việc không?」"
    ###------
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
    "{size=192}\n{/size}Không lời hồi đáp."
    ###------
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
    "{size=192}\n{/size}「Em không thích làm việc cùng bọn chị nữa sao?」"
    ###------
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
    "{size=192}\n{/size}Dù biết thừa rằng mình sẽ không nhận được câu trả lời, Satomi vẫn tiếp lời."
    ###------
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
    "{size=192}\n{/size}「Chị ấy nhé, chị từng tin rằng mình sẽ không bao giờ thay đổi.」"
    ###------
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
    "{size=192}\n{/size}「Chị đã luôn nghĩ, rằng vì mình thích những vì sao, vì mình thích cung thiên văn, nên mới có thể tiếp tục được công việc này.」"
    ###------
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
    "{size=192}\n{/size}Cô nhắm mắt lại và hồi tưởng."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    hide ev01b
    hide sbw00_3
    hide sbw00_4
    hide sbw01
    with dissolve
    voice "ovk/z1000/1168.ogg"
    "{size=192}\n{/size}里美(Hồi lên sáu, ba mẹ đã tặng mình một cuốn sách tranh về Thần thoại Hy Lạp làm quà sinh nhật.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1169.ogg"
    "{size=192}\n{/size}里美(Hồi 11 tuổi, mình từng làm một cung thiên văn bằng giấy trong kỳ nghỉ hè và lần đầu tiên chiếu nó lên trần phòng.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1170.ogg"
    "{size=192}\n{/size}里美(15 tuổi, ba mẹ đưa mình về quê tránh nóng, và đấy cũng là lần đầu tiên mình được thấy bầu trời sao đúng nghĩa.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1171.ogg"
    "{size=192}\n{/size}里美(Năm 18 tuổi, nghe rằng có một cung thiên văn đang xây dựng trên sân thượng cửa hàng bách hóa địa phương và hiện tuyển chọn thuyết trình viên, nên dù hồi hộp quá chừng, mình vẫn gọi điện cho họ.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1172.ogg"
    "{size=192}\n{/size}里美(Những bối rối, dằn vặt, và cả mâu thuẫn khi còn là lính mới.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1173.ogg"
    "{size=192}\n{/size}里美(Nỗi căng thẳng khi lần đầu tiên được giao cho công việc thuyết trình một mình.)"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1174.ogg"
    "{size=192}\n{/size}里美(Và cả cái ngày mà giám đốc lệnh cho mình giám sát cô bé robot đồng hành này nữa...)"
    ###------
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
    with dissolve
    "{size=192}\n{/size}Cô mở mắt, và khẽ ngắm Yumemi."
    ###------
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
    with dissolve
    "{size=192}\n{/size}Tại nơi ngoại ô thành phố này, tại chốn ven đường lộng gió này, dẫu cho bản thân không thể tự mình cử động, thì cô bé ấy... cô bé ấy vẫn là người duy nhất mang vẻ vô tư, dịu dàng, trong sáng và hạnh phúc."
    ###------
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
    with dissolve
    voice "ovk/z1000/1179.ogg"
    "{size=192}\n{/size}「Nhưng Yumemi-chan này, đừng bao giờ thay đổi em nhé.」"
    ###------
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
    with dissolve
    "{size=192}\n{/size}Satomi nhẹ nhàng nói với khuôn mặt trông nghiêng đã cứng đờ lại kia."
    ###------
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
    with dissolve
    voice "ovk/z1000/1183.ogg"
    "{size=192}\n{/size}「Dẫu cho một ngày nào đó chị phải rời đi, thì Yumemi-chan cũng đừng bao giờ thay đổi nhé.」"
    ###------
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
    "{size=192}\n{/size}「Xin thứ lỗi cho tôi, chị định rời công ty sao?」"
    ###------
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
    "{size=192}\n{/size}「Chị không có, nhưng mà...」"
    ###------
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
    "{size=192}\n{/size}Sau câu trả lời, cô chợt nhận ra."
    ###------
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
    "{size=192}\n{/size}Yumemi đang nở nụ cười như chưa hề xảy ra chuyện gì."
    ###------
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
    "{size=192}\n{/size}「Oái, Yumemi-chan?!」"
    ###------
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
    "{size=192}\n{/size}「Tôi sẽ không bao giờ thay đổi, tôi sẽ mãi mãi làm việc ở đây, cùng với Satomi-san và mọi người.」"
    ###------
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
    "{size=192}\n{/size}Đôi mắt nhựa của cô chuyển sang màu như vết dầu loang, thấu kính bên trong được lấy nét, và quan sát Satomi đang bối rối một cách điệu đà."
    ###------
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
    "{size=192}\n{/size}Cứ như vừa bị lừa vậy."
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan... không phải em vừa hết pin à?」"
    ###------
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
    "{size=192}\n{/size}「Vâng. Nói chính xác thì, tôi có thể kéo dài khả năng hoạt động thêm 800 giây nữa trong chế độ tiết kiệm pin.」"
    ###------
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
    "{size=192}\n{/size}「Thế có nghĩa là em đã nói dối chị?　Em có thể làm được việc đó ư?」"
    ###------
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
    "{size=192}\n{/size}「Thưa không. Tôi là một robot, nên tôi không thể nói dối.」"
    ###------
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
    "{size=192}\n{/size}Cô trả lời, quả quyết và kiên định."
    ###------
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
    "{size=192}\n{/size}「Hôm qua mọi người đã nói với tôi rằng, \"Thỉnh thoảng em nên lắng nghe Satomi-san than thở một chút nhé.\"」"
    ###------
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
    "{size=192}\n{/size}「Than thở?」"
    ###------
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
    "{size=192}\n{/size}「Vâng, mọi người bảo, \"Có những chuyện mà con người sẽ chỉ nói với robot, vì vậy nếu em ở một mình cùng Satomi-san, hãy giữ yên lặng và lắng nghe chị ấy than thở.\"」"
    ###------
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
    "{size=192}\n{/size}「Mọi người... nói vậy sao?」"
    ###------
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
    "{size=192}\n{/size}「Vâng, tôi xác định đây là một chỉ thị có liên quan mật thiết đến sức khỏe của Satomi-san, nên tôi đã đăng ký chuyện này là nhiệm vụ ưu tiên.」"
    ###------
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
    "{size=192}\n{/size}Trước lời giải thích lưu loát của Yumemi, Satomi không khỏi ngạc nhiên song cũng thấy xấu hổ."
    ###------
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
    "{size=192}\n{/size}Nếu biết cách sử dụng các mệnh lệnh ưu tiên, ta có thể điều khiển hành vi của Yumemi ― vốn không hề linh hoạt ― đến một mức độ nào đó."
    ###------
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
    "{size=192}\n{/size}Đó là điều Satomi đã dạy các hậu bối của mình."
    ###------
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
    "{size=192}\n{/size}Nhưng cô chưa bao giờ nghĩ bọn họ sẽ áp dụng theo cách này."
    ###------
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
    "{size=192}\n{/size}Cô tưởng tượng ra những nét mặt tinh quái của đồng nghiệp tại nơi làm việc."
    ###------
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
    "{size=192}\n{/size}里美(Họ đều quan tâm tới mình trong khi mình thì chẳng làm được gì...)"
    ###------
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
    "{size=192}\n{/size}Nghĩ đến đây, bất giác cô nhớ ra."
    ###------
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
    "{size=192}\n{/size}「Lẽ nào, việc em tự ý chạy ra ngoài thế này là để làm như vậy hả?」"
    ###------
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
    "{size=192}\n{/size}「Vâng?」"
    ###------
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
    "{size=192}\n{/size}Vẫn là cái cử chỉ khẽ nghiêng đầu như mọi khi."
    ###------
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
    "{size=192}\n{/size}Rồi, cơ hồ vừa nghĩ ra gì đó..."
    ###------
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
    "{size=192}\n{/size}「Tôi thành thật xin lỗi!」"
    ###------
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
    "{size=192}\n{/size}「Giờ nghĩ lại, hành động của tôi đã vi phạm nghiêm trọng nguyên tắc công việc! Tôi thật sự... thật sự xin lỗi ạ!」"
    ###------
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
    "{size=192}\n{/size}Cô bé khẩn khoản cúi đầu."
    ###------
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
    "{size=192}\n{/size}Do chế độ tiết kiệm pin mà hành động của cô bé thiếu đi sự sắc sảo, nhưng cái cách cô đột ngột thay đổi thái độ vẫn luôn ngoạn mục như vậy."
    ###------
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
    "{size=192}\n{/size}Không còn sốc và giận nữa, Satomi bật cười."
    ###------
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
    "{size=192}\n{/size}里美(Thôi kệ vậy.)"
    ###------
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
    "{size=192}\n{/size}里美(Làm gì có con người nào không có khuyết điểm kia chứ.)"
    ###------
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
    "{size=192}\n{/size}「Chuyện này em nhớ giữ bí mật với mọi người nhé.」"
    ###------
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
    "{size=192}\n{/size}Satomi ghé miệng vào tai ― dù rằng đương nhiên cô biết đó không phải tai mà là thiết bị thu sóng ― của người bạn thâm niên là robot và thì thầm."
    ###------
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
    "{size=192}\n{/size}「Nếu chị là con trai... nhất định chị sẽ cầu hôn Yumemi-chan đấy.」"
    ###------
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
    "{size=192}\n{/size}Cô duỗi tay phải ra, dịu dàng vuốt tóc Yumemi."
    ###------
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
    "{size=192}\n{/size}Chắc chỉ là nhầm tưởng thôi."
    ###------
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
    "{size=192}\n{/size}Nhưng có cảm giác như cô bé ấy sẽ hạnh phúc khi cô làm vậy."
    ###------
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
    "{size=192}\n{/size}「Nhưng mà nhé, dù mình có kết hôn thì chị cũng sẽ không để Yumemi-chan phải nghỉ việc đâu.」"
    ###------
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
    "{size=192}\n{/size}「Đôi ta sẽ mãi làm việc trong cung thiên văn, cùng với nhau.」"
    ###------
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
    "{size=192}\n{/size}Nói đoạn, cô chợt cảm thấy ngượng ngùng."
    ###------
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
    "{size=192}\n{/size}Satomi thấu cảm điều ấy từ sâu thẳm con tim."
    ###------
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
    "{size=192}\n{/size}里美(Được mà như thế thì tuyệt thật.)"
    ###------
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
    "{size=192}\n{/size}Yumemi nhìn chằm chằm vào Satomi bằng vẻ mặt của một thiếu nữ ngây thơ."
    ###------
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
    "{size=192}\n{/size}Sau đó, cô bé trả lời."
    ###------
    scene bg02
    with fade
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide ev01e
    with dissolve
    voice "ovk/z1000/1280.ogg"
    "{size=192}\n{/size}「Thành thật xin lỗi, tôi đã có hôn ước rồi ạ.」"
    ###------
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
    "{size=192}\n{/size}「Yumemi-chan...? Em vừa nói gì vậy?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1284.ogg"
    "{size=192}\n{/size}「Vâng, tôi vừa nói, \"Thành thật xin lỗi, tôi đã có hôn ước rồi ạ.\"」"
    ###------
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
    "{size=192}\n{/size}Cô bé nhắc lại với khuôn mặt không thể nghiêm túc hơn."
    ###------
    scene bg01
    with fade
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,24)
        zoom 1
    show smw01d zorder 100: 
        offset(97,742)
    hide bg20
    hide kr_f
    hide kr_b
    with dissolve
    play music "nwa/bgm01.wav"
    voice "ovk/z1000/1293.ogg"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###------
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
    "{size=192}\n{/size}Cung thiên văn trên tầng thượng của trụ sở chính trung tâm bách hóa Hanabishi, trước máy bán vé tại quầy lễ tân."
    ###------
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
    "{size=192}\n{/size}Yumemi vẫn đang mời gọi khách như thường lệ."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1298.ogg"
    "{size=192}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận. Vô vàn những vì sao trong vũ trụ này đang chờ quý vị khám phá.」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 21 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 26 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Sau khi lặp lại câu nói nhiều lần, hành vi của Yumemi dần trở nên lóng ngóng."
    ###------
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
    "{size=192}\n{/size}Cô bé di chuyển phần trên cổ và quan sát xung quanh để đảm bảo rằng không có đồng nghiệp nào đang nhìn mình."
    ###------
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
    "{size=192}\n{/size}Đoạn, cô bé khẽ khàng rời khỏi chỗ chiếc máy bán vé."
    ###------
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
    "{size=192}\n{/size}Đó là tật xấu mới đây của cô: rời bỏ nơi làm việc."
    ###------
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
    "{size=192}\n{/size}Đúng lúc đó, khách hàng mới đẩy cửa kính và bước vào."
    ###------
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
    "{size=192}\n{/size}Trông hai người như một cặp đôi cấp ba, hoặc đại học."
    ###------
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
    "{size=192}\n{/size}Chàng trai có thân hình mảnh khảnh cùng mái tóc thẳng, và dù diện mạo của cậu không hẳn là lý tưởng, nhưng cậu lại có một cô bạn gái vừa trông đã toát lên vẻ mạnh mẽ."
    ###------
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
    "{size=192}\n{/size}Cách ăn mặc của hai người có thể gọi là hợp thời trang."
    ###------
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
    "{size=192}\n{/size}Cậu bạn trai vận chiếc áo khoác da quân đội theo lối cổ điển, còn bạn gái mặc váy ngắn cùng kiểu tóc sử dụng keo xịt màu trông như những người nổi tiếng sành điệu trên TV và đeo vòng bạc trên cổ tay."
    ###------
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
    "{size=192}\n{/size}Không ai trong hai người trông mong buổi chiếu, mặc dù họ đến cung thiên văn cùng nhau."
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1311.ogg"
    "{size=192}\n{/size}「Tôi đã luôn chờ bạn.」"
    ###------
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
    "{size=192}\n{/size}Yumemi cất lời vô cùng tự nhiên, và mỉm cười với cậu bạn trai."
    ###------
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
    "{size=192}\n{/size}Cậu ta hình như định nói gì đó, nhưng lại chẳng thốt nên lời."
    ###------
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
    "{size=192}\n{/size}Trông cậu ta cứ như vừa tìm thấy con ma hư cấu mà bản thân từng tán phét với đám bạn từ cái thời hỉ mũi chưa sạch vậy."
    ###------
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
    "{size=192}\n{/size}「...À, ừm... chị vẫn nhớ tôi sao?」"
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 02 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1319.ogg"
    "{size=192}\n{/size}「Vâng, tất nhiên rồi.」"
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1321.ogg"
    "{size=192}\n{/size}「Đã lâu không thấy bạn tới đây, nên tôi cứ lo rằng phải chăng bạn đã gặp vấn đề sức khỏe nào đó.」"
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    "{size=192}\n{/size}Cô bé khẽ nghiêng đầu, và nhìn thẳng vào cậu ta."
    ###------
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
    "{size=192}\n{/size}Cô gái đi cùng cậu ta trưng ra một biểu cảm còn thiếu sức sống hơn cả cô robot đứng trước mặt hai người."
    ###------
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
    "{size=192}\n{/size}Cuối cùng, cơ hồ vừa quyết định điều gì đó, cậu ta lên tiếng."
    ###------
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
    "{size=192}\n{/size}「Tôi ấy, từng... ờ, cầu hôn Yumemi-chan, chuyện đấy... quả nhiên là chị nhớ hả?」"
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1329.ogg"
    "{size=192}\n{/size}「Vâng, tôi nhớ. Vì tôi là một robot nên ghi nhớ là thế mạnh của tôi.」"
    ###------
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
    "{size=192}\n{/size}Yumemi mỉm cười, không vương chút tà tâm."
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1333.ogg"
    "{size=192}\n{/size}「Giờ... tôi muốn rút lại lời cầu hôn ấy.」"
    ###------
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
    "{size=192}\n{/size}Xem chừng đã chấp nhận sự lố bịch trong lời lẽ của mình, cậu ta ấp úng nói tiếp."
    ###------
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
    "{size=192}\n{/size}「Vì... giờ... tôi thích nhỏ này.」"
    ###------
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
    "{size=192}\n{/size}Cậu ta hất cằm về phía cô bạn gái."
    ###------
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
    "{size=192}\n{/size}Cô ta không giấu được vẻ khó chịu khi vòng tay ôm lấy tay bạn trai."
    ###------
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
    "{size=192}\n{/size}Cô liếc cậu ta bằng ánh nhìn thoáng vẻ khinh khi, và chu đôi môi đỏ lòm của mình lên."
    ###------
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
    "{size=192}\n{/size}Yumemi một lần nữa mỉm cười."
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 01 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1344.ogg"
    "{size=192}\n{/size}「Tôi hiểu rồi. Tôi đã ghi nhận rằng hôn ước giữa chúng ta đã bị hủy bỏ.」"
    ###------
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
    "{size=192}\n{/size}Cô bé nói bằng giọng của một nhân viên quản lý việc đặt hàng từ xa vừa chấp nhận hủy đơn hàng."
    ###------
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
        offset(0,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(0,24)
        zoom 1
    show yu_f 12 zorder 4: 
        offset(0,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1348.ogg"
    "{size=192}\n{/size}「Chúc hai bạn mãi hạnh phúc bên nhau.」"
    ###------
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
    "{size=192}\n{/size}Cô bé cúi nhẹ đầu và tươi tỉnh nói, dù chẳng biết cô có hiểu tình hình hay không."
    ###------
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
    "{size=192}\n{/size}Sau khi đã nhận lời chúc từ tận đáy lòng ấy, cặp đôi trẻ nhanh chóng rời khỏi cung thiên văn."
    ###------
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
    "{size=192}\n{/size}「Đã mất công gửi vé miễn phí cho rồi thì ở lại xem cả buổi chiếu đi chứ... tôi mà nghĩ thế thì có bị coi là keo kiệt không nhỉ?」"
    ###------
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
    "{size=192}\n{/size}Gorou, người đang ngồi trên ghế lễ tân vừa quan sát sự việc diễn ra, nói."
    ###------
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
    "{size=192}\n{/size}「Thì chắc tại thằng bé hết hứng thú với cung thiên văn rồi chứ gì.」"
    ###------
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
    "{size=192}\n{/size}Satomi ngồi ghế bên cạnh đáp lại."
    ###------
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
    "{size=192}\n{/size}「Nói sao thì nói chứ, nhóc Susumu ấy...」"
    ###------
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
    "{size=192}\n{/size}「Thật tình. Nói sao giờ nhỉ... tôi vẫn tưởng thằng nhóc là người chất phác lắm kia.」"
    ###------
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
    "{size=192}\n{/size}「Ngày nay thì đấy đã là chất phác rồi. Mỗi thời mỗi khác mà chị.」"
    ###------
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
    "{size=192}\n{/size}「Gorou-kun nói chuyện cứ như ông già ấy.」"
    ###------
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
    "{size=192}\n{/size}Nhóc Susumu, hay chính xác hơn là Akino Susumu, từng là khách quen của cung thiên văn vào đúng 10 năm trước."
    ###------
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
    "{size=192}\n{/size}Đương nhiên là cậu bé thích thiên văn rồi, nhưng trên hết, cậu ta cũng thích việc chăm sóc Yumemi ― khi ấy vừa mới nhận việc ― đến mức thái quá, gây ra rất nhiều rắc rối cho dàn nhân sự lúc bấy giờ."
    ###------
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
    "{size=192}\n{/size}Đến một ngày nọ, cậu bé đột ngột ngừng ghé qua."
    ###------
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
    "{size=192}\n{/size}Mọi người đều quên béng đi mất, bởi học sinh tiểu học vốn là như thế."
    ###------
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
    "{size=192}\n{/size}Tuy vậy, Satomi vẫn nhớ cảm giác nhẹ nhõm khi ấy, song hành cùng chút buồn bã nữa."
    ###------
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
    "{size=192}\n{/size}「...Thật tình, thằng bé cứ thế chuyển đi, chẳng nói với chúng ta một lời, rồi còn tinh tướng đi kiếm bạn gái nữa.」"
    ###------
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
    "{size=192}\n{/size}「Bạn gái hay gì là cách cậu ta khẳng định giá trị bản thân, nên tôi xin phép miễn bình luận...」"
    ###------
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
    "{size=192}\n{/size}Gorou nói trong lúc thao tác với chiếc bàn phím hàng cổ một cách thuần thục."
    ###------
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
    "{size=192}\n{/size}「Nhưng thứ tôi không hiểu là cái mệnh lệnh ưu tiên bị bỏ lại suốt tận 10 năm này này.」"
    ###------
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
    "{size=192}\n{/size}Gorou làu bàu khi nhìn vào cửa sổ trạng thái ở giữa màn hình, thứ được dành riêng cho việc bảo trì Yumemi trong vài ngày qua."
    ###------
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
    "{size=192}\n{/size}と表題がついたウィンドウがアクティブになっている。"
    ###------
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
    "{size=192}\n{/size}Một dòng số 0 ― thứ đáng ra không thể tồn tại ― chứa đầy các mã thập lục phân."
    ###------
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
    "{size=192}\n{/size}Nói đơn giản, thì đây giống như một dòng thần chú ma thuật ẩn nấp trong trí nhớ Yumemi suốt 10 năm trời và gây ra hiện tượng \"rời bỏ nơi làm việc\" của cô bé."
    ###------
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
    "{size=192}\n{/size}「Mà, khi ấy chúng ta hãy còn đang điều chỉnh con bé, cả hệ thống học tập nữa ha.」"
    ###------
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
    "{size=192}\n{/size}「Có hàng tá lỗi nghiêm trọng đã được sửa lại rồi. Cả cái này, nguyên nhân chính cũng là do việc xử lý ngoại lệ thôi, cơ mà...」"
    ###------
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
    "{size=192}\n{/size}Anh ta tiếp tục nhấp vào màn hình bằng chiếc bút mực có kèm chức năng của một cây bút cảm ứng."
    ###------
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
    "{size=192}\n{/size}「Vì được bảo là phải giữ bí mật mà con bé có thể thực hiện một hành vi phức tạp như hook chính quá trình gỡ lỗi hàng ngày và làm cho danh sách mệnh lệnh bị ẩn đi, chuyện này chính tôi cũng chẳng tin nổi.」"
    ###------
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
    "{size=192}\n{/size}「Hay ngược lại, tôi còn thấy phục con bé.」"
    ###------
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
    "{size=192}\n{/size}「Nhưng dù không biết về mệnh lệnh đó, thì nếu xem video từ lúc đầu, cậu vẫn sẽ tìm được khởi điểm chứ?」"
    ###------
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
    "{size=192}\n{/size}「Ý chị là kiểm tra toàn diện xuyên 10 năm ấy hả? Xét về mặt vật chất thì chuyện đó là bất khả thi đấy.」"
    ###------
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
    "{size=192}\n{/size}「Cũng phải...」"
    ###------
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
    "{size=192}\n{/size}Cũng có thể Satomi đã từng thấy rồi, nhưng sau đó cô lại quên đi mất."
    ###------
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
    "{size=192}\n{/size}Phát không ngừng ở góc phải màn hình máy tính là một video đa chiều do Yumemi quay lại được nén xuống còn hai chiều."
    ###------
    scene black
    with fade
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
    with dissolve
    play music "nwa/bgm13.wav"
    "{size=192}\n{/size}Ngày quay là 10 năm và 8 ngày trước."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Tại quầy lễ tân của cung thiên văn, trước máy bán vé tự động, một cậu bé đang nhìn chằm chằm vào Yumemi từ chính diện."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Khuôn mặt cậu lộ rõ vẻ tinh nghịch, mái tóc ngắn lòa xòa và đôi mắt như sắp khóc tới nơi."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1413.ogg"
    "{size=192}\n{/size}晋（９歳）『Yumemi-chan, chị em mình cưới nhau đi!』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Một lời cầu hôn hết lòng hết dạ và tha thiết đến từ phía cậu bé."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1417.ogg"
    "{size=192}\n{/size}晋（９歳）『Mai em phải chuyển nhà rồi... Vì thế chúng ta sẽ không thể gặp nhau được nữa.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1419.ogg"
    "{size=192}\n{/size}ゆめみ『Nhưng tôi là một robot, nên tôi không thể cưới bạn được.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1421.ogg"
    "{size=192}\n{/size}晋（９歳）『Làm gì có chuyện đấy! Yêu nhau là cưới nhau được mà!』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1423.ogg"
    "{size=192}\n{/size}晋（９歳）『Mẹ em dạy như vậy đó. Chỉ cần yêu là có thể thành thân được rồi.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1425.ogg"
    "{size=192}\n{/size}ゆめみ『Thật sự xin lỗi, nhưng tôi không tìm thấy bất cứ dữ liệu nào trong cơ sở dữ liệu để khẳng định những điều bạn vừa nói.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Cậu bé tỏ ra thất vọng vì cuộc trò chuyện không đúng hướng như dự kiến."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1429.ogg"
    "{size=192}\n{/size}晋（９歳）『Nếu không cưới được Yumemi-chan... chắc em chết mất...』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Màn hình hơi chếch đi một chút."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Có lẽ Yumemi đang nghiêng đầu nghĩ ngợi gì đó."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1434.ogg"
    "{size=192}\n{/size}ゆめみ『Thật thất lễ quá, nhưng tôi có thể biết quý khách Susumu năm nay bao nhiêu tuổi được không?』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1436.ogg"
    "{size=192}\n{/size}晋（９歳）『Em chín tuổi.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1438.ogg"
    "{size=192}\n{/size}ゆめみ『Nếu là như vậy thì thật đáng tiếc, nhưng ở độ tuổi này bạn chưa được phép kết hôn.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Một thoáng lặng im."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1442.ogg"
    "{size=192}\n{/size}晋（９歳）『Yumemi-chan, đợi em 10 năm nữa nhé! 10 năm nữa em sẽ đến đón chị!』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1444.ogg"
    "{size=192}\n{/size}晋（９歳）『Em sẽ cố gắng giữ mình cho đến lúc đó, nên khi ấy mình kết hôn đi!』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1446.ogg"
    "{size=192}\n{/size}ゆめみ『Đây... là thứ gọi là hôn ước phải không ạ?』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1448.ogg"
    "{size=192}\n{/size}晋（９歳）『Đúng, là hôn ước đó!』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1450.ogg"
    "{size=192}\n{/size}ゆめみ『Nhưng... tôi còn phải làm việc.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1452.ogg"
    "{size=192}\n{/size}晋（９歳）『Khi không ai thấy thì chị cứ ra ngoài cũng có sao đâu, giả vờ như đang làm việc là được.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1454.ogg"
    "{size=192}\n{/size}晋（９歳）『Khi ấy em sẽ đến đón chị. Nhất định, nhất định em sẽ đến...』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    "{size=192}\n{/size}Sau khi lưỡng lự đôi chút, Yumemi lên tiếng trả lời dứt khoát."
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1458.ogg"
    "{size=192}\n{/size}ゆめみ『Xin nhận lệnh, đã đăng ký mệnh lệnh này ở mức ưu tiên cao hơn.』"
    ###------
    show kuros : 
        offset(0,0)
        anchor(0,0)
    show bg32 : 
        offset(128,22)
        anchor(0,0)
    with dissolve
    voice "ovk/z1000/1460.ogg"
    "{size=192}\n{/size}晋（９歳）『Ừm! Chị nhớ giữ bí mật nhé. Lời hứa bí mật của đôi ta...』"
    ###------
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
    play music "nwa/bgm08.wav"
    "{size=192}\n{/size}Video ghi lại dừng ở đó và quay lại cảnh đầu tiên."
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    "{size=192}\n{/size}Một lời hứa ngây ngô và trong sáng giữa cô gái ấy và một cậu chàng bé nhỏ."
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    "{size=192}\n{/size}Lời hứa nhảy múa vòng quanh không ngừng tựa như bông tuyết chứa trong quả cầu tuyết."
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    "{size=192}\n{/size}Dù cho cậu bé ấy đã quên đi mọi chuyện."
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    "{size=192}\n{/size}Satomi không ngừng suy nghĩ."
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    voice "ovk/z1000/1473.ogg"
    "{size=192}\n{/size}里美(Con người luôn quên đi, và Yumemi không thể quên...)"
    ###------
    show bg35a : 
        offset(128,22)
        anchor(0,0)
    show ef11 : 
        offset(0,0)
        anchor(0,0)
        ysize 726
        xsize 1152
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
    voice "ovk/z1000/1475.ogg"
    "{size=192}\n{/size}里美(Liệu bên nào mới hạnh phúc đây?)"
    ###------
    scene bg01
    with fade
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
    hide ef11
    with dissolve
    play sound "nwa/se011.wav"
    voice "ovk/z1000/1477.ogg"
    "{size=192}\n{/size}「Phù...」"
    ###------
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
    "{size=192}\n{/size}Satomi vươn vai trên ghế như thể đang dối lừa những cảm xúc đương trào dâng."
    ###------
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
    "{size=192}\n{/size}「Để tôi đoán chị đang nghĩ gì nhé?」"
    ###------
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
    "{size=192}\n{/size}Gorou lên tiếng."
    ###------
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
    "{size=192}\n{/size}「Gì hở?」"
    ###------
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
    "{size=192}\n{/size}「Làm sao để tính phí vé đi-về của hai đứa kia đúng không?」"
    ###------
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
    "{size=192}\n{/size}Anh ta chỉ ra cùng một vẻ tự tin."
    ###------
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
    "{size=192}\n{/size}「Chán cậu lắm Gorou-kun ạ.」"
    ###------
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
    "{size=192}\n{/size}Xen lẫn với một tiếng thở dài, Satomi đáp."
    ###------
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
    "{size=192}\n{/size}Giờ đây nguyên nhân đã được xác định, tất cả những gì họ cần làm chỉ đơn giản là viết lại danh sách mệnh lệnh mà thôi, nhưng không một ai ― bao gồm cả Gorou là người đề xuất ý tưởng này ― đồng ý làm thế."
    ###------
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
    "{size=192}\n{/size}Để đề phòng trường hợp khai man danh tính, những robot đồng hành như Yumemi sử dụng rất nhiều lớp quét sinh trắc học nhằm định dạng một cá thể, vậy nên việc nhờ chính chủ từng xác nhận mệnh lệnh ưu tiên tới để \"hủy bỏ hôn ước\" là điều tối cần thiết."
    ###------
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
    "{size=192}\n{/size}Kết quả sinh ra từ những dữ kiện này là một màn kịch nhỏ với đương sự làm vai chính."
    ###------
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
    "{size=192}\n{/size}Tất nhiên ta không thể bỏ qua những công sức và phí tổn của bọn họ trong việc tìm kiếm địa chỉ hiện tại của cậu bé Susumu ngày nào từ danh sách khách hàng thời đó, đi giải thích tình hình rồi lại yêu cầu cậu ta tới gặp Yumemi ngay lập tức."
    ###------
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
    "{size=192}\n{/size}里美(Thật tình, cái chỗ làm việc gì mà rặt một đám nhân viên vô dụng đi thấu cảm cho một robot.)"
    ###------
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
    "{size=192}\n{/size}Cô không biết nhóc Susumu và cô bạn gái sẽ đi đâu."
    ###------
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
    "{size=192}\n{/size}里美(Liệu hai đứa nó sẽ đi thăm thú thành phố nơi bạn trai từng sống, hay sẽ đi vào quán cà phê, trung tâm trò chơi hay thậm chí là rạp chiếu phim 3D...)"
    ###------
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
    "{size=192}\n{/size}Quả nhiên là cô vẫn thấy bực khi cung thiên văn không nằm trong kế hoạch hò hẹn ấy."
    ###------
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
    "{size=192}\n{/size}「Thôi thì, xin được chúc cho những cặp yêu nhau một tương lai xán lạn.」"
    ###------
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
    "{size=192}\n{/size}「...Nghe câu đậm mùi cà khịa.」"
    ###------
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
    "{size=192}\n{/size}「Cậu thấy thế thì thế.」"
    ###------
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
    "{size=192}\n{/size}「Đã cho Yumemi dễ thương nhà mình ăn bơ vậy rồi mà còn không đến gặp con bé thì tôi sẽ cho thằng nhóc đó một bài học. Như 10 năm trước vậy.」"
    ###------
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
    "{size=192}\n{/size}「Thế giờ ta làm gì đây? Nguyên nhân thì xác định được rồi, và tôi có thể tự tin đảm bảo là bây giờ lỗi sẽ không xuất hiện nữa đâu...」"
    ###------
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
    "{size=192}\n{/size}「Nhưng nếu lỗi ở cấp độ này vẫn còn lưu lại thì khi giám đốc trở về, có lẽ tôi sẽ phải đề xuất một lần cập nhật lại hệ thống cho con bé.」"
    ###------
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
    "{size=192}\n{/size}「Nhưng làm vậy thì tính cách em nó cũng sẽ thay đổi theo chứ gì? Kệ đi, cứ để thế này cũng được mà.」"
    ###------
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
    "{size=192}\n{/size}里美(Ai mà chẳng phải có một hai bí mật muốn giấu người khác chứ.)"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 25 zorder 4: 
        offset(-830,24)
        zoom 1
    hide kr_f
    hide kr_b
    with dissolve
    voice "ovk/z1000/1531.ogg"
    "{size=192}\n{/size}「Quý vị nghĩ thế nào về cung thiên văn?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 20 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 21 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1533.ogg"
    "{size=192}\n{/size}「Bất kể lúc nào, quý vị cũng được ngắm nhìn những điều tuyệt vời, những tia sáng lấp lánh tưởng như vô tận...」"
    ###------
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
    "{size=192}\n{/size}Yumemi quay trở lại vị trí thường ngày, liên tục mời chào khách không biết mệt mỏi."
    ###------
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
    "{size=192}\n{/size}Làn gió đầu đông luồn qua khe cửa kính làm cho mái tóc chẻ hai đuôi lỗi mốt của cô bé khẽ dao động."
    ###------
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
    "{size=192}\n{/size}Sắc diện của cô trông như yêu kiều nữ tính hơn, tràn đầy sức sống hơn bình thường."
    ###------
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
    "{size=192}\n{/size}「Nè, Yumemi-chan, sao em không thử thay đổi kiểu tóc nhỉ?」"
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 01 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 08 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1542.ogg"
    "{size=192}\n{/size}「...?」"
    ###------
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
    "{size=192}\n{/size}Bất ngờ được gọi, cô bé nhìn Satomi với một vẻ ngây ngô."
    ###------
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
        offset(-830,24)
        zoom 1
    show yu_a 00 zorder 4: 
        offset(-830,24)
        zoom 1
    show yu_f 00 zorder 4: 
        offset(-830,24)
        zoom 1
    with dissolve
    voice "ovk/z1000/1546.ogg"
    "{size=192}\n{/size}「Mái tóc của tôi đóng vai trò như bộ tản nhiệt từ bộ phận tính toán trên đầu, nên không được phép uốn hoặc buộc lại.」"
    ###------
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
    "{size=192}\n{/size}「Ra thế, chị hiểu rồi...」"
    ###------
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
    "{size=192}\n{/size}Satomi liếc mắt lên đồng hồ treo tường trong lúc nghe cô bé trả lời."
    ###------
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
    "{size=192}\n{/size}Ở trong phòng trình chiếu, nhạc nền đã chuyển, đã sắp đến lúc buổi chiếu lúc bình minh bắt đầu."
    ###------
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
    "{size=192}\n{/size}Chuẩn bị có thêm một lượt khách tới xem."
    ###------
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
    "{size=192}\n{/size}Cô cần phải trở về vị trí của mình."
    ###------
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
    "{size=192}\n{/size}Satomi thì thầm vào tai Gorou trong khi anh đứng dậy khỏi chiếc ghế xếp."
    ###------
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
    "{size=192}\n{/size}「Nè, cậu nghĩ đeo thêm phụ kiện tóc cho Yumemi có ổn không?」"
    ###------
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
    "{size=192}\n{/size}「Nếu ta chuẩn bị một thứ dành cho máy móc dòng cao cấp thì tôi nghĩ sẽ chẳng sao đâu. Tất nhiên, ngân sách đâu ra thì lại là một chuyện khác nhé.」"
    ###------
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
    "{size=192}\n{/size}「Chỉ còn cách làm việc quần quật để kiếm chác thôi ha.」"
    ###------
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
    "{size=192}\n{/size}Satomi nói và mỉm cười."
    ###------
    return
