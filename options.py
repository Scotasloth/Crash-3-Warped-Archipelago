from dataclasses import dataclass

from Options import (
    Toggle,
    Range,
    Choice,
    DeathLink,
    PerGameCommonOptions,
    OptionGroup,
)


class ExampleToggle(Toggle):
    display_name = "Example Toggle"


class ExampleRange(Range):
    display_name = "Example Range"
    range_start = 0
    range_end = 100
    default = 50


class ExampleChoice(Choice):
    display_name = "Example Choice"
    option_disabled = 0
    option_enabled = 1
    default = option_disabled


@dataclass
class Crash3WarpedOptions(PerGameCommonOptions):
    example_toggle: ExampleToggle
    example_range: ExampleRange
    example_choice: ExampleChoice
    death_link: DeathLink


option_groups = [
    OptionGroup(
        "General",
        [ExampleToggle, ExampleRange, ExampleChoice, DeathLink],
    )
]