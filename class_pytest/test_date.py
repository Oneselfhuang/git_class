#code=utf-8

import pytest
import yaml

"""
参数化@pytest.mark.parametrize("user", [1, 2])

"""

#单参数、笛卡尔积
@pytest.mark.parametrize("user", [1, 2])
@pytest.mark.parametrize("name", ["abc", "efg"])
def test_date(user, name):
    print(f"user:{user},name:{name}")


#多参数
@pytest.mark.parametrize("user,name",[[1,"abc"],[2,"efg"]],ids=["no.1","NO.2"])
def test_date_yaml(user, name):
    print(f"user:{user},name:{name}")


#引用yaml
@pytest.mark.parametrize("kwargs",yaml.safe_load(open("./data/data.yaml")))
def test_date_yaml(kwargs):
    print(f"user:{kwargs['user']},name:{kwargs['name']}")