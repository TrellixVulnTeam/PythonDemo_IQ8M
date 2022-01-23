import demo_test


class Func:

    def test02_func(self):
        # print("test02_func")
        print(__name__)


if __name__ == '__main__':
    # 输出运行代码的名字
    demo_test.FuncTest().test01_func()
    # 当前运行的代码文件的名字就是__main__
    Func().test02_func()
