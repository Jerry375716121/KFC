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
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp:
                pre = temp
                temp = temp.next
            pre.next = new_node

    def mid_insert(self, value):  # 中间插入，实现插队效果
        new_node = Order(value)
        if self.head is None:
            self.insert(value)
        else:
            temp = self.head
            counter = 0
            while temp:
                counter += 1
                temp = temp.next
            mid = int(counter/2)
            temp = self.head
            for i in range(mid-1):
                temp = temp.next
            temp1 = temp.next
            temp.next = new_node
            new_node.next = temp1

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
OrderID = 0000
menu = [['Hamburger', 20],
        ['Milk Tea', 25],
        ['Cola', 8],
        ['Fresh-Made Salad', 7],
        ['Vanilla Frosty', 10],
        ['Large Fries', 15],
        ['Middle Fries', 12]]


def set_menu(menu):  # 生成menu
    print('✿ MENU'.rjust(25), '✿')
    for i in range(len(menu)):
        print(i+1, '', menu[i][0].ljust(20), '  $'.rjust(20), menu[i][1])
    return menu


def Show_Ready_list():
    for i in Ready_list:
        print(i)


def GetOrderID():  # 按照顺序生成取餐码
    global OrderID
    OrderID += 1
    return OrderID


def get_total_price(food_arr):  # 计算总价
    total = 0
    for num in food_arr:
        index = int(num)
        total += menu[index][1]
    return total


def Cut_in(orders, ID):  # 插队
    flag = input(
        'Do you want to pay 10% more to cut into the queue? \nY for yes N for no\n')
    if flag == 'Y':
        print('You have been moved forward')
        Preparing_list.mid_insert(ID)
        return get_total_price(orders)*1.1
    elif flag == 'N':
        print('OK, total price is:')
        Preparing_list.insert(ID)
        return get_total_price(orders)


def update_dic(code, order_arr):
    order_dic = {}
    food_list = []
    for i in range(order_arr):
        food_list.append(menu[i][0])
    order_dic[code] = food_list


def Ordering():  # 用户点餐
    set_menu(menu)
    ID = GetOrderID()
    order_food_arr = []
    want = input('Do you want to order something? (yes or no):')
    if want == 'yes':
        order_food = (
            input('please choose your meal by entering the serial number\n'))
        for content in order_food:
            if content.isnumeric():
                if int(content) <= 7:
                    order_food_arr.append(int(content))
                else:
                    print('OUT OF RANGE')
        print(order_food_arr)
        print('Total price is:', Cut_in(order_food_arr, ID))
    else:
        print('Thank you for using the system')


def Transfer_to_Ready(order_id):  # 制作完成，通知取餐
    if Preparing_list.search(order_id) == True:
        Ready_list.append(order_id)
        Preparing_list.delete(order_id)
        Show_Ready_list()
    else:
        print('This ID is not in the Preparing_list')


def main():
    print('The food in processing:')
    Preparing_list.print_list()
    print('The food is ready:')
    Show_Ready_list()
    user_type = input('Input 1 if you are a customer, 2 if you are a worker:')
    if user_type == '1':
        Ordering()
        main()
    elif user_type == '2':
        Transfer_to_Ready(
            int(input('Input the order_id that is ready for serve:\n')))
        main()
    else:
        main()


main()
