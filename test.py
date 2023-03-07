import pickle


class student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id


student1 = student('Jerry', 19)
student2 = student('Icey', 18)

fp = open('Order.dat', 'rb+')
pickle.dump(student1, fp)
pickle.dump(student2, fp)
fp.close()

fp = open('Order.dat', 'rb+')
print(pickle.load(fp).name)
print(pickle.load(fp).name)
fp.close()

fp=open('Order.dat','w')
fp.close()
