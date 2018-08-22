# -*- coding:utf-8 -*-
# @Time    : 2018/8/20 16:04
# @Author  : leolee
# @File    : Main.py.py
import pygame,time,random
from pygame.locals import *
from Tkinter import *
import codecs
if __name__=="__main__":
    config = {}
    def init():
        global config
        #读取配置文件
        conf = codecs.open("config.properties","r",encoding="utf-8")
        config = {}
        for a in conf.readlines():
            s = a.replace("\n","").replace("\r","").split("=")
            config[s[0]] = s[1]
    init()
    #----------------------------配置部分-----------------------------
    root = Tk()
    root.title("男师范生的职业性别刻板印象")
    root.geometry('1024x768')
    root.attributes("-fullscreen", False)
    fram = Frame(root,height=768,width=1024,bg="gray")
    fram.pack()
    canvas = Canvas(fram,height=200,width=1024)
    image_file = PhotoImage(file='pictures/pz_bg.gif')
    image = canvas.create_image(0,0,anchor='nw',image=image_file)
    canvas.pack(side='top')
    choosenFram = Frame(fram,height=568,width=1024,bg="gray")
    choosenFram.pack(side='bottom')
    insideFram1 = Frame(choosenFram, height=500, width=200, bg="gray")
    insideFram2 = Frame(choosenFram, height=500, width=200, bg="gray")
    insideFram3 = Frame(choosenFram, height=500, width=200, bg="gray")
    insideFram4 = Frame(choosenFram, height=500, width=200, bg="gray")
    insideFram1.grid(row=0, column=0, padx=28, pady=34)
    insideFram2.grid(row=0, column=1, padx=28, pady=34)
    insideFram3.grid(row=0, column=2, padx=28, pady=34)
    insideFram4.grid(row=0, column=3, padx=28, pady=34)
    #version
    rVersion = StringVar()
    def versionRadio():
        global config
        config["version"]=rVersion.get()
    l1 = Label(insideFram1,fg="red",bg="gray",font=("Arial 30 bold"),text="程序版本")
    l1.grid(row=0,column=0,padx=10,pady=20)
    r11 = Radiobutton(insideFram1,bg="gray",font=("Arial",25),text="version 1",value="1",variable=rVersion,command=versionRadio)
    r11.grid(row=1,column=0,padx=10,pady=20)
    r12 = Radiobutton(insideFram1,bg="gray",font=("Arial",25),text="version 2",value="2",variable=rVersion,command=versionRadio)
    r12.grid(row=2,column=0,padx=10,pady=20)
    #grade
    rGrade = StringVar()
    def gradeRadio():
        global config
        config["grade"]=rGrade.get()
    l2 = Label(insideFram2,fg="red",bg="gray",font=("Arial 30 bold"),text="年级")
    l2.grid(row=0,column=0,padx=10,pady=10)
    r21 = Radiobutton(insideFram2,bg="gray",font=("Arial",20),text="大一",value="大一",variable=rGrade,command=gradeRadio)
    r21.grid(row=1,column=0,padx=10,pady=0)
    r22 = Radiobutton(insideFram2,bg="gray",font=("Arial",20),text="大二",value="大二",variable=rGrade,command=gradeRadio)
    r22.grid(row=2,column=0,padx=10,pady=0)
    r23 = Radiobutton(insideFram2, bg="gray", font=("Arial", 20), text="大三", value="大三", variable=rGrade,command=gradeRadio)
    r23.grid(row=3, column=0, padx=10, pady=0)
    r24 = Radiobutton(insideFram2, bg="gray", font=("Arial", 20), text="大四", value="大四", variable=rGrade,command=gradeRadio)
    r24.grid(row=4, column=0, padx=10, pady=0)
    r25 = Radiobutton(insideFram2, bg="gray", font=("Arial", 20), text="研一", value="研一", variable=rGrade,command=gradeRadio)
    r25.grid(row=5, column=0, padx=10, pady=0)
    r26 = Radiobutton(insideFram2, bg="gray", font=("Arial", 20), text="研二", value="研二", variable=rGrade,command=gradeRadio)
    r26.grid(row=6, column=0, padx=10, pady=0)
    r27 = Radiobutton(insideFram2, bg="gray", font=("Arial", 20), text="研三", value="研三", variable=rGrade,command=gradeRadio)
    r27.grid(row=7, column=0, padx=10, pady=0)
    #major
    rMajor = StringVar()
    def majorRadio():
        global config
        config["major"]=rMajor.get()
    l3 = Label(insideFram3,fg="red",bg="gray",font=("Arial 30 bold"),text="专业")
    l3.grid(row=0,column=0,padx=10,pady=10)
    r31 = Radiobutton(insideFram3,bg="gray",font=("Arial",20),text="文科",value="文科",variable=rMajor,command=majorRadio)
    r31.grid(row=1,column=0,padx=10,pady=20)
    r32 = Radiobutton(insideFram3,bg="gray",font=("Arial",20),text="理科",value="理科",variable=rMajor,command=majorRadio)
    r32.grid(row=2,column=0,padx=10,pady=20)
    r32 = Radiobutton(insideFram3, bg="gray", font=("Arial", 20), text="其他", value="其他", variable=rMajor,command=majorRadio)
    r32.grid(row=3, column=0, padx=10, pady=20)
    #age
    l4 = Label(insideFram4,fg="red",bg="gray",font=("Arial 15 bold"),text="年龄")
    l4.grid(row=0,column=0,padx=20,pady=20)
    varAge = StringVar()
    tAge = Entry(insideFram4,textvariable=varAge)
    tAge.grid(row=0,column=1,padx=20,pady=20)
    l5 = Label(insideFram4,fg="red",bg="gray",font=("Arial 15 bold"),text="序号")
    l5.grid(row=1,column=0,padx=20,pady=20)
    varNumber = StringVar()
    tNumber = Entry(insideFram4,textvariable=varNumber)
    tNumber.grid(row=1,column=1,padx=20,pady=20)
    def submit():
        global config,varAge,varNumber,root
        config["age"] = tAge.get()
        config["number"] = tNumber.get()
        root.quit()
    b1 = Button(insideFram4,text="提交",bg="white",width=15,height=2,command=submit)
    b1.grid(row=2,column=0,padx=20,pady=20)
    root.mainloop()
    #----------------------------实验部分-----------------------------
    out = codecs.open("result.zpp","a+",encoding="utf-8")
    out.write("user:"+config["number"]+"\t")
    out.write("version:"+config["version"]+"\t")
    out.write("grade:"+config["grade"]+"\t")
    out.write("major:"+config["major"]+"\t")
    out.write("age:"+config["age"]+"\r\n")
    version = int(config["version"])
    pygame.init()
    pygame.font.init()

    msgFont = pygame.font.Font('simkai.ttf',120)
    screenSize=(1024,768)
    #三类词
    menWords=[a.replace("\n","").replace("\r","") for a in codecs.open("men.txt","r",encoding="utf-8").readlines()]
    womenWords=[a.replace("\n","").replace("\r","") for a in codecs.open("women.txt","r",encoding="utf-8").readlines()]
    midWords=[a.replace("\n","").replace("\r","") for a in codecs.open("mid.txt","r",encoding="utf-8").readlines()]

    #全屏
    screen = pygame.display.set_mode((1024,768),pygame.FULLSCREEN,32)
    # screen = pygame.display.set_mode((1024,768),0,32)

    #正确和错误的图标
    right = pygame.image.load("pictures/right.png").convert_alpha()
    wrong = pygame.image.load("pictures/wrong.png").convert_alpha()

    #两张背景图
    bg1 = pygame.image.load("pictures/bg1.jpg").convert_alpha()
    bg2 = pygame.image.load("pictures/bg2.jpg").convert_alpha()


    def message(content,screen,flag="0"):
        if flag.__eq__("mid") or flag.__eq__("0"):
            x = screenSize[0]/2 - msgFont.size(content)[0]/2
            y = screenSize[1]/2 - msgFont.size(content)[1]/2
            screen.blit(msgFont.render(content, True, (255,255,255)), (x,y))
        elif flag.__eq__("leftTop"):
            screen.blit(msgFont.render(content, True, (255,255,255)), (10, 10))
        else:
            message("errorLocation",screen,"mid")

    def wait4key(keySet):
        if len(keySet)==0:
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        return
                pygame.display.update()
        else:
            while True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key in keySet:
                            return event.key
                pygame.display.update()

    def action(word,isLeft,background,screen):
        start = time.time()
        screen.blit(background,(0,0))
        message(word,screen)
        k = wait4key([K_f,K_j])
        end = time.time()
        if isLeft and k == K_f or not isLeft and k == K_j:
            return True,end-start
        elif isLeft and k == K_j or not isLeft and k == K_f:
            return False,end-start

    def showResult(isRight,screen):
        global right,wrong
        screen.fill((74,74,74))
        if isRight:
            screen.blit(right,(0,0))
        else:
            screen.blit(wrong,(0,0))
        pygame.display.update()
        time.sleep(0.2)

    def showPic(pic,screen):
        notification1 = pygame.image.load(pic).convert_alpha()
        screen.blit(notification1, (0, 0))
        wait4key([K_SPACE])

    def exp1test():
        global menWords,womenWords,midWords,screen,bg1
        exp1ExeList = menWords*2+womenWords+midWords
        random.shuffle(exp1ExeList)
        for word in exp1ExeList:
            if word in womenWords or word in midWords:
                flag,gap = action(word,True,bg1,screen)
                showResult(flag,screen)
            else:
                flag,gap = action(word,False,bg1,screen)
                showResult(flag,screen)

    def exp1():
        global menWords,womenWords,midWords,screen,bg1,out
        out.write(u"\t--------------实验1-------------------\r\n")
        exp1ExeList = menWords*4+womenWords*2+midWords*2
        random.shuffle(exp1ExeList)
        for word in exp1ExeList:
            if word in womenWords or word in midWords:
                flag,gap = action(word,True,bg1,screen)
                out.write("\t"+word+":"+str(flag)+"-"+str(gap)+"\r\n")
                showResult(flag,screen)
            else:
                flag,gap = action(word,False,bg1,screen)
                out.write("\t"+word+":"+str(flag)+"-"+str(gap)+"\r\n")
                showResult(flag,screen)

    def exp2test():
        global menWords,womenWords,midWords,screen,bg2
        exp1ExeList = menWords+womenWords*2+midWords
        random.shuffle(exp1ExeList)
        for word in exp1ExeList:
            if word in womenWords:
                flag,gap = action(word,True,bg2,screen)
                showResult(flag,screen)
            else:
                flag,gap = action(word,False,bg2,screen)
                showResult(flag,screen)

    def exp2():
        global menWords,womenWords,midWords,screen,out,bg2
        out.write(u"\t--------------实验2-------------------\r\n")
        exp1ExeList = menWords*2+womenWords*4+midWords*2
        random.shuffle(exp1ExeList)
        for word in exp1ExeList:
            if word in womenWords:
                flag,gap = action(word,True,bg2,screen)
                out.write("\t"+word+":"+str(flag)+"-"+str(gap)+"\r\n")
                showResult(flag,screen)
            else:
                flag,gap = action(word,False,bg2,screen)
                out.write("\t"+word+":"+str(flag)+"-"+str(gap)+"\r\n")
                showResult(flag,screen)

    #指导语
    showPic("pictures/1.jpg",screen)
    #实验一规则
    if version==1:
        showPic("pictures/2.jpg",screen)
    else:
        showPic("pictures/6.jpg", screen)
    #实验一练习提示
    showPic("pictures/3.jpg",screen)
    #实验一练习开始
    if version==1:
        exp1test()
    else:
        exp2test()
    #实验一正式阶段
    showPic("pictures/4.jpg",screen)
    #实验一正式开始
    if version==1:
        exp1()
    else:
        exp2()
    #实验二过度
    showPic("pictures/5.jpg",screen)
    #实验二规则
    if version==1:
        showPic("pictures/6.jpg",screen)
    else:
        showPic("pictures/2.jpg", screen)
    #实验二练习提示
    showPic("pictures/3.jpg",screen)
    #实验二练习开始
    if version==1:
        exp2test()
    else:
        exp1test()
    #实验二正式阶段
    showPic("pictures/4.jpg",screen)
    #实验二正式开始
    if version==1:
        exp2()
    else:
        exp1()
    #实验结束
    notification7 = pygame.image.load("pictures/7.jpg").convert_alpha()
    screen.blit(notification7,(0,0))
    pygame.display.update()
    time.sleep(5)

    out.close()