import copy
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    if llist_1.size()==0:
        if llist_2.size()==0:
            return None
        else:
            return llist_2
    elif  llist_2.size()==0:
        return llist_1
    else:
        union_list=copy.deepcopy(llist_1)
        current = union_list.head
        while(current.next):
            current=current.next
        current.next=llist_2.head
        return union_list
    pass

def intersection(llist_1, llist_2):
    if llist_1.size() == 0 or llist_2.size() == 0  :
        return None
    else:
        intersectionList=LinkedList()
        current_list1 = llist_1.head
        while (current_list1):
            value=current_list1.value
            current_list2 = llist_2.head
            while (current_list2):
                value2=current_list2.value
                if value==value2:
                    intersectionList.append(value)
                    break
                current_list2 = current_list2.next
            current_list1 = current_list1.next
        if intersectionList.size()==0:
            return None
        return intersectionList



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

union1_solution_array=[3,2,4,35,6,65,6,4,3,21,6,32,4,9,6,1,11,21,1]
union1_solution_list=LinkedList()
for i in union1_solution_array:
    union1_solution_list.append(i)
result1=union(linked_list_1,linked_list_2)
test_case1=[result1,union1_solution_list]
union2_solution_array=[3,2,4,35,6,65,6,4,3,23,1,7,8,9,11,21,1]
union2_solution_list=LinkedList()
for i in union2_solution_array:
    union2_solution_list.append(i)
result2=union(linked_list_3,linked_list_4)
test_case2=[result2,union2_solution_list]
intersection1_solution_array=[4,6,6,4,21]
intersection1_solution_list=LinkedList()
for i in intersection1_solution_array:
    intersection1_solution_list.append(i)
result3=intersection(linked_list_1,linked_list_2)
test_case3=[result3,intersection1_solution_list]
intersection2_solution=None
result4=intersection(linked_list_3,linked_list_4)
test_case4=[result4,intersection2_solution]


def test_functions(test_case):
    result = test_case[0]
    solution = test_case[1]
    if solution==None:
        if result==None:
            print("Pass")
        else:
            print("Fail")
    else:
        try:
            r_head=result.head
            s_head=solution.head
            while (r_head and s_head):
                if (r_head.value!=s_head.value):
                    print("Fail")
                    return
                    r_head=r_head.next
                    s_head=s_head.next
                print("Pass")
                return
            else:
                print("Fail")
        except Exception as e:
            print("Fail")

test_functions(test_case1)
test_functions(test_case2)
test_functions(test_case3)
test_functions(test_case4)