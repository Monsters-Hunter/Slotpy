#引入套件
import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#載入字體
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']


#建立主視窗和框架
window = tk.Tk()                                                #創建主視窗
top_frame = tk.Frame(window)                                    #創建Frame
window.title("SLOT RTP計算機")                                   #顯示標題
window.geometry('440x1000')                                      #設定視窗大小

def dataimport():                                               #設定函數 : 取得輸入的名稱  
    result1_str.set("{}".format(ICON1_entry0.get()))
    result2_str.set("{}".format(ICON2_entry0.get()))
    result3_str.set("{}".format(ICON3_entry0.get()))
    result4_str.set("{}".format(ICON4_entry0.get()))
    result5_str.set("{}".format(ICON5_entry0.get()))
    result6_str.set("{}".format(ICON6_entry0.get()))
    result7_str.set("{}".format(ICON7_entry0.get()))
    SCAT_str.set("{}".format(SCAT_entry0.get()))
    WILD_str.set("{}".format(WILD_entry0.get()))

    #1                                                          #取得輸入的數字
    ICON1_entry1_num = int(ICON1_entry1.get())
    ICON1_entry2_num = int(ICON1_entry2.get())
    ICON1_entry3_num = int(ICON1_entry3.get())
    ICON1_entry4_num = int(ICON1_entry4.get())
    ICON1_entry5_num = int(ICON1_entry5.get())
    #2
    ICON2_entry1_num = int(ICON2_entry1.get())
    ICON2_entry2_num = int(ICON2_entry2.get())
    ICON2_entry3_num = int(ICON2_entry3.get())
    ICON2_entry4_num = int(ICON2_entry4.get())
    ICON2_entry5_num = int(ICON2_entry5.get())
    #3
    ICON3_entry1_num = int(ICON3_entry1.get())
    ICON3_entry2_num = int(ICON3_entry2.get())
    ICON3_entry3_num = int(ICON3_entry3.get())
    ICON3_entry4_num = int(ICON3_entry4.get())
    ICON3_entry5_num = int(ICON3_entry5.get())
    #4
    ICON4_entry1_num = int(ICON4_entry1.get())
    ICON4_entry2_num = int(ICON4_entry2.get())
    ICON4_entry3_num = int(ICON4_entry3.get())
    ICON4_entry4_num = int(ICON4_entry4.get())
    ICON4_entry5_num = int(ICON4_entry5.get())
    #5
    ICON5_entry1_num = int(ICON5_entry1.get())
    ICON5_entry2_num = int(ICON5_entry2.get())
    ICON5_entry3_num = int(ICON5_entry3.get())
    ICON5_entry4_num = int(ICON5_entry4.get())
    ICON5_entry5_num = int(ICON5_entry5.get())
    #6
    ICON6_entry1_num = int(ICON6_entry1.get())
    ICON6_entry2_num = int(ICON6_entry2.get())
    ICON6_entry3_num = int(ICON6_entry3.get())
    ICON6_entry4_num = int(ICON6_entry4.get())
    ICON6_entry5_num = int(ICON6_entry5.get())
    #7
    ICON7_entry1_num = int(ICON7_entry1.get())
    ICON7_entry2_num = int(ICON7_entry2.get())
    ICON7_entry3_num = int(ICON7_entry3.get())
    ICON7_entry4_num = int(ICON7_entry4.get())
    ICON7_entry5_num = int(ICON7_entry5.get())
    #SCAT
    SCAT_entry1_num = int(SCAT_entry1.get())
    SCAT_entry2_num = int(SCAT_entry2.get())
    SCAT_entry3_num = int(SCAT_entry3.get())
    SCAT_entry4_num = int(SCAT_entry4.get())
    SCAT_entry5_num = int(SCAT_entry5.get())
    #WILD
    WILD_entry1_num = int(WILD_entry1.get())
    WILD_entry2_num = int(WILD_entry2.get())
    WILD_entry3_num = int(WILD_entry3.get())
    WILD_entry4_num = int(WILD_entry4.get())
    WILD_entry5_num = int(WILD_entry5.get())

    #計算各輪總個數
    #第一輪
    wheel1=[]
    wheel1.append(ICON1_entry1_num)
    wheel1.append(ICON2_entry1_num)
    wheel1.append(ICON3_entry1_num)
    wheel1.append(ICON4_entry1_num)
    wheel1.append(ICON5_entry1_num)
    wheel1.append(ICON6_entry1_num)
    wheel1.append(ICON7_entry1_num)
    wheel1.append(SCAT_entry1_num)
    wheel1.append(WILD_entry1_num)
    wheel1_sum = sum(wheel1)
    #第二輪
    wheel2=[]
    wheel2.append(ICON1_entry2_num)
    wheel2.append(ICON2_entry2_num)
    wheel2.append(ICON3_entry2_num)
    wheel2.append(ICON4_entry2_num)
    wheel2.append(ICON5_entry2_num)
    wheel2.append(ICON6_entry2_num)
    wheel2.append(ICON7_entry2_num)
    wheel2.append(SCAT_entry2_num)
    wheel2.append(WILD_entry2_num)
    wheel2_sum = sum(wheel2)
    #第三輪
    wheel3=[]
    wheel3.append(ICON1_entry3_num)
    wheel3.append(ICON2_entry3_num)
    wheel3.append(ICON3_entry3_num)
    wheel3.append(ICON4_entry3_num)
    wheel3.append(ICON5_entry3_num)
    wheel3.append(ICON6_entry3_num)
    wheel3.append(ICON7_entry3_num)
    wheel3.append(SCAT_entry3_num)
    wheel3.append(WILD_entry3_num)
    wheel3_sum = sum(wheel3)
    #第四輪
    wheel4=[]
    wheel4.append(ICON1_entry4_num)
    wheel4.append(ICON2_entry4_num)
    wheel4.append(ICON3_entry4_num)
    wheel4.append(ICON4_entry4_num)
    wheel4.append(ICON5_entry4_num)
    wheel4.append(ICON6_entry4_num)
    wheel4.append(ICON7_entry4_num)
    wheel4.append(SCAT_entry4_num)
    wheel4.append(WILD_entry4_num)
    wheel4_sum = sum(wheel4)
    #第五輪
    wheel5=[]
    wheel5.append(ICON1_entry5_num)
    wheel5.append(ICON2_entry5_num)
    wheel5.append(ICON3_entry5_num)
    wheel5.append(ICON4_entry5_num)
    wheel5.append(ICON5_entry5_num)
    wheel5.append(ICON6_entry5_num)
    wheel5.append(ICON7_entry5_num)
    wheel5.append(SCAT_entry5_num)
    wheel5.append(WILD_entry5_num)
    wheel5_sum = sum(wheel5)

    #DataFrame
    wheel_table = pd.DataFrame({
        "first": wheel1, "second":wheel2, "third":wheel3, "fourth":wheel4, "fivth":wheel5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get(),
                SCAT_entry0.get(),
                WILD_entry0.get() ])

    wheelist1 = [ICON1_entry1_num + WILD_entry1_num , ICON2_entry1_num + WILD_entry1_num , ICON3_entry1_num + WILD_entry1_num ,ICON4_entry1_num + WILD_entry1_num,
                 ICON5_entry1_num + WILD_entry1_num , ICON6_entry1_num + WILD_entry1_num , ICON7_entry1_num + WILD_entry1_num ]
    wheelist2 = [ICON1_entry2_num + WILD_entry2_num , ICON2_entry2_num + WILD_entry2_num , ICON3_entry2_num + WILD_entry2_num ,ICON4_entry2_num + WILD_entry2_num,
                 ICON5_entry2_num + WILD_entry2_num , ICON6_entry2_num + WILD_entry2_num , ICON7_entry2_num + WILD_entry2_num]
    wheelist3 = [ICON1_entry3_num + WILD_entry3_num , ICON2_entry3_num + WILD_entry3_num , ICON3_entry3_num + WILD_entry3_num ,ICON4_entry3_num + WILD_entry3_num,
                 ICON5_entry3_num + WILD_entry3_num , ICON6_entry3_num + WILD_entry3_num , ICON7_entry3_num + WILD_entry3_num]
    wheelist4 = [ICON1_entry4_num + WILD_entry4_num , ICON2_entry4_num + WILD_entry4_num , ICON3_entry4_num + WILD_entry4_num ,ICON4_entry4_num + WILD_entry4_num,
                 ICON5_entry4_num + WILD_entry4_num , ICON6_entry4_num + WILD_entry4_num , ICON7_entry4_num + WILD_entry4_num]
    wheelist5 = [ICON1_entry5_num + WILD_entry5_num , ICON2_entry5_num + WILD_entry5_num , ICON3_entry5_num + WILD_entry5_num ,ICON4_entry5_num + WILD_entry5_num,
                 ICON5_entry5_num + WILD_entry5_num , ICON6_entry5_num + WILD_entry5_num , ICON7_entry5_num + WILD_entry5_num]

    #WILD+各圖案數量
    wildsum = pd.DataFrame({
        "轉輪1":wheelist1,
        "轉輪2":wheelist2,
        "轉輪3":wheelist3,
        "轉輪4":wheelist4,
        "轉輪5":wheelist5         
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])

    notlist1 = [ wheel1_sum-wheelist1[0], wheel1_sum-wheelist1[1] , wheel1_sum-wheelist1[2], wheel1_sum-wheelist1[3] , wheel1_sum-wheelist1[4] , wheel1_sum-wheelist1[5], wheel1_sum-wheelist1[6]]
    notlist2 = [ wheel2_sum-wheelist2[0], wheel2_sum-wheelist2[1] , wheel2_sum-wheelist2[2], wheel2_sum-wheelist2[3] , wheel2_sum-wheelist2[4] , wheel2_sum-wheelist2[5], wheel2_sum-wheelist2[6]]
    notlist3 = [ wheel3_sum-wheelist3[0], wheel3_sum-wheelist3[1] , wheel3_sum-wheelist3[2], wheel3_sum-wheelist3[3] , wheel3_sum-wheelist3[4] , wheel3_sum-wheelist3[5], wheel3_sum-wheelist3[6]]
    notlist4 = [ wheel4_sum-wheelist4[0], wheel4_sum-wheelist4[1] , wheel4_sum-wheelist4[2], wheel4_sum-wheelist4[3] , wheel4_sum-wheelist4[4] , wheel4_sum-wheelist4[5], wheel4_sum-wheelist4[6]]
    notlist5 = [ wheel5_sum-wheelist5[0], wheel5_sum-wheelist5[1] , wheel5_sum-wheelist5[2], wheel5_sum-wheelist5[3] , wheel5_sum-wheelist5[4] , wheel5_sum-wheelist5[5], wheel5_sum-wheelist5[6]]


    #非WILD也非各圖案
    notwild = pd.DataFrame({
        "非WILD數輪1":notlist1,
        "非WILD數輪2":notlist2,
        "非WILD數輪3":notlist3,
        "非WILD數輪4":notlist4,
        "非WILD數輪5":notlist5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])
    
