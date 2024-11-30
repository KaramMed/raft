from raft import RaftNode
import time

def manually_trigger_election():
    # Initialize the RaftNode 
    s0 = RaftNode('address_book.json', 'node1', 'follower')
    s0.start()

    # Give the node some time to start and become a follower
    time.sleep(2)

    # Manually transition s0 (node1) to a candidate
    print("Transitioning node to candidate...")
    s0._set_current_role('candidate')  # Directly set the role to candidate

    # After transitioning to a candidate, it should send a vote request
    # The term will be incremented (or set to a value higher than the current leader's term)
    # Use existing method to send vote request
    s0._send_request_vote()  # Send the vote request to other nodes

    # Allow time for the vote request to propagate and process
    time.sleep(2)

    # After sending vote requests, we stop the node (optional)
    s0.stop()

if __name__ == "__main__":
    manually_trigger_election()
