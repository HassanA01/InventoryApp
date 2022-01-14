"""
This class will focus on the Brands that the inventory currently holds.
This will be useful for various features such as filtering inventory,
ensuring a clean inventory, etc.
"""


class Brand:
    """
    Attributes:

        name: str - name of brand:
    """

    name: str

    def __init__(self) -> None:
        self.set_name()

    def set_name(self):
        """
        Setter for brand name.
        :return:
        """
        self.name = input("Enter name of Brand:")
