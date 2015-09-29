#!/usr/bin/env python
import pika
import sys
import json


class Evento:

    def __init__(self, idt, ver, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10):
        self.idt=idt
        self.ver=ver
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.s6=s6
        self.s7=s7
        self.s8=s8
        self.s9=s9
        self.s10=s10

str = "04fe8, v10, 0,0,1,1,0,0,0,0,1,0"

cades = str.split(",")
print cades

evento=Evento(cades[0], cades[1], cades[2], cades[3], cades[4], cades[5], "0", "1", "0", "0", "0", "0")
strRabbit = json.dumps(vars(evento))



connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


#channel.exchange_declare(exchange='logs',type='fanout')




if(strRabbit == " "):
    print "No hay nada que enviar"
else:
    print "Se va a enviar: ", json.dumps(vars(evento))
    
    message = ' '.join(sys.argv[1:]) or strRabbit
    channel.basic_publish(exchange='fromcard',
                      routing_key='',
                      body=message)
    print " [x] Sent %r" % (message,)
connection.close()
