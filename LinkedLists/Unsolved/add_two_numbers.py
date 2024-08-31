
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#Time: 0(l1+l2) -- need to process both lists
#Space: 0(l1 or l2) -- whichever is larger
def add_two_numbers(l1: LinkedList, l2: LinkedList) -> LinkedList:
        #initialize a temp_node to be returned
        temp_head = Node(0)

        #initialize a temp_ptr that will build out return list
        temp_ptr = temp_head

        #account for carry being added to sum
        carry = 0

        #iterate through the lists
        while l1 or l2 or carry:
            #add values from each node
            num_l1 = l1.val if l1 else 0
            num_l2 = l2.val if l2 else 0

            sum = num_l1 + num_l2 + carry

            #account for carry
            carry = sum // 10

            #get remainder for l3 digit
            num_l3 = sum % 10

            #build return list with num_l3
            temp_ptr.next = Node(num_l3)

            #move l1 l2 AND temp_ptr
            temp_ptr = temp_ptr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next


        return temp_head.next

test_cases = [
    {"input": {"l1": [2, 4, 3], "l2": [5, 6, 4]}, "output": [7, 0, 8]},
    {"input": {"l1": [0], "l2": [0]}, "output": [0]},
    {
        "input": {"l1": [9, 9, 9, 9, 9, 9, 9], "l2": [9, 9, 9, 9]},
        "output": [8, 9, 9, 9, 0, 0, 0, 1],
    },
]


def test_solution(test_cases):
    for i in range(len(test_cases)):
        print(
            "Test",
            i + 1,
            "Pass:",
            LinkedList.compare_linked_list(
                add_two_numbers(
                    LinkedList.create_linked_list(test_cases[i]["input"]["l1"]),
                    LinkedList.create_linked_list(test_cases[i]["input"]["l2"]),
                ),
                LinkedList.create_linked_list(test_cases[i]["output"]),
            ),
        )
    return

if __name__=='__main__':
    test_solution(test_cases)