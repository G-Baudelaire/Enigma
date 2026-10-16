from nose.tools import assert_raises

from enigma import create_enigma_machine, rotor_from_name
from plug_board import Plugboard
from plug_lead import PlugLead

lead = PlugLead("AG")
assert (lead.encode("A") == "G")
assert (lead.encode("D") == "D")

lead = PlugLead("DA")
assert (lead.encode("A") == "D")
assert (lead.encode("D") == "A")

assert_raises(ValueError, PlugLead, "AA")
plugboard = Plugboard()

plugboard.add(PlugLead("SZ"))
plugboard.add(PlugLead("GT"))
plugboard.add(PlugLead("DV"))
plugboard.add(PlugLead("KU"))

assert (plugboard.encode("K") == "U")
assert (plugboard.encode("A") == "A")
rotor = rotor_from_name("I")
assert (rotor.encode_right_to_left("A") == "E")
assert (rotor.encode_left_to_right("A") == "U")

# Below is an example test, you should test your code with more examples to ensure it works as descibed above.

# With _rotors I II III, reflector B, ring settings 01 01 01, and initial positions A A Z,
# encoding an A produces a U.
#
_rotors = "I II III"
reflector = "B"
ring_settings = "01 01 01"
initial_positions = "A A Z"

enigma = create_enigma_machine(_rotors, reflector, ring_settings, initial_positions)
output = enigma.encode("A")
assert (output == "U")

# Example 1
# Set up your enigma_package machine with _rotors `I II III`, reflector `B`, ring settings `01 01 01`, and initial positions `A A Z`.
# The plugboard should map the following pairs: `HL MO AJ CX BZ SR NI YW DG PK`.
# The result of encoding the string* `HELLOWORLD` should be `RFKTMBXVVW`.


rotors = "I II III"
reflector = "B"
ring_settings = "01 01 01"
initial_positions = "A A Z"
plugboard = ["HL", "MO", "AJ", "CX", "BZ", "SR", "NI", "YW", "DG", "PK"]
enigma_package = create_enigma_machine(rotors, reflector, ring_settings, initial_positions, plugboard)
output = enigma_package.encode("HELLOWORLD")
print(output)
assert (output == "RFKTMBXVVW")
