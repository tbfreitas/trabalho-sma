from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

import random

from sys import argv
from agent_1 import AgenteSistemaAutonomo

def __initializeWorld__():
    matrizCaminho = [] 
    indexesBuracos = [] # indexes dos buracos
    indexesBarricadas = [] # indexes das barricadas
    i = 0
    # sorteando os index de celulas com buraco
    while i < 3:   
        valCol = random.randint(0, 6)
        valLin = random.randint(0, 6)

        #  verificando se já existem aqueles indexesBuracos salvos 
        achou = [valCol,valLin] in indexesBuracos
        #  nao pode ter buraco no [0,0] nem no [6,6]
        if achou == False and (valCol + valLin != 0) and (valCol * valLin != 36): 
            tmp = []
            tmp.append(valCol)
            tmp.append(valLin)
            indexesBuracos.append(tmp)
            i+=1
    
    i=0
    # sorteando os indexes das barricadas
    while i < 3:
        valColBar = random.randint(0, 6)
        valLinBar = random.randint(0, 6)

        #  verificando se já existem aqueles indexesBuracos salvos 
        achouIndexBuraco = [valColBar,valLinBar] in indexesBuracos
        achouIndexBarrica = [valColBar,valLinBar] in indexesBarricadas
        #  nao pode ter buraco no [0,0] nem no [6,6]
        if achouIndexBuraco == False and achouIndexBarrica == False and (valColBar + valLinBar != 0) and (valColBar * valLinBar != 36): 
            tmp = []
            tmp.append(valColBar)
            tmp.append(valLinBar)
            indexesBarricadas.append(tmp)
            i+=1

    # preenchendo a matriz de caminho
    j = 0
    while j < 7:
        k = 0
        linha = []
        while k < 7:

            # verificando se já existem aqueles valores salvos 
            valorBuraco = [j,k] in indexesBuracos
            valorBarricada = [j,k] in indexesBarricadas

            if(valorBuraco):
                linha.append('0')
            else:
                if(valorBarricada):
                    linha.append('B')
                else:
                    linha.append(' ')

            k+=1
        matrizCaminho.append(linha)
        j+=1 
    
    return matrizCaminho

def main():

    AMS = {'name' : 'localhost', 'port' : 8000}
    set_ams(AMS['name'], AMS['port'])

    agentes = list()

    a = AgenteSistemaAutonomo(AID(name='autonomo'))
    a.ams = AMS
    agentes.append(a)

    start_loop(agentes)

if __name__ == '__main__':
    
    main()

   