import pytest


"""
@pytest.mark.skip
@pytest.mark.skipif
pytest.skip(reason)
"""


@pytest.mark.skip(reason="没有理由跳过")
def test_case():
    assert 1 == 1



def login():
    return False



def test_login():
    print("start")
    if not login():
        pytest.skip("this is skip demo")
    print("end")

class TestDemo:
    def test_case_01(self):
        assert 1 == 1
    @pytest.mark.skipif(1==1,reason="1")
    def test_case_02(self):
        assert 0 == 1
