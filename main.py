if __name__ == "__main__":
   from functions import LinkedList;
   from colorama import init;
   from termcolor import colored

   init()
   MyList = LinkedList()
   #Adding data to linked list.
   MyList.add(dict(_id='Jamie123', name='Jamie'));
   MyList.add(dict(_id='Kylie311', name='Kylie'));
   MyList.add(dict(_id='Acey591', name='Acey'));
   MyList.add(dict(_id='Jay319', name='Jay'));
   MyList.add(dict(_id='_KC191', name='K.C.'));

   MyList.add("The quick brown fox jumped over the lazy dog...") #Should throw an exception error.

   # Search person profile based on _id.
   print(MyList.id_search('Kylie311'));

   print("\nLength of My List:",len(MyList), end="\n\n") #List length.
   str1 = "="*37 + " CHAIN " + "="*37;
   str2= "="*81;
   print(colored(str1, color='red', attrs=['bold']))
   print(MyList.ViewChain())
   print(colored(str2, color='red', attrs=['bold']))

