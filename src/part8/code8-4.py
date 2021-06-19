class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Cell(None)

    def insert(self, value):
        front = self.head
        rear = front.next

        cell = Cell(value)
        cell.next = rear
        front.next = cell

    def delete(self, value):
        front = self.head
        rear = front.next
        while rear:
            if rear.value == value:
                break
            front = rear
            rear = rear.next

        if not rear:
            print("[*] Data not found")
            return
        front.next = rear.next
        rear = None
    
    def show(self):
        tmp = self.head.next
        show_str = ""
        while tmp:
            if len(show_str) == 0:
                show_str += tmp.value
            else:
                show_str = tmp.value + "->" + show_str
            tmp = tmp.next

        print(show_str)

def bulk_insert(linklist: LinkedList, data: list):
    for i in data:
        linklist.insert(i)
        linklist.show()
    return linklist

data = ["a", "b", "c"]
l = bulk_insert(LinkedList(), data)
# l.show()
# l = LinkedList()
# print('insert 3, 5, 1...')
# l.insert("a")
# l.insert("b")
# l.insert("c")
# print('print data')
# l.show()
# print('delete 3...')
l.delete("b")
# print('print data')
l.show()