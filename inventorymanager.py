from datetime import datetime

class InventoryManager:
    """
    A class representing an inventory manager.

    This class manages the inventory of various parts, allowing for addition, deletion, and retrieval of parts,
    as well as searching for specific parts based on certain criteria.

    Attributes:
        inventory (dict): A dictionary containing the inventory, where the keys are SKUs (Stock Keeping Units)
            and the values are instances of Part subclasses representing the parts in the inventory.
    """

    def __init__(self):
        """
        Initializes a new instance of the InventoryManager class.

        The inventory is initially empty.
        """
        self.inventory = {}

    def addPart(self, part):
        """
        Add a part to the inventory.

        Args:
            part (Part): The part to be added to the inventory.
        """
        self.inventory[part.sku] = part

    def addInventory(self, sku, quantity):
        """
        Add inventory for a specific part.

        Args:
            sku (int): The SKU (Stock Keeping Unit) of the part.
            quantity (int): The quantity of the part to be added to the inventory.

        Raises:
            ValueError: If the part with the specified SKU is not found in the inventory.
        """
        if sku in self.inventory:
            self.inventory[sku].last_updated = datetime.now()
            self.inventory[sku].quantity += quantity  # Update quantity directly
        else:
            raise ValueError("Part not found in inventory.")

    def getQuantity(self, sku):
        """
        Get the quantity of a specific part in the inventory.

        Args:
            sku (int): The SKU (Stock Keeping Unit) of the part.

        Returns:
            int: The quantity of the part in the inventory.

        Raises:
            ValueError: If the part with the specified SKU is not found in the inventory.
        """
        if sku in self.inventory:
            return self.inventory[sku].quantity
        else:
            raise ValueError("Part not found in inventory.")

    def getInventory(self):
        """
        Get the entire inventory.

        Returns:
            dict: A dictionary containing the inventory, where the keys are SKUs and the values are instances
            of Part subclasses representing the parts in the inventory.
        """
        return self.inventory

    def getPart(self, sku):
        """
        Get a specific part from the inventory.

        Args:
            sku (int): The SKU (Stock Keeping Unit) of the part.

        Returns:
            Part: The part with the specified SKU.

        Raises:
            ValueError: If the part with the specified SKU is not found in the inventory.
        """
        if sku in self.inventory:
            return self.inventory[sku]
        else:
            raise ValueError("Error, Part not found in inventory.")

    def search(self, part_class, **kwargs):
        """
        Search for parts in the inventory based on certain criteria.

        Args:
            part_class (class): The class of the part to search for (e.g., Resistor, Solder).
            **kwargs: Keyword arguments representing search criteria (e.g., resistance=100 for searching resistors with resistance 100).

        Returns:
            list: A list of parts matching the search criteria.
        """
        results = []
        for sku, part in self.inventory.items():
            if isinstance(part, part_class):
                match = True
                for key, value in kwargs.items():
                    if not hasattr(part, key) or getattr(part, key) != value:
                        match = False
                        break
                if match:
                    results.append(part)
        return results

    def deletePart(self, sku):
        """
        Delete a part from the inventory.

        Args:
            sku (int): The SKU (Stock Keeping Unit) of the part to delete.

        Raises:
            ValueError: If the part with the specified SKU is not found in the inventory.
        """
        if sku in self.inventory:
            del self.inventory[sku]
        else:
            raise ValueError("Error, Part not found in inventory.")
