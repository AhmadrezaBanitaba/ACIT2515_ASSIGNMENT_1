from abstract_menu_item import AbstractMenuItem


class Drink(AbstractMenuItem):
    """ creates drink """

    def __init__(self, menu_item_name, menu_item_no, date_added, price, calories, manufacturer, size, is_fizzy, is_hot):
        super().__init__(menu_item_name, menu_item_no, date_added, price, calories)
        self._manufacturer= manufacturer
        self._size= size
        self._is_fizzy= is_fizzy
        self._is_hot= is_hot

    def menu_item_description(self):
        pass
    def get_type(self):
        pass

    def get_manufacturer(self):
        pass
    def get_size(self):
        pass


