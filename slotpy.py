#引入套件
import tkinter as tk

#建立主視窗和框架
window = tk.Tk()
top_frame = tk.Frame(window)
window.title("SLOT RTP計算機")
window.geometry('500x700')

def dataimport():
    result1_str.set("{}".format(ICON1_entry0.get()))
    result2_str.set("{}".format(ICON2_entry0.get()))
    result3_str.set("{}".format(ICON3_entry0.get()))
    result4_str.set("{}".format(ICON4_entry0.get()))
    result5_str.set("{}".format(ICON5_entry0.get()))
    result6_str.set("{}".format(ICON6_entry0.get()))
    result7_str.set("{}".format(ICON7_entry0.get()))
    



# class Button:
#     def __init__(self):
#         self.

#視窗內訊息
tk.Label(window, text = "圖案名稱").place(x=70,y=30)
tk.Label(window, text = "轉輪1").place(x=150,y=30)
tk.Label(window, text = "轉輪2").place(x=200,y=30)
tk.Label(window, text = "轉輪3").place(x=250,y=30)
tk.Label(window, text = "轉輪4").place(x=300,y=30)
tk.Label(window, text = "轉輪5").place(x=350,y=30)

#輸入欄位
#ICON1欄位
tk.Label(window,text = "ICON1").place(x=10, y=50)
ICON1_entry0 = tk.StringVar()
ICON1_entry0 = tk.Entry(window,width = 10,textvariable=ICON1_entry0)
ICON1_entry0.place(x=60,y=50)
ICON1_entry1 = tk.Entry(window,width = 5)
ICON1_entry1.place(x=150,y=50)
ICON1_entry2 = tk.Entry(window,width = 5)
ICON1_entry2.place(x=200,y=50)
ICON1_entry3 = tk.Entry(window,width = 5)
ICON1_entry3.place(x=250,y=50)
ICON1_entry4 = tk.Entry(window,width = 5)
ICON1_entry4.place(x=300,y=50)
ICON1_entry5 = tk.Entry(window,width = 5)
ICON1_entry5.place(x=350,y=50)


#ICON2欄位
tk.Label(window,text = "ICON2").place(x=10, y=75)
ICON2_entry0 = tk.Entry(window,width = 10)
ICON2_entry0.place(x=60,y=75)
ICON2_entry1 = tk.Entry(window,width = 5)
ICON2_entry1.place(x=150,y=75)
ICON2_entry2 = tk.Entry(window,width = 5)
ICON2_entry2.place(x=200,y=75)
ICON2_entry3 = tk.Entry(window,width = 5)
ICON2_entry3.place(x=250,y=75)
ICON2_entry4 = tk.Entry(window,width = 5)
ICON2_entry4.place(x=300,y=75)
ICON2_entry5 = tk.Entry(window,width = 5)
ICON2_entry5.place(x=350,y=75)

#ICON3欄位
tk.Label(window,text = "ICON3").place(x=10, y=100)
ICON3_entry0 = tk.Entry(window,width = 10)
ICON3_entry0.place(x=60,y=100)
ICON3_entry1 = tk.Entry(window,width = 5)
ICON3_entry1.place(x=150,y=100)
ICON3_entry2 = tk.Entry(window,width = 5)
ICON3_entry2.place(x=200,y=100)
ICON3_entry3 = tk.Entry(window,width = 5)
ICON3_entry3.place(x=250,y=100)
ICON3_entry4 = tk.Entry(window,width = 5)
ICON3_entry4.place(x=300,y=100)
ICON3_entry5 = tk.Entry(window,width = 5)
ICON3_entry5.place(x=350,y=100)

#ICON4欄位
tk.Label(window,text = "ICON4").place(x=10, y=125)
ICON4_entry0 = tk.Entry(window,width = 10)
ICON4_entry0.place(x=60,y=125)
ICON4_entry1 = tk.Entry(window,width = 5)
ICON4_entry1.place(x=150,y=125)
ICON4_entry2 = tk.Entry(window,width = 5)
ICON4_entry2.place(x=200,y=125)
ICON4_entry3 = tk.Entry(window,width = 5)
ICON4_entry3.place(x=250,y=125)
ICON4_entry4 = tk.Entry(window,width = 5)
ICON4_entry4.place(x=300,y=125)
ICON4_entry5 = tk.Entry(window,width = 5)
ICON4_entry5.place(x=350,y=125)

#ICON5欄位
tk.Label(window,text = "ICON5").place(x=10, y=150)
ICON5_entry0 = tk.Entry(window,width = 10)
ICON5_entry0.place(x=60,y=150)
ICON5_entry1 = tk.Entry(window,width = 5)
ICON5_entry1.place(x=150,y=150)
ICON5_entry2 = tk.Entry(window,width = 5)
ICON5_entry2.place(x=200,y=150)
ICON5_entry3 = tk.Entry(window,width = 5)
ICON5_entry3.place(x=250,y=150)
ICON5_entry4 = tk.Entry(window,width = 5)
ICON5_entry4.place(x=300,y=150)
ICON5_entry5 = tk.Entry(window,width = 5)
ICON5_entry5.place(x=350,y=150)

