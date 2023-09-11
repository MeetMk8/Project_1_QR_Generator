from guizero import *
import pyqrcode
import png
from pyqrcode import QRCode

app = App(title="QR Code Generator",width=1366,height=768)
app.bg="#ffffe6"


def another_window():
    app.hide()
    second_window.show()
    
    

def generate_qr():
    qr_link = url_link.value
    code_image = pyqrcode.create(qr_link)
    img_name = image_name.value
    name = img_name[0:len(img_name)-3]
    code_image.png(f"{name}.png",scale=15)
    qr_show = Picture(second_window,image=f"{name}.png")
    
#title of the main screen
message_box = Box(app, width="fill",height=200)
title_message = Text(message_box,text="Welcome to QR Code Generator",align="bottom")
title_message.text_size = 42
title_message.font = "Lucida Console"
title_message.text_color = "#902cc9"


#Second message box
message_box = Box(app, width="fill",height=200)

#textbox for getting url
url_link = TextBox(message_box,align="bottom",height=3,width=70,multiline=True)
url_link.bg="#ffffff"


text_message= Text(message_box,text="Enter URL here",align="bottom")
text_message.font = "Cooper Black"
text_message.text_color = "#4ecfc8"
text_message.text_size = 32

#submit button
message_box = Box(app,width="fill",height=100)
submit_button = PushButton(message_box,width=20,align="bottom",text="Generate QR",command=another_window)
submit_button.bg = "#e6e6e6"
submit_button.text_size=16



#second Screen
second_window = Window(app,title="QR Code Generator",width=1367,height=768)
msg_box = Box(second_window,width="fill",height=100)
msg = Text(msg_box,text="Enter Image Name")
msg.text_size=30
image_name = TextBox(msg_box,width=70,height=40,multiline=True)
submit_box = Box(second_window,width="fill",height=80)
submit_name = PushButton(submit_box,text="Generate",command=generate_qr,align="bottom")
second_window.hide()


app.display()
