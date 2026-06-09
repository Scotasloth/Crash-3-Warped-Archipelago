from BaseClasses import Region, Entrance


def create_regions(world):
    multiworld = world.multiworld
    player = world.player

    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    levels = [
        "Turtle Woods",
        "Snow Go",
        "Hang Eight",
        "The Pits",
        "Crash Dash",
        "Air Crash",
        "Bear It"
    ]

    previous = menu

    for name in levels:
        region = Region(name, player, multiworld)
        multiworld.regions.append(region)

        entrance = Entrance(f"{previous.name} -> {name}", previous)

        # ✅ ONLY THIS IS REQUIRED
        entrance.connect(region)

        previous.exits.append(entrance)

        previous = region

    final = Region("Final Area", player, multiworld)
    multiworld.regions.append(final)

    entrance = Entrance(f"{previous.name} -> Final Area", previous)

    entrance.connect(final)

    previous.exits.append(entrance)