# create a list
Set = set((1, 3, 3, 2, 4, 6, 7, 8, 9))
print("Original list ", set)


class Set_match:
    def __int__(self):
        pass

    # Reverse the set by using list method
    def reverse(self):
        Set_list = list(Set)
        Set_list.reverse()
        reversed_Set = set(Set_list)
        print("Reverse for list ", reversed_Set)
        Set_list.reverse()
        Ori_Set = set(Set_list)
        print("Original for list ", Ori_Set)

    # Copy the one set list to another Tuple list
    def copy(self):
        Set2 = Set.copy()
        print("Copy of list1 in list2 ", Set2)

    # Multiply by 10 in set by using list element
    def mulbyten(self):
        list1 = list(Set)
        a = 10
        list2 = []
        for x in list1:
            list2.append(x * a)
            Set_list2 = set(list2)
            print("Multiply by 10 for list ", Set_list2)

    # divided by 10 in set by using list element
    def divbyten(self):
        list1 = list(Set)
        a = 10
        list1[:] = [x / a for x in list1]
        Set_list1 = set(list1)
        print("divide by 10 for list ", Set_list1)

    # Add element in set by using list both sides
    def add(self):
        list1 = list(Set)
        list1.insert(0, 100)
        print("add value first element in list ", list1)

        list1.append(100)
        Set_list2 = set(list1)
        print("add value in last element list ", Set_list2)

    # element in set by using list both sides
    def remove(self):
        list1 = list(Set)
        del list1[0]
        print("remove value first element in list ", list1)

        list1.pop(-1)
        Set_list2 = set(list1)
        print("remove value in last element list ", Set_list2)

    # check the average Set
    def average(self):
        Average = sum(Set) / len(Set)
        print("Average value of list ", Average)

    # Find the odd element in Set
    def odd(self):
        for x in Set:
            if x % 2 != 0:
                odd_Set = {x}
                print("Odd value of list ", odd_Set)

    # Find the even element in Set by using List
    def even(self):
        list1 = list(Set)
        list1 = [x for x in list1 if x % 2 == 0]
        Set_list2 = set(list1)
        print("Even value of list ", Set_list2)


obj = Set_match()
obj.reverse()
obj.copy()
obj.mulbyten()
obj.divbyten()
obj.add()
obj.remove()
obj.average()
obj.odd()
obj.even()
