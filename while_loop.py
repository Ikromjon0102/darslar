from random import randint

# while shart:
#     salom

# qadam = 1
# # for harf in "Python":
# #     print(harf * 10)
#
# for i in range(1, 15, 2):
#     print(f"{i*'*'}".center(25))
#
# print("| |".center(25))


# =============== while ===========

# qadam = 1
#
# while qadam <= 5:
#     print(qadam)
#     qadam += 1         # qadam = qadam + 1
#
# print(f"sikl tugadi sabab qadam qiymati {qadam} ga teng boldi")

#
# while True:
#     print("Salom dunyo!")
#
# print("loop tugadi")

# print("kiritilgan sonni kvsi qaytaradi, yakunlash uchun (stop) deb yozing")
# belgi = True
# while belgi:
#     son = input("son kiriting: ")
#     if son == "stop":
#         belgi = False
#         print("Loop yakunlandi, Faydalanganiz un rahmat")
#     else:
#         print(int(son) ** 2)



# ====== break bilan to'xtatish ========
# print("kiritilgan sonni kvsi qaytaradi, yakunlash uchun (stop) deb yozing")
# while True:
#     son = input("son kiriting: ")
#     if son == "stop":
#         print("Loop yakunlandi, Faydalanganiz un rahmat")
#         break
#     else:
#         print(int(son) ** 2)


# ========== son topish o'yini ===========

from random import randint
com_num = randint(1,10)
print("🤖 Men 1-10 orasidan 1ta son tanladim, topoliysizmi?")
qadam = 0
while qadam < 3:
    qadam += 1
    user_num = int(input(f"{qadam} - Taxminingiz{com_num}: "))
    if com_num < user_num:
        print("🤖 men tanlagan raqam kichikroq")

    elif com_num > user_num:
        print("🤖 men tanlagan raqam kattaroq")

    else:
        print("🏆 Tabriklaymiz! yutdingiz")
        break
else:
    print("Mag'lubiyat 😫") 

    # if qadam == 4:
    #     print("Mag'lubiyat 😫")
    #     break





























