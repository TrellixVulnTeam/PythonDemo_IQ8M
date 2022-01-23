# 不同的子类对象调用相同的父类方法，产生不同的执行结果
class animal(object):
    def food(self):
        print("食物")

    def eat(self):
        self.food()


class dog(animal):
    def food(self):
        print("狗吃肉")


class cattle(animal):
    # 重写了food方法
    def food(self):
        print("牛吃草")

    # def eat(self):
    #     print("重写吃的方法")


if __name__ == '__main__':
    d = dog()
    # 调用父类的 eat 方法
    d.eat()
    c = cattle()
    # 调用父类的 eat 方法
    c.eat()
