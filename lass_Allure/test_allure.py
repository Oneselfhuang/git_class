import allure

"""
@allure.epic()    描述
feature()      模块名称     
story()     用例名称
title()       用例标题
step()       操作步骤
        使用with allure.step()
description()   用例描述


severity()    用例等级  (blocker,critical,normal,minor)
@allure.severity(allure.severity_level.blocker)

link()       定义链接  @allure.link()
 
testcase()  用例相关链接@allure.testcase()
issue()      缺陷地址   @allure.issue()
attachment()    附件

测试数据
pytest --alluredir=./result

方式一：查看报告
allure serve ./result
方式二：
生产报告
allure generate ./result -o ./report/ --clean
查看报告
allure open -h 127.0.0.1 -p 8883 ./report/
"""


@allure.title("第一个用例")
def test_sucess():
    print("case1")
    assert 1 == 1


@allure.feature("登录模块的用例")
class TestCase01():

    @allure.story("登录成功")
    def test_case1_01(self):
        with allure.step("第一步，打开登录页面"):
            print("成功打开页面")
        with allure.step("第二步，输入账号"):
            print("输入账号")
        with allure.step("第三步，输入密码"):
            print("输入密码")
            assert 1 == 2

    @allure.story("登录失败")
    def test_case1_02(self):
        print("case2")


@allure.feature("模块2的用例")
class TestCase02():
    @allure.link("www.baidu.com")
    def test_allure_link(self):
        print("case1")

    @allure.testcase("www.baidu.com", name="百度")
    def test_allure_testcase(self):
        print("case2")



    """
    --allure-link-pattern=issue:http://www.baidu.com/issue/{}
    """

    @allure.issue("140", name="issue链接")
    def test_allure_issue_link(self):
        print("case2")
