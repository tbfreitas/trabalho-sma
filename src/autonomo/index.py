from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

from src.autonomo.comport_seg import CompRequest2
from src.autonomo.comport_ter import ComportTemporal

import json

# update no caminho

# Pegando o indice atual do onibus
def getAtualIndex(caminho):
    for idx, col in enumerate(caminho):
        for idxlin, lin in enumerate(col):
            if(lin == 'I'):
                    return [idx,idxlin]

class AgenteSistemaAutonomo(Agent):
    def __init__(self, aid,caminho):

        super(AgenteSistemaAutonomo, self).__init__(aid=aid, debug=False)

        indiceAtual = getAtualIndex(caminho)

        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name='sensor'))
        message.set_content(json.dumps(indiceAtual))

        self.comport_request = CompRequest2(self, message)
        self.comport_temp = ComportTemporal(self, 2.0, message)
        
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)