from enum import Enum

class EthernetAlphaType(Enum):
    """

    Attributes:
        MALE: Represents a male alpha connector.
        FEMALE: Represents a female alpha connector.
    """

    MALE = "male"
    FEMALE = "female"

class EthernetBetaType(Enum):
    """    

    Attributes:
        MALE: Represents a male beta connector.
        FEMALE: Represents a female beta connector.
    """

    MALE = "male"
    FEMALE = "female"

class EthernetSpeed(Enum):
    """
    
    Attributes:
        _10MBPS: Represents a speed rating of 10 Mbps.
        _100MBPS: Represents a speed rating of 100 Mbps.
        _1GBPS: Represents a speed rating of 1 Gbps.
        _10GBPS: Represents a speed rating of 10 Gbps.
    """

    _10MBPS = "10mbps"
    _100MBPS = "100mbps"
    _1GBPS = "1gbps"
    _10GBPS = "10gbps"

class DisplayType(Enum):
    """

    Attributes:
        HDMI: Represents an HDMI display cable.
        VGA: Represents a VGA display cable.
        DISPLAYPORT: Represents a DisplayPort display cable.
        MICRO_HDMI: Represents a micro HDMI display cable.
    """

    HDMI = "hdmi"
    VGA = "vga"
    DISPLAYPORT = "displayport"
    MICRO_HDMI = "micro-hdmi"

class SolderType(Enum):
    """

    Attributes:
        LEAD: Represents lead-based solder.
        LEAD_FREE: Represents lead-free solder.
        ROSIN_CORE: Represents rosin-core solder.
        ACID_CORE: Represents acid-core solder.
    """

    LEAD = "lead"
    LEAD_FREE = "lead-free"
    ROSIN_CORE = "rosin-core"
    ACID_CORE = "acid-core"
