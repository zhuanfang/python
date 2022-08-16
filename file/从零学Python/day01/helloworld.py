
# 取4个随机数，并生成一个列表
import random


def test_randmo():
    i = 0
    random_list = []
    # while i <4:
    #     random_num = random.randint(0,499)
    #     if random_num not in random_list:
    #         random_list.append(random_num)
    #         i += 1
    #         print(random_list)
# ==
    for i in range(0,10,3): # range(start,stop,step)
        random_num = random.randint(0,499)
        if random_num not in random_list:
            random_list.append(random_num)
            print(random_list)

