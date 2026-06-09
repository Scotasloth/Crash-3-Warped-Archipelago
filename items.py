from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from Options import OptionError

if TYPE_CHECKING:
    from .world import Crash3World


# -------------------------
# ITEM TABLE
# -------------------------
ITEM_NAME_TO_ID = {
    "Crystal": 1,
    "Clear Gem": 2,
    "Blue Gem": 3,
    "Red Gem": 4,
    "Green Gem": 5,
    "Yellow Gem": 6,
    "Purple Gem": 7,

    "Life": 8,
    "Wumpa Fruit": 9,

    "Double Jump": 10,
    "Super Body Slam": 11,
    "Death Tornado Spin": 12,
    "Fruit Bazooka": 13,
    "Speed Shoes": 14,

    "Progressive Relic": 15,
    "Progressive Relic 2": 16,
    "Progressive Relic 3": 17,
}


# -------------------------
# CLASSIFICATIONS
# -------------------------
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Crystal": ItemClassification.progression,
    "Clear Gem": ItemClassification.progression,
    "Blue Gem": ItemClassification.progression,
    "Red Gem": ItemClassification.progression,
    "Green Gem": ItemClassification.progression,
    "Yellow Gem": ItemClassification.progression,
    "Purple Gem": ItemClassification.progression,

    "Life": ItemClassification.filler,
    "Wumpa Fruit": ItemClassification.filler,

    "Double Jump": ItemClassification.progression,
    "Super Body Slam": ItemClassification.progression,
    "Death Tornado Spin": ItemClassification.progression,
    "Fruit Bazooka": ItemClassification.progression,
    "Speed Shoes": ItemClassification.progression,

    "Progressive Relic": ItemClassification.progression,
    "Progressive Relic 2": ItemClassification.progression,
    "Progressive Relic 3": ItemClassification.progression,
}


class Crash3Item(Item):
    game = "crash3warped"


# -------------------------
# ITEM CREATION (Crash 2 style safety)
# -------------------------
def create_item(world: Crash3World, name: str):
    if name not in ITEM_NAME_TO_ID:
        raise OptionError(f"Unknown item: {name}")

    classification = DEFAULT_ITEM_CLASSIFICATIONS.get(
        name,
        ItemClassification.filler
    )

    return Crash3Item(name, classification, ITEM_NAME_TO_ID[name], world.player)


# -------------------------
# FILLER SYSTEM (Crash 2 pattern)
# -------------------------
def get_filler_item_name(world: Crash3World) -> str:
    # simple safe filler pool
    return world.random.choice([
        "Life",
        "Wumpa Fruit",
    ])


# -------------------------
# FULL ITEMPOOL BUILDER (CRASH 2 CORE LOGIC)
# -------------------------
def create_all_items(world: Crash3World) -> None:
    itempool: list[Item] = []

    # -------------------------
    # CORE ITEMS
    # -------------------------
    gems = [
        "Blue Gem",
        "Red Gem",
        "Green Gem",
        "Yellow Gem",
        "Purple Gem",
    ]

    for gem in gems:
        itempool.append(world.create_item(gem))

    # crystals equivalent (if you use them as progression)
    for _ in range(25):
        itempool.append(world.create_item("Clear Gem"))

    # -------------------------
    # ABILITIES
    # -------------------------
    abilities = [
        "Double Jump",
        "Super Body Slam",
        "Death Tornado Spin",
        "Fruit Bazooka",
        "Speed Shoes",
    ]

    for a in abilities:
        itempool.append(world.create_item(a))

    # -------------------------
    # RELICS (your progression system)
    # -------------------------
    relics = [
        "Progressive Relic",
        "Progressive Relic 2",
        "Progressive Relic 3",
    ]

    itempool += [world.create_item(r) for r in relics]

    # -------------------------
    # BALANCE AGAINST LOCATIONS (CRASH 2 CRITICAL PART)
    # -------------------------
    num_locations = len(world.multiworld.get_unfilled_locations(world.player))
    num_items = len(itempool)

    needed_filler = num_locations - num_items

    if needed_filler < 0:
        raise OptionError(
            f"Too many items ({num_items}) for locations ({num_locations})."
        )

    # -------------------------
    # FILLER (Crash 2 style)
    # -------------------------
    itempool += [
        world.create_item(get_filler_item_name(world))
        for _ in range(needed_filler)
    ]

    # -------------------------
    # SUBMIT ITEMPOOL
    # -------------------------
    world.multiworld.itempool += itempool