#!/usr/bin/env python

import socket
import sys
sys.path.append('./gen-py')

from HelloWorld import HelloWorld
from HelloWorld.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandler:
    def birth_year(self, stu):
        print "name: ", stu.name
        print "age: ", stu.age
        print "birth_year: ", 2020 - stu.age
        return 2020 - stu.age

    def say(self, msg):
        ret = "Received: " + msg
        print ret
        return ret

handler = HelloWorldHandler()

processor = HelloWorld.Processor(handler)

transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Starting thrift server in python..."
server.serve()
print "done!"
