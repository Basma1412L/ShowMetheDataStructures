import hashlib
import datetime
from time import gmtime, strftime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash=None,prev=None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = previous_hash
      self.prev = prev


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail=None

    def __str__(self):
        cur_head = self.tail
        out_string = ""
        while cur_head:
            out_string += str(cur_head.data) + " ->"
            cur_head = cur_head.prev
        return out_string

    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def append(self, data):
        timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime())

        if self.head is None:
            self.head = Block(timestamp, data, 0,None)
            self.tail=self.head
            self.head.next=self.tail
            return

        node=self.tail
        previous_hash=self.calc_hash(node.data)
        node.next = Block(timestamp, data, previous_hash,node)
        self.tail=node.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


#
#  Blockchain is a sequential chain of records, similar to a linked list.
#  Each block contains some information and how it is connected related to the other blocks in the chain.
#  Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data.
#  For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
# Use your knowledge of linked lists and hashing to create a blockchain implementation.
newchain = BlockChain()
newchain.append('Some Information1')
newchain.append('Some Information2')
newchain.append('Some Information3')
newchain.append('Some Information4')
newchain.append('Some Information5')
newchain.append('Some Information6')

print(newchain)