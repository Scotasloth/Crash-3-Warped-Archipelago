from . import options  # IMPORTANT: forces registration in 0.6.7
from typing import Any, Mapping
from worlds.AutoWorld import World, WebWorld

from . import items, locations, regions, rules


class Crash3World(World):
    game = "crash3warped"
    name = "Crash Bandicoot 3: Warped"

    web = WebWorld()

    options_dataclass = options.Crash3WarpedOptions
    options: options.Crash3WarpedOptions

    item_name_to_id = items.ITEM_NAME_TO_ID
    location_name_to_id = locations.LOCATION_NAME_TO_ID

    origin_region_name = "Menu"

    # -------------------------
    # Init (safe for AP 0.6.7)
    # -------------------------
    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    # -------------------------
    # Generation hooks
    # -------------------------
    def create_regions(self):
        regions.create_regions(self)

    def create_items(self):
        for item_name in items.ITEM_NAME_TO_ID.keys():
            item = items.create_item(self, item_name)
            self.multiworld.itempool.append(item)

    def create_item(self, name: str):
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return "Extra Life"

    def set_rules(self):
        rules.set_rules(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict()