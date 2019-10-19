import datetime

class AbstractMenuItem:
    """ creates menu item """ 
    
    def __init__(self,  menu_item_name, menu_item_no, date_added, price, calories):
        self._id = None

        self._validate_input(menu_item_name, " menu_item_name")
        self._menu_item_name = menu_item_name

        self._validate_input(menu_item_no, "  menu_item_no")
        self._menu_item_no = menu_item_no

        self._validate_input(date_added, "  date_added")
        self._date_added = date_added

        self._validate_input(price, "  price")
        self._price = price

        self._validate_input(calories, "  calories")
        self._calories = calories


    def set_id(self, menu_item_id):
        """ sets menu item id"""
        self._id = menu_item_id 


    def get_id(self):
        """ returns menu item id """
        return self._id


    def get_menu_item_name(self):
        """ returns menu item name """ 
        return self._menu_item_name

    def get_menu_item_no(self):
        """ returns menu  item no """
        return self._menu_item_no

    def get_date_added(self):
        """ returns date added """
        return self._date_added
    
    def menu_item_description(self):
        """ abstract method. returns menu item description"""
        raise NotImplementedError("abstract method")

    def set_price(self, price):
        """ sets menu item price """
        self._price = price

    def get_price(self):
        """ returns menu item price """
        return self._price

    def get_type(self):
        """ abstract method. returns type """
        raise NotImplementedError("abstract method")


    @staticmethod
    def _validate_input(input, input_display):
        """Private method to validate inputs

        Args:
            input: Input to be validated
            input_display (string): String used in ValueError message

        Raises:
            ValueError: If input is undefined
            ValueError: If input is empty
        """
        if input == None:
            raise ValueError(input_display + " input cannot be undefined")

        if input == "":
            raise ValueError(input_display + " input cannot be empty")