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

    s0 = RaftNode(address_book_fname, 'node4', 'follower')

    s0.start()

    s0._set_current_role('candidate')

    s0._increment_term()

    # Request for nodes to vote for you
    s0._send_request_vote()

    # Vote for yourself
    s0._send_vote(s0.my_id, True)

    time.sleep(2)

    #s0.stop()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()