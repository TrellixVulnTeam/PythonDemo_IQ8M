import time

from tqdm import tqdm

"""
iterable: 可迭代的对象, 在手动更新时不需要进行设置
desc: 字符串, 左边进度条描述文字
total: 总的项目数
leave: bool值, 迭代完成后是否保留进度条
file: 输出指向位置, 默认是终端, 一般不需要设置
ncols: 调整进度条宽度, 默认是根据环境自动调节长度, 如果设置为0, 就没有进度条, 只有输出的信息
unit: 描述处理项目的文字, 默认是'it', 例如: 100 it/s, 处理照片的话设置为'img' ,则为 100 img/s
unit_scale: 自动根据国际标准进行项目处理速度单位的换算, 例如 100000 it/s >> 100k it/s
"""


# 发呆0.5s
def action():
    time.sleep(0.5)


with tqdm(total=100000, desc='Example', leave=True, ncols=100, unit='B', unit_scale=True) as pbar:
    for i in range(10):
        # 发呆0.5秒
        action()
        # 更新发呆进度
        pbar.update(10000)
# Example: 100%|███████████████████████████████████████████████████| 100k/100k [00:05<00:00, 19.6kB/s]
