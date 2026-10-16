from string import ascii_uppercase
from typing import Tuple, Union, List, NoReturn

from plug_board import Plugboard
from rotor import Rotor


class EnigmaMachine:
    _ALPHABET = tuple(char for char in ascii_uppercase)

    def __init__(self, rotors: Tuple[Rotor, ...], reflector: Rotor, plug_board: Plugboard):
        self._place_rotors(rotors)
        self._reflector = reflector
        self._plug_board = plug_board

    def _place_rotors(self, rotors: Tuple[Rotor, ...]):
        self._left_rotor = rotors[0]
        self._middle_rotor = rotors[1]
        self._right_rotor = rotors[2]

    def get_positions(self):
        return [self._left_rotor.get_position(),
                self._middle_rotor.get_position(),
                self._right_rotor.get_position()]

    def set_positions(self, positions: Union[List[int], List[str]]) -> NoReturn:
        left_position, middle_position, right_position = positions
        self._left_rotor.set_position(left_position)
        self._middle_rotor.set_position(middle_position)
        self._right_rotor.set_position(right_position)

    def set_reflector(self, reflector: Rotor):
        self._reflector = reflector

    def set_left_rotor(self, rotor: Rotor):
        self._left_rotor = rotor

    def set_middle_rotor(self, rotor: Rotor):
        self._middle_rotor = rotor

    def set_right_rotor(self, rotor: Rotor):
        self._right_rotor = rotor

    def _turn_rotors(self):
        if self._middle_rotor.is_at_notch():
            self._left_rotor.turn_rotor()
            self._middle_rotor.turn_rotor()
        elif self._right_rotor.is_at_notch():
            self._middle_rotor.turn_rotor()
        self._right_rotor.turn_rotor()

    def encode(self, text) -> str:
        return "".join(self._encode_character(char) for char in text)

    def _encode_character(self, char: str) -> str:
        self._turn_rotors()
        char = self._plug_board.encode(char)
        char = self._right_rotor.encode_right_to_left(char)
        char = self._middle_rotor.encode_right_to_left(char)
        char = self._left_rotor.encode_right_to_left(char)
        char = self._reflector.encode_right_to_left(char)
        char = self._left_rotor.encode_left_to_right(char)
        char = self._middle_rotor.encode_left_to_right(char)
        char = self._right_rotor.encode_left_to_right(char)
        char = self._plug_board.encode(char)
        return char
