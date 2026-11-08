import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def bun():
    return Bun('black bun', 100)


@pytest.fixture
def ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def database():
    return Database()