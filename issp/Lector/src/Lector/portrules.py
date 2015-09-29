import re
from ThreadLectura import ReadingThread

from ChecaPuertos import ChkPort
import br
import pika
'''
    cosas por hacer en el main, recordar hacerlas
    TODO una vez listo el proceso para mandarse por la API por JSON juntar todo
    con asyncIO
'''


patterns = r"^\w{5},V\d{2}(,[0-1]+){10}$" #pattern list

class emitMsg():

	def __init__(self, con):
		self.connection = con
		self.channel = self.connection.channel()

	def emit(self, msg):
		self.channel.basic_publish(exchange='fromcard', routing_key='', body=msg)
		print (" [x] Sent %r" % (msg,))



class IterPat:

    #variables declaradas
    pat2 = ""
    lec = ""

    def __init__(self, lect, pat = patterns):
        self.pat2 = pat  # lista de patrones posibles para sensores
        self.lect = str(lect)  # lectura siendo analizada
        #self.patLen = len(pat)  #Largo de patrones // no sabemos si lo usaremos
        print(lect)


    def Iterar(self):

        for self.iteracion in self.pat2:
            
            
            #prog = re.compile(self.pat2)
            #comp = prog.match(self.iteracion)
            #print(comp)
            comp = re.match(self.pat2,lectura)
            if comp == True:
                re_value = (self.pattern, self.lect)
                return re_value
            else:
                return

    #jsjsjs

            
def main():

    parameters = pika.URLParameters("amqp://guest:guest@localhost:5672/%2F")

    conn = pika.BlockingConnection(parameters)
    #conn = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
    dbr = emitMsg(conn)



    cps = ChkPort()
    puertos = cps.serial_ports()

    if( puertos[0] != None):
        print("---------> ", puertos[0])
        lector = ReadingThread(puertos[0])
        
        while True:

            lectura = lector.PortReader()
            
            if(lectura != None):
                #br.emit("{\"t\":\"1\", \"sensor\": \"2\", \"val\":", lectura, "}")
            
                aFiltrar = IterPat(lectura)#parametro faltante  (pat)
                #filtrado = aFiltrar.Iterar()
                #if filtrado != None:
                    #print(filtrado)

if __name__ == "__main__":
    main()
        
