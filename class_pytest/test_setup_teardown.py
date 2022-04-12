##模块级别
def setup_module():
    print("这是模块的准备setup")

def teardown_module():
    print("这是模块的teardown")

def setup_function():
    print("这是函数的准备setup")

def teardown_function():
    print("这是函数的teardown")


def test_case():
    assert 1 == 1


class TestDemo:
    def setup_class(self):
        print("这是类类类类的开始准备")

    def teardown_class(self):
        print("这是累累累类的down")

    def setup(self):
        print("这是方法的准备setup")

    def teardown(self):
        print("这是方法的后置down")

    def test_case_01(self):
        assert 1 == 1

    def test_case_02(self):
        assert 0 == 1
