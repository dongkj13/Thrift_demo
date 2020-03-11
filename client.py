#!/usr/bin/env python

import sys
sys.path.append('./gen-py')

from HelloWorld import HelloWorld
from HelloWorld.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloWorld.Client(protocol)
    transport.open()

    stu = Student('Jim', 20)

    print "client - birth_year"
    print "server - ", client.birth_year(stu)

    print "client - say"
    msg = client.say("Hello!")
    print "server - " + msg

    transport.close()
except Thrift.TException, ex:
    print "%s" % (ex.message)
