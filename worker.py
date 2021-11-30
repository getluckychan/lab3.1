from main import Number, Real


def main_func():
    first_number = float(input("Введіть перше число: "))
    second_number = float(input("Введіть друге число: "))
    working = Number(first_number, second_number)
    new_working = Real(first_number, second_number)
    return working.add(), working.sub(), new_working.sqrt(), new_working.step()


main_func()
