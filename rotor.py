from string import ascii_uppercase
from typing import Union, NoReturn


class Rotor:
    _ALPHABET = tuple(char for char in ascii_uppercase)
    _WIRING = None
    _NOTCH = None
    _ASCII_VALUE_OF_CAPITAL_A = ord("A")

    def __init__(self):
        self._ring_setting = 1
        self._position = 1

    def _convert_char_position_to_int(self, char: str):
        return self._ALPHABET.index(char) + 1

    def set_position(self, position: Union[int, str]) -> NoReturn:
        self._position = self._convert_char_position_to_int(position) if type(position) == str else position

    def get_position(self):
        return self._position

    def get_position_as_char(self):
        return self._ALPHABET[self._position - 1]

    def set_ring_setting(self, ring_position: int):
        self._ring_setting = ring_position

    def get_ring_setting(self):
        return self._ring_setting

    def turn_rotor(self):
        self._position = (self._position % 26) + 1

    def encode_right_to_left(self, character: str) -> str:
        shift = self._position - self._ring_setting
        character = self.shift_character_in_alphabet(character, shift)
        character = self._WIRING[self._ALPHABET.index(character)]
        return self.shift_character_in_alphabet(character, -shift)

    def encode_left_to_right(self, character: str) -> str:
        shift = self._position - self._ring_setting
        character = self.shift_character_in_alphabet(character, shift)
        character = self._ALPHABET[self._WIRING.index(character)]
        return self.shift_character_in_alphabet(character, -shift)

    def shift_character_in_alphabet(self, char: str, shift: int):
        place_in_alphabet = (ord(char) + shift - self._ASCII_VALUE_OF_CAPITAL_A) % 26
        ascii_value_of_character = place_in_alphabet + self._ASCII_VALUE_OF_CAPITAL_A
        return chr(ascii_value_of_character)

    def is_at_notch(self):
        return self._NOTCH == self._ALPHABET[self._position - 1]


class RotorI(Rotor):
    _WIRING = tuple(char for char in "EKMFLGDQVZNTOWYHXUSPAIBRCJ")
    _NOTCH = "Q"


class RotorII(Rotor):
    _WIRING = tuple(char for char in "AJDKSIRUXBLHWTMCQGZNPYFVOE")
    _NOTCH = "E"


class RotorIII(Rotor):
    _WIRING = tuple(char for char in "BDFHJLCPRTXVZNYEIWGAKMUSQO")
    _NOTCH = "V"


class RotorIV(Rotor):
    _WIRING = tuple(char for char in "ESOVPZJAYQUIRHXLNFTGKDCMWB")
    _NOTCH = "J"


class RotorV(Rotor):
    _WIRING = tuple(char for char in "VZBRGITYUPSDNHLXAWMJQOFECK")
    _NOTCH = "Z"


class ReflectorA(Rotor):
    _WIRING = tuple(char for char in "EJMZALYXVBWFCRQUONTSPIKHGD")


class ReflectorB(Rotor):
    _WIRING = tuple(char for char in "YRUHQSLDPXNGOKMIEBFZCWVJAT")


class ReflectorC(Rotor):
    _WIRING = tuple(char for char in "FVPJIAOYEDRZXWGCTKUQSBNMHL")


class RotorGamma(Rotor):
    _WIRING = tuple(char for char in "FSOKANUERHMBTIYCWLQPZXVGJD")


class RotorBeta(Rotor):
    _WIRING = tuple(char for char in "LEYJVCNIXWPBQMDRTAKZGFUHOS")
