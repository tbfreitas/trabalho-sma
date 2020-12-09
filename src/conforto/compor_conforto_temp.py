from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
from src.autonomo.message import message_conforto
import json

from datetime import datetime

class ComportConfortoTemporal(TimedBehaviour):
    """Comportamento FIPA Request
    do agente Relogio"""
    def __init__(self, agent, time, caminho):
        super(ComportConfortoTemporal, self).__init__(agent, time)
        self.caminho = caminho
       
    def on_time(self):
        super(ComportConfortoTemporal, self).on_time()
        self.agent.send(message_conforto)

 