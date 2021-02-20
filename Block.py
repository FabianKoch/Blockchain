import hashlib

class Block:
    def __init__(self, previous_hash, transactions):
        self.transactions = transactions
        self.previous_hash = previous_hash
        #Make a string out of the transaction and append the previous hash
        string_to_hash = "".join(transactions) + previous_hash
        #Make a hash out of the string we created
        self.block_hash = hashlib.sha256(string_to_hash.encode()).hexdigest()

