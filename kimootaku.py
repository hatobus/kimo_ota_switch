# -*- coding:utf-8 -*- 

##################################################
#                                                #
#           キモオタを煽るボタンです             #
#           python3系統を使用する際は            #
#    TkinterのTは小文字にしないとエラーが出ます  #
#                                                #
##################################################

import matplotlib.pyplot as plt
from matplotlib.image import imread
import Tkinter 
  
img = imread('kimootaku.png') 
#カレントディレクトリに煽り画像(.png形式でないとエラーが出ます)を入れておき、ここで使用

def on_clicked(): 
     plt.imshow(img)
     plt.show()
#この二行で全てが解決する
               
window = Tkinter.Tk()  #ウィンドウ上にボタンを作る 

label = Tkinter.Label(window, text = "お前ほんまきついって時に押してください") 

#ここの文字を変えればウィンドウに出てくる文字が変わります

label.pack()  

button = Tkinter.Button(window, text = "お前ほんまきつい。", 
                        command = on_clicked ) 
#ボタンに表示させる言葉です

button.pack() 
                
window.mainloop()