def datacalcul():
    #1
    ICON1_bet1_num = int(ICON1_bet1.get())
    ICON1_bet2_num = int(ICON1_bet2.get())
    ICON1_bet3_num = int(ICON1_bet3.get())
    ICON1_bet4_num = int(ICON1_bet4.get())
    ICON1_bet5_num = int(ICON1_bet5.get())
    #2
    ICON2_bet1_num = int(ICON2_bet1.get())
    ICON2_bet2_num = int(ICON2_bet2.get())
    ICON2_bet3_num = int(ICON2_bet3.get())
    ICON2_bet4_num = int(ICON2_bet4.get())
    ICON2_bet5_num = int(ICON2_bet5.get())
    #3
    ICON3_bet1_num = int(ICON3_bet1.get())
    ICON3_bet2_num = int(ICON3_bet2.get())
    ICON3_bet3_num = int(ICON3_bet3.get())
    ICON3_bet4_num = int(ICON3_bet4.get())
    ICON3_bet5_num = int(ICON3_bet5.get())
    #4
    ICON4_bet1_num = int(ICON4_bet1.get())
    ICON4_bet2_num = int(ICON4_bet2.get())
    ICON4_bet3_num = int(ICON4_bet3.get())
    ICON4_bet4_num = int(ICON4_bet4.get())
    ICON4_bet5_num = int(ICON4_bet5.get())
    #5
    ICON5_bet1_num = int(ICON5_bet1.get())
    ICON5_bet2_num = int(ICON5_bet2.get())
    ICON5_bet3_num = int(ICON5_bet3.get())
    ICON5_bet4_num = int(ICON5_bet4.get())
    ICON5_bet5_num = int(ICON5_bet5.get())
    #6
    ICON6_bet1_num = int(ICON6_bet1.get())
    ICON6_bet2_num = int(ICON6_bet2.get())
    ICON6_bet3_num = int(ICON6_bet3.get())
    ICON6_bet4_num = int(ICON6_bet4.get())
    ICON6_bet5_num = int(ICON6_bet5.get())
    #7
    ICON7_bet1_num = int(ICON7_bet1.get())
    ICON7_bet2_num = int(ICON7_bet2.get())
    ICON7_bet3_num = int(ICON7_bet3.get())
    ICON7_bet4_num = int(ICON7_bet4.get())
    ICON7_bet5_num = int(ICON7_bet5.get())
    #SCAT
    SCAT_bet1_num = int(SCAT_bet1.get())
    SCAT_bet2_num = int(SCAT_bet2.get())
    SCAT_bet3_num = int(SCAT_bet3.get())
    SCAT_bet4_num = int(SCAT_bet4.get())
    SCAT_bet5_num = int(SCAT_bet5.get())
    #WILD
    WILD_bet1_num = int(WILD_bet1.get())
    WILD_bet2_num = int(WILD_bet2.get())
    WILD_bet3_num = int(WILD_bet3.get())
    WILD_bet4_num = int(WILD_bet4.get())
    WILD_bet5_num = int(WILD_bet5.get())
    
    #列出組合表
    #圖案種類
    table_icon = []
    for i in range(3):
        table_icon.append(ICON1_entry0.get())
    for i in range(3):
        table_icon.append(ICON2_entry0.get())    
    for i in range(3):
        table_icon.append(ICON3_entry0.get())
    for i in range(3):
        table_icon.append(ICON4_entry0.get())
    for i in range(3):
        table_icon.append(ICON5_entry0.get())
    for i in range(3):
        table_icon.append(ICON6_entry0.get())
    for i in range(3):
        table_icon.append(ICON7_entry0.get())
    table_icon.append(SCAT_entry0.get())
      
    #連線數
    link = [5,4,3]*7+[3]

    #計算出現次數
    
    #1                                                          #取得輸入的數字
    ICON1_entry1_num = int(ICON1_entry1.get())
    ICON1_entry2_num = int(ICON1_entry2.get())
    ICON1_entry3_num = int(ICON1_entry3.get())
    ICON1_entry4_num = int(ICON1_entry4.get())
    ICON1_entry5_num = int(ICON1_entry5.get())
    #2
    ICON2_entry1_num = int(ICON2_entry1.get())
    ICON2_entry2_num = int(ICON2_entry2.get())
    ICON2_entry3_num = int(ICON2_entry3.get())
    ICON2_entry4_num = int(ICON2_entry4.get())
    ICON2_entry5_num = int(ICON2_entry5.get())
    #3
    ICON3_entry1_num = int(ICON3_entry1.get())
    ICON3_entry2_num = int(ICON3_entry2.get())
    ICON3_entry3_num = int(ICON3_entry3.get())
    ICON3_entry4_num = int(ICON3_entry4.get())
    ICON3_entry5_num = int(ICON3_entry5.get())
    #4
    ICON4_entry1_num = int(ICON4_entry1.get())
    ICON4_entry2_num = int(ICON4_entry2.get())
    ICON4_entry3_num = int(ICON4_entry3.get())
    ICON4_entry4_num = int(ICON4_entry4.get())
    ICON4_entry5_num = int(ICON4_entry5.get())
    #5
    ICON5_entry1_num = int(ICON5_entry1.get())
    ICON5_entry2_num = int(ICON5_entry2.get())
    ICON5_entry3_num = int(ICON5_entry3.get())
    ICON5_entry4_num = int(ICON5_entry4.get())
    ICON5_entry5_num = int(ICON5_entry5.get())
    #6
    ICON6_entry1_num = int(ICON6_entry1.get())
    ICON6_entry2_num = int(ICON6_entry2.get())
    ICON6_entry3_num = int(ICON6_entry3.get())
    ICON6_entry4_num = int(ICON6_entry4.get())
    ICON6_entry5_num = int(ICON6_entry5.get())
    #7
    ICON7_entry1_num = int(ICON7_entry1.get())
    ICON7_entry2_num = int(ICON7_entry2.get())
    ICON7_entry3_num = int(ICON7_entry3.get())
    ICON7_entry4_num = int(ICON7_entry4.get())
    ICON7_entry5_num = int(ICON7_entry5.get())
    #SCAT
    SCAT_entry1_num = int(SCAT_entry1.get())
    SCAT_entry2_num = int(SCAT_entry2.get())
    SCAT_entry3_num = int(SCAT_entry3.get())
    SCAT_entry4_num = int(SCAT_entry4.get())
    SCAT_entry5_num = int(SCAT_entry5.get())
    #WILD
    WILD_entry1_num = int(WILD_entry1.get())
    WILD_entry2_num = int(WILD_entry2.get())
    WILD_entry3_num = int(WILD_entry3.get())
    WILD_entry4_num = int(WILD_entry4.get())
    WILD_entry5_num = int(WILD_entry5.get())

    #計算各輪總個數
    #第一輪
    wheel1=[]
    wheel1.append(ICON1_entry1_num)
    wheel1.append(ICON2_entry1_num)
    wheel1.append(ICON3_entry1_num)
    wheel1.append(ICON4_entry1_num)
    wheel1.append(ICON5_entry1_num)
    wheel1.append(ICON6_entry1_num)
    wheel1.append(ICON7_entry1_num)
    wheel1.append(SCAT_entry1_num)
    wheel1.append(WILD_entry1_num)
    wheel1_sum = sum(wheel1)
    #第二輪
    wheel2=[]
    wheel2.append(ICON1_entry2_num)
    wheel2.append(ICON2_entry2_num)
    wheel2.append(ICON3_entry2_num)
    wheel2.append(ICON4_entry2_num)
    wheel2.append(ICON5_entry2_num)
    wheel2.append(ICON6_entry2_num)
    wheel2.append(ICON7_entry2_num)
    wheel2.append(SCAT_entry2_num)
    wheel2.append(WILD_entry2_num)
    wheel2_sum = sum(wheel2)
    #第三輪
    wheel3=[]
    wheel3.append(ICON1_entry3_num)
    wheel3.append(ICON2_entry3_num)
    wheel3.append(ICON3_entry3_num)
    wheel3.append(ICON4_entry3_num)
    wheel3.append(ICON5_entry3_num)
    wheel3.append(ICON6_entry3_num)
    wheel3.append(ICON7_entry3_num)
    wheel3.append(SCAT_entry3_num)
    wheel3.append(WILD_entry3_num)
    wheel3_sum = sum(wheel3)
    #第四輪
    wheel4=[]
    wheel4.append(ICON1_entry4_num)
    wheel4.append(ICON2_entry4_num)
    wheel4.append(ICON3_entry4_num)
    wheel4.append(ICON4_entry4_num)
    wheel4.append(ICON5_entry4_num)
    wheel4.append(ICON6_entry4_num)
    wheel4.append(ICON7_entry4_num)
    wheel4.append(SCAT_entry4_num)
    wheel4.append(WILD_entry4_num)
    wheel4_sum = sum(wheel4)
    #第五輪
    wheel5=[]
    wheel5.append(ICON1_entry5_num)
    wheel5.append(ICON2_entry5_num)
    wheel5.append(ICON3_entry5_num)
    wheel5.append(ICON4_entry5_num)
    wheel5.append(ICON5_entry5_num)
    wheel5.append(ICON6_entry5_num)
    wheel5.append(ICON7_entry5_num)
    wheel5.append(SCAT_entry5_num)
    wheel5.append(WILD_entry5_num)
    wheel5_sum = sum(wheel5)

    #計算總機率(各輪可能出現的數量相乘)
    total_prob = wheel1_sum*wheel2_sum*wheel3_sum*wheel4_sum*wheel5_sum

    #取得輸入的連線賠率(只有3連線才會得分)
    #ICON1 (3連線~5連線)
    ICON1_bet3_num = int(ICON1_bet3.get())
    ICON1_bet4_num = int(ICON1_bet4.get())
    ICON1_bet5_num = int(ICON1_bet5.get())
    #ICON2 (3連線~5連線)
    ICON2_bet3_num = int(ICON2_bet3.get())
    ICON2_bet4_num = int(ICON2_bet4.get())
    ICON2_bet5_num = int(ICON2_bet5.get())
    #ICON3 (3連線~5連線)
    ICON3_bet3_num = int(ICON3_bet3.get())
    ICON3_bet4_num = int(ICON3_bet4.get())
    ICON3_bet5_num = int(ICON3_bet5.get())
    #ICON4 (3連線~5連線)
    ICON4_bet3_num = int(ICON4_bet3.get())
    ICON4_bet4_num = int(ICON4_bet4.get())
    ICON4_bet5_num = int(ICON4_bet5.get())
    #ICON5 (3連線~5連線)
    ICON5_bet3_num = int(ICON5_bet3.get())
    ICON5_bet4_num = int(ICON5_bet4.get())
    ICON5_bet5_num = int(ICON5_bet5.get())
    #ICON6 (3連線~5連線)
    ICON6_bet3_num = int(ICON6_bet3.get())
    ICON6_bet4_num = int(ICON6_bet4.get())
    ICON6_bet5_num = int(ICON6_bet5.get())
    #ICON7 (3連線~5連線)
    ICON7_bet3_num = int(ICON7_bet3.get())
    ICON7_bet4_num = int(ICON7_bet4.get())
    ICON7_bet5_num = int(ICON7_bet5.get())
    #SCAT (3連線~5連線)
    SCAT_bet3_num = int(SCAT_bet3.get())
    SCAT_bet4_num = int(SCAT_bet4.get())
    SCAT_bet5_num = int(SCAT_bet5.get())
    #WILD (3連線~5連線)
    WILD_bet3_num = int(WILD_bet3.get())
    WILD_bet4_num = int(WILD_bet4.get())
    WILD_bet5_num = int(WILD_bet5.get())

    #將取得的賠率列成串列
    score = [ICON1_bet5_num , ICON1_bet4_num , ICON1_bet3_num ,
             ICON2_bet5_num , ICON2_bet4_num , ICON2_bet3_num ,
             ICON3_bet5_num , ICON3_bet4_num , ICON3_bet3_num , 
             ICON4_bet5_num , ICON4_bet4_num , ICON4_bet3_num ,
             ICON5_bet5_num , ICON5_bet4_num , ICON5_bet3_num ,
             ICON6_bet5_num , ICON6_bet4_num , ICON6_bet3_num ,
             ICON7_bet5_num , ICON7_bet4_num , ICON7_bet3_num ,
             SCAT_bet3_num
    ]
    #將賠率轉成 [1 * 21] 陣列，方便計算 
    score_array = np.array(score).T


    #DataFrame
    wheel_table = pd.DataFrame({
        "first": wheel1, "second":wheel2, "third":wheel3, "fourth":wheel4, "fivth":wheel5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get(),
                SCAT_entry0.get(),
                WILD_entry0.get() ])

    wheelist1 = [ICON1_entry1_num + WILD_entry1_num , ICON2_entry1_num + WILD_entry1_num , ICON3_entry1_num + WILD_entry1_num ,ICON4_entry1_num + WILD_entry1_num,
                 ICON5_entry1_num + WILD_entry1_num , ICON6_entry1_num + WILD_entry1_num , ICON7_entry1_num + WILD_entry1_num ]
    wheelist2 = [ICON1_entry2_num + WILD_entry2_num , ICON2_entry2_num + WILD_entry2_num , ICON3_entry2_num + WILD_entry2_num ,ICON4_entry2_num + WILD_entry2_num,
                 ICON5_entry2_num + WILD_entry2_num , ICON6_entry2_num + WILD_entry2_num , ICON7_entry2_num + WILD_entry2_num]
    wheelist3 = [ICON1_entry3_num + WILD_entry3_num , ICON2_entry3_num + WILD_entry3_num , ICON3_entry3_num + WILD_entry3_num ,ICON4_entry3_num + WILD_entry3_num,
                 ICON5_entry3_num + WILD_entry3_num , ICON6_entry3_num + WILD_entry3_num , ICON7_entry3_num + WILD_entry3_num]
    wheelist4 = [ICON1_entry4_num + WILD_entry4_num , ICON2_entry4_num + WILD_entry4_num , ICON3_entry4_num + WILD_entry4_num ,ICON4_entry4_num + WILD_entry4_num,
                 ICON5_entry4_num + WILD_entry4_num , ICON6_entry4_num + WILD_entry4_num , ICON7_entry4_num + WILD_entry4_num]
    wheelist5 = [ICON1_entry5_num + WILD_entry5_num , ICON2_entry5_num + WILD_entry5_num , ICON3_entry5_num + WILD_entry5_num ,ICON4_entry5_num + WILD_entry5_num,
                 ICON5_entry5_num + WILD_entry5_num , ICON6_entry5_num + WILD_entry5_num , ICON7_entry5_num + WILD_entry5_num]

    #WILD+各圖案數量
    wildsum = pd.DataFrame({
        "轉輪1":wheelist1,
        "轉輪2":wheelist2,
        "轉輪3":wheelist3,
        "轉輪4":wheelist4,
        "轉輪5":wheelist5         
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])

    notlist1 = [ wheel1_sum-wheelist1[0], wheel1_sum-wheelist1[1] , wheel1_sum-wheelist1[2], wheel1_sum-wheelist1[3] , wheel1_sum-wheelist1[4] , wheel1_sum-wheelist1[5], wheel1_sum-wheelist1[6]]
    notlist2 = [ wheel2_sum-wheelist2[0], wheel2_sum-wheelist2[1] , wheel2_sum-wheelist2[2], wheel2_sum-wheelist2[3] , wheel2_sum-wheelist2[4] , wheel2_sum-wheelist2[5], wheel2_sum-wheelist2[6]]
    notlist3 = [ wheel3_sum-wheelist3[0], wheel3_sum-wheelist3[1] , wheel3_sum-wheelist3[2], wheel3_sum-wheelist3[3] , wheel3_sum-wheelist3[4] , wheel3_sum-wheelist3[5], wheel3_sum-wheelist3[6]]
    notlist4 = [ wheel4_sum-wheelist4[0], wheel4_sum-wheelist4[1] , wheel4_sum-wheelist4[2], wheel4_sum-wheelist4[3] , wheel4_sum-wheelist4[4] , wheel4_sum-wheelist4[5], wheel4_sum-wheelist4[6]]
    notlist5 = [ wheel5_sum-wheelist5[0], wheel5_sum-wheelist5[1] , wheel5_sum-wheelist5[2], wheel5_sum-wheelist5[3] , wheel5_sum-wheelist5[4] , wheel5_sum-wheelist5[5], wheel5_sum-wheelist5[6]]


    #非WILD也非各圖案
    notwild = pd.DataFrame({
        "非WILD數輪1":notlist1,
        "非WILD數輪2":notlist2,
        "非WILD數輪3":notlist3,
        "非WILD數輪4":notlist4,
        "非WILD數輪5":notlist5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])
    #計算出現次數
    appear = [wheelist1[0]*wheelist2[0]*wheelist3[0]*wheelist4[0]*wheelist5[0],
              wheelist1[0]*wheelist2[0]*wheelist3[0]*wheelist4[0]*notlist5[0],
              wheelist1[0]*wheelist2[0]*wheelist3[0]*notlist4[0]*wheel5_sum,
              wheelist1[1]*wheelist2[1]*wheelist3[1]*wheelist4[1]*wheelist5[1],
              wheelist1[1]*wheelist2[1]*wheelist3[1]*wheelist4[1]*notlist5[1],
              wheelist1[1]*wheelist2[1]*wheelist3[1]*notlist4[1]*wheel5_sum,
              wheelist1[2]*wheelist2[2]*wheelist3[2]*wheelist4[2]*wheelist5[2],
              wheelist1[2]*wheelist2[2]*wheelist3[2]*wheelist4[2]*notlist5[2],
              wheelist1[2]*wheelist2[2]*wheelist3[2]*notlist4[2]*wheel5_sum,
              wheelist1[3]*wheelist2[3]*wheelist3[3]*wheelist4[3]*wheelist5[3],
              wheelist1[3]*wheelist2[3]*wheelist3[3]*wheelist4[3]*notlist5[3],
              wheelist1[3]*wheelist2[3]*wheelist3[3]*notlist4[3]*wheel5_sum,
              wheelist1[4]*wheelist2[4]*wheelist3[4]*wheelist4[4]*wheelist5[4],
              wheelist1[4]*wheelist2[4]*wheelist3[4]*wheelist4[4]*notlist5[4],
              wheelist1[4]*wheelist2[4]*wheelist3[4]*notlist4[4]*wheel5_sum,
              wheelist1[5]*wheelist2[5]*wheelist3[5]*wheelist4[5]*wheelist5[5],
              wheelist1[5]*wheelist2[5]*wheelist3[5]*wheelist4[5]*notlist5[5],
              wheelist1[5]*wheelist2[5]*wheelist3[5]*notlist4[5]*wheel5_sum,
              wheelist1[6]*wheelist2[6]*wheelist3[6]*wheelist4[6]*wheelist5[6],
              wheelist1[6]*wheelist2[6]*wheelist3[6]*wheelist4[6]*notlist5[6],
              wheelist1[6]*wheelist2[6]*wheelist3[6]*notlist4[6]*wheel5_sum,
              wheel1_sum*(wheel2[-2]*3)*(wheel3[-2]*3)*(wheel4[-2]*3)*wheel5_sum
              ]
    #轉成矩陣方便計算
    appear_array = np.array(appear)

    appear_prob = appear_array / total_prob
    value = appear_prob * score_array
    
    #DataFrame
    wheel_betable = pd.DataFrame({
        "圖案名稱":table_icon,
        "連線數":link,
        "出現次數":appear,
        "出現機率":appear_prob,
        "得分賠率":score,
        "期望值": value
    }, index = [ "ICON1","","","ICON2","","","ICON3","","",
                 "ICON4","","","ICON5","","","ICON6","","",
                 "ICON7","","","SCAT"])
    wheel_betable["期望值"] = wheel_betable["期望值"].apply(lambda x: format(x, '.2%'))
    #計算各Icon的群組期望值
    value1 = value.tolist().pop()
    value_total = []
    for i in range(0,len(value)):
        suma = 0
        for j in range(0,len(value)):
            if j // 3 == i:
                suma += value[j]
        value_total.append(round(suma,4))
    while len(value)//3 != len(value_total):
        value_total.pop()
    value_total.append(value1)
    category = [ICON1_entry0.get(),ICON2_entry0.get(),ICON3_entry0.get(),ICON4_entry0.get(),ICON5_entry0.get(),ICON6_entry0.get(),ICON7_entry0.get(),WILD_entry0.get()]
    plt.figure("各ICON得分比例")
    separeted = [0,0,0,0,0,0,0,0]
    value_total = [x*1000 for x in value_total]
    plt.pie(
    value_total,    
    #colors = color,
    labels = category,
    autopct = '%3.2f%%',
    explode = separeted,
    #pctdistance = 0.6,
    #textprops = {'fontsize':12},
    shadow = False       
    )
    plt.axis('equal')
    plt.legend(loc = 'best')
    plt.show()
    

    print(wheel_table)
    print(wildsum)
    print(notwild)
    print(wheel_betable)
    print(value.sum())  #印出總RTP
    
    #產出CSV檔案
    wheel_betable.to_csv("wheel_betable.csv", encoding = 'utf_8_sig')
    
