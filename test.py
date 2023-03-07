import pickle


class student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id


student1 = student('Jerry', 19)
student2 = student('Icey', 18)
student3 = student('Bob', 10)

temp = []

fp = open('Order.dat', 'rb+')
pickle.dump(student1, fp)
pickle.dump(student2, fp)
pickle.dump(student3, fp)
fp.close()


fp = open('Order.dat', 'rb+')
for i in range(3):
    data = pickle.load(fp)
    if data.name != 'Jerry':
        temp.append(data)
fp.close()

fp = open('Order.dat', 'w')
fp.close()

fp = open('Order.dat', 'rb+')
for i in range(len(temp)):
    pickle.dump(temp[i], fp)
fp.close()


fp = open('Order.dat', 'rb+')
for i in range(2):
    print(pickle.load(fp).name)
fp.close()

fp = open('Order.dat', 'w')
fp.close()
