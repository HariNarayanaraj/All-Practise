class exercise:
# Calculate the multiplication and sum of two numbers
    # 1 = Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
    def multiplication_of_two(num1 , num2):
        # calculate product of two number
        product = num1 * num2
        # check if product is less then 1000
        if product <=1000:
            return product
        else:
            return num1 + num2
    
    # first condition
    result1 = multiplication_of_two(20 , 30)
    print("result is", result1)
    
    
    # second condition
    result2 = multiplication_of_two(40 , 30)
    print("result is", result2)
    
    print(' NEXT '.center(80, '-'))


# Print the sum of the current number and the previous number    
    # 2 = Write a program  iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.
    def part(self):
        priviousnum = 0
        for i in range(1,11):
            x_sum = priviousnum + i
            print("current number :", i, "privious number :", priviousnum, "sum of :", x_sum)
            
            priviousnum = i

    
    
obj = exercise()
obj.part()
print(' NEXT '.center(80, '-'))


