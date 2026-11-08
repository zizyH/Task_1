from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_available_buns_returns_three_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_buns_content(self):
        database = Database()
        actual = [(b.get_name(), b.get_price()) for b in database.available_buns()]
        assert actual == [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ]

    def test_available_ingredients_returns_six(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_content(self):
        database = Database()
        actual = [
            (i.get_type(), i.get_name(), i.get_price())
            for i in database.available_ingredients()
        ]
        assert actual == [
            (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
            (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
            (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
            (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
            (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
            (INGREDIENT_TYPE_FILLING, 'sausage', 300),
        ]