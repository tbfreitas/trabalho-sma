from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
import random
from src.message import updateIndex
import json

from datetime import datetime

def decideMelhorCaminho(disp):
    
    maior = []
    indexesMaior = -1
    for d in disp:
        if d[0] + d[1] > indexesMaior:
            indexesMaior = d[0] + d[1]
            maior = d
    
    return maior
     

class CompRequest2(FipaRequestProtocol):
    def __init__(self, agent):
        super(CompRequest2, self).__init__(agent=agent,
                                           is_initiator=True)

    def handle_inform(self, message):
        disponiveis = json.loads(message.content)
 
        disp = disponiveis['disponiveis']
        print('valor disponivel' , disp)
        melhor = decideMelhorCaminho(disp)
        print('Decidi andar para o ', melhor)
        # message_novo.set_content(json.dumps(melhor))
        updateIndex(json.dumps(melhor))
        # display_message(self.agent.aid.localname, message.content)