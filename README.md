# Enigma

An archived Python implementation of the Enigma machine (rotors, reflectors and plugboard).

Written during my second year of university.

## Usage

Requires Python 3. `main.py` also needs `nose` (`pip install nose`) for its tests.

```python
from enigma import create_enigma_machine

machine = create_enigma_machine(
    rotors="I II III",            # supported: I-V, Beta, Gamma
    reflector="B",                # supported: A, B, C
    ring_settings="01 01 01",
    initial_positions="A A Z",
    plugboard_pairs=["HL", "MO", "AJ", "CX", "BZ", "SR", "NI", "YW", "DG", "PK"],
)

print(machine.encode("HELLOWORLD"))  # RFKTMBXVVW
```

Input must be uppercase letters (A-Z). To decrypt, create a machine with the same settings and encode the ciphertext.

Run the included example checks with:

```
python main.py
```
