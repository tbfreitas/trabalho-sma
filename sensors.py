from pade.misc.utility import display_message, start_loop
from pade.core.agent import Agent

class Sensors(Agent):
    def __init__(self, aid, caminho):

        super(Sensors, self).__init__(aid=aid)
        display_message(self.aid.localname, 'Hello World')

