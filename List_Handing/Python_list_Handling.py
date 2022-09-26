# create a list
list1 = list((10, 20, 30, 40, 50, 60, 70, 80, 90))
print("Original list ", list1)


class List:
    def __int__(self):
        pass

    # Reverse the list
    def reverse(self):
        originalList = list1
        list1.reverse()
        print("Reverse for list ", list1)
        list1.reverse()

    # Copy the one list to another list
    def copy(self):
        list2 = list1.copy()
        print("Copy of list1 in list2 ", list2)

    # Multiply by 10
    def mulbyten(self):
        a = 10
        list3 = []
        for x in list1:
            list3.append(x * a)
            print("Multiply by 10 for list ", list3)

    # divide by 10
    def divbyten(self):
        a = 10
        list1[:] = [x / a for x in list1]
        print("divide by 10 for list ", list1)

    # Add the value in side the list front and last
    def add(self):
        list1.insert(0, 100)
        print("add value first element in list ", list1)

        list1.append(100)
        print("add value in last element list ", list1)

    # remove the value in side the list front and bottom
    def remove(self):
        del list1[0]
        print("remove value first element in list ", list1)

        list1.pop(-1)
        print("remove value in last element list ", list1)

    # check the Average of the list
    def average(self):
        Average = sum(list1) / len(list1)
        print("Average value of list ", Average)

    # check the odd Numbers of the list
    def odd(self):
        for x in list1:
            if x % 2 != 0:
                odd_list = [x]
                print("Odd value of list ", odd_list)

    # check the even Numbers of the list
    def even(self):
        evenlist = [x for x in list1 if x % 2 == 0]
        print("Even value of list ", evenlist)

    # clear all element in the list
    def clear(self):
        list1.clear()
        print(list1)


obj = List()
obj.reverse()
obj.copy()
obj.mulbyten()
obj.divbyten()
obj.add()
obj.remove()
obj.average()
obj.odd()
obj.even()
obj.clear()


