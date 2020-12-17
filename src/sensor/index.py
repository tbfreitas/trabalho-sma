
from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaContractNetProtocol

from src.sensor.comport import CompRequest

class Sensors(Agent):

    def __init__(self, aid, caminho):

        super(Sensors, self).__init__(aid=aid)
        
        self.comport_request = CompRequest(self,caminho)
        self.behaviours.append(self.comport_request)