from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_stateNCKUCSIEIntroduction(self, update):
        text = update.message.text
        return text.lower() == 'ncku csie'

    def is_going_to_stateHistory(self, update):
        text = update.message.text
        return text.lower() == 'history'

    def is_going_to_stateProfessor(self, update):
        text = update.message.text
        return text.lower() == 'professor'
    
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '1'
    
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '2'
    
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '3'
    
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '4'
    
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '5'
    
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == '6'
    
    def is_going_to_state7(self, update):
        text = update.message.text
        return text.lower() == '7'
    
    def is_going_to_state8(self, update):
        text = update.message.text
        return text.lower() == '8'
    
    def is_going_to_state9(self, update):
        text = update.message.text
        return text.lower() == '9'
    
    def is_going_to_state10(self, update):
        text = update.message.text
        return text.lower() == '10'
    
    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == '11'
    
    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '12'
    
    def is_going_to_state13(self, update):
        text = update.message.text
        return text.lower() == '13'
    
    def is_going_to_state14(self, update):
        text = update.message.text
        return text.lower() == '14'
    
    def is_going_to_state15(self, update):
        text = update.message.text
        return text.lower() == '15'
    
    def is_going_to_state16(self, update):
        text = update.message.text
        return text.lower() == '16'
    
    def is_going_to_state17(self, update):
        text = update.message.text
        return text.lower() == '17'
    
    def is_going_to_state18(self, update):
        text = update.message.text
        return text.lower() == '18'
    
    def is_going_to_state19(self, update):
        text = update.message.text
        return text.lower() == '19'
    
    def is_going_to_state20(self, update):
        text = update.message.text
        return text.lower() == '20'
    
    def is_going_to_state21(self, update):
        text = update.message.text
        return text.lower() == '21'
    
    def is_going_to_state22(self, update):
        text = update.message.text
        return text.lower() == '22'
    
    def is_going_to_state23(self, update):
        text = update.message.text
        return text.lower() == '23'
    
    def is_going_to_state24(self, update):
        text = update.message.text
        return text.lower() == '24'
    
    def is_going_to_state25(self, update):
        text = update.message.text
        return text.lower() == '25'
    
    def is_going_to_state26(self, update):
        text = update.message.text
        return text.lower() == '26'
    
    def is_going_to_state27(self, update):
        text = update.message.text
        return text.lower() == '27'
    
    def is_going_to_state28(self, update):
        text = update.message.text
        return text.lower() == '28'
    
    def is_going_to_state29(self, update):
        text = update.message.text
        return text.lower() == '29'
    
    def is_going_to_state30(self, update):
        text = update.message.text
        return text.lower() == '30'
    
    def is_going_to_state31(self, update):
        text = update.message.text
        return text.lower() == '31'
    
    def is_going_to_state32(self, update):
        text = update.message.text
        return text.lower() == '32'
    
    def is_going_to_state33(self, update):
        text = update.message.text
        return text.lower() == '33'
    
    def is_going_to_state34(self, update):
        text = update.message.text
        return text.lower() == '34'
    
    def is_going_to_state35(self, update):
        text = update.message.text
        return text.lower() == '35'
    
    def is_going_to_state36(self, update):
        text = update.message.text
        return text.lower() == '36'
    
    def is_going_to_state37(self, update):
        text = update.message.text
        return text.lower() == '37'
    
    def is_going_to_state38(self, update):
        text = update.message.text
        return text.lower() == '38'
    
    def is_going_to_state39(self, update):
        text = update.message.text
        return text.lower() == '39'
    
    def is_going_to_state40(self, update):
        text = update.message.text
        return text.lower() == '40'
    
    def is_going_to_state41(self, update):
        text = update.message.text
        return text.lower() == '41'
    
    def is_going_to_state42(self, update):
        text = update.message.text
        return text.lower() == '42'
    
    def is_going_to_statePsychologicalTest(self, update):
        text = update.message.text
        return text.lower() == 'test'

    def is_going_to_stateLove(self, update):
        text = update.message.text
        return text.lower() == 'love'
    
    def is_going_to_stateLoveA(self, update):
        text = update.message.text
        return text.lower() == 'a'
        
    def is_going_to_stateLoveB(self, update):
        text = update.message.text
        return text.lower() == 'b'
        
    def is_going_to_stateLoveC(self, update):
        text = update.message.text
        return text.lower() == 'c'
        
    def is_going_to_stateLoveD(self, update):
        text = update.message.text
        return text.lower() == 'd'
        
    def is_going_to_stateLoveE(self, update):
        text = update.message.text
        return text.lower() == 'e'
    
    def is_going_to_statePersonality(self, update):
        text = update.message.text
        return text.lower() == 'personality'

    def is_going_to_statePersonalityA(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_statePersonalityB(self, update):
        text = update.message.text
        return text.lower() == 'b'

    def is_going_to_statePersonalityC(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def is_going_to_statePersonalityD(self, update):
        text = update.message.text
        return text.lower() == 'd'

    def is_going_to_stateWork(self, update):
        text = update.message.text
        return text.lower() == 'work'

    def is_going_to_stateWorkA(self, update):
        text = update.message.text
        return text.lower() == 'a'

    def is_going_to_stateWorkB(self, update):
        text = update.message.text
        return text.lower() == 'wb'

    def is_going_to_stateWorkC(self, update):
        text = update.message.text
        return text.lower() == 'c'

    def is_going_to_stateWorkD(self, update):
        text = update.message.text
        return text.lower() == 'd'
    
    def is_going_to_stateChat(self, update):
        text = update.message.text
        return text.lower() == 'chat'

    def is_going_to_stateChat1(self, update):
        text = update.message.text
        return text.lower() == 'hi'

    def is_going_to_stateChat2(self, update):
        text = update.message.text
        return text.lower() == 'good'

    def is_going_to_stateChat3(self, update):
        text = update.message.text
        return text.lower() == 'yes'

    def is_going_to_stateChat4(self, update):
        text = update.message.text
        return text.lower() == 'no'

    def is_going_to_stateJoke(self, update):
        text = update.message.text
        return text.lower() == 'joke'

    def is_going_to_stateJokeNormal(self, update):
        text = update.message.text
        return text.lower() == 'normal'

    def is_going_to_stateJokeTurbo(self, update):
        text = update.message.text
        return text.lower() == 'turbo'

    def on_enter_stateNCKUCSIEIntroduction(self, update):
        update.message.reply_text("history or professor")
        #self.go_back(update)

    def on_exit_stateNCKUCSIEIntroduction(self, update):
        print('Leaving stateNCKUCSIEIntroduction')

    def on_enter_stateHistory(self, update):
        update.message.reply_text("系所歷史與沿革\n本系為南台灣第一個純以資訊及計算機工程為重心的高級學術單位， 於民國七十六年八月成立碩士班，八十一年八月成立博士班， 於八十六年八月成立大學部，九十一年八月擴增大學部為兩班， 並於九十五學年度再增設醫學資訊研究所，一百年八月製造資訊與系統研究所整合至本系，以一系三所之模式進行。\n為因應國內高科技產業人力需求， 每位教授及研究生均積極參與國內外學術活動，並在高水準的期刊及會議上發表研究成果， 並有多位教授獲得學術榮譽如國科會傑出研究獎等獎項。")
        self.go_back(update)

    def on_exit_stateHistory(self, update):
        print('Leaving stateHistory')

    def on_enter_stateProfessor(self, update):
        update.message.reply_text("1.高宏宇\n2.連震杰\n3.李同益\n4.鄭芳田\n5.吳宗憲\n6.孫永年\n7.黃崇明\n8.謝孫源\n9.黃宗立\n10.郭耀煌\n11.陳裕民\n12.蔣榮先\n13.陳培殷\n14.李強\n15.陳響亮\n16.鄭憲宗\n17.楊大和\n18.蘇文鈺\n19.張燕光\n20.郭淑美\n21.王士豪\n22.蘇銓清\n23.蕭宏章\n24.張大緯\n25.梁勝富\n26.許靜芳\n27.盧文祥\n28.楊中平\n29.藍崑展\n30.林英超\n31.吳明龍\n32.陳朝鈞\n33.李家岩\n34.趙梓程\n35.蔡孟勳\n36.莊坤達\n37.蔡佩璇\n38.胡敏君\n39.涂嘉恒\n40.李信杰\n41.張瑞紘\n42.黃敬群\nexit")
        #self.go_back(update)

    def on_exit_stateProfessor(self, update):
        print('Leaving stateProfessor')

    def on_enter_state1(self, update):
        update.message.reply_text("高宏宇 教授 兼 代理系主任 兼 醫資所所長\n\n專長及研究領域:\n資訊檢索/資訊擷取、資料探勘、機器學習、全球資訊網資訊系統、生物資訊、社群網路計算\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62546\n\nE-mail：\nhykao@mail.ncku.edu.tw\n\n實驗室：\n智慧型知識管理實驗室 (資訊系館新大樓9F 65903)\n\n個人網頁：\nhttp://myweb.ncku.edu.tw/~hykao/\n")
        self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')
    
    def on_enter_state2(self, update):
        update.message.reply_text("連震杰 教授 兼 副系主任 兼 製造所所長\n\n專長及研究領域:\n智慧型機器人及自動化、人機互動及擴增實境、3D自動光學檢測、視覺伺服控制、影像處理,3D電腦視覺及圖形辨識、機器學習、嵌入式系統、雲端智慧型監控服務\n\n系所別：\n資訊系 / 資訊所 / 製造所\n\n電話：\n06-2757575 ext 62540\n\nE-mail：\njjlien@csie.ncku.edu.tw\n\n實驗室：\n機器人實驗室 (資訊系館新大樓9F 65904)")
        self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')
    
    def on_enter_state3(self, update):
        update.message.reply_text("李同益 講座教授\n\n專長及研究領域:\n3D遊戲設計 (3D Game Design)、3D NPR動畫合成(3D Non-photo-realistic rendering)、電腦繪圖與動畫(Computer Graphics and Animation)、電腦視覺化模擬(Visualization)、虛擬實境與環境(Virtual Reality and Environment)、醫學手術模擬系統(3D Medical Surgical Simulation and Application)、Video/Image Retargeting、3D Captcha Design for Internet Security\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62531\n\nE-mail：\ntonylee@mail.ncku.edu.tw\n\n實驗室：\n電腦繪圖研究群/視覺系統實驗室 (資訊系館新大樓7F 65701)")
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')
    
    def on_enter_state4(self, update):
        update.message.reply_text("鄭芳田 講座教授\n\n專長及研究領域:\nE化製造 (工業4.0)、半導體生產自動化、虛擬量測、預測保養、智慧型製造系統\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34224\n\nE-mail：\nchengft@mail.ncku.edu.tw\n\n實驗室：\n自動化實驗室 (自強校區儀器設備大樓95619)\n\n個人網頁：\nhttp://super.ime.ncku.edu.tw/pages/teacher.htm")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')
    
    def on_enter_state5(self, update):
        update.message.reply_text("吳宗憲 講座教授\n\n專長及研究領域:\n人工智慧與深度學習、語音與語者識別、語音合成與變音、口述語言對話與理解、多媒體情緒辨識與追蹤、影音多媒體摘要與檢索、聽語障口/手語學習輔具、電腦輔助口說語言學習、多媒體人機互動\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n電話：06-2757575 ext 62521\n\nE-mail：\nchunghsienwu@gmail.com; chwu@csie.ncku.edu.tw\n\n實驗室：\n多媒體人機通訊實驗室 (資訊系館新大樓8F 65801)\n\n個人網頁：\nhttp://chinese.csie.ncku.edu.tw/web_tw/professor/")
        self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')
    
    def on_enter_state6(self, update):
        update.message.reply_text("孫永年 特聘教授\n\n專長及研究領域:\n影像處理、電腦視覺、醫學影像、工業檢測、醫學資訊、視訊科學、虛擬環境\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62526\n\nE-mail：\nynsun@mail.ncku.edu.tw\n\n實驗室：\n視覺系統實驗室 (資訊系館新大樓7F 65702)")
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
    
    def on_enter_state7(self, update):
        update.message.reply_text("黃崇明 特聘教授\n\n專長及研究領域:\n無線及行動網路和協定設計與分析、多媒體處理和串流技術、綠色通訊與計算、創意網路應用與服務\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62523\n\nE-mail：\nhuangcm@locust.csie.ncku.edu.tw\ncmdhuang@gmail.com\n\n實驗室：\n多媒體行動電腦網路實驗室 (資訊系館新大樓3F 65303)")
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
    
    def on_enter_state8(self, update):
        update.message.reply_text("謝孫源 特聘教授 兼 研發長\n\n專長及研究領域:\n容錯計算、生物資訊、平行及分散式計算、演算法設計與分析、圖形理論\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62538\n\nE-mail：\nhsiehsy@mail.ncku.edu.tw\n\n實驗室：\n互連網路暨高效率計算實驗室 (資訊系館新大樓8F 65803)\n\n個人網頁：\nhttp://algorithm.csie.ncku.edu.tw/syhsieh.htm")
        self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')
    
    def on_enter_state9(self, update):
        update.message.reply_text("黃宗立 特聘教授\n\n專長及研究領域:\n密碼技術、網路安全、資訊安全、門禁系統、錯誤控制碼、量子密碼學\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62524\n\nE-mail：\nhwangtl@csie.ncku.edu.tw\n\n實驗室：\n量子資訊與網路安全實驗室 (資訊系館新大樓6F 65603)")
        self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')
    
    def on_enter_state10(self, update):
        update.message.reply_text("郭耀煌 特聘教授\n\n專長及研究領域:\n嵌入式系統與應用、感測網路與隨意計算、寬頻網路系統、智慧型資訊系統、網際網路服務、物件導向式設計、模糊系統、知識庫系統、系統晶片設計、人工智慧、情境感知、數位家庭\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62522\n\nE-mail：\nkuoyh@ismp.csie.ncku.edu.tw\n\n實驗室：\n智慧型系統暨媒體處理實驗室 (資訊系館新大樓5F 65507)")
        self.go_back(update)

    def on_exit_state10(self, update):
        print('Leaving state10')
    
    def on_enter_state11(self, update):
        update.message.reply_text("陳裕民 特聘教授\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34222\n\nE-mail：\nymchen@mail.ncku.edu.tw\n\n實驗室：\n企業工程與整合實驗室 (自強校區儀器設備大樓95604)")
        self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11')
    
    def on_enter_state12(self, update):
        update.message.reply_text("蔣榮先 特聘教授 兼 計算機與網路中心主任\n\n專長及研究領域:\n生醫資訊探勘、人工智慧、智慧型計算、雲端醫療照護、癌症與幹細胞研究、巨量資料分析、手持穿戴裝置行動計算\n\n系所別：\n資訊系 / 資訊所 / 醫資所 / 計網中心\n\n電話：\n06-2757575 ext 62534\n\nE-mail：\njchiang@mail.ncku.edu.tw\n\n實驗室：\n智慧型資訊擷取實驗室 (資訊系館新大樓6F 65604)")
        self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')
    
    def on_enter_state13(self, update):
        update.message.reply_text("陳培殷 特聘教授 兼 電資學院副院長\n\n專長及研究領域:\nVLSI電路/FPGA晶片設計、人工智慧AI影像處理與應用、資訊系統開發、嵌入式系統開發設計\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62547\n\nE-mail：\npychen@mail.ncku.edu.tw\n\n實驗室：\n數位晶片設計實驗室 (資訊系館新大樓10F 65A01)")
        self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')
    
    def on_enter_state14(self, update):
        update.message.reply_text("李強 教授\n\n專長及研究領域:\n大數據/巨量資料處理技術、社群網站/雲端平行計算、地理資訊系統、網際網路資料庫與處理技術\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62528\n\nE-mail：\nleec@mail.ncku.edu.tw\n\n實驗室：\n高等資料系統(ADS)實驗室 (資訊系館新大樓3F 65302)")
        self.go_back(update)

    def on_exit_state14(self, update):
        print('Leaving state14')
    
    def on_enter_state15(self, update):
        update.message.reply_text("陳響亮 教授\n\n專長及研究領域:\n資訊與機電整合、智慧型遠端監控系統、C#物件導向程式設計、PC-based 多軸控制器設計、自動化光學檢測、CAD/CAM、雲端服務系統\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 61001\n\nE-mail：\nslchen@mail.ncku.edu.tw\n\n實驗室：\n資訊與機電整合實驗室 (自強校區儀器設備大樓95507)\n\n個人網頁：\nhttp://140.116.86.180")
        self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')
    
    def on_enter_state16(self, update):
        update.message.reply_text("鄭憲宗 教授\n\n專長及研究領域:\n雲端計算,行動裝置App研究與開發,無線通訊, 行動計算, 數位生活科技, 量子計算與通訊, 電腦網路\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62529\n\nE-mail：\nstcheng@mail.ncku.edu.tw\n\n實驗室：\n塵間感知與雲端計算實驗室 (資訊系館新大樓6F 65607)")
        self.go_back(update)

    def on_exit_state16(self, update):
        print('Leaving state16')
    
    def on_enter_state17(self, update):
        update.message.reply_text("楊大和 教授\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34225\n\nE-mail：\ntyang@mail.ncku.edu.tw\n\n實驗室：\n製造管理實驗室 (自強校區儀器設備大樓95623)")
        self.go_back(update)

    def on_exit_state17(self, update):
        print('Leaving state17')
    
    def on_enter_state18(self, update):
        update.message.reply_text("蘇文鈺 教授\n\n專長及研究領域:\n數位音訊處理、影像視訊處理與壓縮、電腦音樂分析合成、文件影像處理、媒體處理機設計、MPEG-4多媒體標準、數位訊號處理用SoC\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62537\n\nE-mail：\nalvinsu@mail.ncku.edu.tw\n\n實驗室：\n音樂多媒體系統實驗室 (資訊系館新大樓7F 65707)")
        self.go_back(update)

    def on_exit_state18(self, update):
        print('Leaving state18')
    
    def on_enter_state19(self, update):
        update.message.reply_text("張燕光 教授\n\n專長及研究領域:\nRouter & Switch Design、Scalable Web Server、Cooperative Web Proxy、QoS、Network Processor Design、Computer Architecture、Multiprocessor Network and Cache Coherence Design、Fault-Tolerant\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62539\n\nE-mail：\nykchang@mail.ncku.edu.tw\n\n實驗室：\n計算機網路架構實驗室 (資訊系館新大樓5F 65502)\n\n個人網頁：\nhttp://cial.csie.ncku.edu.tw/")
        self.go_back(update)

    def on_exit_state19(self, update):
        print('Leaving state19')
    
    def on_enter_state20(self, update):
        update.message.reply_text("郭淑美 教授\n\n專長及研究領域:\n影像處理、醫療影像處理、進化計算論、渾沌系統應用、模糊理論、系統工程\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62525\n\nE-mail：\nguosm@mail.ncku.edu.tw\n\n實驗室：\n智慧型數位影像處理實驗室 (資訊系館新大樓4F 65403)")
        self.go_back(update)

    def on_exit_state20(self, update):
        print('Leaving state20')
    
    def on_enter_state21(self, update):
        update.message.reply_text("王士豪 教授 兼 成大醫院資訊室主任\n\n專長及研究領域:\n超音波訊號及成像技術、超音波鑑別生物組織與材料、醫用物聯網與機器學習、訊號與影像處理、醫學與健康照護資訊、醫療器材\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62519\n\nE-mail：\nshyhhau@mail.ncku.edu.tw\n\n實驗室：\n生醫超音波系統實驗室 (資訊大樓8樓) (資訊系館新大樓8F 65804)")
        self.go_back(update)

    def on_exit_state21(self, update):
        print('Leaving state21')
    
    def on_enter_state22(self, update):
        update.message.reply_text("蘇銓清 教授\n\n專長及研究領域:\n光接取網路、多波長分波多工光纖網路、無線感測網路、網際網路電視系統\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62543\n\nE-mail：\nsuecc@mail.ncku.edu.tw\n\n實驗室：\n可靠計算及網路實驗室 (資訊系館新大樓7F 65703)")
        self.go_back(update)

    def on_exit_state22(self, update):
        print('Leaving state22')
    
    def on_enter_state23(self, update):
        update.message.reply_text("蕭宏章 教授\n\n專長及研究領域:\n巨量資料儲存體與計算平台、Apache開源專案、平行暨分散式計算、雲端計算、同儕網路\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62548\n\nE-mail：\nhchsiao@csie.ncku.edu.tw\n\n實驗室：\n分散式計算實驗室 (資訊系館新大樓10F 65A03)")
        self.go_back(update)

    def on_exit_state23(self, update):
        print('Leaving state23')
    
    def on_enter_state24(self, update):
        update.message.reply_text("張大緯 教授\n\n專長及研究領域:\n容錯機制、作業系統、虛擬機器、嵌入式系統\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62551\n\nE-mail：\ndavidchang@csie.ncku.edu.tw\n\n實驗室：\n作業系統與嵌入式系統實驗室 (資訊系館新大樓4F 65409)\n\n個人網頁：\nhttp://140.116.247.213/")
        self.go_back(update)

    def on_exit_state24(self, update):
        print('Leaving state24')
    
    def on_enter_state25(self, update):
        update.message.reply_text("梁勝富 教授\n\n專長及研究領域:\n智慧型科技及其應用、神經認知腦機界面、生醫訊號處理、可攜式嵌入式系統、多媒體訊號與系統\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62549\n\nE-mail：\nsfliang@mail.ncku.edu.tw\n\n個人網頁：\nncbci.csie.ncku.edu.tw")
        self.go_back(update)

    def on_exit_state25(self, update):
        print('Leaving state25')
    
    def on_enter_state26(self, update):
        update.message.reply_text("許靜芳 副教授\n\n專長及研究領域:\n光波分割多工網路、繞徑策略設計、網際網路通訊協定\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62535\n\nE-mail：\nhsucf@csie.ncku.edu.tw\n\n實驗室：\n高速網路實驗室 (資訊系館新大樓5F 65503)")
        self.go_back(update)

    def on_exit_state26(self, update):
        print('Leaving state26')
    
    def on_enter_state27(self, update):
        update.message.reply_text("盧文祥 副教授\n\n專長及研究領域:\n文件探勘、網路探勘、資訊檢索、自然語言處理、機器翻譯、跨語知識系統、數位典藏、醫學資訊檢索\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62545\n\nE-mail：\nwhlu@mail.ncku.edu.tw\n\n實驗室：\n網路探勘暨跨語知識系統實驗室 (資訊系館新大樓8F 65802)")
        self.go_back(update)

    def on_exit_state27(self, update):
        print('Leaving state27')
    
    def on_enter_state28(self, update):
        update.message.reply_text("楊中平 副教授\n\n專長及研究領域:\nMicroprocessor Architecture and Interface、Real-time Embedded System、Virtual Instrumentation\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62533\n\nE-mail：\ndryncku@gmail.com\n\n實驗室：\n聯網型嵌入式應用與技術實驗室 (資訊系館新大樓4F 65402)")
        self.go_back(update)

    def on_exit_state28(self, update):
        print('Leaving state28')
    
    def on_enter_state29(self, update):
        update.message.reply_text("藍崑展 副教授\n\n專長及研究領域:\n車載網路, 感測網路, 物聯網, 預防醫學大資料分析, 雲端照護, 中醫電腦化(自動診斷. 無痛針灸, 智慧處方系\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62550\n\nE-mail：\nklan@csie.ncku.edu.tw\n\n實驗室：\n精準醫療與網路系統實驗室 (資訊系館新大樓5F 65501)\n\n個人網頁：\nhttp://www.csie.ncku.edu.tw/~klan/")
        self.go_back(update)

    def on_exit_state29(self, update):
        print('Leaving state29')
    
    def on_enter_state30(self, update):
        update.message.reply_text("林英超 副教授\n\n專長及研究領域:\n計算機結構、可靠節能系統設計、電子設計自動化、嵌入式系統設計、超大型積體電路/系統單晶片設計 、物聯網系統及架構、記憶體系統及架構、數位系統設計、異質運算系統及架構設計\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62553\n\nE-mail：\niclin@csie.ncku.edu.tw\n\n實驗室：\n電腦架構與晶片設計實驗室 (資訊系館新大樓10F 65A02)\n\n個人網頁：\nhttps://sites.google.com/a/caid.tw/iclin/")
        self.go_back(update)

    def on_exit_state30(self, update):
        print('Leaving state30')
    
    def on_enter_state31(self, update):
        update.message.reply_text("吳明龍 副教授\n\n專長及研究領域:\n生醫影像處理、平行計算、核磁共振影像成像技術、大腦功能性磁振造影、核磁共振脈衝序列設計、機器學習、資料科學\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62541\n\nE-mail：\nminglong.wu@csie.ncku.edu.tw\n\n實驗室：\n生醫影像實驗室 (資訊系館新大樓9F 65902)")
        self.go_back(update)

    def on_exit_state31(self, update):
        print('Leaving state31')
    
    def on_enter_state32(self, update):
        update.message.reply_text("陳朝鈞 副教授\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34226\n\nE-mail：\nchaochun@mail.ncku.edu.tw\n\n實驗室：\n製造與行動資料庫實驗室 (自強校區儀器設備大樓95508)")
        self.go_back(update)

    def on_exit_state32(self, update):
        print('Leaving state32')
    
    def on_enter_state33(self, update):
        update.message.reply_text("李家岩 副教授\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34223\n\nE-mail：\ncylee@mail.ncku.edu.tw\n\n實驗室：\n生產力最佳化實驗室")
        self.go_back(update)

    def on_exit_state33(self, update):
        print('Leaving state33')
    
    def on_enter_state34(self, update):
        update.message.reply_text("趙梓程 副教授\n\n專長及研究領域:\n醫學影像與數位影像處理、計算神經學、磁振造影技術、磁振造影加速演算法、分子系統模擬\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext\n\nE-mail：\ntcchao@mail.ncku.edu.tw\n\n實驗室：\n醫學影像處理實驗室 (資訊系館新大樓4F 65401)")
        self.go_back(update)

    def on_exit_state34(self, update):
        print('Leaving state34')
    
    def on_enter_state35(self, update):
        update.message.reply_text("蔡孟勳 副教授\n\n專長及研究領域:\n網路效能評估、行動網路設計與分析、網際網路電話、行動計算、行動網路與網際網路整合\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62518\n\nE-mail：\ntsaimh@csie.ncku.edu.tw\n\n實驗室：\n智慧化行動服務實驗室 (資訊系館新大樓10F 65A04)\n\n個人網頁：\nhttp://imslab.org/~tsaimh/")
        self.go_back(update)

    def on_exit_state35(self, update):
        print('Leaving state35')
    
    def on_enter_state36(self, update):
        update.message.reply_text("莊坤達 助理教授\n\n專長及研究領域:\n資料探勘、資料庫系統、行動運算、網路資訊系統\n\n系所別：\n資訊系 / 資訊所 / 醫資所\n\n電話：\n06-2757575 ext 62556\n\nE-mail：\nktchuang@mail.ncku.edu.tw\n\n實驗室：\n前瞻網路資料庫實驗室 (資訊系館新大樓6F 65602)\n\n個人網頁：\nhttp://cv_ktchuang.cannerapp.com/")
        self.go_back(update)

    def on_exit_state36(self, update):
        print('Leaving state36')
    
    def on_enter_state37(self, update):
        update.message.reply_text("蔡佩璇 助理教授\n\n專長及研究領域:\n即時定位與導航服務、智慧型系統與應用程式開發、影像壓縮與即時傳輸、即時排程理論、使用者介面結構設計、健康看護應用及個人設備\n\n系所別：\n資訊系 / 製造所\n\n電話：\n06-2757575 ext 34228\n\nE-mail：\nphtsai@mail.ncku.edu.tw\n\n實驗室：\n資訊系統與應用實驗室 (自強校區儀器設備大樓95508)")
        self.go_back(update)

    def on_exit_state37(self, update):
        print('Leaving state37')
    
    def on_enter_state38(self, update):
        update.message.reply_text("胡敏君 助理教授\n\n專長及研究領域:\n多媒體資訊系統、雲端多媒體計算、電腦視覺與圖形識別、機器學習、電腦圖學、虛擬實境與擴增實境技術應用\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62557\n\nE-mail：\nanita_hu@mail.ncku.edu.tw\n\n實驗室：\n多媒體資訊系統實驗室 (資訊系館新大樓6F 65601)\n\n個人網頁：\nhttp://mislab.csie.ncku.edu.tw/trimy")
        self.go_back(update)

    def on_exit_state38(self, update):
        print('Leaving state38')
    
    def on_enter_state39(self, update):
        update.message.reply_text("涂嘉恒 助理教授\n\n專長及研究領域:\n異質平行計算、嵌入式系統設計與最佳化、編譯器設計\n\n系所別：\n資訊系 / 資訊所\n\n電話：\n06-2757575 ext 62527\n\nE-mail：\nchiaheng@mail.ncku.edu.tw\n\n實驗室：\n前瞻系統研究實驗室 (資訊系館新大樓7F 65708)\n\n個人網頁：\nhttp://chiaheng.wordpress.com")
        self.go_back(update)

    def on_exit_state39(self, update):
        print('Leaving state39')
    
    def on_enter_state40(self, update):
        update.message.reply_text("李信杰 副教授\n\n專長及研究領域:\n軟體工程、網頁自動化測試、服務導向架構、程式碼分析、軟體代理人\n\n系所別：\n資訊系 / 資訊所 / 計網中心\n\n電話：\n06-2757575 ext 61035\n\nE-mail：\njielee@mail.ncku.edu.tw\n\n實驗室：\n軟體工程實驗室 (資訊系館新大樓9F 65912)")
        self.go_back(update)

    def on_exit_state40(self, update):
        print('Leaving state40')
    
    def on_enter_state41(self, update):
        update.message.reply_text("張瑞紘 助理教授\n\n專長及研究領域:\n資料挖掘、雲端運算平台應用、資料庫管理、系統分析與設計、數位學習系統、程式設計與撰寫、程式設計與撰寫\n\n系所別：\n資訊系 / 資訊所 / 計網中心\n\n電話：\n06-2757575 ext 61053\n\nE-mail：\nchangrh@mail.ncku.edu.tw\n\n實驗室：\n創新系統軟體應用實驗室 (資訊系館新大樓9F 65912)")
        self.go_back(update)

    def on_exit_state41(self, update):
        print('Leaving state41')
    
    def on_enter_state42(self, update):
        update.message.reply_text("黃敬群 業界專家 兼 助理教授\n\n專長及研究領域:\n作業系統、嵌入式系統、消費性電子產品\n\n系所別：\n資訊系\n\n電話：\n06-2757575 ext 62542\n\nE-mail：\njserv.tw@gmail.com\n\n個人網頁：\nhttp://wiki.csie.ncku.edu.tw/User/jserv")
        self.go_back(update)

    def on_exit_state42(self, update):
        print('Leaving state42')
    
    def on_enter_statePsychologicalTest(self, update):
        update.message.reply_text("love or personality or work")
        #self.go_back(update)

    def on_exit_statePsychologicalTest(self, update):
        print('Leaving statePsychologicalTest')

    def on_enter_stateLove(self, update):
        update.message.reply_text("你走在森林中，突然愛神維納斯出現，祂要送你一款愛情糖果，你覺得他送你的是下面哪一款？\na、紅白條紋糖\nb、彩色鑽石糖\nc、七彩星星糖\nd、白色方糖\ne、橘色圓形糖")
        self.go_back(update)

    def on_exit_stateLove(self, update):
        print('Leaving stateLove')
    
    def on_enter_stateLoveA(self, update):
        update.message.reply_text("a、你的必修課題是「放下矜持與面子」\n你喜歡一個人很明顯，眼光總是追著對方在轉，每每開口都是與對方有關的話題，然而碰到你不喜歡的人，你也不會浪費時間在他身上。對於你有好感的對象，你卻不一定有勇氣告白，總是一再試探對方的感覺，就怕自己表錯情。\n愛面子沒有錯，但你戀愛時也會因為太愛面子而不願意承認錯誤。個性活潑的你，其實不缺戀愛機會。千萬不要將就在沒有心動的關係，挑選與你勢均力敵的對象，才能彰顯你耀眼的特質。")
        self.go_back(update)

    def on_exit_stateLoveA(self, update):
        print('Leaving stateLoveA')
    
    def on_enter_stateLoveB(self, update):
        update.message.reply_text("b、你的必修課題是「學習放下武裝與面具」\n你是個多愁善感的人，在感情中受過不少傷害（童年不受重視的陰影、青少年同儕的爭執排擠），導致現在的你對愛情缺乏信心。為了保護自己武裝成尖銳、難以捉摸的人。其實你的內心是單純而渴望愛的，偏偏你老是愛上與你不同世界的人，讓你陷入無止境的猜心遊戲。\n最後，你只好流連於曖昧關係，心軟脆弱的你，因為害怕寂寞，心裡面其實沒有安全感卻又捨不得放手，導致自己不斷輪迴。是該讓自己解脫的時候了，抽身，其實比你想的還容易。")
        self.go_back(update)

    def on_exit_stateLoveB(self, update):
        print('Leaving stateLoveB')
    
    def on_enter_stateLoveC(self, update):
        update.message.reply_text("c、你的必修課題是「放下對感情的理想化，找回平衡感」\n你對於愛情抱持著太美好的憧憬，你渴望另一半可以徹底了解你的想法，所以當兩人因為某些事而意見不合時，你會感到非常沮喪。然而，在同樣生長環境下的姐妹都有意見不合的時候，更何況是一個生長家庭、環境都不同的人。\n你需要在夢想與現實間求得平衡、學習在黏膩的關係中，找回獨處時的平靜。當你學會寬宥自己與對方，你將會感受到更自在的情感關係。")
        self.go_back(update)

    def on_exit_stateLoveC(self, update):
        print('Leaving stateLoveC')
    
    def on_enter_stateLoveD(self, update):
        update.message.reply_text("d、你的必修課題是「找回對自己的自信」\n你根本還沒準備好談戀愛，又或是對戀愛心存恐懼，害怕自己沒資格被愛，怕自己都照顧不好自己了，如何去對別人好？你的問題在於對自己缺乏自信，習慣把事情想的太悲觀來嚇自己。\n回想一下你所擔心過的事，是否有許多不曾發生、讓自己白擔心一場呢？那麽，你還在擔心什麽呢？勇敢去愛吧。相信自己值得被愛，你也有能力去愛別人。")
        self.go_back(update)

    def on_exit_stateLoveD(self, update):
        print('Leaving stateLoveD')
    
    def on_enter_stateLoveE(self, update):
        update.message.reply_text("e、你的必修課題是「學會獨立，放下害怕被忽略的感受」\n在愛情面前，你還是個孩子，貪玩、任性、依賴。單身時，你依賴你的家人、你的閨蜜；談戀愛、結婚後，依賴你的另一半。好奇的你喜歡問「為什麽？」得不到滿意的答案便自顧自的生氣。不喜歡被對方忽略的感覺，卻常因為專注在自己的興趣而忽略對方。\n愛上你得有照顧孩子的心理準備。你要學會的，是獨立，不要擔心另一半這一刻沒想你，就會把你忘記。要知道，愛一個人是放在心上，而不是掛在嘴邊。")
        self.go_back(update)

    def on_exit_stateLoveE(self, update):
        print('Leaving stateLoveE')

    def on_enter_statePersonality(self, update):
        update.message.reply_text("如果要你隨身攜帶「幸運符」，你會把它放在哪裡，以保佑你平安呢？\na、放在內衣裡\nb、放在隨身的包包中\nc、掛在手機上\nd、當成項鍊或手鍊掛在身上")
        #self.go_back(update)

    def on_exit_statePersonality(self, update):
        print('Leaving statePersonality')

    def on_enter_statePersonalityA(self, update):
        update.message.reply_text("a、緊張大師指數：100% \n你是大夥人眼中的緊張大師！只要你一緊張起來，臉色就跟著難看，身旁的人都會感受到你的緊張氣氛。因為你的個性急，遇上狀況急著快快解決，而未能思考完善就行動，反而會陷入另一個麻煩中。")
        self.go_back(update)

    def on_exit_statePersonalityA(self, update):
        print('Leaving statePersonalityA')

    def on_enter_statePersonalityB(self, update):
        update.message.reply_text("b、緊張大師指數：50% \n你不會過於緊張，因為任何事情對你來說，都是有解決方法的，與其花費太多時間，讓自己陷入焦慮痛苦的狀態，不如老神在在，等到事情發生再去思考。")
        self.go_back(update)

    def on_exit_statePersonalityB(self, update):
        print('Leaving statePersonalityB')

    def on_enter_statePersonalityC(self, update):
        update.message.reply_text("c、緊張大師指數：20% \n你神經算有些大條，有時候事情大家都知道了，你才恍然大悟，可以說常在狀況外。但你卻很容易受人影響，只要親朋好友緊張兮兮地找你商量事情，即使你還搞不清楚狀況，也跟著一起窮緊張！")
        self.go_back(update)

    def on_exit_statePersonalityC(self, update):
        print('Leaving statePersonalityC')

    def on_enter_statePersonalityD(self, update):
        update.message.reply_text("d、緊張大師指數：80%\n你是一個滿容易緊張的人，一點風吹草動，就會讓你胡思亂想起來，要是真的發生大事，很容易往壞處想。而你又不想讓別人發現而努力撐住，無形中讓你的精神、身體都長期處於緊張的狀態！")
        self.go_back(update)

    def on_exit_statePersonalityD(self, update):
        print('Leaving statePersonalityD')

    def on_enter_stateWork(self, update):
        update.message.reply_text("如果你是一家大企業的負責人，有一位年輕貌美的私人秘書，你有權規定她的上班服裝，你認為下列何者較符合你的想法？\na、保守的套裝裙長過膝才顯得莊重\nb、突顯身材的窄裙不但可以帶出去應酬自己也賞心悅目\nc、一律和其他職員一樣穿工作服公司要注意紀律\nd、任其自由穿著")
        #self.go_back(update)

    def on_exit_stateWork(self, update):
        print('Leaving stateWork')

    def on_enter_stateWorkA(self, update):
        update.message.reply_text("a、保守的套裝裙長過膝才顯得莊重\n你是個平常看起來很散漫，實際上只要投入工作便一本正經的人。認真是你一貫的做事方式，而且勇於負責，絲毫不馬虎，你最痛恨敷衍了事的工作態度，所以你是十足的工作狂。")
        self.go_back(update)

    def on_exit_stateWorkA(self, update):
        print('Leaving stateWorkA')

    def on_enter_stateWorkB(self, update):
        update.message.reply_text("b、突顯身材的窄裙不但可以帶出去應酬自己也賞心悅目\n你很聰明機靈，懂得在該努力的時候努力工作，能偷懶的時候也不放過休息的機會，所以你在工作時精神特別好，還滿注意工作環境的情調，你只能說是看起來象個工作狂。")
        self.go_back(update)

    def on_exit_stateWorkB(self, update):
        print('Leaving stateWorkB')

    def on_enter_stateWorkC(self, update):
        update.message.reply_text("c、一律和其他職員一樣穿工作服公司要注意紀律\n你是個公私分明的人，雖然談不上是個工作狂，但是只要辦公事時，你不喜歡涉及私人的事情，基本上你也算工作狂型的人物。")
        self.go_back(update)

    def on_exit_stateWorkC(self, update):
        print('Leaving stateWorkC')

    def on_enter_stateWorkD(self, update):
        update.message.reply_text("d、任其自由穿著\n你是個奇才型人物，比較擅長策劃性的工作，如果認真起來，做事一絲不茍；但是如果你根本沒興趣，你就會搪塞過去，不大理會。所以你是不是工作狂，完全視工作性質而定。")
        self.go_back(update)

    def on_exit_stateWorkD(self, update):
        print('Leaving stateWorkD')

    def on_enter_stateChat(self, update):
        update.message.reply_text("Hi!")
        #self.go_back(update)

    def on_exit_stateChat(self, update):
        print('Leaving stateChat')

    def on_enter_stateChat1(self, update):
        update.message.reply_text("How are you?")
        #self.go_back(update)

    def on_exit_stateChat1(self, update):
        print('Leaving stateChat1')

    def on_enter_stateChat2(self, update):
        update.message.reply_text("Are you single?")
        #self.go_back(update)

    def on_exit_stateChat2(self, update):
        print('Leaving stateChat2')

    def on_enter_stateChat3(self, update):
        update.message.reply_text("Ok~This is for you.\nhttps://youtu.be/WCpKhCyqmFE")
        self.go_back(update)

    def on_exit_stateChat3(self, update):
        print('Leaving stateChat3')

    def on_enter_stateChat4(self, update):
        update.message.reply_text("Congratulations!\nhttps://pbs.twimg.com/media/DB4AHDFU0AEu6G4.jpg")
        self.go_back(update)

    def on_exit_stateChat4(self, update):
        print('Leaving stateChat4')

    def on_enter_stateJoke(self, update):
        update.message.reply_text("normal or turbo")
        #self.go_back(update)

    def on_exit_stateJoke(self, update):
        print('Leaving stateJoke')

    def on_enter_stateJokeNormal(self, update):
        update.message.reply_text("有一天總統不小心掉到水溝里了.恰好有三個小孩經過\n總統就對他們說:「如果你們救我起來我就給你們每人一個願望」\n第一個小孩就說他要一輛腳踏車\n第二個小孩就說他要一個棒球手套\n第三個小孩想了很久說他要一台輪椅\n總統心里就覺得很奇怪手腳好好的為什麼需要輪椅呢?\n就問第三個小孩說:「你為什麼要輪椅呢?」\n第三個小孩就說:「如果我爸知道我救你起來會把我的腿打斷」\n")
        self.go_back(update)

    def on_exit_stateJokeNormal(self, update):
        print('Leaving stateJokeNormal')

    def on_enter_stateJokeTurbo(self, update):
        update.message.reply_text("有個人，來到本地一家健身館想減肥，好使自己苗條些，健身館裡備有各種健身計劃，看來挺複雜，於是，這傢伙選了一種最便宜的，就是在一小時內減掉一磅。他被帶到一間房子裡，裡面站著一個赤裸的女孩子，手裡拿著個牌子，上面寫道：「如果你能抓住我，就允許你幹我！」這傢伙立即接受了挑戰，開始追逐女孩，但每次都是快要抓住女孩時，又給她跑掉，一個小時過去了，他仍沒有抓住那個女孩，健身教練帶他去稱了一下體重，剛好少了一磅。「這挺不錯嘛，」這傢伙心想，「我既能減肥，又能開心耶。」\n這次，他選了一個稍貴些的減肥方案，可以在一小時內減去兩磅。他被帶到一間房裡，裡面站著兩位全裸的女孩，手裡都拿著牌子，上面也寫道：「如果你能抓住我，就允許你幹我！」這傢伙十分興奮，拚命地追趕這兩個女孩子，最後還是一個也沒追到，一小時後，教練又給他稱了下體重，剛好掉了兩磅肉。\n這時，這傢伙被激怒了，他告訴經理，他要選用最貴的減肥方案，經理向他保證他一定能夠在一小時內減去十磅，但是又補充說，這個方案十分危險，這傢伙心想，不就是再多幾個女孩嗎，越多就越有機會，至少能夠抓住一個吧。他催經理趕快把他送到那個最貴的房間去，儘管經理不斷向他聲明危險。於是，這人被帶到一個稍遠些的一間房子裡，他們讓他進去後，在外面鎖上了門，房間裡燈光昏暗，等待他的是一隻黑猩猩，只見它手裡拿著一個牌子，上面寫道：「如果我抓住你，我就幹你」")
        self.go_back(update)

    def on_exit_stateJokeTurbo(self, update):
        print('Leaving stateJokeTurbo')
