import tkinter as tk


win = tk.Tk()#建立主視窗
win.title("ghost legs")

#大小
win.geometry("400x400")#寬*高
win.minsize(width=400,height=400)
win.maxsize(width=800,height=800)

#icon
win.iconbitmap()#檔名or路徑 副檔名.ico 圖片要放在同一個資料夾裡

#background
win.config(background="blue")

#透明度
win.attributes("-alpha",0.5)#1~0 1=100% 0=0%

#置頂
win.attributes("-topmost",1) #1=true 0=false

win.mainloop() #常駐主視窗
