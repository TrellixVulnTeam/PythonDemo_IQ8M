# random 返回随机生成的一个实数
import random


def get_mobile():
    mobiles = ['135', '136', '138', '176']
    # 获取时间戳
    m_time = str(int(time.time()))[2:]
    list = []

    for n in range(100):
        m_time = int(m_time) + 2
        # print(m_time)
        moble = random.choice(mobiles) + str(m_time)
        list.append(moble)

    return list


if __name__ == '__main__':
    print(get_mobile())