#建立輸入提示訊息
tk.Label(window, text = "請輸入各ICON的名稱\n並請輸入各ICON在各轉輪的個數, 預設為0",
                 font = ("Arial",10), width = 40 , height = 5).place(x=60,y = 0)



#視窗內訊息
tk.Label(window, text = "圖案名稱").place(x=70,y=70)
tk.Label(window, text = "轉輪1").place(x=150,y=70)
tk.Label(window, text = "轉輪2").place(x=200,y=70)
tk.Label(window, text = "轉輪3").place(x=250,y=70)
tk.Label(window, text = "轉輪4").place(x=300,y=70)
tk.Label(window, text = "轉輪5").place(x=350,y=70)

#輸入欄位
#ICON1欄位
tk.Label(window,text = "ICON1").place(x=10, y=90)
#ICON1_entry0 = tk.StringVar()                                           #令格子可輸入文字
ICON1_entry0 = tk.Entry(window,width = 10)#,textvariable=ICON1_entry0)    #設定接收 Icon1_entry0 的值   
ICON1_entry0.place(x=60,y=90)                                           #設定座標
ICON1_entry1 = tk.Entry(window,width = 5)
ICON1_entry1.place(x=150,y=90)
ICON1_entry1.insert(0,"0")                                              #插入預設數字0
ICON1_entry2 = tk.Entry(window,width = 5)
ICON1_entry2.place(x=200,y=90)
ICON1_entry2.insert(1,"0")
ICON1_entry3 = tk.Entry(window,width = 5)
ICON1_entry3.place(x=250,y=90)
ICON1_entry3.insert(2,"0")
ICON1_entry4 = tk.Entry(window,width = 5)
ICON1_entry4.place(x=300,y=90)
ICON1_entry4.insert(3,"0")
ICON1_entry5 = tk.Entry(window,width = 5)
ICON1_entry5.place(x=350,y=90)
ICON1_entry5.insert(4,"0")


