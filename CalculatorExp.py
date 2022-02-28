class Calculator:
    def add_Numbers(self,num1, num2, *additional):
        sum = num1 + num2
        for num in additional:
            sum = sum + num
        print (sum)

    def subtract_Numbers(self,num1, num2):
        diff = num1 - num2
        print (diff)

    def multiply_Numbers(self,num1, num2):
        product = num1 * num2
        print(product)

    def divide_Numbers(self,num1,num2):
        div = num1/num2
        print(div)


#basicCal = Calculator()
#basicCal.add_Numbers(122,20)