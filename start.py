#!/usr/bin/env python
from raft import RaftNode
import json
import time

address_book_fname = 'address_book.json'

if __name__ == '__main__':
    d = {"node1": {"ip": "192.168.1.1", "port": "2380"}, 
         "node2": {"ip": "192.168.1.2", "port": "2380"}, 
         "node3": {"ip": "192.168.1.3", "port": "2380"}}
        
    with open(address_book_fname, 'w') as outfile:
        json.dump(d, outfile)

    s0 = RaftNode(address_book_fname, 'node1', 'follower')

    s0.start()
    
    # for the attacker node
    # after 20 seconds, this node will intercept the current index, term, increment term and send vote requests
    #time.sleep(20)
    #s0.transition_to_candidate()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()