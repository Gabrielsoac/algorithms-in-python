from Queue import Queue

my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print(my_queue)

my_queue.dequeue()

print(my_queue)