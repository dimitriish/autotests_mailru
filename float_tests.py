import pytest

# float_abs
@pytest.mark.parametrize("num, abss", [(0, 0), (10.5, 10.5), (-10.6, 10.6)])
def test_float_abs(num, abss):
    assert abs(num) == abss

# float_round
@pytest.mark.parametrize("num, rounded", [(0, 0), (10.5, 10), (-10.6, -11), (2.3, 2)])
def test_float_round(num, rounded):
    assert round(num) == rounded


# float_NaN_convert_to_float
def test_NaN_convert_to_float():
    with pytest.raises(ValueError):
        assert float("text")


