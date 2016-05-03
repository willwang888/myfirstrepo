
class Node(object):
    def __init__(self, value, next=None): # if we're considering Nodes to be immutable
        self.value = value                # we need to set all their attributes up
        self.next = next                  # front, since we can't change them later

def reverse_list_nondestructive(head):
    new_head = None
    while head:
        new_head = Node(head.value, new_head)
        head = head.next
    return new_head

def print_list(n):
  print(n.value),
  nxt = n.next
  while nxt:
    print(nxt.value),
    nxt = nxt.next

n0 = Node(20)
n1 = Node(4,n0)
n2 = Node(15,n1)
n3 = Node(85,n2)
n4 = Node(9,n3)
n5 = Node(4,n4)

print("linked list original: ")
print_list(n5)
new_head = reverse_list_nondestructive(n5)
print
print("linked list reversed: ")
print_list(new_head)
print
print("linked list original: ")
print_list(n5)

