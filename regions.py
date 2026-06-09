from BaseClasses import Region, Location


def create_regions(world):
    multiworld = world.multiworld
    player = world.player

    menu = Region("Menu", player, multiworld)

    # ✔ create real location
    loc = Location(player, "Test Location 1", 1, menu)
    menu.locations.append(loc)

    multiworld.regions.append(menu)