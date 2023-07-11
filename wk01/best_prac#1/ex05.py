class MyInt:
    def __init__(self, number):
        self.number = number

    def __sub__(self, number):
        return self.number - number.number//2

    def isPrime(self):
        if self.number < 2:
            return False
        for i in range(2, self.number):
            if self.number % i == 0:
                return False
        return True

    def showPrime(self):
        prime_numbers = []
        for number in range(2, self.number + 1):
            if self.isNumberPrime(number):
                prime_numbers.append(str(number))

        if len(prime_numbers) == 0:
            return "!!!A prime number is a natural number greater than 1"
        return " ".join(prime_numbers)

    def isNumberPrime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True


print(" *** class MyInt ***")
numbers = input("Enter 2 number : ").split()
num1, num2 = int(numbers[0]), int(numbers[1])

a = MyInt(num1)
b = MyInt(num2)

print(f"{num1} isPrime : {a.isPrime()}")
print(f"{num2} isPrime : {b.isPrime()}")

print(f"Prime number between 2 and {num1} : {a.showPrime()}")
print(f"Prime number between 2 and {num2} : {b.showPrime()}")

result = num1 - round(num2 / 2)
print(f'{a.number} - {b.number} = {a-b}')
