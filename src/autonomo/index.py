from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent

from src.autonomo.comport import CompRequest

class AgenteSistemaAutonomo(Agent):
    def __init__(self, aid,caminho):

        super(AgenteSistemaAutonomo, self).__init__(aid=aid, debug=False)

        self.comport_request = CompRequest(self)
        self.behaviours.append(self.comport_request)