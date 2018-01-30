"""
Codename generator.

Credits to projectcodename.com
"""
from hashlib import sha1
from random import choice
from argparse import ArgumentParser


ATTRIBUTES = [
    # Environ
    "desert", "tundra", "mountain", "space", "field", "urban",
    # Stealth and cunning
    "hidden", "covert", "uncanny", "scheming", "decisive", "untouchable",
    "stalking",
    # Volitility
    "rowdy", "dangerous", "explosive", "threatening", "warring", "deadly",
    "killer", "insane", "wild",
    # Needs correction
    "bad", "unnecessary", "unknown", "unexpected", "waning",
    # Organic Gems and materials
    "amber", "bone", "coral", "ivory", "jet", "nacre", "pearl", "obsidian",
    "glass",
    # Regular Gems
    "agate", "beryl", "diamond", "opal", "ruby", "onyx", "sapphire", "emerald",
    "jade",
    # Colors
    "red", "orange", "yellow", "green", "blue", "violet",
    # Unsorted
    "draconic", "wireless", "spinning", "falling", "orbiting", "hunting",
    "chasing", "searching", "revealing", "flying", "destroyed",
    "inconceivable", "tarnished"
]

OBJECTS = [
    # Large cats
    "panther", "wildcat", "tiger", "lion", "cheetah", "cougar", "leopard",
    # Snakes
    "viper", "cottonmouth", "python", "boa", "sidewinder", "cobra",
    # Other predators
    "grizzly", "jackal", "falcon",
    # Prey
    "wildebeest", "gazelle", "zebra", "elk", "moose", "deer", "stag", "pony",
    "koala", "sloth",
    # HORSES!
    "horse", "stallion", "foal", "colt", "mare", "yearling", "filly",
    "gelding",
    # Mythical creatures
    "mermaid", "unicorn", "fairy", "troll", "yeti", "pegasus", "griffin",
    "dragon",
    # Occupations
    "nomad", "wizard", "cleric", "pilot", "captain", "commander", "general",
    "major", "admiral", "chef", "inspector",
    # Technology
    "mainframe", "device", "motherboard", "network", "transistor", "packet",
    "robot", "android", "cyborg", "display", "battery", "memory", "disk",
    "cartridge", "tape", "camera", "projector",
    # Sea life
    "octopus", "lobster", "crab", "barnacle", "hammerhead", "orca", "piranha",
    # Weather
    "storm", "thunder", "lightning", "rain", "hail", "sun", "drought", "snow",
    "drizzle",
    # Musical
    "piano", "keyboard", "guitar", "trumpet", "trombone", "flute", "cornet",
    "horn", "tuba", "clarinet", "saxophone", "piccolo", "violin", "harp",
    "cello", "drum", "organ", "banjo", "rhythm", "beat", "sound", "song",
    # Tools
    "screwdiver", "sander", "lathe", "mill", "welder", "mask", "hammer",
    "drill", "compressor", "wrench", "mixer", "router", "vacuum",
    # Other
    "warning", "presence", "weapon", "player", "ink", "case", "cup", "chain",
    "door"
]


def codename(capitalize=False, uppercase=False, separator=' ', id=None):
    """
    Generate and return a codename consisting of adjective and noun.
    """
    if id:
        id_hash = sha1(id.strip().encode('utf-8')).hexdigest()
        seed1 = int(id_hash[:20], 16)
        seed2 = int(id_hash[20:], 16)
        words = [
            ATTRIBUTES[seed1 % len(ATTRIBUTES)],
            OBJECTS[seed2 % len(OBJECTS)]
        ]
    else:
        words = [choice(ATTRIBUTES), choice(OBJECTS)]
    if capitalize:
        words = list(map(str.capitalize, words))
    if uppercase:
        words = list(map(str.upper, words))
    return separator.join(words)


def main():
    """
    App entrypoint.
    """
    parser = ArgumentParser()
    parser.add_argument(
        '-c', '--capitalize',
        action='store_true',
        help='Capitalize words.'
    )
    parser.add_argument(
        '-u', '--uppercase',
        action='store_true',
        help='Upper-case each word.'
    )
    parser.add_argument(
        '-s', '--separator',
        help='String to use to join words. Defaults to whitespace.',
        default=' '
    )
    parser.add_argument(
        '-i', '--id',
        help='String to use as random seed for deterministic codenames.',
        default=None
    )
    args = parser.parse_args()
    print(codename(**vars(args)))


if __name__ == '__main__':
    main()
