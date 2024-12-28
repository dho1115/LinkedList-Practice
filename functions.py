class Node(object):
   def __init__(self, data=None, pointer=None):
      self.data = data;
      self.pointer = pointer;

   def __repr__(self):
      return f"{dict(head=self.data, pointer=self.pointer)}";

class LinkedList(object):
   def __init__(self, head=None, middle=None, tail=None):
      """
      head: Where the newest data is added.
      middle: Where data BEFORE the addition of new data will be moved to.
      tail: Where the Node() class is that takes in self.middle & self.tail as its parameters.
      """
      self.head = head;
      self.middle = middle;
      self.tail = tail;
   
   def add(self, data):
      if self.tail: self.middle = self.head;

      self.tail, self.head = Node(self.middle, self.tail), data;   
   
   def id_search(self, _id):
      if self.head.get('_id') == _id:
         return f"SUCCESS!!! Profile returned: {scanner.head}."
      else: 
         scanner = self.tail; #initialize scanner to self.tail, which is Node(data, pointer). See above in add() where we set self.tail to Node(self.middle, self.tail);

         while scanner.pointer != None:
            print(f"Currently scanning...", scanner.data);
            scanner = scanner.pointer; #This will give the parameters inside Node(data, pointer) new arguments because, as we can see inside add(), that self.tail = Node()
            if scanner.data.get('_id') == _id:
               return f"SUCCESS!!! Profile returned: {scanner.data}."

         return f"Sorry... I could not find {_id}."
   
   def __repr__(self):
      return f"{self.head} - {self.tail}"
