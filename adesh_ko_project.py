
print("StudentName: Aadesh Ghimire StudentId: 21506191 \n")

def fibonacci_sequence(n):
    if n<=2:
        return 1
    return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)
print("fibonacci number of 4 is " + str(fibonacci_sequence(4)))
print("fibonacci number of 8 is " + str(fibonacci_sequence(8)))
print("fibonacci number of 3 is " + str(fibonacci_sequence(3)))
print("fibonacci number of 7 is " + str(fibonacci_sequence(7)))























# print("StudentName: Aadesh Ghimire   StudentId: 21506191 \n")
#
# def insertionSort(alist):
#     for index in range(1,len(alist)):
#         currentvalue = alist[index]
#         position = index
#
#         while position > 0 and alist[position-1]>currentvalue:
#             alist[position]=alist[position-1]
#             position = position-1
#
#         alist[position]=currentvalue
#         print(alist)
#
# studentnumber = [2,1,5,0,6,1,9,1]
# print("student number insertion sorting steps by steps")
# insertionSort(studentnumber)
#
# print("\nsorted student number by insertion sort")
# print(studentnumber)



































# print("StudentName: Aadesh Ghimire   StudentId: 21506191 \n")
#
# def selectionSort(alist):
#     for fillslot in range (len(alist)-1,0,-1):
#         positionOfMax= 0
#         for location in range(1,fillslot+1):
#             if alist[location]>alist[positionOfMax]:
#                 positionOfMax = location
#
#         temp = alist[fillslot]
#         alist[fillslot] = alist[positionOfMax]
#         alist[positionOfMax] = temp
#         print(alist)
#
# student_number = [2,1,5,0,6,1,9,1]
# print("Student number selection sorting steps by steps:")
# selectionSort(student_number)
#
# print("\nsorted student number by selection sort")
# print(student_number)
# print()





























# class Node:
#     def __init__(self,init_data):
#         self.data=init_data
#         self.next = None
#     def get_data(self):
#         return self.data
#     def get_next(self):
#         return self.next
#     def set_data(self,new_data):
#         self.data = new_data
#     def set_next(self,new_next):
#         self.next = new_next
#
# class UnorderedList:
#     def __init__(self):
#         self.head = None
#
#     def add(self,item):
#         temp = Node(item)
#         temp.set_next(self.head)
#         self.head = temp
#
#     def is_empty(self):
#         return self.head == None
#
#     def size(self):
#         curr= self.head
#         count = 0
#         while curr!= None:
#             count = count +1
#             curr = curr.get_next()
#         return count
#
#     def search(self,item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.get_data() == item:
#                 found = True
#             else:
#                 current = current.get_next()
#         return found
#
#     def print_list(self):
#         curr = self.head
#         while curr != None:
#             print(curr.get_data())
#             curr = curr.get_next()
#         print()
#
# studentnumber=[2,1,5,0,6,1,9,1]
# list = UnorderedList()
# for i in (studentnumber):
#     list.add(i)
# print(list.size())
# print(list.is_empty())
# print(list.print_list())
# print("Enter a number to search in the list:")
# y = input()
# print(list.search(y))













# print("StudentName: Aadesh Ghimire   StudentId: 21506191 \n")
# class stack:
#     def __init__(self):
#         self.items= []
#     def isEmpty(self):
#         return self.items==[]
#     def push(self,item):
#         self.items.append(item)
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         return self.items[len(self.items)-1]
#     def size(self):
#         return len(self.items)
#
# class queue:
#     def __init__(self):
#         self.items=[]
#     def isEmpty(self):
#         return self.items ==[]
#     def size(self):
#         return len(self.items)
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue(self):
#         return self.items.pop()
#
# newstack = stack()
# newqueue = queue()
# #
# # #Instering student id to stack
# newstack.push(2)
# newstack.push(1)
# newstack.push(5)
# newstack.push(0)
# newstack.push(6)
# newstack.push(1)
# newstack.push(9)
# newstack.push(1)
# #
# # #emptying the stack and enqueueing to queue
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
# newqueue.enqueue(newstack.pop())
#
# # Emptying the queue
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())
# print(newqueue.dequeue())








