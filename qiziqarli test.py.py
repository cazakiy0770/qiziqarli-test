import random
while True:
    print("Test o'tkazasizmi ha yoki yo'q")
    bosh = input("boshlaymizmi;")
    if bosh == "ha":
        print("Bu test orqalisezning sevgingiz necha foiz ekanini bilib olasiz")
        print("O'gilbolamisiz(1) yoki qizbola(0) tanlang birordasini")
        javob1=int(input("javobingiz;"))
        if javob1==1:
                se01=input("ismingizni keriting;")
                se02=input("sevgan qizingizni ismini yozing;")
        else:
                se01=input("ismingizni keriting;") 
                se02=input("yigitingizni ismini yozing;")
        def fi02():
            hisob = len(se01) + len(se02)
            if hisob > 10:
                y=40
            else:
                y=20
            x=100
            qwert = random.randint(y, x)
            if qwert < 50:
                print(f"{qwert}% sevarkan. {se01} seni {se02} sevmaykan")
            elif 70>qwert>50:
                print(f"{qwert}% sevarkan. {se01} sen {se02}dan pul undiradigan darajada u seni sevmaykan ")
            elif 70 < qwert < 90:
                print( f"{qwert}% sevarkan. {se01} sen {se02}ni sigir qilib sog'ib bir tiyin puli qomaguncha shilsang ham buladi")
            else:
                print(f"{qwert}% sevarkan. {se01} seni {se01} o'lib quguday sevadi, o'zini osib quyguday sevadi. Xuddi toshbaqa tuxumini yxshi kurganday sevadi ")
               
         
    else:
        print("Bu hammasi hazil edi u seni bir teyingayan olmaydi latta")
        break
    fi02()












