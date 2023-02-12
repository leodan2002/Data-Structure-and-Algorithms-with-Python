from blossom_lib import flower_definitions


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, new_node):
        current_node = self.head_node

        if not current_node:
            self.head_node = new_node

        while (current_node):
            next_node = current_node.get_next_node()
            if not next_node:
                current_node.set_next_node(new_node)
            current_node = next_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def __iter__(self):
        current_node = self.head_node
        while (current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()


class HashMap:

    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for number in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        # self.array[array_index] = [key, value]
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        print(f"Node {payload.value} -- index {array_index}")

        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return
        list_at_array.insert(payload)


    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index]
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None

blossom = HashMap(len(flower_definitions))

for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve("chrysanthemum"))

print(blossom.retrieve("hyacinth"))

