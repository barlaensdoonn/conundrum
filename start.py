#!/usr/bin/python3
# send TCP socket message to Blackmagic HyperDeck Studio Mini player
# to start looping playback of Conundrum (Gary Hill)
# 4/29/18
# updated: 4/29/18

from socket import *
from time import sleep


def encode(msg):
    return '{}\r\n'.format(msg).encode()


def client_send(hostport, msg):
    with socket(AF_INET, SOCK_STREAM) as client:
        client.connect(hostport)
        client.sendall(msg)
        response = client.recv(1024)

        return response.decode().strip()


if __name__ == '__main__':
    # make sure everyone's awake
    sleep(5)

    # HyperDeck Ethernet Protocol server listens on port 9993
    hostport = ('192.168.0.166', 9993)
    response = client_send(hostport, encode('play: loop: true'))
