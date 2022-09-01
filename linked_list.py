class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, node_data):
        new_node = Node(data=node_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = self.tail.next_node

    def insert_at_beginning(self, node_data):
        if not self.head:
            self.insert_at_end(node_data)
        else:
            new_node = Node(data=node_data)
            new_node.next_node = self.head
            self.head = new_node

    def to_list(self):
        l = []
        if self.head is None:
            return l
        
        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        ll_str = ''
        node = self.head
        while node:
            ll_str += str(node.data) + ' -> '
            node = node.next_node
        print(ll_str)


# ll = LinkedList()

# while True:
#     command = input('command start -> "start", end -> "end", print -> "print", head -> "h", list -> "l", quit -> "q": ')
#     if command == 'start':
#         data = input('Data to add to beginning of list: ')
#         ll.insert_at_beginning(data)
#     elif command == 'end':
#         data = input('Data to add to end of list: ')
#         ll.insert_at_end(data)
#     elif command == "print":
#         ll.print_ll()
#     elif command == "q":
#         break
#     elif command == "h":
#         ll.get_head()
#     elif command == 'l':
#         print(ll.to_list())
#     else: 
#         print("invalid input")


