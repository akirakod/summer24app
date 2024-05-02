from datetime import datetime
from enumtypes import *
from partcharacteristics import *
from inventorymanager import *

def displayMenu():
    """
    Displays the menu options for the inventory management system.
    """
    print("\nInventory Management System")
    print("1. Add Part")
    print("2. Add Inventory")
    print("3. View Inventory")
    print("4. Search Parts")
    print("5. Delete Part")
    print("6. Exit")

def addPart(inventoryManager):
    """
    Adds a new part to the inventory.

    Args:
        inventoryManager (InventoryManager): An instance of the InventoryManager class.
    """
    sku = int(input("Enter SKU: "))
    part_type = input("Enter Part Type (Resistor/Solder/Wire/Display Cable/Ethernet Cable): ").lower()

    if part_type == "resistor":
        resistance = int(input("Enter Resistance (Ohms): "))
        tolerance = int(input("Enter Tolerance (%): "))
        part = Resistor(sku=sku, last_updated=datetime.now(), resistance=resistance, tolerance=tolerance)
    elif part_type == "solder":
        solder_type = input("Enter Solder Type (Lead/Lead-Free/Rosin-Core/Acid-Core): ")
        length = float(input("Enter Length (inches): "))
        part = Solder(sku=sku, last_updated=datetime.now(), solder_type=SolderType[solder_type.upper()], length=length)
    elif part_type == "wire":
        gauge = float(input("Enter Gauge: "))
        length = float(input("Enter Length (inches): "))
        part = Wire(sku=sku, last_updated=datetime.now(), gauge=gauge, length=length)
    elif part_type == "display cable":
        cable_type = input("Enter Cable Type (HDMI/VGA/DISPLAYPORT/MICRO HDMI): ")
        length = float(input("Enter Length (inches): "))
        color = input("Enter Color (Hexadecimal format, e.g., #RRGGBB): ")
        part = DisplayCable(sku=sku, last_updated=datetime.now(), cable_type=DisplayType[cable_type.upper()], length=length, color=color)
    elif part_type == "ethernet cable":
        alpha_type = input("Enter Alpha Type (MALE/FEMALE): ")
        beta_type = input("Enter Beta Type (MALE/FEMALE): ")
        speed = input("Enter Speed (10MBPS/100MBPS/1GBPS/10GBPS): ")
        length = float(input("Enter Length (inches): "))
        part = EthernetCable(sku=sku, last_updated=datetime.now(), alpha_type=EthernetAlphaType[alpha_type.upper()], beta_type=EthernetBetaType[beta_type.upper()], speed=EthernetSpeed[speed.upper()], length=length)
    else:
        print("Invalid part type.")
        return

    inventoryManager.addPart(part)
    print("Part added successfully.")

def addInventory(inventoryManager):
    """
    Adds inventory for an existing part.

    Args:
        inventoryManager (InventoryManager): An instance of the InventoryManager class.
    """
    sku = int(input("Enter SKU of the part: "))
    quantity = int(input("Enter quantity to add: "))
    try:
        inventoryManager.addInventory(sku, quantity)
        print("Inventory updated successfully.")
    except ValueError as e:
        print(e)

def viewInventory(inventoryManager):
    """
    Displays the current inventory.

    Args:
        inventoryManager (InventoryManager): An instance of the InventoryManager class.
    """
    inventory = inventoryManager.getInventory()
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for sku, part in inventory.items():
            print(f"SKU: {sku}, Part: {part.__class__.__name__}, Quantity: {part.quantity}")

def searchParts(inventoryManager):
    """
    Searches for parts based on user-specified criteria.

    Args:
        inventoryManager (InventoryManager): An instance of the InventoryManager class.
    """
    partType = input("Enter Part Type (Resistor/Solder/Wire/Display Cable/Ethernet Cable): ")
    criteria = input("Enter Search Criteria (e.g., resistance=100 for resistors): ")
    try:
        partClass = globals()[partType]
        criteriaDict = dict([criteria.split("=")])
        results = inventoryManager.search(partClass, **criteriaDict)
        if results:
            print("\nSearch Results:")
            for result in results:
                print(result)
        else:
            print("No matching parts found.")
    except KeyError:
        print("Invalid part type.")

def deletePart(inventoryManager):
    """
    Deletes a part from the inventory.

    Args:
        inventoryManager (InventoryManager): An instance of the InventoryManager class.
    """
    sku = int(input("Enter SKU of the part to delete: "))
    try:
        inventoryManager.deletePart(sku)
        print("Part deleted successfully.")
    except ValueError as e:
        print(e)

def main():
    """
    Main function to run the inventory management system.
    """
    inventoryManager = InventoryManager()

    while True:
        displayMenu()
        choice = input("Enter your choice: ")

        if choice == "1":
            addPart(inventoryManager)
        elif choice == "2":
            addInventory(inventoryManager)
        elif choice == "3":
            viewInventory(inventoryManager)
        elif choice == "4":
            searchParts(inventoryManager)
        elif choice == "5":
            deletePart(inventoryManager)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()