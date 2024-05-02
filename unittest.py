import unittest
from datetime import datetime
from partcharacteristics import *
from inventorymanager import *

class TestInventoryManager(unittest.TestCase):
    """

    This unit test suite contains several test cases to validate the functionality of the InventoryManager class.

    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.inventory_manager = InventoryManager()

    def testAddPart(self):
        """
        Test the addition of parts to the inventory.

        This test case checks if parts of different types such as Resistor & Solder can be added to the inventory.
        """
        # Test adding Resistor
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        self.inventory_manager.addPart(resistor)
        self.assertIn(1, self.inventory_manager.inventory)

        # Test adding Solder
        solder = Solder(sku=2, last_updated=datetime.now(), solder_type=SolderType.LEAD_FREE, length=1.5)
        self.inventory_manager.addPart(solder)
        self.assertIn(2, self.inventory_manager.inventory)

    def testAddInventory(self):
        """
        Test adding inventory to existing parts.

        This test case checks if inventory can be added to existing parts in the inventory.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        self.inventory_manager.addPart(resistor)

        # Test adding inventory for existing part
        self.inventory_manager.addInventory(1, 10)
        self.assertEqual(self.inventory_manager.getQuantity(1), 10)

        # Test adding inventory for non-existent part
        with self.assertRaises(ValueError):
            self.inventory_manager.addInventory(3, 5)

    def testGetQuantity(self):
        """
        Test retrieving the quantity of a part.

        This test case checks if the quantity of a part in the inventory can be retrieved.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        self.inventory_manager.addPart(resistor)

        # Test getting quantity for existing part
        self.inventory_manager.addInventory(1, 10)
        self.assertEqual(self.inventory_manager.getQuantity(1), 10)

        # Test getting quantity for non-existent part
        with self.assertRaises(ValueError):
            self.inventory_manager.getQuantity(3)

    def testGetInventory(self):
        """
        Test retrieving the entire inventory.

        This test case checks if the entire inventory can be retrieved as a dictionary.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        solder = Solder(sku=2, last_updated=datetime.now(), solder_type=SolderType.LEAD_FREE, length=1.5)
        self.inventory_manager.addPart(resistor)
        self.inventory_manager.addPart(solder)
        self.inventory_manager.addInventory(1, 10)
        self.inventory_manager.addInventory(2, 5)

        expected_inventory = {1: resistor, 2: solder}
        self.assertDictEqual(self.inventory_manager.getInventory(), expected_inventory)

    def testGetPart(self):
        """
        Test retrieving a specific part.

        This test case checks if a specific part can be retrieved from the inventory.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        self.inventory_manager.addPart(resistor)

        self.assertEqual(self.inventory_manager.getPart(1), resistor)

        # Test getting non-existent part
        with self.assertRaises(ValueError):
            self.inventory_manager.getPart(2)

    def testSearch(self):
        """
        Test searching for parts in the inventory.

        This test case checks if parts can be searched based on certain criteria.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        solder = Solder(sku=2, last_updated=datetime.now(), solder_type=SolderType.LEAD_FREE, length=1.5)
        self.inventory_manager.addPart(resistor)
        self.inventory_manager.addPart(solder)
        self.inventory_manager.addInventory(1, 10)
        self.inventory_manager.addInventory(2, 5)

        # Search for resistors with resistance = 100
        results = self.inventory_manager.search(Resistor, resistance=100)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], resistor)

    def testDeletePart(self):
        """
        Test deleting a part from the inventory.

        This test case checks if a part can be successfully deleted from the inventory.
        """
        resistor = Resistor(sku=1, last_updated=datetime.now(), resistance=100, tolerance=5)
        self.inventory_manager.addPart(resistor)
        self.assertIn(1, self.inventory_manager.inventory)

        self.inventory_manager.deletePart(1)
        self.assertNotIn(1, self.inventory_manager.inventory)

        # Test deleting non-existent part
        with self.assertRaises(ValueError):
            self.inventory_manager.deletePart(2)

if __name__ == '__main__':
    unittest.main()
