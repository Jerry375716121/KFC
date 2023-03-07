import pprint as ppt
import pyinputplus as pyip
import pickle


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
            print(str(temp.OrderID).zfill(4))
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
            if now.OrderID == item:
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
Order_dic = {}       #是不是不需要了, 毕竟都在file里面了
OrderID = 0000
Order_count=0
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
        print(str(i).zfill(4))


def GetOrderID():  # 按照顺序生成取餐码
    global OrderID
    OrderID += 1
    return OrderID


def get_total_price(food_arr):  # 计算总价
    total = 0
    for num in food_arr:
        index = int(num)
        total += menu[index-1][1]
    return total


def Cut_in(orders, ID):  # 插队 (bug maybe)
    flag = pyip.inputMenu(['yes', 'no'],
                          'Do you want to pay 10% more to cut into the queue?\n')
    if flag == 'yes':
        print('You have been moved forward')
        Preparing_list.mid_insert(ID)
        return get_total_price(orders)*1.1
    elif flag == 'no':
        print('OK, total price is:')
        Preparing_list.insert(ID)
        return get_total_price(orders)
    else:
        return Cut_in(orders, ID)


def update_dic(dic, key, value):
    dic[key] = value


def Ordering():  # 用户点餐
    set_menu(menu)
    order_serial_arr = []
    order_food_arr = []
    is_change = True
    want = pyip.inputMenu(
        ['yes', 'no'], 'Do you want to order something?\n', lettered=True)
    if want == 'yes':
        ID = GetOrderID()
        order_food = (
            input('please choose your meal by entering the serial numbers\n'))
        for content in order_food:
            if content.isnumeric():
                if int(content) <= 7:
                    order_serial_arr.append(int(content))
                else:
                    print(f'{content} IS OUT OF RANGE')
        for i in order_serial_arr:
            order_food_arr.append(menu[i - 1][0])
        print('please check the orders:')
        order_instant_dic = {}
        for food in order_food_arr:
            if food in order_instant_dic:
                order_instant_dic[food] += 1
            else:
                update_dic(order_instant_dic, food, 1)
        ppt.pprint(order_instant_dic)
        change = pyip.inputMenu(
            ['yes', 'no'], 'Do you want to change anything?\n', lettered=True)
        while is_change:
            if change == 'yes':
                how_change = pyip.inputMenu(
                    ['add', 'reduce'], 'Add food or reduce food?\n', lettered=True)
                if how_change == 'add':
                    change_serial = (
                        input('Please enter the additions here:'))
                    for content in change_serial:
                        order_food_arr = []
                        if content.isnumeric():
                            if int(content) <= 7:
                                order_serial_arr.append(int(content))
                                print(f'___{content} is added')
                            else:
                                print(f"___{content} IS OUT OF RANGE")
                    for i in order_serial_arr:
                        order_food_arr.append(menu[i-1][0])
                elif how_change == 'reduce':
                    change_serial = (
                        input('Please enter the serial number of the reduces here:'))
                    for content in change_serial:
                        if int(content) not in order_serial_arr:
                            print(f'___{content} is not in the list')
                        else:
                            order_food_arr = []
                            if content.isnumeric():
                                if int(content) <= 7:
                                    order_serial_arr.remove(int(content))
                                    print(f'___{content} is removed')
                                    for i in order_serial_arr:
                                        order_food_arr.append(menu[i - 1][0])
                                else:
                                    print(f'___{content} IS OUT OF RANGE')
                else:
                    print('Error exists')
                print('The updated food list is:')
                order_instant_dic = {}
                for food in order_food_arr:
                    if food in order_instant_dic:
                        order_instant_dic[food] += 1
                    else:
                        update_dic(order_instant_dic, food, 1)
                ppt.pprint(order_instant_dic)
            want_change = pyip.inputMenu(['yes', 'no'], 'No change?\n')
            if want_change == 'no':
                is_change = False
            elif want_change == "yes":
                change = "yes"
        print('Total price is: $', '%.2f' %
              round(Cut_in(order_serial_arr, ID), 2))
    else:
        print('Thank you for using the system')
    update_dic(Order_dic, ID, order_food_arr)
    get_txtFile(ID)


def Transfer_to_Ready(order_id):  # 制作完成，通知取餐
    if Preparing_list.search(order_id) == True:
        Ready_list.append(order_id)
        Preparing_list.delete(order_id)
        Show_Ready_list()
    else:
        print('This ID is not in the Preparing_list')
# 把取餐码存在文件里 文件需要更新（插队）


def get_txtFile(orderID):
    fp = open('OrderID.txt', 'a')
    fp.write(str(orderID))
    fp.write("\n")
    fp.close()
    print(fp)


def delete_txtFile(orderID):
    fp = open('OrderID.txt', 'r+')
    arr = []
    for i in fp:
        arr.append(str(i))
    arr.remove(orderID)
    for i in arr:
        fp.write(i)
    fp.close()


def get_OrderDat(order):
    global Order_count
    with open('Order.dat', 'rb+') as fp:
        pickle.dump(order, fp)
    Order_count+=1

def remove_OrderDat(ID):
    global Order_count
    with open('Order.dat', 'rb+') as fp:
        for i in range(Order_count):
            data=pickle.load(fp)
            if data.OrderID==ID:
                return
        return  


def main():
    print('The food in processing:')
    Preparing_list.print_list()
    print('The food is ready:')
    Show_Ready_list()
    user_type = pyip.inputMenu(
        ['worker', 'customer'], 'Hello, you are?\n', lettered=True)
    if user_type == 'customer':
        Ordering()
    elif user_type == 'worker':
        print('The pick-up code in processing is:')
        ppt.pprint(Order_dic)
        ID = int(input('Input the order_id that is ready for serve:\n'))
        Transfer_to_Ready(ID)
        del Order_dic[ID]
        print('The updated pick-up code in processing is:')
        ppt.pprint(Order_dic)
        delete_txtFile(ID)


main()
