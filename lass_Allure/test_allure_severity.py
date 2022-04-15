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

命令行
pytest test_allure_severity.py --allure-severities=blocker --alluredir ./result -vs 
--clean-alluredir


link()       定义链接  @allure.link()

testcase()  用例相关链接@allure.testcase()
issue()      缺陷地址   @allure.issue()
attachment()    附件

"""

@allure.severity(allure.severity_level.BLOCKER)
@allure.title("第一个用例")
def test_sucess():
    print("case1")
    assert 1 == 1

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("登录模块的用例")
class TestCase01():
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录成功")
    def test_case1_01(self):
        with allure.step("第一步，打开登录页面"):
            print("成功打开页面")
        with allure.step("第二步，输入账号"):
            print("输入账号")
        with allure.step("第三步，输入密码"):
            print("输入密码")
            assert 1 == 2

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("登录失败")
    def test_case1_02(self):
        print("case2")

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("模块2的用例")
class TestCase02():
    @allure.severity(allure.severity_level.NORMAL)
    @allure.link("www.baidu.com")
    def test_allure_link(self):
        print("case1")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("www.baidu.com", name="百度")
    def test_allure_testcase(self):
        print("case2")

    """
    --allure-link-pattern=issue:http://www.baidu.com/issue/{}
    """

    @allure.severity(allure.severity_level.NORMAL)
    def test_allure_issue_link(self):
        print("case2")