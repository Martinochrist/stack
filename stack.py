#_____ this code is to demostrate how stack works____

# 1. create a linked list based stack
# push five values to the stack then pop three out
#  of the stack finally peek the stack.


# first to create a linklist we have to create how Node that will hold data

class Node:
    """ we then initialize the node """
    def __init__ (self,data=None):
        self.data = data
        self.next = None

# now we call how class where we difine functions that can help 
# how linked list work and we give it a class of stack

class Stack:
    """ now we will be initializing the stack  that holds the size of the  stack and is last value(top value)"""
    def __init__(self):
        self.top = None  # as we know we give the top none so we can give add values
        self.size = 0    #we initalize the size of the stack

    # now we define funtion that can push, pop and peek iteams from our stack

    def push(self,value):
        # create a new node
        node = Node(value)
        if self.top:
            node.next = self.top # this part of the code target the last code 
            self.top = node   # then we sent our top value to the new value we have 

        else:
            self.top = node #then -we make the to value point to the new item
        self.size += 1

    def pop(self): 
        # we difine the pop funcition
        if self.top:
            data =  self.top.data
            size = -1
            if self.top.next:
                self.top.next

            else:
                self.top =None
            return data
        else:
            print("stack is empty")

    def peek(self):
        #  this part of the code simple 
        if self.top:
            return self.top.data
        else:
            print("how stack is empty.")
# now we will call the function 
# we pass items to how push
# call the stack class and passing it to the instant iteam so we could work with it 
values = Stack()
values.push("man")
values.push("woman")
values.push("woman")
#  to comfirm that my program is run i picked the last value
print('i love the name', values.peek()) 




# #############  Question ###### two #########
#  2. write a program(using a stack) that accepts
#  user inputs which are sentences then when 
#  the user enters z it brings up all the previous 
#  sentences watch the example out                                                                                                                                                                                                                                                                 

# we know stack for its size for its size property so we give it a size of 5, we all assign an array to hold the data that will be inputed, and
#  lastly we check for the last value which is -1
# this code will be simple as no complex stuff
size = 4
data = []

#  we use a while loop to enable use take as much input as we can  take  
while True:

    #  this part takes input from the use 
     uer_i = input('enter a sentence or phare:\n')

     if  uer_i == 'z': # if we enter the word 'z' it keeps print out the value that was stored in the list 
         output = data.pop() # i am using the pop funtion to get the top of the starck and printing them out 
         print(output)
        

     elif uer_i != 'stop':
         data.append(uer_i)  # this part of the code send the data inputed to our local database which is data
         
         if len(data) == size: # this is where i impleented the stack property where i cheche to see how many values i have enter 
            # this part of the program print (caution to the use)
            print('my stack don full!! ')
            print("to remove stacked value enter 'z'")
            print("enter stop to stop the program! ") 

         else:
             print('spac still dey!!')  

     else:
         break

     


 

########### Question ####### three ########
# A Linked List Node
# this program is similar to what you though out but a sligth difference
# i added some extra function(method ) to them to get a deep understanding and also add more funtion  
class Node:
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next
 
#  i used another method to better understanding of how i can use linked list with my stack
class Stack:
    def __init__(self):
        self.top = None
        self.nodesCount = 0
 
    # function to add an element `x` to the stack
    def push(self, x):        # insert at the beginning
 
        # allocate a new node in a heap
        node = Node(x)
 
        # check if stack (heap) is full. Then inserting an element would
        # lead to stack overflow
        if node is None:
            print('stack Overflow')
            return
 
        # set data in the allocated node
        node.data = x
 
        # set the .next pointer of the new node to point to the current
        # top node of the list
        node.next = self.top
 
        # update top pointer
        self.top = node
 
        # increase stack's size by 1
        self.nodesCount += 1
 
    # Utility function to check if the stack is empty or not
    def isEmpty(self):
        return self.top is None
 
    # Utility function to return the top element of the stack
    def peek(self):
        # check for an empty stack
        if not self.isEmpty():
            return self.top.data
        else:
            print('The stack is empty')
            exit(-1)
 
    # Utility function to pop a top element from the stack
    def pop(self):            # remove at the beginning
 
        # check for stack underflow
        if self.top is None:
            print('Stack Underflow')
            exit(-1)
 
        # take note of the top node's data
        top = self.top.data
 
        # update the top pointer to point to the next node
        self.top = self.top.next
 
        # decrease stack's size by 1
        self.nodesCount -= 1
 
        return top
 
    # Function to return the size of the stack
    def size(self):
        return self.nodesCount
 
 
 
stack = Stack()
 
stack.push(1)
stack.push(2)
stack.push(3)
 
print('Top element is', stack.peek())
 
stack.pop()
stack.pop()
stack.pop()


# second list using link list
# initialization of how link list 
class Node:
    def __init__(self, data, next=None):
        self.data  = data
        self.next = next
 
 
class Stack_two:
    def __init__(self):
        self.top = None
        self.nodesCount = 0
 
    # function to add an element `x` to the stack
    def push(self, x):        # insert at the beginning
 
        # allocate a new node in a heap
        node = Node(x)
 
        # check if stack (heap) is full. Then inserting an element would
        # lead to stack overflow
        if node is None:
            print('Heap Overflow')
            return
 
        # set data in the allocated node
        node.data = x
 
        # set the .next pointer of the new node to point to the current
        # top node of the list
        node.next = self.top
 
        # update top pointer
        self.top = node
 
        # increase stack's size by 1
        self.nodesCount += 1
 
    # function to check if the stack is empty or not
    def isEmpty(self):
        return self.top is None
 

    # Function to return the size of the stack
    def size(self):
        return self.nodesCount
 
 

 
stack = Stack_two()
    #  then i saved  some list to work on.
stack.push('martin')
stack.push('lucky')
stack.push('francis')

    # i call the class stack to  my emty list to check my linked list if its empty or not 
if stack.isEmpty():
    print('The stack is empty')
else:
    print('The stack is not empty')



####### comment to the last class materal ######### 
#### i will reate it 10/10 because the  material is very detailed and understanding for me than the last one.

# thanks







    
    









