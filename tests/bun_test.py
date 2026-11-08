import pytest
from praktikum.bun import Bun

BUN_CASES = [
    ('black bun', 100),
    ('white bun', 200),
    ('red bun', 300),
]


class TestBun:
    @pytest.mark.parametrize('name, price', BUN_CASES)
    def test_get_name_returns_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', BUN_CASES)
    def test_get_price_returns_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
