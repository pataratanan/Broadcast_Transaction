# Broadcast_Transaction

I did that by Pycharm. Suspect that different editors may result in error

Documentation

import requests is a library for making HTTP requests
import time is a scripts to work with time

class TransactionCLient is a class of client module to get a transaction of HTTP requests

__init__ is a constructor and base_url is the base URL of the HTTP server.

broadcast_transaction is a function broadcast requirement provided by assignment

payload is an object of all arguments for using purpose(We need to convert that to JSON)
# Perform an HTTP POST request to broadcast a transaction
response = requests.post(f"{self.base_url}/broadcast", json=payload)

# Parse the response as JSON
response_data = response.json()

# Extract the transaction hash from the response data
tx_hash = response_data.get("tx_hash")

check_transaction_status is a function of checking status
# Perform an HTTP GET request to check the status of a transaction
response = requests.get(f"{self.base_url}/check/{tx_hash}")

# Parse the response as JSON
response_data = response.json()

# Extract the transaction status from the response data, defaulting to "DNE" if not present
tx_status = response_data.get("tx_status", "DNE")

# Return the transaction status
return tx_status

MAIN METHOD
client = TransactionClient("https://mock-node-wgqbnxruha-as.a.run.app") is a base URL of the HTTP server

#Hash the broadcast transaction
tx_hash = client.broadcast_transaction(symbol, price, timestamp)

#while loop for checking transaction status
    while True:
        tx_status = client.check_transaction_status(tx_hash)
        print(f"Transaction Status: {tx_status}")

        if tx_status in ["CONFIRMED", "FAILED"]:
            print(f"Status: {tx_status}")
            break

        # Wait 5 sec until check it again
        time.sleep(5)
