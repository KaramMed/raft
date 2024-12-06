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

    s0 = RaftNode(address_book_fname, 'node3', 'follower')

    s0.start()
    
    # for the attacker node
    # after 20 seconds, this node will send the malicious request based on captured vote requests "vote_request.json"
    #time.sleep(20)
    s0.replay_attack(bypass_timestamp=False)

    # send malicious append entry (when not leader)
    '''
    time.sleep(20)
    if s0.check_role != 'leader':
        entry = {'term': 100, 'entry': 'Malicious Entry', 'id': 123}
        s0._broadcast_append_entries(entry)
    '''

    try:
        while True:
            pass
    except KeyboardInterrupt:
        s0.stop()