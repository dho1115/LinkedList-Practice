if __name__ == "__main__":
   from functions import LinkedList;

   MyList = LinkedList()
   MyList.add(dict(_id='Jamie123', name='Jamie'));
   MyList.add(dict(_id='Kylie311', name='Kylie'));
   MyList.add(dict(_id='Acey591', name='Acey'));
   MyList.add(dict(_id='Jay319', name='Jay'));
   MyList.add(dict(_id='_KC191', name='K.C.'));

   print(MyList, end="\n=========\n")

   print(MyList.id_search('Kylie311'));

