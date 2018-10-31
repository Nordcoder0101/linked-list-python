class SList:
    def __init__(self):
        self.head = None


    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = Node(val)  
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head.next == None:
            return self
        else:    
            self.head = self.head.next
        return self

    def remove_from_back(self):
        if self.head.next == None:
            return self
        else:
            previous_node = self.head
            runner = self.head.next
            while runner.next != None:
                previous_node = runner
                runner = runner.next
            previous_node.next = None
        return self

    def remove_val(self, val):
        if self.head.next == None:
            return self
        elif self.head.value != val:
            previous_node = self.head
            runner = self.head.next
            while runner.value != val:
                previous_node = runner
                runner = runner.next
            if runner.next != None:
              previous_node.next = runner.next
              return self  
            else:
                previous_node.next = None
                return self
    
    def insert_at(self, val, n):
        if self.head.next == None:
            return self
        else:
          if n == 1:
            self.add_to_front(val)
            return self
          else:
            previous_node = self.head
            runner = self.head.next
            current_n = 2
            while current_n != n:
                previous_node = runner
                runner = runner.next
                current_n += 1
            new_node = Node(val)
            new_node.next = runner
            previous_node.next = new_node    
        return self

        

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun").insert_at('super',4).print_values()
