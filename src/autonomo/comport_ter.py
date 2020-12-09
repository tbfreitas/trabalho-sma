from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
from src.message import message_autonomo
import json

from datetime import datetime


class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)
       
    def on_time(self):
        super(ComportTemporal, self).on_time()
        self.agent.send(message_autonomo)

 