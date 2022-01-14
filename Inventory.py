"""
Class that handles the CRUD Functionality of the Inventory.
"""
from typing import List  # A library that allows user to enhance documentation

import Item
from Brand import Brand
from Product import Product


class Inventory:
    """
    Private Attributes
    ----------------------

    _items: List[Item] - a list that stores all the items in the inventory
    _name: str - Name for the inventory
    """

    _items: list
    _name: str

    def __init__(self) -> None:
        self._items = []
        self.set_name()
        print("Created a new Inventory", self.get_name())

    def set_name(self, name=None):
        if name is not None:
            self._name = name
        else:
            self._name = input("Please enter name of inventory: ")

    def __str__(self) -> str:
        return f'Items in inventory {self.get_name()}: {self.get_items()}'

    def add_item(self) -> bool:
        """
        adds Item to inventory
        :return: bool - True if item was added otherwise False
        """
        brand = Brand()
        item = Product(brand)

        if item:
            self._items.append(item)
            print("Item added to inventory.")
            return True
        else:
            print("Error: Item could not be added to inventory.")
            return False

    def add_more_than_one_item(self, items: List[Item]) -> None:
        """

        :param items: a list of items to be added to the inventory. <items> is a non-empty list.
        :return: None
        """
        self._items.extend(items)

    def view_items(self) -> None:
        print(self)

    def get_items(self) -> List[Item]:
        """

        :return: List of the items <self._items>
        """
        return self._items

    def get_name(self):
        """

        :return: Name attribute
        """
        return self._name

    def filter(self) -> None:
        """
        Main function for the filter feature.
        User will be able to filter inventory with various ways

        :return: None
        """
