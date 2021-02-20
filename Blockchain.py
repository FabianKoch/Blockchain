from Block import Block

Blockchain = []

#Create the first block
genesis_block = Block('This is my first block of my fist blockchain', ['Fabian sent 1 BTC to Patrick',
                                                                       'Patrick sent 1 BTC to Jon',
                                                                       'Jon sent 1 BTC to Fabian'])

second_block = Block(genesis_block.block_hash, ['Fabian sent 10 BTC to Patrick',
                                                'Patrick sent 10 BTC to Jon',
                                                'Jon sent 10 BTC to Fabian'])

third_block = Block(second_block.block_hash, ['Fabian sent 100 BTC to Patrick',
                                                'Patrick sent 100 BTC to Jon',
                                                'Jon sent 100 BTC to Fabian'])

print('Genesis Block Hash: '+genesis_block.block_hash)
print('Second Block Hash: '+second_block.block_hash)
print('Third Block Hash: '+third_block.block_hash)