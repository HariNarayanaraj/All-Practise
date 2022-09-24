# create a list
list1 = list((1, 2, 3, 4, 5))
print("Original list ", list1)


class list:

    def __int__(self):
        pass

    def reverse(self):
        originalList = list1
        list1.reverse()
        print("Reverse for list ", list1)
        list1.reverse()

    def copy(self):
        list2 = list1.copy()
        print("Copy of list1 in list2 ", list2)


obj = list()
obj.reverse()
obj.copy()
