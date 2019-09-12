class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            newnode.next=self.head
            self.head=newnode
    def insertatend(self,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            newnode=Node(value)
            self.tail.next=newnode
            self.tail=newnode
    def insertatpos(self,position,value):
        if(self.head==None):
            self.head=self.tail=Node(value)
        else:
            temp=self.head
            for i in range(1,position-1):
                temp=temp.next
            newnode=Node(value)
            newnode.next=temp.next
            temp.next=newnode
            temp=None

    def deleteatbeg(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp=None

    def deleteatend(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.next is not None):
                prev = temp
                temp = prev.next
            self.tail=prev
            self.tail.next=None

    def deleteatpos(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            count=0
            temp=self.head
            while(temp.data is not key):
                count=count+1
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value to be deleted is not found in the list")
                    break
            if(count is not 0):
                prev.next=temp.next
            else:
                print("You are trying to delete the first value in the list,so kindly go for option 1 in deletion menu")
            temp=None
            prev=None

    def searching(self,key):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not key):
                if(temp.next is not None):
                    prev = temp
                    temp = prev.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                print("Value is found")
            temp=None

    def updating(self,oldv,newv):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head
            while(temp.data is not oldv):
                if(temp.next is not None):
                    temp=temp.next
                else:
                    print("Value is not found in the list")
                    break
            else:
                temp.data=newv
            temp=None

    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next

s=LL()
print("Welcome to linked list")
while(True):
    print("Menu")
    print("Which below operations need to be performed?")
    print("1. Insertion")
    print("2. Deletion")
    print("3. Searching")
    print("4. Updation")
    print("5. Display")
    print("6. Exit")
    n=int(input())
    if(n is 1):
        print("Which mode of insertion need to be performed?")
        print("1. Insertion at beginning")
        print("2. Insertion at end")
        print("3. Insertion at any position between start and end")
        n=int(input())
        if(n is 1):
            print("Enter value to be inserted")
            val=int(input())
            s.insertatbeg(val)
        elif(n is 2):
            print("Enter value to be inserted")
            val=int(input())
            s.insertatend(val)
        elif(n is 3):
            print("Enter the position, where value to be inserted")
            pos=int(input())
            print("Enter value to be inserted")
            val=int(input())
            s.insertatpos(pos,val)
        else:
            print("Invalid input")
    elif(n is 2):
        print("Which mode of deletion need to be performed?")
        print("1. Deletion at beginning")
        print("2. Deletion at end")
        print("3. Deletion at any position between start and end")
        n=int(input())
        if(n is 1):
            s.deleteatbeg()
        elif(n is 2):
            s.deleteatend()
        elif(n is 3):
            print("Enter value to be deleted")
            val=int(input())
            s.deleteatpos(val)
        else:
            print("Invalid input")
    elif(n is 3):
        print("Enter value to be searched")
        val=int(input())
        s.searching(val)
    elif(n is 4):
        print("Enter the value to be updated")
        val=int(input())
        print("Enter the new value")
        val1=int(input())
        s.updating(val,val1)
    elif(n is 5):
        s.display()
    elif(n is 6):
        exit()
    else:
        print("Invalid input")
