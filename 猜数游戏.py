import random


def guess_number():
    a = random.randint(0, 100)
    print(a)
    count = 0
    print("最多输入十次")
    while count <= 10:
        num = input("输入一个整数：")
        count += 1
        if int(num) == a:
            print("您猜对了！猜测的次数：" + str(count))
            break
        elif int(num) > a:
            print("The number is bigger!")
        else:
            print("The number is smaller!")
        if count == 10:
            print("您已超过输入次数！")
            break


guess_number()







