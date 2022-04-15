"""
@allure.attach()
报告添加附件

"""
import allure


@allure.feature("登录模块的用例")
class TestCase01():

    @allure.story("登录成功")
    def test_case1_01(self):
        with allure.step("第一步，打开登录页面"):
            print("成功打开页面")
            allure.attach.file(r"C:\Users\oneself\Desktop\测试\驾驶证.jpg",
                               name="截图",
                               attachment_type=allure.attachment_type.JPG,
                               extension=".jpg")
        with allure.step("第二步，输入账号"):
            allure.attach("这是一段文本信息",name="文本片段")
            print("输入账号")
        with allure.step("第三步，输入密码"):
            print("输入密码")
            assert 1 == 2

    @allure.story("登录失败")
    def test_case1_02(self):
        assert 1==1
        print("case2")
