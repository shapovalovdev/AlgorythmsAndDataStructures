from src.Queue.queue_stacks import QueueStacks

def circle_queue(queue,round_to_n):
    #check if queue is Queue
    #check if queue is empty
    if round_to_n==0:
        return
    while round_to_n>0:
        item=queue.dequeue()
        queue.enqueue(item)
        round_to_n-=1
