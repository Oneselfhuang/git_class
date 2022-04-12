import pytest

"""
@pytest.mark.str   标签

运行方式
pytest -s XXXX,py -m 标签名
"""
@pytest.mark.str
def test_case():
    assert 1 == 1


class TestDemo:
    def test_case_01(self):
        assert 1 == 1

    def test_case_02(self):
        assert 0 == 1
