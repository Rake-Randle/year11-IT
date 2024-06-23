from hashlib import sha256

def updatehash(*args):
    """
    Takes in any number of arguments and produces a sha256 hash as a result.
    """
    hashing_text = "".join(str(arg) for arg in args)
    return sha256(hashing_text.encode('utf-8')).hexdigest()

class Block:
    """
    The "node" of the blockchain. Points to the previous block by its unique hash in previous_hash.
    """
    def __init__(self, number=0, previous_hash="0"*64, data=None, nonce=0):
        """
        Default data for block defined in constructor. Minimum specified should be number and data.
        """
        self.number = number
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = nonce

    def hash(self):
        """
        Returns a sha256 hash for the block's data.
        """
        return updatehash(self.number, self.previous_hash, self.data, self.nonce)

    def __str__(self):
        """
        Returns a string of the block's data. Useful for diagnostic print statements.
        """
        return f"Block#: {self.number}\nHash: {self.hash()}\nPrevious: {self.previous_hash}\nData: {self.data}\nNonce: {self.nonce}\n"