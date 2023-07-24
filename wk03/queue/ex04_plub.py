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

data_info = [data+','+str(id+1)+','+'0' for id, data in enumerate(inp) ]
data_info = [[int(x) for x in i.split(',')] for i in data_info]

queue = Queue()
barista_queue = Queue()
waiter_queue = Queue()
waiter_time = -1
customer_time = -1

for data in data_info:
    queue.enqueue(data)

time = 0
while not barista_queue.is_empty() or not waiter_queue.is_empty() or not queue.is_empty():
    while not queue.is_empty() and queue.in_front()[0] <= time:
        waiter_queue.enqueue(queue.dequeue())

    while barista_queue.size() < 2 and not waiter_queue.is_empty():
        customer = waiter_queue.dequeue()
        customer[3] = abs(time - customer[0])
        if customer[3] > waiter_time:
            waiter_time = customer[3]
            customer_time = customer[2]
        barista_queue.enqueue(customer)

    result = Queue()
    for customer in barista_queue.queue:
        customer[1] -= 1
        if customer[1] <= 0:
            print(f"Time {time+1} customer {customer[2]} get coffee")
        else:
            result.enqueue(customer)

    barista_queue = result

    time += 1

if waiter_time > 0:
  print(f"The customer who waited the longest is : {customer_time}")
  print(f"The customer waited for {waiter_time} minutes")
else:
  print("No waiting")