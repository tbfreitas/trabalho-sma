from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
import json

message_novo = ACLMessage(ACLMessage.REQUEST)
message_novo.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
message_novo.add_receiver(AID(name='sensor'))
message_novo.set_content(json.dumps([0,0]))