import sys;input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class LinkedList():
    def __init__(self):
        self.tail = Node(None)
        self.head = Node(None)
        self.start_node, self.end_node = Node('start'), Node('end')
        self.start_node.right = self.tail

        self.tail.right = self.start_node
        self.head.left = self.end_node
        self.end_node.left = self.head

        self.cursor = self.start_node

    def initial_append(self, data):
        init_node = Node(data)
        init_node.right = self.end_node
        init_node.left = self.start_node
        self.end_node.left = init_node
        self.start_node.right = init_node
        self.tail = init_node
        self.head = init_node
        self.cursor = init_node.right

    def append(self, data):
        new_node = Node(data)
        new_node.left = self.tail
        new_node.right = self.end_node
        self.tail.right = new_node
        self.tail = new_node
        self.end_node.left = new_node
        self.cursor = new_node.right

    def insert_left(self, data):
        new_node = Node(data)
        if self.cursor.data != 'start':
            prev = self.cursor.left
            new_node.left = prev
            new_node.right = self.cursor
            prev.right = new_node
            self.cursor.left = new_node
        else:
            new_node.left = self.start_node
            new_node.right = self.cursor
            self.start_node.right = new_node
            self.cursor.left = new_node
            self.head = new_node
        
    def delete_left(self):
        if self.cursor.left != self.start_node:
            del_node = self.cursor.left
            prev = del_node.left
            next = del_node.right
            prev.right = next
            next.left = prev
            if del_node == self.head:
                self.head = next

    def move_cursor_left(self):
        if self.cursor != self.start_node.right:
            self.cursor = self.cursor.left
    
    def move_cursor_right(self):
        if self.cursor != self.end_node:
            self.cursor = self.cursor.right

    def print(self):
        res, now = [], self.start_node
        now = now.right
        while now != self.end_node:
            res.append(now.data)
            now = now.right
        print(''.join(res))
    
char = input().strip()
arr = LinkedList()
arr.initial_append(char[0])
for i in range(1, len(char)):
    arr.append(char[i])

for _ in range(int(input())):
    c = input().split()
    if c[0] == 'L':
        arr.move_cursor_left()
    elif c[0] == 'D':
        arr.move_cursor_right()
    elif c[0] == 'B':
        arr.delete_left()
    else:
        arr.insert_left(c[1])

arr.print()