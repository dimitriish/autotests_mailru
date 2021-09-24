import pytest

# intsum
@pytest.mark.parametrize('a, b, summ', [(0, -10, -10), (0, 10, 10), (5, -5, 0)])
def test_int_sum(a, b, summ):
    assert a + b == summ

# intmultuply
@pytest.mark.parametrize('a, b, multiple', [(5, 0, 0), (10, -5, -50), (0, 0, 0), (100, 10, 1000)])
def test_int_mul(a, b, multiple):
    assert a * b == multiple

# intsum_with_str
def test_int_sum_with_str():
    with pytest.raises(TypeError):
        assert 21 + '33'

