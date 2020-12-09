from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

from src.conforto.compor_conforto_temp import ComportConfortoTemporal
from src.conforto.compor_conforto import ComportConforto

class AgenteSistemaConforto(Agent):
    def __init__(self, aid):
        super(AgenteSistemaConforto, self).__init__(aid=aid)

        self.comport_request = ComportConforto(self)
        self.comport_temp = ComportConfortoTemporal(self, 5.0)
        
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)
    
