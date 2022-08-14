import datetime
import time
import os


def logger_self(old_function):
    def new_function(*args, **kwargs):
        print(f'Вызвана функция : {old_function.__name__} с аргументами {args} и {kwargs}')
        print(f'Время вызова функции: {datetime.datetime.now()}')

        result = old_function(*args, **kwargs)
        print(f'Результат : {result}')
        return result

    return new_function


def logger_to_file(old_fuction):
    def new_function(*args, **kwargs):
        result = old_fuction(*args, **kwargs)
        with open(os.path.join('logs.txt'), 'a') as logs_result:
            logs_result.write(
                f'Время :{datetime.datetime.now()} Функция: {old_fuction.__name__},Аргументы: {args} -{kwargs} , Результат: {result}\n')

        return result

    return new_function


@logger_to_file
def summator(a, b):
    result = a + b
    print(result)
    return result
