
from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaContractNetProtocol

from src.sensor.comport_seg import CompRequest2
from src.sensor.comport_ter import ComportTemporal

# Pegando o indice atual do onibus
def getAtualIndex(caminho):
    for idx, col in enumerate(caminho):
        for idxlin, lin in enumerate(col):
            if(lin == 'I'):
                    return [idx,idxlin]

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

class Sensors(Agent):

    def __init__(self, aid, caminho):

        super(Sensors, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World')
        
        index = getAtualIndex(caminho)
        proximosValores = getNextValues(caminho,index)
        print(proximosValores)

        message = ACLMessage(ACLMessage.REQUEST)
        message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        message.add_receiver(AID(name='autonomo'))
        message.set_content('time')

        self.comport_request = CompRequest2(self, message)
        self.comport_temp = ComportTemporal(self, 5.0, message)

        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)
