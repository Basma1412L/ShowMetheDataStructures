import sys

class Node:
    def __init__(self, value,frequency,left_child=None,right_child=None):
        self.value = value
        self.frequency=frequency
        self.left_child=left_child
        self.right_child=right_child
        self.left_bit=0
        self.right_bit=1

    def __repr__(self):
        return str(self.frequency,':',self.value)

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)
    def insert(self, data):
        self.queue.append(data)

    def top(self):
        try:
            min = -1
            for i in range(len(self.queue)):
                if self.queue[i].frequency < 10000:
                    min = i
            item = self.queue[min]
            return item
        except IndexError:
            print()
            exit()

    def pop(self):
        try:
            min = -1
            for i in range(len(self.queue)):
                if self.queue[i].frequency < 10000:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

def encode(root,path,codes):
    if (not root.left_child==None):
        path+=str(root.left_bit)
        encode(root.left_child,path,codes)
    if (not root.right_child==None and  root.left_child==None):
        path+=str(root.right_bit)
        encode(root.right_child,path,codes)
    if (not root.right_child==None and not root.left_child==None):
        path=path[:-1]
        path+=str(root.right_bit)
        encode(root.right_child,path,codes)
    if (root and root.right_child==None and root.left_child==None):
        codes[root.value]=path



def huffman_encoding(data):
    frequencies={}
    pQueue=PriorityQueue()
    for letter in data:
        if letter in frequencies:
            frequencies[letter]+=1
        else:
            frequencies[letter]=1
    for i in frequencies:
        temp_node=Node(i,frequencies[i])
        pQueue.insert(temp_node)

    while(pQueue.length()>1):
        left_child=pQueue.pop()
        right_child=pQueue.pop()
        nFreq=left_child.frequency+right_child.frequency
        nValue=left_child.value+' '+right_child.value
        nNode=Node(nValue,nFreq,left_child,right_child)
        pQueue.insert(nNode)
    codes={}
    encode(pQueue.top(),"",codes)
    code=''
    for i in data:
        code+=str(codes[i])
    return code,pQueue.top()
    pass


def decode(data,tree,fullTree):
    if (tree and tree.left_child==None and tree.right_child==None):
        d=str(tree.value)
        if data=="":
            return d
        else:
            return d+str(decode(data,fullTree,fullTree))
    if (data[0]=="0"):
        return decode(data[1:],tree.left_child,fullTree)
    if (data[0]=="1"):
        return decode(data[1:],tree.right_child,fullTree)


def huffman_decoding(data,tree):
    decoded=decode(data,tree,tree)
    return decoded


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data=="The bird is the word")



    a_great_sentence = "Life is beautiful"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data=="Life is beautiful")


    a_great_sentence = "Keep smiling"
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data=="Keep smiling")



    a_great_sentence = ""
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data=="")



    a_great_sentence = "   "
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data=="   ")


    a_great_sentence = " l "
    encoded_data, tree = huffman_encoding(a_great_sentence)
    decoded_data = huffman_decoding(encoded_data, tree)
    assert (decoded_data==" l ")