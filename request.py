from pade.misc.utility import display_message
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import FipaRequestProtocol
from pade.behaviours.protocols import TimedBehaviour

from datetime import datetime

class CompRequest(FipaRequestProtocol):
    """Comportamento FIPA Request
    do agente Horario"""
    def __init__(self, agent):
        super(CompRequest, self).__init__(agent=agent,
                                          message=None,
                                          is_initiator=False)

    def handle_request(self, message):
        super(CompRequest, self).handle_request(message)
        display_message(self.agent.aid.localname, 'mensagem request recebida')
        now = datetime.now()
        reply = message.create_reply()
        reply.set_performative(ACLMessage.INFORM)
        reply.set_content(now.strftime('%d/%m/%Y - %H:%M:%S'))
        self.agent.send(reply)