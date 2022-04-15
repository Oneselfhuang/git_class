# code=utf-8

import pytest
import yaml

"""
参数化@pytest.mark.parametrize("user", [1, 2])

"""


# 单参数、笛卡尔积
@pytest.mark.parametrize("user", [1, 2])
@pytest.mark.parametrize("name", ["abc", "efg"])
@pytest.mark.parametrize("password", [1, 2, 3, 4])
def test_date(user, name, password):
    print(f"user:{user},name:{name},pass:{password}")


# 多参数
@pytest.mark.parametrize("user,name", [[1, "abc"], [2, "efg"]], ids=["no.1", "NO.2"])
def test_date_yaml1(user, name):
    print(f"user222222:{user},name222222:{name}")


# 引用yaml
@pytest.mark.parametrize("kwargs", yaml.safe_load(open("./data/data.yaml")))
def test_date_yaml(kwargs):
    print(f"user:{kwargs['user']},name:{kwargs['name']}")



def test_data11111():
    date = yaml.safe_load(open("./data/2222.yaml"))
    print(date)
    key = date.keys()
    print(key)
