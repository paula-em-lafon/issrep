#!/usr/bin/env python
import pika
import sys
import json

from porcentajes import Porcentajes




def Envio(lectura):

    print "---> " , lectura.count(",1")
    cades = lectura.split(",")

    base = 2
    nohay  = cades.count(",1")

    dato = Porcentajes( base, nohay)


    print "Mensaje/////////////////////////"

	
	
	
	
    strRabbit = json.dumps(vars(dato))
	
	
	
    connection = pika.BlockingConnection(pika.ConnectionParameters(
	        host='localhost'))
    channel = connection.channel()
	
	
    #channel.exchange_declare(exchange='logs',type='fanout')
	
	
	
	
    if(strRabbit == ""):
        print "No hay nada que enviar"
    else:
	    print "Se va a enviar: ", json.dumps(vars(dato))
	    
	    message = ' '.join(sys.argv[1:]) or strRabbit
	    channel.basic_publish(exchange='fromcard',
	                      routing_key='',
	                      body=message)
	    print " [x] Sent %r" % (message,)

	    connection.close()


def Calculo(base, hay):
    y = (hay/base) * 100
    x = 100 - y



class Evento:

    def __init__(self, x, y):
        self.x=x
        self.y=y