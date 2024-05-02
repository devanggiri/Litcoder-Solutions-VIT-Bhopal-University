class CustomQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None  # Queue is empty

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            front = self.stack2[-1]
            print(front)
        else:
            print("Queue is empty")

# Example Usage
def process_queries(queries):
    queue = CustomQueue()
    for query in queries:
        if query[0] == 1:
            # Enqueue
            queue.enqueue(query[1])
        elif query[0] == 2:
            # Dequeue
            queue.dequeue()
        elif query[0] == 3:
            # Print Front
            queue.print_front()


inputVal = input()    
outputVal = process_queries(inputVal)
print (outputVal)
                                                                                                                            
