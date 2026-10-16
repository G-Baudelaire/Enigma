class PlugLead:
    def __init__(self, mapping: str):
        mapping.upper()
        if len(mapping) != 2:
            raise ValueError(f"Invalid mapping '{mapping}'. Must be of length 2.")
        elif mapping[0] == mapping[1]:
            raise ValueError("PlugLead cannot connect to the same socket twice")
        elif not mapping.isalpha():
            raise ValueError("Invalid mapping")
        self._socket1 = mapping[0]
        self._socket2 = mapping[1]

    def encode(self, character: str):
        if self._socket1 == character:
            return self._socket2
        elif self._socket2 == character:
            return self._socket1
        else:
            return character

