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
            return True
        else:
            return False

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


Preparing_list = Preparing()
Ready_list = []


def Show_Ready_list():
    for i in Ready_list:
        print(i)


def GetOrderID():  # 随机生成取餐码
    return


def Ordering():  # 用户点餐
    return


def Transfer_to_Ready(order_id):  # 制作完成，通知取餐
    if Preparing_list.search(order_id) == True:
        Ready_list.append(order_id)
        Preparing_list.delete(order_id)
        Show_Ready_list()
    else:
        print('This ID is not in the Preparing_list')
