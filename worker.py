from main import Number, Real


def main_func():
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))
    return Number(x, y).add(), Number(x, y).sub(), Real(x, y).sqrt(float(input("введіть дробове число: "))), Real(x,
                                                                                                                  y).step()


def display():
    print(main_func())


display()