#ICON2欄位
tk.Label(window,text = "ICON2").place(x=10, y=115)
ICON2_entry0 = tk.Entry(window,width = 10)
ICON2_entry0.place(x=60,y=115)
ICON2_entry1 = tk.Entry(window,width = 5)
ICON2_entry1.place(x=150,y=115)
ICON2_entry1.insert(0,"0")
ICON2_entry2 = tk.Entry(window,width = 5)
ICON2_entry2.place(x=200,y=115)
ICON2_entry2.insert(1,"0")
ICON2_entry3 = tk.Entry(window,width = 5)
ICON2_entry3.place(x=250,y=115)
ICON2_entry3.insert(2,"0")
ICON2_entry4 = tk.Entry(window,width = 5)
ICON2_entry4.place(x=300,y=115)
ICON2_entry4.insert(3,"0")
ICON2_entry5 = tk.Entry(window,width = 5)
ICON2_entry5.place(x=350,y=115)
ICON2_entry5.insert(4,"0")

#ICON3欄位
tk.Label(window,text = "ICON3").place(x=10, y=140)
ICON3_entry0 = tk.Entry(window,width = 10)
ICON3_entry0.place(x=60,y=140)
ICON3_entry1 = tk.Entry(window,width = 5)
ICON3_entry1.place(x=150,y=140)
ICON3_entry1.insert(0,"0")
ICON3_entry2 = tk.Entry(window,width = 5)
ICON3_entry2.place(x=200,y=140)
ICON3_entry2.insert(1,"0")
ICON3_entry3 = tk.Entry(window,width = 5)
ICON3_entry3.place(x=250,y=140)
ICON3_entry3.insert(2,"0")
ICON3_entry4 = tk.Entry(window,width = 5)
ICON3_entry4.place(x=300,y=140)
ICON3_entry4.insert(3,"0")
ICON3_entry5 = tk.Entry(window,width = 5)
ICON3_entry5.place(x=350,y=140)
ICON3_entry5.insert(4,"0")

