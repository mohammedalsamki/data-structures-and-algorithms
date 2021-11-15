from stack_and_queue.queue import Queue

class AnimalShelter:

    """
    class which holds only dogs and cats.
    The shelter operates using a first-in, first-out approach.
    Methods:
    enqueue() -> enqueues animals into queue ,animal can be either a dog or a cat object.
        - Arguments: animal
        - return : None
    dequeue() -> dequeue animal from the queue
        - Arguments: pref -> pref can be either "dog" or "cat"
        - Return: either a dog or a cat, based on preference. If pref is not "dog" or "cat" then return null.
    """
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue_animal(self,animal):
        if animal.lower().startswith("cat") :
            self.cat.enqueue(animal)
        elif animal.lower().startswith("dog") :
            self.dog.enqueue(animal)
        else:
           raise Exception('This shelter for cats and dogs only !!!')

    def dequeue_animal(self,pref):
        if pref.lower().startswith("cat"):
            return self.cat.dequeue()
        elif pref.lower().startswith("dog"):
            return self.dog.dequeue()
        else :
            return "NULL"
