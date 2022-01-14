"""
The global class which will contain everything the user needs to know.

A store the user creates. This class contains the backend data relevant to the user such as inventory data, etc.

User can create as many inventories as they want as seems satisfying to them.
"""
from typing import List, Optional

import Inventory


class Store:

    """
    Private Attributes:

    _name: str: Name of the users Store
    _inventory: List[Inventory] - The list containing all Users inventories in their store.
    _curr_inv: Optional[Inventory] - the inventory user is currently accessing.
    """
    _name: str
    _inventory: List[Inventory]
    _current_inventory: Optional[Inventory]

    def __init__(self):
        self.set_name()
        self.set_curr_inv()

    def set_name(self) -> None:
        """
        Setter for <self._name>
        :return: None
        """
        self._name = input("Enter new name for Store: ")

    def set_curr_inv(self, inv=None):
        """
        Setter for <self._curr_inv>
        :return: None
        """
        if inv is None:
            self._current_inventory = None
        else:
            self._current_inventory = inv

    def create_new_inventory(self) -> None:
        """
        Creates an inventory object and appends it to <self._inventory>
        :return: None
        """

        print(f'Created new inventory for Store {self.get_name()}')

    def get_name(self) -> str:
        """
        Getter for <self._name>
        :return: str
        """
        return self._name

    def get_inventory(self) -> List[Inventory]:
        """
        Getter for <self._inventory>
        :return: List[Inventory]
        """
        return self._inventory




