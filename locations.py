from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, LocationProgressType

from . import items

from . import data

if TYPE_CHECKING:
    from .world import Crash3World

levelNameToId = {
    #Level set 1
    "Toad Village": 0x1E,
    "Under Presssure": 0x0E,
    "Orient Express": 0x19,
    "Bone Yard": 0x1F,
    "Makin' Waves": 0x18,

    #Boss 1
    "Tiny Tiger": 0x06,

    #Level set 2
    "Gee Wiz": 0x11,
    "Hang'em High": 0x20,
    "Hog Ride": 0x1D,
    "Tomb Time": 0x1B,
    "Midnight Run": 0x23,

    #Boss 2
    "Dingodile": 0x08,

    #Level set 3
    "Plant Food": 0x21,
    "Sewer or Later": 0x0A,
    "Bear Down": 0x22,
    "Road to Ruin": 0x16,
    "Un-Bearable": 0x17,

    #Boss 3
    "Tiny Tiger": 0x03,

    #Level set 4
    "Hangin' Out": 0x0D,
    "Diggin' It": 0x15,
    "Cold Hard Crash": 0x13,
    "Ruination": 0x0F,
    "Bee-Having": 0x24,

    #Boss 4
    "Dr. N. Gin": 0x09,

    #Level set 5
    "Piston it Away": 0x10,
    "Rock It": 0x12,
    "Night Fight": 0x0C,
    "Pack Attack": 0x1A,
    "Spaced Out": 0x26,

    #Final Boss
    "Dr. Neo Cortex": 0x07,
    "Totally Bear": 0x25,
    "Totally Fly": 0x27,
}
