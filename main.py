import requests
import time

class TransactionClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def broadcast_transaction(self, symbol, price, timestamp):
        payload = {
            "symbol": symbol,
            "price": price,
            "timestamp": timestamp
        }

        response = requests.post(f"{self.base_url}/broadcast", json=payload)
        response_data = response.json()

        tx_hash = response_data.get("tx_hash")
        return tx_hash

    def check_transaction_status(self, tx_hash):
        response = requests.get(f"{self.base_url}/check/{tx_hash}")
        response_data = response.json()

        tx_status = response_data.get("tx_status", "DNE")
        return tx_status

if __name__ == "__main__":
    client = TransactionClient("https://mock-node-wgqbnxruha-as.a.run.app")

    # Broadcasting Transaction
    symbol = "ETH"
    price = 4500
    timestamp = 1678912345
    tx_hash = client.broadcast_transaction(symbol, price, timestamp)
    print(f"Transaction Hash: {tx_hash}")

    # Checking Transaction Status
    while True:
        tx_status = client.check_transaction_status(tx_hash)
        print(f"Transaction Status: {tx_status}")

        if tx_status in ["CONFIRMED", "FAILED"]:
            print(f"Status: {tx_status}")
            break

        # Wait 5 sec until check it again
        time.sleep(5)
