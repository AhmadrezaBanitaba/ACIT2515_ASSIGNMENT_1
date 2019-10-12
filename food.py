from abstract_menu_item import AbstractMenuItem

class Food(AbstractMenuItem):
    """ creates food """

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, cuisine_country, main_ingredient, portion_size, is_vegetarian):
        super().__init__(menu_item_name, menu_item_no, date_added, price, calories)
        self._cuisine_country= cuisine_country
        self._main_ingredient= main_ingredient
        self._portion_size= portion_size
        self._is_vegetarian= is_vegetarian



    def menu_item_description(self):
        pass
    def get_type(self):
        pass
    def get_portion_size(self):
        pass
    def get_main_ingredient(self):
        pass
    def get_cuisine_country(self):
        pass
    