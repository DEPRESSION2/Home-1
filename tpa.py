wide = 0
line = ''
space_am = 0
star_am = 1
while wide % 2 == 0:
    try:
        wide = int(input("Введите ширину ромба(нечётное число): "))
    except:
        print("Нужно нечётное!")
    else:
        space_am = int(wide - 1)
        for i in range(0, int(wide/2)):
            print(" " * int(space_am/2) + "*" * int(star_am) + " " * int(space_am/2))
            star_am += 2
            space_am -= 2
        for i in range(0, int(wide/2)+ 1):
            print(" " * int(space_am/2) + "*" * int(star_am) + " " * int(space_am/2))
            star_am -= 2
            space_am += 2