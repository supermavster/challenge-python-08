import time
from datetime import datetime


def finish_date(func):
    # You have to code here!!
    # Debe modificar el comportamiento de una función de cualquier tipo añadiendo al final un print en consola que indique la fecha y hora en la que terminó de ejecutarse la función, en el formato `dd/mm/YYYY - HH:MM:SS`
    def wrapper(*args, **kwargs):
        # Initial Date
        initial_time = time.time()
        # Execute function
        func(*args, **kwargs)
        # End Date
        final_time = time.time()
        # Convert format Date
        initial_time = datetime.fromtimestamp(
            initial_time).strftime("%d/%m/%Y - %H:%M:%S")
        final_time = datetime.fromtimestamp(
            final_time).strftime("%d/%m/%Y - %H:%M:%S")
        print(
            f'The function {func.__name__} took {initial_time} to {final_time}')
    return wrapper


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
