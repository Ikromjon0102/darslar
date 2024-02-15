# fayllar bilan ishlash
# r = read
# w = write
# a = append

# numbers = open("sonlar.txt", "r")
# # print(numbers.read())
# # print(numbers.readline())
# # print(numbers.readlines())
# sonlar = numbers.readlines()
# for son in sonlar:
#     print(int(son) ** 2)
#
# numbers.close()

# ismlar = open("names.txt", "w")
# # matn = "Hello world!"
# # ismlar.write(matn)
# for i in range(2):
#     ism = input("ism kiriting: ")
#     ismlar.write(f"{ism.capitalize()}\n")
# ismlar.close()

# ism_qosh = open("names.txt", "a")
# for i in range(2):
#     ism = input("ism kiriting: ")
#     ism_qosh.write(f"{ism.capitalize()}\n")
#
# ism_qosh.close()


# with open("names.txt", "a") as ismlar:
#     ismlar.write("Hakimjon")

# with open("sonlar.txt", "r") as nums:
#     with open("sonlar_kvadrati.txt", "w") as nums_kv:
#         for son in nums:
#             text = f"{son.strip("\n")} ning kvadrati {int(son) ** 2} ga teng \n"
#             nums_kv.write(text)
#
# print("fayl o'qildi va yangi faylga yozildi")

with open("document/textlar/salom.txt", "r") as file:
    print(file.read())