#ICON4欄位
tk.Label(window,text = "ICON4").place(x=10, y=165)
ICON4_entry0 = tk.Entry(window,width = 10)
ICON4_entry0.place(x=60,y=165)
ICON4_entry1 = tk.Entry(window,width = 5)
ICON4_entry1.place(x=150,y=165)
ICON4_entry1.insert(0,"0")
ICON4_entry2 = tk.Entry(window,width = 5)
ICON4_entry2.place(x=200,y=165)
ICON4_entry2.insert(1,"0")
ICON4_entry3 = tk.Entry(window,width = 5)
ICON4_entry3.place(x=250,y=165)
ICON4_entry3.insert(2,"0")
ICON4_entry4 = tk.Entry(window,width = 5)
ICON4_entry4.place(x=300,y=165)
ICON4_entry4.insert(3,"0")
ICON4_entry5 = tk.Entry(window,width = 5)
ICON4_entry5.place(x=350,y=165)
ICON4_entry5.insert(4,"0")

#ICON5欄位
tk.Label(window,text = "ICON5").place(x=10, y=190)
ICON5_entry0 = tk.Entry(window,width = 10)
ICON5_entry0.place(x=60,y=190)
ICON5_entry1 = tk.Entry(window,width = 5)
ICON5_entry1.place(x=150,y=190)
ICON5_entry1.insert(0,"0")
ICON5_entry2 = tk.Entry(window,width = 5)
ICON5_entry2.place(x=200,y=190)
ICON5_entry2.insert(1,"0")
ICON5_entry3 = tk.Entry(window,width = 5)
ICON5_entry3.place(x=250,y=190)
ICON5_entry3.insert(2,"0")
ICON5_entry4 = tk.Entry(window,width = 5)
ICON5_entry4.place(x=300,y=190)
ICON5_entry4.insert(3,"0")
ICON5_entry5 = tk.Entry(window,width = 5)
ICON5_entry5.place(x=350,y=190)
ICON5_entry5.insert(4,"0")

#ICON6欄位
tk.Label(window,text = "ICON6").place(x=10, y=215)
ICON6_entry0 = tk.Entry(window,width = 10)
ICON6_entry0.place(x=60,y=215)
ICON6_entry1 = tk.Entry(window,width = 5)
ICON6_entry1.place(x=150,y=215)
ICON6_entry1.insert(0,"0")
ICON6_entry2 = tk.Entry(window,width = 5)
ICON6_entry2.place(x=200,y=215)
ICON6_entry2.insert(1,"0")
ICON6_entry3 = tk.Entry(window,width = 5)
ICON6_entry3.place(x=250,y=215)
ICON6_entry3.insert(2,"0")
ICON6_entry4 = tk.Entry(window,width = 5)
ICON6_entry4.place(x=300,y=215)
ICON6_entry4.insert(3,"0")
ICON6_entry5 = tk.Entry(window,width = 5)
ICON6_entry5.place(x=350,y=215)
ICON6_entry5.insert(4,"0")

