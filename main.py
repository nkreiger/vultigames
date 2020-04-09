# grpc client
from __future__ import print_function
from settings import settings
import grpc
import protos.game_pb2_grpc as sb
import protos.game_pb2 as pb

connected = True
channel = grpc.insecure_channel(settings.GRPC_CONFIG['CLIENT_BASE_URL'])
stub = sb.StatusStub(channel)


def status_check():
    """
    Status check function to ensure connection to gRPC client
    :return:
    """
    try:
        res = stub.test(pb.StatusRequest(check="Status check from svc-blackjack client"))
        return True
    except:
        return False


if status_check():
    print('Ok.')
else:
    print('Not Connected')
