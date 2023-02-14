class Order:
    def __init__(self, OrderID) -> None:
        self.OrderID = OrderID
        self.next = None

class Preparing:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.OrderID)
            temp = temp.next

    def search(self, item):
        temp = self.head
        found = False
        while temp and not found:
            if temp.OrderID == item:
                found = True
            else:
                temp = temp.next

        if found == True:
            print('Found')
        else:
            print('Not found')

    def insert(self, value):
        new_node = Order(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, item):
        now = self.head
        pre = now
        found = False
        while now and not found:
            if now.data == item:
                found = True
                if now != self.head:
                    pre.next = now.next
                    now = None
                else:
                    self.head = self.head.next
                    now = None

            else:
                pre = now
                now = now.next

Preparing_list=Preparing()


def GetOrderID():  #随机生成取餐码
    return 