#ICON7欄位
tk.Label(window,text = "ICON7").place(x=10, y=240)
ICON7_entry0 = tk.Entry(window,width = 10)
ICON7_entry0.place(x=60,y=240)
ICON7_entry1 = tk.Entry(window,width = 5)
ICON7_entry1.place(x=150,y=240)
ICON7_entry1.insert(0,"0")
ICON7_entry2 = tk.Entry(window,width = 5)
ICON7_entry2.place(x=200,y=240)
ICON7_entry2.insert(1,"0")
ICON7_entry3 = tk.Entry(window,width = 5)
ICON7_entry3.place(x=250,y=240)
ICON7_entry3.insert(2,"0")
ICON7_entry4 = tk.Entry(window,width = 5)
ICON7_entry4.place(x=300,y=240)
ICON7_entry4.insert(3,"0")
ICON7_entry5 = tk.Entry(window,width = 5)
ICON7_entry5.place(x=350,y=240)
ICON7_entry5.insert(4,"0")

#SCAT欄位
tk.Label(window,text = "SCAT").place(x=10, y=265)
SCAT_entry0 = tk.Entry(window,width = 10)
SCAT_entry0.place(x=60,y=265)
SCAT_entry1 = tk.Entry(window,width = 5)
SCAT_entry1.place(x=150,y=265)
SCAT_entry1.insert(0,"0")
SCAT_entry2 = tk.Entry(window,width = 5)
SCAT_entry2.place(x=200,y=265)
SCAT_entry2.insert(1,"0")
SCAT_entry3 = tk.Entry(window,width = 5)
SCAT_entry3.place(x=250,y=265)
SCAT_entry3.insert(2,"0")
SCAT_entry4 = tk.Entry(window,width = 5)
SCAT_entry4.place(x=300,y=265)
SCAT_entry4.insert(3,"0")
SCAT_entry5 = tk.Entry(window,width = 5)
SCAT_entry5.place(x=350,y=265)
SCAT_entry5.insert(4,"0")

#WILD欄位
tk.Label(window,text = "WILD").place(x=10, y=290)
WILD_entry0 = tk.Entry(window,width = 10)
WILD_entry0.place(x=60,y=290)
WILD_entry1 = tk.Entry(window,width = 5)
WILD_entry1.place(x=150,y=290)
WILD_entry1.insert(0,"0")
WILD_entry2 = tk.Entry(window,width = 5)
WILD_entry2.place(x=200,y=290)
WILD_entry2.insert(1,"0")
WILD_entry3 = tk.Entry(window,width = 5)
WILD_entry3.place(x=250,y=290)
WILD_entry3.insert(2,"0")
WILD_entry4 = tk.Entry(window,width = 5)
WILD_entry4.place(x=300,y=290)
WILD_entry4.insert(3,"0")
WILD_entry5 = tk.Entry(window,width = 5)
WILD_entry5.place(x=350,y=290)
WILD_entry5.insert(4,"0")

#1                                                          #取得輸入的數字
ICON1_entry1_num = int(ICON1_entry1.get())
ICON1_entry2_num = int(ICON1_entry2.get())
ICON1_entry3_num = int(ICON1_entry3.get())
ICON1_entry4_num = int(ICON1_entry4.get())
ICON1_entry5_num = int(ICON1_entry5.get())
#2
ICON2_entry1_num = int(ICON2_entry1.get())
ICON2_entry2_num = int(ICON2_entry2.get())
ICON2_entry3_num = int(ICON2_entry3.get())
ICON2_entry4_num = int(ICON2_entry4.get())
ICON2_entry5_num = int(ICON2_entry5.get())
#3
ICON3_entry1_num = int(ICON3_entry1.get())
ICON3_entry2_num = int(ICON3_entry2.get())
ICON3_entry3_num = int(ICON3_entry3.get())
ICON3_entry4_num = int(ICON3_entry4.get())
ICON3_entry5_num = int(ICON3_entry5.get())
#4
ICON4_entry1_num = int(ICON4_entry1.get())
ICON4_entry2_num = int(ICON4_entry2.get())
ICON4_entry3_num = int(ICON4_entry3.get())
ICON4_entry4_num = int(ICON4_entry4.get())
ICON4_entry5_num = int(ICON4_entry5.get())
#5
ICON5_entry1_num = int(ICON5_entry1.get())
ICON5_entry2_num = int(ICON5_entry2.get())
ICON5_entry3_num = int(ICON5_entry3.get())
ICON5_entry4_num = int(ICON5_entry4.get())
ICON5_entry5_num = int(ICON5_entry5.get())
#6
ICON6_entry1_num = int(ICON6_entry1.get())
ICON6_entry2_num = int(ICON6_entry2.get())
ICON6_entry3_num = int(ICON6_entry3.get())
ICON6_entry4_num = int(ICON6_entry4.get())
ICON6_entry5_num = int(ICON6_entry5.get())
#7
ICON7_entry1_num = int(ICON7_entry1.get())
ICON7_entry2_num = int(ICON7_entry2.get())
ICON7_entry3_num = int(ICON7_entry3.get())
ICON7_entry4_num = int(ICON7_entry4.get())
ICON7_entry5_num = int(ICON7_entry5.get())
#SCAT
SCAT_entry1_num = int(SCAT_entry1.get())
SCAT_entry2_num = int(SCAT_entry2.get())
SCAT_entry3_num = int(SCAT_entry3.get())
SCAT_entry4_num = int(SCAT_entry4.get())
SCAT_entry5_num = int(SCAT_entry5.get())
#WILD
WILD_entry1_num = int(WILD_entry1.get())
WILD_entry2_num = int(WILD_entry2.get())
WILD_entry3_num = int(WILD_entry3.get())
WILD_entry4_num = int(WILD_entry4.get())
WILD_entry5_num = int(WILD_entry5.get())

#計算各輪總個數
#第一輪
wheel1=[]
wheel1.append(ICON1_entry1_num)
wheel1.append(ICON2_entry1_num)
wheel1.append(ICON3_entry1_num)
wheel1.append(ICON4_entry1_num)
wheel1.append(ICON5_entry1_num)
wheel1.append(ICON6_entry1_num)
wheel1.append(ICON7_entry1_num)
wheel1.append(SCAT_entry1_num)
wheel1.append(WILD_entry1_num)
wheel1_sum = sum(wheel1)
#第二輪
wheel2=[]
wheel2.append(ICON1_entry2_num)
wheel2.append(ICON2_entry2_num)
wheel2.append(ICON3_entry2_num)
wheel2.append(ICON4_entry2_num)
wheel2.append(ICON5_entry2_num)
wheel2.append(ICON6_entry2_num)
wheel2.append(ICON7_entry2_num)
wheel2.append(SCAT_entry2_num)
wheel2.append(WILD_entry2_num)
wheel2_sum = sum(wheel2)
#第三輪
wheel3=[]
wheel3.append(ICON1_entry3_num)
wheel3.append(ICON2_entry3_num)
wheel3.append(ICON3_entry3_num)
wheel3.append(ICON4_entry3_num)
wheel3.append(ICON5_entry3_num)
wheel3.append(ICON6_entry3_num)
wheel3.append(ICON7_entry3_num)
wheel3.append(SCAT_entry3_num)
wheel3.append(WILD_entry3_num)
wheel3_sum = sum(wheel3)
#第四輪
wheel4=[]
wheel4.append(ICON1_entry4_num)
wheel4.append(ICON2_entry4_num)
wheel4.append(ICON3_entry4_num)
wheel4.append(ICON4_entry4_num)
wheel4.append(ICON5_entry4_num)
wheel4.append(ICON6_entry4_num)
wheel4.append(ICON7_entry4_num)
wheel4.append(SCAT_entry4_num)
wheel4.append(WILD_entry4_num)
wheel4_sum = sum(wheel4)
#第五輪
wheel5=[]
wheel5.append(ICON1_entry5_num)
wheel5.append(ICON2_entry5_num)
wheel5.append(ICON3_entry5_num)
wheel5.append(ICON4_entry5_num)
wheel5.append(ICON5_entry5_num)
wheel5.append(ICON6_entry5_num)
wheel5.append(ICON7_entry5_num)
wheel5.append(SCAT_entry5_num)
wheel5.append(WILD_entry5_num)
wheel5_sum = sum(wheel5)

