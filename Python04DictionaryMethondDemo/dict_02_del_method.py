#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 集合
def dict_add_method():
    set_data = {
        "cityid": "101010100",
        "city": "北京",
        "update_time": "00:17",
        "wea": "多云",
        "wea_img": "yun",
        "tem": "-2",
        "tem_day": "6",
        "tem_night": "-8",
        "win": "西南风",
        "win_speed": "2级",
        "win_meter": "6km/h",
        "air": "51"
    }
    return set_data


if __name__ == '__main__':
    data = dict_add_method()
    print("_" * 100)
    print(data)
    print("_" * 100)

    # 如果这个键存在则更新值内容
    print("删除cityid后的字典值为：")
    data.pop("cityid")
    print(data)

    print("_" * 100)
    print("清空列表的值后，打印字典")
    data.clear()
    print(data)
