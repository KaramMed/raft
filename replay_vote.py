import time
from protocol import RequestVotesMessage, MessageType, MessageDirection
from interface import Talker

def send_vote_requests(term, last_log_index, source, destinations):
    """
    Sends manual vote requests to the specified Raft nodes.

    Args:
        term (int): The election term to use in the requests.
        last_log_index (int): The last log index of the sender.
        source (str): The ID of the source node (e.g., '192.168.1.1:5557').
        destinations (list): List of destination node IDs (e.g., ['192.168.1.2:5557', '192.168.1.3:5557']).
    """
    # Initialize the Talker to send messages
    talker = Talker(identity={'my_id': source, 'my_name': 'manual_sender'})
    talker.start()

    try:
        for destination in destinations:
            print(f"Sending vote request from {source} to {destination}...")

            # Create the vote request message
            vote_request = RequestVotesMessage(
                type_=MessageType.RequestVotes,
                term=term,
                sender=source,
                receiver=destination,
                direction=MessageDirection.Request,
                candidate_id=source,
                last_log_index=last_log_index,
                last_log_term=term  # Assuming last_log_term matches the current term
            )

            # Send the message
            talker.send_message(vote_request.jsonify())
            print(f"Vote request sent to {destination}.")
            time.sleep(0.1)  # Slight delay to prevent overwhelming the system
    finally:
        # Clean up and stop the Talker
        talker.stop()

if __name__ == "__main__":
    # Example variables (modify these as needed)
    term = 5
    last_log_index = 10
    source = "192.168.1.1:5557"
    destinations = ["192.168.1.2:5557", "192.168.1.3:5557"]

    # Call the function to send vote requests
    send_vote_requests(term, last_log_index, source, destinations)
