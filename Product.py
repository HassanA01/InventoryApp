"""
This class will create all the products and set their specified attributes.
"""

import Brand


class Product:
    """
    Product will be an abstract class that will further specify into specific products which the user
    may add and modify to the inventory.

    Attributes common to All products:

    Brand - All products will have a brand. A NoName product will have the brand NoName
    """

    brand: Brand

    def __init__(self, product_brand: Brand):
        self.brand = product_brand


class Apparel(Product):
    """
    An apparel class for products that are apparel. These products will have more attributes specific to apparel.

    Attributes of an Apparel product:

    category: str - represents which is the target audience (Men, Women, Children, etc.)
    color: str - color of the apparel
    size: int - size of the apparel (Small, Medium, Large, etc.)
    apparel_type: str - the type of the apparel (Pants, Shirts, Shorts, etc.)
    """
    _apparel_type: str
    _category: str
    _color: str
    _size: int

    def __init__(self, brand):
        super().__init__(brand)

    def set_apparel_type(self):
        self._apparel_type = input(f'Please enter the type of apparel(Pants, Shirts, Shorts, etc: ')

    def set_color(self):
        self._color = input(f'Please enter the color of the item {self._apparel_type}: ')

    def set_category(self):
        self._category = input(f'Enter the category for this item')