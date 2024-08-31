

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def remove_nth_node_from_end(head:LinkedList, n:int):
    if not (head):
        return

    # establish temp node
    temp = Node(0)
    # set temp node next to head of list
    temp.next = head

    # init slow and fast pointers to temp node
    slow_ptr = temp
    fast_ptr = temp

    # move fast pointer to n
    for _ in range(n):
        fast_ptr = fast_ptr.next

    # while fast pointer is not at last node in list
    # move fast and slow pointers by 1
    while fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next

    # when at end, node between fast and slow is target,
    # set next node of slow pointer to the current fast pointer node
    slow_ptr.next = slow_ptr.next.next

    return temp.next

test_cases = [
    {'input': { 'list': [1,2,3,4], 'index': 2 }, 'output': [1,2,4]},
    {'input': { 'list': [1,2,3,4], 'index': 3 }, 'output': [1,3,4]},
    {'input': { 'list': [1,2,3,4,5,6], 'index': 6 }, 'output': [2,3,4,5,6]},
    {'input': { 'list': [1], 'index': 1 }, 'output': []},
    {'input': { 'list': [1,2,3,4,5,6], 'index': 3 }, 'output': [1,2,3,5,6]}
]

def test_solution(test_cases):
    for i in range(len(test_cases)):
        print(
            "Test",
            i + 1,
            "Pass:",
            LinkedList.compare_linked_list(
                remove_nth_node_from_end(
                    LinkedList.create_linked_list(test_cases[i]["input"]['list']), 
                    test_cases[i]['input']['index']
                    ),
                LinkedList.create_linked_list(test_cases[i]["output"]),
            )
        )
        
if __name__ == '__main__':
    test_solution(test_cases)