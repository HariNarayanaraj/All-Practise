# create a list
Tuple = tuple((1, 3, 3, 2, 4, 6, 7, 8, 9))
print("Original list ", Tuple)


class List:
    def __int__(self):
        pass

    # Reverse the Tuple_list1
    def reverse(self):
        tuple_list = list(Tuple)
        tuple_list.reverse()
        reversed_tuple = tuple(tuple_list)
        print("Reverse for list ", reversed_tuple)
        tuple_list.reverse()
        Ori_tuple = tuple(tuple_list)
        print("Original for list ", Ori_tuple)

    # Copy the one list to another list
    def copy(self):
        tuple_list = list(Tuple)
        tuple_list2 = tuple_list.copy()
        Ori_tuple = tuple(tuple_list2)
        print("Copy of list1 in list2 ", tuple_list2)

    # Multiply by 10
    def mulbyten(self):
        list1 = list(Tuple)
        a = 10
        list2 = []
        for x in list1:
            list2.append(x * a)
            tuple_list2 = tuple(list2)
            print("Multiply by 10 for list ", tuple_list2)

    # divide by 10
    def divbyten(self):
        list1 = list(Tuple)
        a = 10
        list1[:] = [x / a for x in list1]
        tuple_list2 = tuple(list1)
        print("divide by 10 for list ", tuple_list2)

    def add(self):
        list1 = list(Tuple)
        list1.insert(0, 100)
        print("add value first element in list ", list1)

        list1.append(100)
        tuple_list2 = tuple(list1)
        print("add value in last element list ", tuple_list2)

    def remove(self):
        list1 = list(Tuple)
        del list1[0]
        print("remove value first element in list ", list1)

        list1.pop(-1)
        tuple_list2 = tuple(list1)
        print("remove value in last element list ", tuple_list2)

    def average(self):
        list1 = list(Tuple)
        Average = sum(list1) / len(list1)
        print("Average value of list ", Average)

    def odd(self):
        list1 = list(Tuple)
        for x in list1:
            if x % 2 != 0:
                odd_list = [x]
                tuple_list2 = tuple(odd_list)
                print("Odd value of list ", tuple_list2)

    def even(self):
        list1 = list(Tuple)
        list1 = [x for x in list1 if x % 2 == 0]
        tuple_list2 = tuple(list1)
        print("Even value of list ", tuple_list2)


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
