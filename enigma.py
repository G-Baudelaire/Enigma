import itertools
import re
from time import time
from typing import Iterable

from enigma_machine import EnigmaMachine
from plug_board import Plugboard
from plug_lead import PlugLead
from rotor import *


def rotor_from_name(rotor_name: str, ring_setting: int = 1, position: Union[int, str] = 1) -> Rotor:
    rotor = {
        "I": RotorI(),
        "II": RotorII(),
        "III": RotorIII(),
        "IV": RotorIV(),
        "V": RotorV(),
        "Beta": RotorBeta(),
        "Gamma": RotorGamma(),
        "A": ReflectorA(),
        "B": ReflectorB(),
        "C": ReflectorC(),
    }[rotor_name]
    rotor.set_ring_setting(ring_setting)
    rotor.set_position(position)
    return rotor


#
# # method with returns an fully set up enigma_package machine object
# # @param - _rotors - string of the _rotors used in this enigma_package machine e.g. "I II III"
# # @param - reflector - string of the reflector used in this enigma_package machine e.g. "B"
# # @param - ring_settings - string of the ring settings for the _rotors, numbered from 01-26 e.g. "01 02 03"
# # @param - initial_positions - string of the starting positions of the _rotors, from A-Z e.g. "A A Z"
# # @param - plugboard_pairs - list of the plugboard pairs to be used, default is an empty list
def create_enigma_machine(
        rotors: str,
        reflector: str,
        ring_settings="1 1 1",
        initial_positions: str = "A A Z",
        plugboard_pairs: Iterable[str] = None):
    if plugboard_pairs is None:
        plugboard_pairs = tuple()

    rotor_objects = _create_rotors(rotors, ring_settings, initial_positions)
    reflector_object = rotor_from_name(reflector)
    plug_board = _create_plug_board(plugboard_pairs)
    return EnigmaMachine(rotor_objects, reflector_object, plug_board)


def _create_rotors(rotors: str, ring_settings: str, initial_positions: str):
    rotors = rotors.split()
    ring_settings = ring_settings.split()
    initial_positions = initial_positions.split()
    rotor_objects = list()
    for rotor_name, ring_setting, position in zip(rotors, ring_settings, initial_positions):
        rotor_objects.append(rotor_from_name(rotor_name, int(ring_setting), position))
    return tuple(rotor_objects)


def _create_plug_board(plugboard_pairs: Iterable[str]):
    plug_board = Plugboard()
    for pair in plugboard_pairs:
        plug_board.add(PlugLead(pair))
    return plug_board


# # Part 2 : functions to implement to demonstrate code breaking.
# # each function should return a list of all the possible answers
# # code_one provides an example of how you might declare variables and the return type
#
# def code_one():
#     # _rotors = "Beta Gamma V"
#     # reflector = "B"
#     # ring_settings = "23 02 10"
#     # # initial_positions are unknown
#     # plugboard = ["KI", "XN", "FL"]
#     #
#     # code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
#     # crib = "UNIVERSITY"
#
#     positions_generator = itertools.product(ascii_uppercase, repeat=3)
#     return [code]

def code_one():
    _rotors = "Beta Gamma V"
    ring_settings = "04 02 14"
    initial_positions = "M J M"
    plugboard = ["KI", "XN", "FL"]

    code = "DMEXBMKYCVPNQBEDHXVPZGKMTFFBJRPJTLHLCHOTKOYXGGHZ"
    crib = "SECRETS"

    potential_decodes = list()
    for reflector in "ABC":
        enigma_machine = create_enigma_machine(_rotors, reflector, ring_settings, initial_positions, plugboard)
        decoded_string = enigma_machine.encode(code)
        if crib in decoded_string:
            potential_decodes.append(decoded_string)
    return potential_decodes


def code_two():
    time1 = time()
    _rotors = "Beta I III"
    ring_settings = "23 02 10"
    plugboard = ["VH", "PT", "ZG", "BJ", "EY", "FS"]
    reflector = "B"
    code = "CMFSUPKNCBMUYEQVVDYKLRQZTPUFHSWWAKTUGXMPAMYAFITXIJKMH"
    crib = "UNIVERSITY"

    enigma_machine = create_enigma_machine(
        rotors=_rotors,
        reflector=reflector,
        ring_settings=ring_settings,
        plugboard_pairs=plugboard)

    potential_decodes = list()
    for initial_positions in itertools.product(ascii_uppercase, repeat=3):
        enigma_machine.set_positions(initial_positions)
        decoded_string = enigma_machine.encode(code)
        if re.search(crib, decoded_string):
            potential_decodes.append(decoded_string)
        # if crib in decoded_string:
        #     potential_decodes.append(decoded_string)
    time2 = time()
    print(time2 - time1)
    return potential_decodes


#
def code_three():
    return []
#
#
# def code_four():
#     return []
#
#
# def code_five():
#     return []


if __name__ == "__main__":
    print(code_one())
    print(code_two())
