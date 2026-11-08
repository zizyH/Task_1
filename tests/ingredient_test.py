import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type_returns_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'name', 100)
        assert ingredient.get_type() == ingredient_type

    def test_get_name_returns_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert ingredient.get_name() == 'hot sauce'

    def test_get_price_returns_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        assert ingredient.get_price() == 100