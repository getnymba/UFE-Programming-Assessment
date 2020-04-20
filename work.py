import random

print("Escape тоглоомонд тавтай морил.\nТа их элсэн говийн дунд байдаг шоронгоос оргож байгаа ба зугтаахын тулд харгалзагчийнхаа тэмээг хулгайлах болно.\nМэдээж хэрэг цагдаа нар таны араас хөөх ба 200 км-ийн цаана байрлах нуувчиндаа хүрч чадвал та аврагдах болно.\nТаны эсэн мэнд зугтан гарах эсэх нь таны гаргах шийдвэрүүдээс хамаарах болно.\nТанд амжилт хүсье.\n")


done = False
km_traveled =0
thirst = 0
camel_tired = 0
oasis = 0
police_traveled = -20
drink = 5

while not done:
    print("A.Ус уух.\nB.Дундаж хурдаар явах\nC.Бүх хурдаар явах\nD.Зогсож амрах\nE.Нөхцөл байдлыг шалгах\nQ.Гарах")
    choice = input("Таны сонголт: ")
    print("\n")
    
    if choice.upper() == "Q":
        done = True

    elif choice.upper() == "E":
        print("Туулсан зам:", km_traveled, "км")
        print("Савтай усны тоо:", drink, "ш")
        print("Цагдаа таниас:", km_traveled - police_traveled, "км зайтай байна")
        print("Тэмээний ядарсан хэмжээ:", camel_tired, "%")
        print("Ам цангасан хэмжээ:", thirst, "\n")

    elif choice.upper() == "D":
        camel_tired = 0
        police_up = random.randrange(6,15)
        police_traveled += police_up
        print("Тэмээ амарч авлаа! гэвч цагдаа", police_up, "км зам тууллаа.\n")

    elif choice.upper() == "C":
        full_speed = random.randrange(10,20)
        km_traveled += full_speed
        police_up = random.randrange(6,15)
        police_traveled += police_up
        thirst += 1 
        camel_tired += random.randrange(2,3)*10
        oasis = random.randrange(1,20)
        if oasis == 10:
            thirst = 0
            camel_tired = 0
            drink = 5
            print("Та", full_speed, "км-ийн зам тууллаа.\n", "Баянбүрд тааралдлаа, Баяр хүргье.\nТаны амны цангаа тайлагдаж савнуудаа усаар дүүргэж авлаа.\n Мөн таны тэмээ амарч авлаа.\n Гэвч цагдаа", police_up,"км зам тууллаа.\n")
        else:
            print("Та", full_speed, "км зам тууллаа.\nТэмээний ядарсан хэмжээ:", camel_tired, "%\n", "Ам цангасан хэмжээ:", thirst, "\nЦагдаа", police_up, "км зам тууллаа.\n")

    elif choice.upper() == "B":
        mid_speed = random.randrange(5,12)
        km_traveled += mid_speed
        police_up = random.randrange(6,15)
        police_traveled += police_up
        thirst += 1
        camel_tired += random.randrange(1,2)*10
        oasis = random.randrange(1,20)
        if oasis == 10:
            thirst = 0
            camel_tired = 0
            drink = 5
            print("Та", mid_speed, "км-ийн зам тууллаа.\n", "Баянбүрд тааралдлаа, Баяр хүргье.\nТаны амны цангаа тайлагдаж савнуудаа усаар дүүргэж авлаа.\n Мөн таны тэмээ амарч авлаа.\n Гэвч цагдаа", police_up,"км зам тууллаа.\n")
        else:
            print("Та", mid_speed, "км зам тууллаа.\nТэмээний ядарсан хэмжээ:", camel_tired, "%\n", "Ам цангасан хэмжээ:", thirst, "\nЦагдаа", police_up, "км зам тууллаа.\n")
    
    elif choice.upper() == "A":
        if drink > 0:
            print("Та цангаагаа тайлж 1 савтай усаа уулаа.")
            drink -= 1
            print("Танд", drink, "ширхэг савтай ус үлдлээ\n")
            thirst = 0
        else:
            print("Ус дууссан!")

    if thirst >= 5:
        print("Та цангаж үхэв.!\n")
        print("Тоглоом дууслаа.")
        done = True
        break
    elif thirst >= 4:
        print("Ам цангаж үхлээ!\n")
    elif thirst >= 3: 
        print("Ам цангаж байна!\n")
    
    
    if camel_tired >= 100:
        print("Таны тэмээ ядарч үхэв!\n")
        print("Тоглоом дууслаа.")
        done = True
        break
    elif camel_tired >= 50:
        print("Таны тэмээ ядарч байна!\n")
    
    
    if km_traveled - police_traveled <= 0:
        print("Та цагдаад баригдлаа.\n")
        print("Тоглоом дууслаа.")
        done = True
        break
    elif km_traveled - police_traveled <= 15:
        print("Цагдаа ойртож байна.\n")
    
    if km_traveled >= 200:
        print("Та чадлаа, их элсэн говийг амжилттай туулж цагдаагаас зугтаж чадлаа.")
        print("Тоглоом дууслаа.")
        done = True
    
    
    if camel_tired >= 50:
        full_speed = random.randrange(5,10)
    else:
        full_speed = random.randrange(10,20)
    if camel_tired >= 50:
        mid_speed = random.randrange(3,8)
    else:
        mid_speed = random.randrange(5,12)
    

