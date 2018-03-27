from block import *

class Blockchain:
  def __init__(self):
    self.blockchain = []
    self.blockchain.append(Block(date.datetime.now(), "Genesis Block", "0"))
    self.difficulty = 3
    self.delay_exchange = []
    self.bonus = 100

  def last_block(self):
    return self.blockchain[-1]

  def create_block(self, new_block):
    new_block.previous_hash = self.last_block().hash
    # new_block.hash = new_block.hash_block()
    new_block.mine_block(self.difficulty)
    self.blockchain.append(new_block)

  def accept_blockchain(self):
    for i in range(1, len(self.blockchain)):
      current_block = self.blockchain[i]
      pre_block = self.blockchain[i - 1]
      if(current_block.hash != current_block.hash_block()):
        return False
      elif(current_block.previous_hash != pre_block.hash):
        return False
    return True
