from util import logger_self, logger_to_file, parametrized_logger_to_file


@logger_self
def summator(a, b):
    result = a + b
    return result


@logger_to_file
def devider(a, b):
    result = a / b
    return result


@parametrized_logger_to_file('logs2')
def summator2(a, b):
    result = a + b
    print(result)
    return result
