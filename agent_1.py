from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent

class AgenteSistemaAutonomo(Agent):
    def __init__(self, aid):
        super(AgenteSistemaAutonomo, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World!')
