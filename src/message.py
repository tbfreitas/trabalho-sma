from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
import json

index = [0,0]

message_autonomo = ACLMessage(ACLMessage.REQUEST)
message_autonomo.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
message_autonomo.add_receiver(AID(name='sensor'))
message_autonomo.set_content(json.dumps(index))

message_conforto = ACLMessage(ACLMessage.REQUEST)
message_conforto.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
message_conforto.add_receiver(AID(name='sensor'))
message_conforto.set_content(json.dumps(index))

def updateIndex(NewValue):
    message_autonomo.set_content(NewValue)
    message_conforto.set_content(NewValue)