#ICON6欄位
tk.Label(window,text = "ICON6").place(x=10, y=175)
ICON6_entry0 = tk.Entry(window,width = 10)
ICON6_entry0.place(x=60,y=175)
ICON6_entry1 = tk.Entry(window,width = 5)
ICON6_entry1.place(x=150,y=175)
ICON6_entry2 = tk.Entry(window,width = 5)
ICON6_entry2.place(x=200,y=175)
ICON6_entry3 = tk.Entry(window,width = 5)
ICON6_entry3.place(x=250,y=175)
ICON6_entry4 = tk.Entry(window,width = 5)
ICON6_entry4.place(x=300,y=175)
ICON6_entry5 = tk.Entry(window,width = 5)
ICON6_entry5.place(x=350,y=175)

#ICON7欄位
tk.Label(window,text = "ICON7").place(x=10, y=200)
ICON7_entry0 = tk.Entry(window,width = 10)
ICON7_entry0.place(x=60,y=200)
ICON7_entry1 = tk.Entry(window,width = 5)
ICON7_entry1.place(x=150,y=200)
ICON7_entry2 = tk.Entry(window,width = 5)
ICON7_entry2.place(x=200,y=200)
ICON7_entry3 = tk.Entry(window,width = 5)
ICON7_entry3.place(x=250,y=200)
ICON7_entry4 = tk.Entry(window,width = 5)
ICON7_entry4.place(x=300,y=200)
ICON7_entry5 = tk.Entry(window,width = 5)
ICON7_entry5.place(x=350,y=200)

#SCAT欄位
tk.Label(window,text = "SCAT").place(x=10, y=225)
#ICON7_entry0 = tk.Entry(window,width = 10)
#ICON7_entry0.place(x=60,y=200)
SCAT_entry1 = tk.Entry(window,width = 5)
SCAT_entry1.place(x=150,y=225)
SCAT_entry2 = tk.Entry(window,width = 5)
SCAT_entry2.place(x=200,y=225)
SCAT_entry3 = tk.Entry(window,width = 5)
SCAT_entry3.place(x=250,y=225)
SCAT_entry4 = tk.Entry(window,width = 5)
SCAT_entry4.place(x=300,y=225)
SCAT_entry5 = tk.Entry(window,width = 5)
SCAT_entry5.place(x=350,y=225)

#WILD欄位
tk.Label(window,text = "WILD").place(x=10, y=250)
#ICON7_entry0 = tk.Entry(window,width = 10)
#ICON7_entry0.place(x=60,y=200)
WILD_entry1 = tk.Entry(window,width = 5)
WILD_entry1.place(x=150,y=250)
WILD_entry2 = tk.Entry(window,width = 5)
WILD_entry2.place(x=200,y=250)
WILD_entry3 = tk.Entry(window,width = 5)
WILD_entry3.place(x=250,y=250)
WILD_entry4 = tk.Entry(window,width = 5)
WILD_entry4.place(x=300,y=250)
WILD_entry5 = tk.Entry(window,width = 5)
WILD_entry5.place(x=350,y=250)

#輸入資料的按鈕
button1 = tk.Button(window, text = "輸入資料",command = dataimport)
button1.place(x=200,y=280)
#分隔線
tk.Label(window, text = "-"*35+"我是分隔線"+"-"*35).place(x=10,y=300)

#賠率訊息
tk.Label(window, text = "圖案名稱").place(x=70,y=320)
tk.Label(window, text = "轉輪1").place(x=150,y=320)
tk.Label(window, text = "轉輪2").place(x=200,y=320)
tk.Label(window, text = "轉輪3").place(x=250,y=320)
tk.Label(window, text = "轉輪4").place(x=300,y=320)
tk.Label(window, text = "轉輪5").place(x=350,y=320)

#欄位1
tk.Label(window,text = "ICON1").place(x=10, y=350)
result1_str = tk.StringVar()
result1_label = tk.Label(window, textvariable=result1_str)
result1_label.place(x=70,y=350)

#欄位2
tk.Label(window,text = "ICON2").place(x=10, y=375)
result2_str = tk.StringVar()
result2_label = tk.Label(window, textvariable=result2_str)
result2_label.place(x=70,y=375)

#欄位3
tk.Label(window,text = "ICON3").place(x=10, y=400)
result3_str = tk.StringVar()
result3_label = tk.Label(window, textvariable=result3_str)
result3_label.place(x=70,y=400)

#欄位4
tk.Label(window,text = "ICON4").place(x=10, y=425)
result4_str = tk.StringVar()
result4_label = tk.Label(window, textvariable=result4_str)
result4_label.place(x=70,y=425)

#欄位5
tk.Label(window,text = "ICON5").place(x=10, y=450)
result5_str = tk.StringVar()
result5_label = tk.Label(window, textvariable=result5_str)
result5_label.place(x=70,y=450)

#欄位6
tk.Label(window,text = "ICON6").place(x=10, y=475)
result6_str = tk.StringVar()
result6_label = tk.Label(window, textvariable=result6_str)
result6_label.place(x=70,y=475)

#欄位7
tk.Label(window,text = "ICON7").place(x=10, y=500)
result7_str = tk.StringVar()
result7_label = tk.Label(window, textvariable=result7_str)
result7_label.place(x=70,y=500)

#欄位SCAT
tk.Label(window,text = "SCAT").place(x=10, y=525)

#欄位WILD
tk.Label(window,text = "WILD").place(x=10, y=550)



#運行主程式
window.mainloop()