#DataFrame
wheel_table = pd.DataFrame({
    "first": wheel1, "second":wheel2, "third":wheel3, "fourth":wheel4, "fivth":wheel5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get(),
                SCAT_entry0.get(),
                WILD_entry0.get() ])

wheelist1 = [ICON1_entry1_num + WILD_entry1_num , ICON2_entry1_num + WILD_entry1_num , ICON3_entry1_num + WILD_entry1_num ,ICON4_entry1_num + WILD_entry1_num,
             ICON5_entry1_num + WILD_entry1_num , ICON6_entry1_num + WILD_entry1_num , ICON7_entry1_num + WILD_entry1_num]
wheelist2 = [ICON1_entry2_num + WILD_entry2_num , ICON2_entry2_num + WILD_entry2_num , ICON3_entry2_num + WILD_entry2_num ,ICON4_entry2_num + WILD_entry2_num,
             ICON5_entry2_num + WILD_entry2_num , ICON6_entry2_num + WILD_entry2_num , ICON7_entry2_num + WILD_entry2_num]
wheelist3 = [ICON1_entry3_num + WILD_entry3_num , ICON2_entry3_num + WILD_entry3_num , ICON3_entry3_num + WILD_entry3_num ,ICON4_entry3_num + WILD_entry3_num,
             ICON5_entry3_num + WILD_entry3_num , ICON6_entry3_num + WILD_entry3_num , ICON7_entry3_num + WILD_entry3_num]
wheelist4 = [ICON1_entry4_num + WILD_entry4_num , ICON2_entry4_num + WILD_entry4_num , ICON3_entry4_num + WILD_entry4_num ,ICON4_entry4_num + WILD_entry4_num,
             ICON5_entry4_num + WILD_entry4_num , ICON6_entry4_num + WILD_entry4_num , ICON7_entry4_num + WILD_entry4_num]
wheelist5 = [ICON1_entry5_num + WILD_entry5_num , ICON2_entry5_num + WILD_entry5_num , ICON3_entry5_num + WILD_entry5_num ,ICON4_entry5_num + WILD_entry5_num,
             ICON5_entry5_num + WILD_entry5_num , ICON6_entry5_num + WILD_entry5_num , ICON7_entry5_num + WILD_entry5_num]

#WILD+各圖案數量
wildsum = pd.DataFrame({
        "轉輪1":wheelist1,
        "轉輪2":wheelist2,
        "轉輪3":wheelist3,
        "轉輪4":wheelist4,
        "轉輪5":wheelist5         
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])

notlist1 = [ wheel1_sum-wheelist1[0], wheel1_sum-wheelist1[1] , wheel1_sum-wheelist1[2], wheel1_sum-wheelist1[3] , wheel1_sum-wheelist1[4] , wheel1_sum-wheelist1[5], wheel1_sum-wheelist1[6]]
notlist2 = [ wheel2_sum-wheelist2[0], wheel2_sum-wheelist2[1] , wheel2_sum-wheelist2[2], wheel2_sum-wheelist2[3] , wheel2_sum-wheelist2[4] , wheel2_sum-wheelist2[5], wheel2_sum-wheelist2[6]]
notlist3 = [ wheel3_sum-wheelist3[0], wheel3_sum-wheelist3[1] , wheel3_sum-wheelist3[2], wheel3_sum-wheelist3[3] , wheel3_sum-wheelist3[4] , wheel3_sum-wheelist3[5], wheel3_sum-wheelist3[6]]
notlist4 = [ wheel4_sum-wheelist4[0], wheel4_sum-wheelist4[1] , wheel4_sum-wheelist4[2], wheel4_sum-wheelist4[3] , wheel4_sum-wheelist4[4] , wheel4_sum-wheelist4[5], wheel4_sum-wheelist4[6]]
notlist5 = [ wheel5_sum-wheelist5[0], wheel5_sum-wheelist5[1] , wheel5_sum-wheelist5[2], wheel5_sum-wheelist5[3] , wheel5_sum-wheelist5[4] , wheel5_sum-wheelist5[5], wheel5_sum-wheelist5[6]]

#非WILD也非各圖案
notwild = pd.DataFrame({
        "非WILD數輪1":notlist1,
        "非WILD數輪2":notlist2,
        "非WILD數輪3":notlist3,
        "非WILD數輪4":notlist4,
        "非WILD數輪5":notlist5
    }, index = [ICON1_entry0.get(),
                ICON2_entry0.get(),
                ICON3_entry0.get(),
                ICON4_entry0.get(),
                ICON5_entry0.get(),
                ICON6_entry0.get(),
                ICON7_entry0.get()
                ])

#輸入資料的按鈕
button1 = tk.Button(window, text = "輸入資料",command = dataimport)                #創建按鈕，設定按鈕名稱，設定按鈕觸發函數
button1.place(x=190,y=320)
#分隔線                                                                            #設置分隔線  版面美觀
tk.Label(window, text = "-"*35+"我是分隔線"+"-"*35).place(x=10,y=350)

#建立輸入提示訊息 (押注額)
tk.Label(window, text = "請輸入各ICON的賠率, 預設為0",
                 font = ("Arial",10), width = 30 , height = 2).place(x=95,y = 370)

#賠率訊息
tk.Label(window, text = "圖案名稱").place(x=70,y=410)
tk.Label(window, text = "1連線").place(x=150,y=410)
tk.Label(window, text = "2連線").place(x=200,y=410)
tk.Label(window, text = "3連線").place(x=250,y=410)
tk.Label(window, text = "4連線").place(x=300,y=410)
tk.Label(window, text = "5連線").place(x=350,y=410)

#欄位1
tk.Label(window,text = "ICON1").place(x=10, y=440)
result1_str = tk.StringVar()
result1_label = tk.Label(window, textvariable=result1_str)
result1_label.place(x=70,y=440)
ICON1_bet1 = tk.Entry(window,width = 5)
ICON1_bet1.place(x=150,y=440)
ICON1_bet1.insert(0,"0")
ICON1_bet2 = tk.Entry(window,width = 5)
ICON1_bet2.place(x=200,y=440)
ICON1_bet2.insert(1,"0")
ICON1_bet3 = tk.Entry(window,width = 5)
ICON1_bet3.place(x=250,y=440)
ICON1_bet3.insert(2,"0")
ICON1_bet4 = tk.Entry(window,width = 5)
ICON1_bet4.place(x=300,y=440)
ICON1_bet4.insert(3,"0")
ICON1_bet5 = tk.Entry(window,width = 5)
ICON1_bet5.place(x=350,y=440)
ICON1_bet5.insert(4,"0")

