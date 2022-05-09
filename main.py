# -*- coding:utf-8 -*- 

import random 
from tkinter import *

from utils.tools import random_bg

w = 1024
h = 768

# init. 
# ----------
window = Tk()
window.geometry(f'{w}x{h}')
window.title('오늘의 명언')
window.resizable(False, False) # fix window size 

canvas = Canvas(window, width=w, height=h, bg="pink")
canvas.pack()


# load background image 
# ----------------------
img_path = random_bg(dir_path="./images", ext="png")
print(img_path)
img = PhotoImage(file=img_path)

canvas.create_image(w//2, h//2, image=img)



# load text 
# ---------------- 
eng = canvas.create_text(w//2, h//2 - 50, text="hi", fill="white",
                    font=('Arial', 30, 'bold italic'),
                    )

kor = canvas.create_text(w//2, h//2 - 50, text="hi", fill="white",
                    font=('Arial', 30, 'bold italic'),
                    )

# button 
# ------------
button = Button(window, text="deck", font=('Arial', 20, 'bold italic'))
button.place(x=w//2 - 50 , y=int(h*0.8))



window.mainloop()
