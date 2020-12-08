from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
import random

from src.autonomo.message import message_novo 
import json

from datetime import datetime

def decideMelhorCaminho(disp):
    
    maior = []
    indexesMaior = 0
    for d in disp:
        if d[0] + d[1] > indexesMaior:
            indexesMaior = d[0] + d[1]
            maior = d
    
    return maior
     

class CompRequest2(FipaRequestProtocol):
    """Comportamento FIPA Request
    do agente Relogio"""
    def __init__(self, agent, caminho):
        super(CompRequest2, self).__init__(agent=agent,
                                           is_initiator=True)
        self.caminho = caminho

    def handle_inform(self, message):
        disponiveis = json.loads(message.content)

        if json.loads(message.content) == [6,6]:
            self.agent.pause_agent()

 
        disp = disponiveis['disponiveis']
        print('valor disponiveis' , disp)
        melhor = decideMelhorCaminho(disp)
        print('Decidi andar para o ', melhor)
        message_novo.set_content(json.dumps(melhor))
        display_message(self.agent.aid.localname, message.content)