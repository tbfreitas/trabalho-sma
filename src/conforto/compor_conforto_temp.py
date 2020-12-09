from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
from src.message import message_conforto
import json

from datetime import datetime

class ComportConfortoTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportConfortoTemporal, self).__init__(agent, time)
       
    def on_time(self):
        super(ComportConfortoTemporal, self).on_time()
        self.agent.send(message_conforto)

 