import demo_test


class Func:

    def test02_func(self):
        print(__file__)


if __name__ == '__main__':
    # 打印当前文件的绝对路径
    Func().test02_func()
    demo_test.FuncTest().test02_func()
