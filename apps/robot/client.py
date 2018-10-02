import sys
import json
from time import time
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# add gen-py to PYTHONPATH
sys.path.append('./gen-py')

from robot_data import RobotReceiver

try:
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = RobotReceiver.Client(protocol)

    transport.open()

    # print("client - ping")
    # print("server - " + client.ping())
    #
    #
    # for x in range(0, 10):
    #     print("client Say: Hello!")
    #     msg = client.say(json.dumps({'v': '100', 's': '3'}))
    #     print("server " + msg)

    start_time = time()
    for x in range(0, 100):
        robot_msg = client.RobotInfo('demo', json.dumps({'v': '100', 'pos': [1+x, 1+x], 'time': time()}))
        print(robot_msg)
    end_time = time() - start_time
    print("duration: " + str(end_time))
    transport.close()
except Thrift.TException as ex:
    print(ex.message)
