from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour
import random

import json

from datetime import datetime

class ComportConforto(FipaRequestProtocol):
    def __init__(self, agent):
        super(ComportConforto, self).__init__(agent=agent,
                                           is_initiator=True)
        self.arCondicionado = False
        self.janelaAberta = True

    
    def handle_inform(self, message):
        obstaculos = json.loads(message.content)
        bur = obstaculos['buracos']
        bar = obstaculos['barricadas']
        
        print('Verificando se tem barricada próxima:', bar)
        if not bar:
            print("=>Não tem barricada próxima, portanto:")
            if self.arCondicionado == False:
                print("==>Ar condicionado continuará desligado")
            else:
                print("==> Desligando o ar condicionado")
        else:
            print("=>Opa, tem barricada próxima, portanto:")
            if self.arCondicionado == True:
                 print("==> Ar condicionado continuará ligado ")
            else:
                print("==> Ligando o ar condicionado")

        print('Verificando se tem buraco próximo: ', bar)
        if not bur:
            print("=>Não tem buraco próximo, portanto:")
            if self.janelaAberta == False:
                print("==>Abrindo a janela.")
            else:
                print("==>Janela continuará aberta.")
        else:
            print("=>Opa, buraco próximo, portanto:")
            if self.janelaAberta == False:
                 print("==>Janela continuará fechada")
            else:
                print("==>Fechando a janela...")
                    
        if bar:
            self.arCondicionado = True
        else:
            self.arCondicionado = False

        if bur:
            self.janelaAberta = False
        else:
            self.janelaAberta = True

        # display_message(self.agent.aid.localname, message.content)