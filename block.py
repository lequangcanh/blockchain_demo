import hashlib as hasher
import datetime as date
import pdb

class Block:
  def __init__(self, timestamp, data, previous_hash = ""):
    self.timestamp = timestamp
    self.data = data
    self.previous_hash = previous_hash
    self.auto_increament = 0
    self.hash = self.hash_block()

  def hash_block(self):
    sha = hasher.sha256()
    sha.update((str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.auto_increament)).encode())
    return sha.hexdigest()

  def mine_block(self, difficulty):
    while(self.hash[0:difficulty] != "0".join([""] * (difficulty + 1))):
      self.auto_increament += 1
      self.hash = self.hash_block()
    print("Mined block: %s" %(self.hash))
