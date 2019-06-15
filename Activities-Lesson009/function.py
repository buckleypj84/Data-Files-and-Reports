def MySubName(name):
    print("Hello " + name)

def Multiply(num1, num2):
    return num1 * num2

MySubName("dino")
x = Multiply(5,3)
print(x)
#print(y)

def MultiplyList(numbers):
    result = 1
    for number in numbers:
        result = result * number
    return result
print(MultiplyList([1,2,4,6,8,13]))


