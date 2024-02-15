#masala 1 #0001
# input: 2 3
# output: 5

# a = input().split()
# print(f"kiritilgan sonlar {a}")
# print(f"kiritilgan son type {type(a)}")
# print(f"kiritilgan belgilar {len(a)}")
# yig = 0
# for i in a:
#     yig += int(i)
# print(yig)


# b = "3,3423454,55"
# b_list = b.split(",")
# print(b)
# print(b_list)




# map
# sonlar = ['1', '2', '3', '4', '5', '6', '7']
# sonlar_str = tuple( map( int , sonlar ) )
# print(sonlar_str)

print(sum(tuple( map( int, input().split() ) ) ) )


