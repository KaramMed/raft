#!/usr/bin/env python
from raft import RaftNode
import json
import time

address_book_fname = 'address_book.json'

if __name__ == '__main__':
    d = {"node1": {"ip": "192.46.237.85", "port": "2380"}, 
         "node2": {"ip": "172.105.85.119", "port": "2380"}, 
         "node3": {"ip": "172.104.149.60", "port": "2380"}}
        
    with open(address_book_fname, 'w') as outfile:
        json.dump(d, outfile)

    s0 = RaftNode(address_book_fname, 'node2', 'follower')

    s0.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()