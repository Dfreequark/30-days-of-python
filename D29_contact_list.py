
class Contact():
    def __init__(self,name, number):
        self.name=name
        self.number=number
        self.next=None

class ContactList():
    def __init__(self) :
        self.head=None
    
    def add(self, name, number):
        new_contact =Contact(name, number)

        if not self.head:
            self.head= new_contact
            return
        
        current_contact= self.head
        next_contact=None
        while current_contact:
            
            #appending at first
            if new_contact.name<current_contact.name and current_contact==self.head:
                self.head=new_contact
                new_contact.next=current_contact
                return
            elif new_contact.name>current_contact.name and current_contact.next is None:
                current_contact.next=new_contact
                return
            elif new_contact.name>current_contact.name and current_contact.next is not None:
                next_contact= current_contact.next
                if new_contact.name<next_contact.name :
                    current_contact.next=new_contact
                    new_contact.next=next_contact
                    return
                else:
                    current_contact= next_contact
                

        
    def print_list(self):
        current_contact = self.head
        print("---------------------------------")
        while current_contact:
            print( f'{current_contact.name}, Ph No: {current_contact.number}')
            current_contact=current_contact.next
        print("---------------------------------")





if __name__=="__main__":
    contact_list=ContactList()
    contact_list.add("alice", 12345)
    contact_list.add("aice", 12345)
    contact_list.add("charlie", 86354)
    contact_list.add("bob", 225666)
    contact_list.add("zil", 225666)
    

    

    contact_list.print_list()
