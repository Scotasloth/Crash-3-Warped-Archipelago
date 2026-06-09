from BaseClasses import Item, ItemClassification


class Crash3Item(Item):
    game = "crash3warped"


ITEM_NAME_TO_ID = {
    "Crash Gem": 1,
    "Extra Life": 2,
    "Aku Aku Mask": 3,
}


def create_item(world, name: str):
    item_id = ITEM_NAME_TO_ID[name]

    # simple classification logic (safe default)
    if name == "Crash Gem":
        classification = ItemClassification.progression
    else:
        classification = ItemClassification.filler

    return Crash3Item(name, classification, item_id, world.player)


def get_filler_item_name(world):
    return "Extra Life"