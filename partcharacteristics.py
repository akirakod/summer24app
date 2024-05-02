import re
from enumtypes import *

class Part:
    """
    A base class representing a generic part.

    Attributes:
        sku (int): The Stock Keeping Unit (SKU) of the part.
        last_updated (datetime): The timestamp indicating the last update time of the part.
        quantity (int): The quantity of the part in inventory.
    """

    def __init__(self, sku, last_updated):
        """
        Initializes a new instance of the Part class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the part.
            last_updated (datetime): The timestamp indicating the last update time of the part.
        """
        self.__sku = sku  # Make sku private
        self.__last_updated = last_updated  # Make last_updated private
        self.quantity = 0

    # Getter methods for private variables
    def getSku(self):
        """
        Get the SKU of the part.

        Returns:
            int: The Stock Keeping Unit (SKU) of the part.
        """
        return self.__sku

    def getLastUpdated(self):
        """
        Get the last updated timestamp of the part.

        Returns:
            datetime: The timestamp indicating the last update time of the part.
        """
        return self.__last_updated

    # Setter methods for private variables (if needed)
    def setSku(self, sku):
        """
        Set the SKU of the part.

        Args:
            sku (int): The Stock Keeping Unit (SKU) to set.
        """
        self.__sku = sku

    def setLastUpdated(self, last_updated):
        """
        Set the last updated timestamp of the part.

        Args:
            last_updated (datetime): The timestamp indicating the last update time of the part.
        """
        self.__last_updated = last_updated

class Resistor(Part):
    """
    A class representing a resistor part, inheriting from Part.

    Attributes:
        resistance (int): The resistance value of the resistor in ohms.
        tolerance (int): The tolerance level of the resistor in percentage.
    """

    def __init__(self, sku, last_updated, resistance: int, tolerance: int):
        """
        Initializes a new instance of the Resistor class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the resistor.
            last_updated (datetime): The timestamp indicating the last update time of the resistor.
            resistance (int): The resistance value of the resistor in ohms.
            tolerance (int): The tolerance level of the resistor in percentage.
        """
        super().__init__(sku, last_updated)
        self.sku = sku
        self.resistance = resistance
        self.tolerance = tolerance

class Solder(Part):
    """
    A class representing a solder part, inheriting from Part.

    Attributes:
        solder_type (SolderType): The type of solder (e.g., lead-free).
        length (float): The length of the solder in inches.
    """

    def __init__(self, sku, last_updated, solder_type: SolderType, length: float):
        """
        Initializes a new instance of the Solder class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the solder.
            last_updated (datetime): The timestamp indicating the last update time of the solder.
            solder_type (SolderType): The type of solder (e.g., lead-free).
            length (float): The length of the solder in inches.
        """
        super().__init__(sku, last_updated)
        self.sku=sku
        self.solder_type = solder_type
        self.length = length

class Wire(Part):
    """
    A class representing a wire part, inheriting from Part.

    Attributes:
        gauge (float): The gauge of the wire.
        length (float): The length of the wire in inches.
    """

    def __init__(self, sku, last_updated, gauge: float, length: float):
        """
        Initializes a new instance of the Wire class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the wire.
            last_updated (datetime): The timestamp indicating the last update time of the wire.
            gauge (float): The gauge of the wire.
            length (float): The length of the wire in inches.
        """
        super().__init__(sku, last_updated)
        self.gauge = gauge
        self.length = length

class DisplayCable(Part):
    """
    A class representing a display cable part, inheriting from Part.

    Attributes:
        cable_type (DisplayType): The type of display cable.
        length (float): The length of the display cable in inches.
        color (str): The color of the display cable in hexadecimal format.
    """

    def __init__(self, sku, last_updated, cable_type: DisplayType, length: float, color):
        """
        Initializes a new instance of the DisplayCable class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the display cable.
            last_updated (datetime): The timestamp indicating the last update time of the display cable.
            cable_type (DisplayType): The type of display cable.
            length (float): The length of the display cable in inches.
            color (str): The color of the display cable in hexadecimal format.
        """
        super().__init__(sku, last_updated)
        self.cable_type = cable_type
        self.length = length
        if not re.match(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color):
            raise ValueError("Invalid color format")
        self.color = color

class EthernetCable(Part):
    """
    A class representing an ethernet cable part, inheriting from Part.

    Attributes:
        alpha_type (EthernetAlphaType): The type of the alpha connector of the ethernet cable.
        beta_type (EthernetBetaType): The type of the beta connector of the ethernet cable.
        speed (EthernetSpeed): The speed rating of the ethernet cable.
        length (float): The length of the ethernet cable in inches.
    """

    def __init__(self, sku, last_updated, alpha_type: EthernetAlphaType, beta_type: EthernetBetaType, speed: EthernetSpeed, length):
        """
        Initializes a new instance of the EthernetCable class.

        Args:
            sku (int): The Stock Keeping Unit (SKU) of the ethernet cable.
            last_updated (datetime): The timestamp indicating the last update time of the ethernet cable.
            alpha_type (EthernetAlphaType): The type of the alpha connector of the ethernet cable.
            beta_type (EthernetBetaType): The type of the beta connector of the ethernet cable.
            speed (EthernetSpeed): The speed rating of the ethernet cable.
            length (float): The length of the ethernet cable in inches.
        """
        super().__init__(sku, last_updated)
        self.alpha_type = alpha_type
        self.beta_type = beta_type
        self.speed = speed
        self.length = length