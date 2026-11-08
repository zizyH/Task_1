from unittest.mock import Mock, patch

import pytest

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_sets_bun(self):
        burger = Burger()
        mock_bun = Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_appends_to_list(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_deletes_by_index(self):
        burger = Burger()
        first, second = Mock(), Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.remove_ingredient(0)
        assert burger.ingredients == [second]

    def test_move_ingredient_changes_order(self):
        burger = Burger()
        first, second, third = Mock(), Mock(), Mock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)
        burger.move_ingredient(0, 2)
        assert burger.ingredients == [second, third, first]

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected', [
        (100, [], 200),                 # только булка ×2
        (100, [50], 250),
        (100, [50, 70], 320),
        (200, [10, 20, 30], 460),
    ])
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient = Mock()
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected

    def test_get_receipt_format(self):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'SAUCE'
        mock_ingredient.get_name.return_value = 'hot sauce'
        mock_ingredient.get_price.return_value = 50
        burger.add_ingredient(mock_ingredient)

        expected = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 250'
        )
        assert burger.get_receipt() == expected