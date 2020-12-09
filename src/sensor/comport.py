from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

import json
from datetime import datetime

def printaLocAtual(caminho, locAtual, locNovo):

    linhaAtual = locAtual[0]
    colAtual = locAtual[1]

    linhaNovo = locNovo[0]
    colNovo = locNovo[1]

    caminho[linhaAtual][colAtual] = ' '
    caminho[linhaNovo][colNovo] = 'I'

    for c in caminho:
        print(c)

# pegando as celulas 
def getNextValues(caminho,indexes):

    linhaAtual = indexes[0]
    colAtual = indexes[1]

    rightValue = indexes[0] + 1
    leftValue = indexes[0] - 1 
    bottomValue = indexes[1] + 1
    topValue = indexes[1] - 1

    mapCaminho = {
        "disponiveis": [],
        "buracos": [],
        "barricadas" : []
    }

    if rightValue <= 6:
        if caminho[rightValue][colAtual] == ' ' or caminho[rightValue][colAtual] == 'I':
            mapCaminho['disponiveis'].append([rightValue,colAtual])
        else:
            if caminho[rightValue][colAtual] == '0':
                mapCaminho['buracos'].append([rightValue,colAtual])
            else:
                mapCaminho['barricadas'].append([rightValue,colAtual])


    if leftValue >= 0:
        if caminho[leftValue][colAtual] == ' ' or caminho[leftValue][colAtual] == 'I':
            mapCaminho['disponiveis'].append([leftValue, colAtual])
        else:
            if caminho[linhaAtual][topValue] == '0':
                mapCaminho['buracos'].append([leftValue, colAtual])
            else:
                mapCaminho['barricadas'].append([leftValue, colAtual])


    if topValue >= 0:
        if caminho[linhaAtual][topValue] == ' ' or caminho[linhaAtual][topValue] == 'I':
            mapCaminho['disponiveis'].append([linhaAtual, topValue])
        else:
            if caminho[linhaAtual][topValue] == '0':
                mapCaminho['buracos'].append([linhaAtual, topValue])
            else:
                mapCaminho['barricadas'].append([linhaAtual, topValue])


    if bottomValue <= 6:
        if caminho[linhaAtual][bottomValue] == ' ' or caminho[linhaAtual][bottomValue] == 'I': 
            mapCaminho['disponiveis'].append([linhaAtual, bottomValue])
        else:
            if caminho[linhaAtual][bottomValue] == '0':
                mapCaminho['buracos'].append([linhaAtual, bottomValue])
            else:
                mapCaminho['barricadas'].append([linhaAtual, bottomValue])

    # Se não houver caminho disponível, fica parado
    if not mapCaminho['disponiveis'] or (linhaAtual == 6 and colAtual == 6):
        mapCaminho['disponiveis'] = [[linhaAtual, colAtual]]

    return mapCaminho    


class CompRequest(FipaRequestProtocol):
    """Comportamento FIPA Request
    do agente Horario"""
    def __init__(self, agent, caminho):
        super(CompRequest, self).__init__(agent=agent,
                                          message=None,
                                          is_initiator=False)
        self.caminho = caminho
        self.locAtual = [0,0]

    def handle_request(self, message):
        super(CompRequest, self).handle_request(message)

        proximosValores = getNextValues(self.caminho, json.loads(message.content))

        if "conforto" not in message.sender.name:
            printaLocAtual(self.caminho, self.locAtual, json.loads(message.content))
            self.locAtual = json.loads(message.content)
       
        # display_message(self.agent.aid.localname, 'Mensagem request recebida pelo sensor')
        reply = message.create_reply()
        reply.set_performative(ACLMessage.INFORM)
        reply.set_content(json.dumps(proximosValores))

        self.agent.send(reply)