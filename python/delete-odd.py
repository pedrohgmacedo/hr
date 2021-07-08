#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


#
# Complete the 'deleteOdd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST_NODE.
# The function accepts INTEGER_SINGLY_LINKED_LIST_NODE listHead as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def remove_odds(listHead):
       # special case: head node
       # remove odd head elements by simply setting head to the next element after
       while (listHead is not None) and (listHead.data % 2 == 1):
            listHead = listHead.head.next
        # regular case: the rest of the nodes
        current_node = listHead.head
        while (current_node is not None) and (current_node.next is not None):
            # if the next node's data is odd, then
            if current_node.next.data % 2 == 1:
                # skip that node by pointing this node's .next to the next node's .next
                current_node.next = current_node.next.next
            # otherwise, move forwards in the list
            else:
                current_node = current_node.next



def deleteOdd(listHead):
    curr = listHead.next
    prev = listHead

    while (listHead is not None) and (listHead.data % 2 == 1):
            listHead = listHead.next

    while curr and curr.next:
        if (curr.next.data % 2) == 1:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return listHead


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    listHead_count = int(input().strip())

    listHead = SinglyLinkedList()

    for _ in range(listHead_count):
        listHead_item = int(input().strip())
        listHead.insert_node(listHead_item)

    result = deleteOdd(listHead.head)

    print_singly_linked_list(result, '\n', fptr)
    fptr.write('\n')

    fptr.close()
