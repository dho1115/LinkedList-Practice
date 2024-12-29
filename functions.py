class Node(object):
   def __init__(self, data=None, pointer=None):
      self.data = data;
      self.pointer = pointer;

   def __repr__(self):
      return f"{dict(head=self.data, pointer=self.pointer)}";

class LinkedList(object):
   def __init__(self, head:any=None, middle:any=None, tail:Node=None):
      
      """
      Parameters:
      head: Where the newest data is added.
      middle: Where data BEFORE the addition of new data will be moved to.
      tail: Where the Node() class is that takes in self.middle & self.tail as its parameters.
      """
      self.head = head;
      self.middle = middle;
      self.tail = tail;
      self.length = 0;
   
   def add(self, data:dict):
      error_message=""
      try: #try/except block in case user enters something other than a dict() or a dict() without '_id' or 'name' as keys.
         if not isinstance(data, dict):
            error_message+= f"ERROR!!! Your data, {data}, MUST be of a type DICTIONARY (dict): dict(_id=str, name=str)!!!\nInstead, your data is of type, {type(data).__name__}.\n";
            raise Exception (error_message);
      
         if not (data.get("_id") and data.get("name")):
            error_message+= f"ERROR!!! You must have the following keys in your entry: _id and data. Your value for _id registered {data.get('_id')} and your name registered {data.get('name')}.\n"
            raise Exception (error_message)
      
         if (self.tail): self.middle = self.head;

         self.tail, self.head = Node(self.middle, self.tail), data;
         self.length+=1;
      except Exception:
         print(f"{Exception}" + "\n" + error_message);
         return;
      
   
   def id_search(self, _id):
      from colorama import init;
      from termcolor import colored;
      from time import sleep;
      init();

      head, tail = self.head, self.tail;
      errMessage = f"Sorry... I cannot find {_id} because:\n";
      try:
         if (head == None) or (tail == None):
            lengtherrmsg = colored(f"{'*'*5} DID YOU CHECK THE LENGTH (len(instance name))???{'*'*5}", color='red',on_color='on_white', attrs=['bold'])
            errMessage = errMessage+"Your chain has no head!!!\n" if (head == None) else errMessage;
            errMessage = errMessage+"Your chain has no tail!!!\n" if (tail == None) else errMessage;
            errMessage+=f"{lengtherrmsg}\nCurrently, the length for your chain is {colored(self.length, color='red', attrs=['bold'])}."
            raise AttributeError;
      
         if self.head.get('_id') == _id:
            return f"{colored('SUCCESS!!!', color='light_green', attrs=['bold', 'underline'])}\n Profile returned: {colored(scanner.head, color='light_green', attrs=['bold'])}."

         scanner = self.tail; #initialize scanner to self.tail, which is Node(data, pointer). See above in add() where we set self.tail to Node(self.middle, self.tail);

         while scanner.pointer:
            print(f"Currently scanning {scanner.data}...");
            sleep(1.75); #Added a delay feature to make it 'APPEAR' like it's querying a database.
            scanner = scanner.pointer; #Gives the parameters inside Node(data, pointer) new arguments because, as we can see inside add(), that self.tail = Node()
            if scanner.data.get('_id') == _id:
               return f"\n{colored('SUCCESS!!!', color='light_green', attrs=['bold', 'underline'])}\nProfile returned: {colored(scanner.data, color='light_green', attrs=['bold'])}."

         return f"Sorry... I could not find {_id}."
      except AttributeError as atterr: #in case there is no head or tail.
         print(atterr);
         return f"{errMessage}\n{dict(errorMessage=atterr)}"
   
   def ViewChain(self):
      try:
         if self.head == None: raise AttributeError;
      
         chain = f"{self.head} "
         tail = self.tail;
         while tail:
            chain+= f" - {tail.data}";
            tail = tail.pointer;
         return chain;
      except AttributeError: #In case there is no head or tail.
         print(AttributeError);
         return f"You have NO CHAIN because...\nself.head is {self.head}.\nself.tail is {self.tail}!!!"
   
   def __len__(self):
      return self.length;
   
   def __repr__(self):
      return f"{self.head} - {self.tail}"
