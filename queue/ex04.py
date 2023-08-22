class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def in_front(self):
        return self.queue[0]
    
print(" ***Cafe***")
inp = input("Log : ").split("/")
run_time = -1
barista1 = Queue()
barista2 = Queue()

serve = []

waiter_queue = [i for i in range(len(inp))]
customer_id = 0
for i in range(len(inp)):
	waiter_queue[i] = list(map(int,inp[i].split(',')))
	customer_id += 1
	waiter_queue[i].append(customer_id)
        
print(waiter_queue)
     
barista1.enqueue(waiter_queue.dequeue())
barista2.enqueue(waiter_queue.dequeue())

while (not barista1.is_empty or not barista2.is_empty):
	run_time += 1
	if not barista1.is_empty() and barista1.in_front[1] == run_time:
		serve.append(barista1.dequeue())
	if not barista2.is_empty() and barista2.in_front[1] == run_time:
		serve.append(barista2.dequeue())
    
        