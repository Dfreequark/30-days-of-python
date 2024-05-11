class Node:
    # node has only two variable: data, next
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None     # first is an empty linked list

    def append_end(self, data):
        new_node = Node(data)           # creation of node with data as input parameter
        if not self.head:               # if list is empty i.e no head, set new node as head
            self.head = new_node
            return                      # finishing the append operation
        
        current_node = self.head        # creation of temporary pointer for traversal along the list
        while current_node.next:        # run the loop until last node is current node
            current_node = current_node.next
        current_node.next = new_node    # linking new node with last node

    def append_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Make the new node point to the current head
        self.head = new_node       # Update the head to be the new node


    def append_pos(self, data, pos):
        new_node=Node(data)
        current_node= self.head
        index=1
        while current_node:
                   #calculate index of the next node
            if pos==1:                              # appending at first position
                new_node.next=current_node          #linking current node/head node to new node
                self.head=new_node                  #setting new node as head
                return
            elif index + 1==pos:                        # checking next of current node is the given postion
                new_node.next=current_node.next         #linking next node to new node
                current_node.next=new_node              # linking new node to previous node
                return
            else:
                current_node= current_node.next
                index +=1                               # traversing and counting index 
                continue


        print("INVALID POSITION!!!")   # return this for any other case

    def remove_initial(self):
        if not self.head:           #checking if it is empty
            return
        elif not self.head.next:        #checking if there is only one node
            self.head = None
        else:
            self.head= self.head.next

    def remove_end(self):
        current_node= self.head
        
        while current_node.next:
            last_node= current_node
            current_node= current_node.next
        
        last_node.next = None

    def remove_pos(self, pos):
        current_node= self.head
        index=1
        while current_node:
            index +=1
            if pos==1:
                self.head=current_node.next
                return
            elif index==pos:
                last_node= current_node
                current_node= current_node.next
                if current_node:
                    next_node= current_node.next
                    last_node.next=next_node
                    
                    return
                else:
                    last_node.next=None
                    return print(pos, "th position outof range!! Length of the list is :", index-1)
            else:
                current_node= current_node.next
                continue
        print(pos, "th position outof range!! Length of the list is :", index-1)

    def sort(self):
        current_node= self.head
        data=[]
        while current_node:
            data.append(current_node.data)
            current_node = current_node.next
        sorted_data= sorted(data)
        self.head=None
        for value in sorted_data:
            self.append_end(value)


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append_end(1)
    linked_list.append_end(2)
    linked_list.append_end(-1)
    linked_list.append_end(4)
    linked_list.append_end(30)
    linked_list.append_beg(0)
    linked_list.append_beg(45)
    linked_list.append_beg(-2)
    linked_list.append_pos(0.5, 4)
 #  linked_list.append_pos(10, 10)
    linked_list.remove_initial()
    linked_list.remove_end()
    linked_list.append_end(12)
    linked_list.append_end(8)
    linked_list.append_end(20)
    linked_list.sort()




    linked_list.print_list()
