#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        
class Blockchain:
    """
    The "LinkedList" of the blocks-- a chain of blocks.
    """
    difficulty = 4

    def __init__(self):
        """
        Initializes a new blockchain.
        """
        self.chain = []
        
    def add(self, block):
        """
        Adds a new block to the chain.
        """
        self.chain.append(block)

    def remove(self, block):
        """
        Removes a block from the chain.
        """
        self.chain.remove(block)

    def mine(self, block):
        """
        Finds the nonce of the block that satisfies the difficulty and adds it to the chain.
        """
        block.previous_hash = self.chain[-1].hash() if self.chain else "0"*64

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block)
                print(block)
                return block
            block.nonce += 1
    
    def isValid(self):
        """
        Checks if the blockchain is valid.
        """
        for i in range(1, len(self.chain)):
            previous_block, current_block = self.chain[i-1], self.chain[i]
            if current_block.previous_hash != previous_block.hash() or not current_block.hash().startswith("0" * self.difficulty):
                return False
        return True

def mining(blockchain):
    """
    Function for testing purposes to mine a specified number of blocks.
    """
    amount = int(input("How many blocks do you want to mine: "))
    initial_length = len(blockchain.chain)
    
    for _ in range(amount):
        data = input(f"What data is in your block {initial_length + 1 + _}: ").lower()
        blockchain.mine(Block(initial_length + 1 + _, data=data))
       
    print(f"Is the blockchain valid: {blockchain.isValid()}")
    
def displayChain(chaining):
    """
    Displays all blocks in the chain.
    """
    for block in chaining:
        print(block)
        
def main():
    """
    Main function to interact with the blockchain.
    """
    blockchain = Blockchain()
    while True:
        command = input("\nWhat do you want to do: \n [M]ine blocks \n [S]how Blockchain \n [Q]uit\nCommand: ").lower()
        if command == 'm':
            mining(blockchain)
        elif command == 's':
            displayChain(blockchain.chain)
        elif command == 'q':
            break
        else:
            print("Please provide a valid input")
    quit()

if __name__ == "__main__":
    main()