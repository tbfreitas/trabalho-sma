from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

from src.autonomo.comport_seg import CompRequest2
from src.autonomo.comport_ter import ComportTemporal

import json

# update no caminho

class AgenteSistemaAutonomo(Agent):
    def __init__(self, aid):

        super(AgenteSistemaAutonomo, self).__init__(aid=aid, debug=False)

        self.comport_request = CompRequest2(self)
        self.comport_temp = ComportTemporal(self, 10.0)
        
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)
    