
from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaContractNetProtocol

from src.sensor.comport_seg import CompRequest2
from src.sensor.comport_ter import ComportTemporal

class Sensors(Agent):
    def __init__(self, aid, caminho):

        super(Sensors, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World')

        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name='autonomo'))
        message.set_content('time')

        self.comport_request = CompRequest2(self, message)
        self.comport_temp = ComportTemporal(self, 5.0, message)

        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)