#欄位2
tk.Label(window,text = "ICON2").place(x=10, y=465)
result2_str = tk.StringVar()
result2_label = tk.Label(window, textvariable=result2_str)
result2_label.place(x=70,y=465)
ICON2_bet1 = tk.Entry(window,width = 5)
ICON2_bet1.place(x=150,y=465)
ICON2_bet1.insert(0,"0")
ICON2_bet2 = tk.Entry(window,width = 5)
ICON2_bet2.place(x=200,y=465)
ICON2_bet2.insert(1,"0")
ICON2_bet3 = tk.Entry(window,width = 5)
ICON2_bet3.place(x=250,y=465)
ICON2_bet3.insert(2,"0")
ICON2_bet4 = tk.Entry(window,width = 5)
ICON2_bet4.place(x=300,y=465)
ICON2_bet4.insert(3,"0")
ICON2_bet5 = tk.Entry(window,width = 5)
ICON2_bet5.place(x=350,y=465)
ICON2_bet5.insert(4,"0")

#欄位3
tk.Label(window,text = "ICON3").place(x=10, y=490)
result3_str = tk.StringVar()
result3_label = tk.Label(window, textvariable=result3_str)
result3_label.place(x=70,y=490)
ICON3_bet1 = tk.Entry(window,width = 5)
ICON3_bet1.place(x=150,y=490)
ICON3_bet1.insert(0,"0")
ICON3_bet2 = tk.Entry(window,width = 5)
ICON3_bet2.place(x=200,y=490)
ICON3_bet2.insert(1,"0")
ICON3_bet3 = tk.Entry(window,width = 5)
ICON3_bet3.place(x=250,y=490)
ICON3_bet3.insert(2,"0")
ICON3_bet4 = tk.Entry(window,width = 5)
ICON3_bet4.place(x=300,y=490)
ICON3_bet4.insert(3,"0")
ICON3_bet5 = tk.Entry(window,width = 5)
ICON3_bet5.place(x=350,y=490)
ICON3_bet5.insert(4,"0")

#欄位4
tk.Label(window,text = "ICON4").place(x=10, y=515)
result4_str = tk.StringVar()
result4_label = tk.Label(window, textvariable=result4_str)
result4_label.place(x=70,y=515)
ICON4_bet1 = tk.Entry(window,width = 5)
ICON4_bet1.place(x=150,y=515)
ICON4_bet1.insert(0,"0")
ICON4_bet2 = tk.Entry(window,width = 5)
ICON4_bet2.place(x=200,y=515)
ICON4_bet2.insert(1,"0")
ICON4_bet3 = tk.Entry(window,width = 5)
ICON4_bet3.place(x=250,y=515)
ICON4_bet3.insert(2,"0")
ICON4_bet4 = tk.Entry(window,width = 5)
ICON4_bet4.place(x=300,y=515)
ICON4_bet4.insert(3,"0")
ICON4_bet5 = tk.Entry(window,width = 5)
ICON4_bet5.place(x=350,y=515)
ICON4_bet5.insert(4,"0")

#欄位5
tk.Label(window,text = "ICON5").place(x=10, y=540)
result5_str = tk.StringVar()
result5_label = tk.Label(window, textvariable=result5_str)
result5_label.place(x=70,y=540)
ICON5_bet1 = tk.Entry(window,width = 5)
ICON5_bet1.place(x=150,y=540)
ICON5_bet1.insert(0,"0")
ICON5_bet2 = tk.Entry(window,width = 5)
ICON5_bet2.place(x=200,y=540)
ICON5_bet2.insert(1,"0")
ICON5_bet3 = tk.Entry(window,width = 5)
ICON5_bet3.place(x=250,y=540)
ICON5_bet3.insert(2,"0")
ICON5_bet4 = tk.Entry(window,width = 5)
ICON5_bet4.place(x=300,y=540)
ICON5_bet4.insert(3,"0")
ICON5_bet5 = tk.Entry(window,width = 5)
ICON5_bet5.place(x=350,y=540)
ICON5_bet5.insert(4,"0")

#欄位6
tk.Label(window,text = "ICON6").place(x=10, y=565)
result6_str = tk.StringVar()
result6_label = tk.Label(window, textvariable=result6_str)
result6_label.place(x=70,y=565)
ICON6_bet1 = tk.Entry(window,width = 5)
ICON6_bet1.place(x=150,y=565)
ICON6_bet1.insert(0,"0")
ICON6_bet2 = tk.Entry(window,width = 5)
ICON6_bet2.place(x=200,y=565)
ICON6_bet2.insert(1,"0")
ICON6_bet3 = tk.Entry(window,width = 5)
ICON6_bet3.place(x=250,y=565)
ICON6_bet3.insert(2,"0")
ICON6_bet4 = tk.Entry(window,width = 5)
ICON6_bet4.place(x=300,y=565)
ICON6_bet4.insert(3,"0")
ICON6_bet5 = tk.Entry(window,width = 5)
ICON6_bet5.place(x=350,y=565)
ICON6_bet5.insert(4,"0")

#欄位7
tk.Label(window,text = "ICON7").place(x=10, y=590)
result7_str = tk.StringVar()
result7_label = tk.Label(window, textvariable=result7_str)
result7_label.place(x=70,y=590)
ICON7_bet1 = tk.Entry(window,width = 5)
ICON7_bet1.place(x=150,y=590)
ICON7_bet1.insert(0,"0")
ICON7_bet2 = tk.Entry(window,width = 5)
ICON7_bet2.place(x=200,y=590)
ICON7_bet2.insert(1,"0")
ICON7_bet3 = tk.Entry(window,width = 5)
ICON7_bet3.place(x=250,y=590)
ICON7_bet3.insert(2,"0")
ICON7_bet4 = tk.Entry(window,width = 5)
ICON7_bet4.place(x=300,y=590)
ICON7_bet4.insert(3,"0")
ICON7_bet5 = tk.Entry(window,width = 5)
ICON7_bet5.place(x=350,y=590)
ICON7_bet5.insert(4,"0")


#欄位SCAT
tk.Label(window,text = "SCAT").place(x=10, y=615)
SCAT_str = tk.StringVar()
SCAT_label = tk.Label(window, textvariable=SCAT_str)
SCAT_label.place(x=70,y=615)
SCAT_bet1 = tk.Entry(window,width = 5)
SCAT_bet1.place(x=150,y=615)
SCAT_bet1.insert(0,"0")
SCAT_bet2 = tk.Entry(window,width = 5)
SCAT_bet2.place(x=200,y=615)
SCAT_bet2.insert(1,"0")
SCAT_bet3 = tk.Entry(window,width = 5)
SCAT_bet3.place(x=250,y=615)
SCAT_bet3.insert(2,"0")
SCAT_bet4 = tk.Entry(window,width = 5)
SCAT_bet4.place(x=300,y=615)
SCAT_bet4.insert(3,"0")
SCAT_bet5 = tk.Entry(window,width = 5)
SCAT_bet5.place(x=350,y=615)
SCAT_bet5.insert(4,"0")

#欄位WILD
tk.Label(window,text = "WILD").place(x=10, y=640)
WILD_str = tk.StringVar()
WILD_label = tk.Label(window, textvariable=WILD_str)
WILD_label.place(x=70,y=640)
WILD_bet1 = tk.Entry(window,width = 5)
WILD_bet1.place(x=150,y=640)
WILD_bet1.insert(0,"0")
WILD_bet2 = tk.Entry(window,width = 5)
WILD_bet2.place(x=200,y=640)
WILD_bet2.insert(1,"0")
WILD_bet3 = tk.Entry(window,width = 5)
WILD_bet3.place(x=250,y=640)
WILD_bet3.insert(2,"0")
WILD_bet4 = tk.Entry(window,width = 5)
WILD_bet4.place(x=300,y=640)
WILD_bet4.insert(3,"0")
WILD_bet5 = tk.Entry(window,width = 5)
WILD_bet5.place(x=350,y=640)
WILD_bet5.insert(4,"0")

#
button1 = tk.Button(window, text = "計算",command = datacalcul)
button1.place(x=200,y=670)



#運行主程式
window.mainloop()