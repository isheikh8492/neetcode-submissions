class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self, head=None):
        self.head = head

    
    def get(self, index: int) -> int:
        current = self.head
        counter = 0
        
        while current and counter != index:
            current = current.next
            counter += 1

        return current.value if current else -1

    def insertHead(self, val: int) -> None:
        node = Node(value=val)
        node.next = self.head
        self.head = node        

    def insertTail(self, val: int) -> None:
        current = self.head
        while current and current.next is not None:
            current = current.next

        if current is not None:
            current.next = Node(value=val)
        else:
            self.head = Node(value=val)
        

    def remove(self, index: int) -> bool:
        prev = None
        current = self.head
        counter = 0

        while current and counter != index:
            prev = current
            current = current.next
            counter += 1

        if current is None:
            return False
        else:
            if prev:
                prev.next = None
                current = current.next
                prev.next = current
            else:
                current = current.next
                self.head = current
            
        return True

        

    def getValues(self) -> List[int]:
        result = []

        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        
        return result
        
