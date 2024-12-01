#!/usr/bin/env python

from raft import RaftNode
import json
import time

address_book_fname = 'address_book.json'

if __name__ == '__main__':
    d = {"node1": {"ip": "127.0.0.1", "port": "2380"}, 
         "node2": {"ip": "127.0.0.1", "port": "2381"}, 
         "node3": {"ip": "127.0.0.1", "port": "2382"},
         "node4": {"ip": "127.0.0.1", "port": "2383"}}
        
    with open(address_book_fname, 'w') as outfile:
        json.dump(d, outfile)

    s0 = RaftNode(address_book_fname, 'node3', 'follower')

    s0.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()