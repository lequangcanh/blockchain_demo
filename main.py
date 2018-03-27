from blockchain import *

my_coin = Blockchain()
my_coin.create_block(Block(date.datetime.now(), "Block1"))
my_coin.create_block(Block(date.datetime.now(), "Block2"))
