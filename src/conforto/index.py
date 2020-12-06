from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID


class AgenteSistemaConforto(Agent):
    def __init__(self, aid,caminho):
        super(AgenteSistemaConforto, self).__init__(aid=aid)
