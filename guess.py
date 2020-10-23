import random


def guess_number():
    # 随机生成100以内的整数
    a = random.randint(0, 100)
    count = 0
    print("最多输入十次")
    while count <= 10:
        num = input("输入一个整数：")
        count += 1
        # 若猜对，结束循环，输出循环次数
        if int(num) == a:
            print("您猜对了！猜测的次数：" + str(count))
            break
        elif int(num) > a:
            print("The number is bigger!")
        else:
            print("The number is smaller!")
        # 超过循环次数，结束循环
        if count == 10:
            print("您已超过输入次数！")
            break


guess_number()







