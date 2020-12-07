from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

import json
from datetime import datetime

# pegando as celulas 
def getNextValues(caminho,indexes):
    
    colAtual = indexes[0]
    linhaAtual = indexes[1]

    rightValue = indexes[0] + 1
    leftValue = indexes[0] - 1 
    bottomValue = indexes[1] + 1
    topValue = indexes[1] - 1

    mapCaminho = {
        "disponiveis": [],
        "buracos": [],
    }

    if rightValue <= 6:
        if caminho[rightValue][colAtual] == ' ':
            mapCaminho['disponiveis'].append([rightValue,colAtual])
        else:
            mapCaminho['buracos'].append([rightValue,colAtual])

    if leftValue >= 0:
        if caminho[leftValue][colAtual] == ' ':
            mapCaminho['disponiveis'].append([leftValue, colAtual])
        else:
            mapCaminho['buracos'].append([leftValue, colAtual])

    if topValue >= 0:
        if caminho[linhaAtual][topValue] == ' ':
            mapCaminho['disponiveis'].append([linhaAtual, topValue])
        else:
            mapCaminho['buracos'].append([linhaAtual, topValue])

    if topValue <= 6:
        if caminho[linhaAtual][bottomValue] == ' ':
            mapCaminho['disponiveis'].append([linhaAtual, bottomValue])
        else:
            mapCaminho['buracos'].append([linhaAtual, bottomValue])

    return mapCaminho    


class CompRequest(FipaRequestProtocol):
    """Comportamento FIPA Request
    do agente Horario"""
    def __init__(self, agent, caminho):
        super(CompRequest, self).__init__(agent=agent,
                                          message=None,
                                          is_initiator=False)
        self.caminho = caminho

    def handle_request(self, message):
        print(self)
        super(CompRequest, self).handle_request(message)
        # mes = json.loads(message)
        proximosValores = getNextValues(self.caminho, json.loads(message.content))

        print('valores disponiveis', proximosValores)
        display_message(self.agent.aid.localname, 'Mensagem request recebida pelo sensor')
        reply = message.create_reply()
        reply.set_performative(ACLMessage.INFORM)
        # reply.set_content(json.dumps(self.valores))
        reply.set_content(message.content)

        self.agent.send(reply)