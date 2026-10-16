from plug_lead import PlugLead


class Plugboard:
    def __init__(self):
        self._plug_leads = list()

    def add(self, plug_lead: PlugLead):
        if len(self._plug_leads) == 10:
            raise ValueError("No more than 10 plug leads.")
        else:
            self._plug_leads.append(plug_lead)

    def encode(self, character: str):
        for plug_lead in self._plug_leads:
            character = plug_lead.encode(character)
        return character
