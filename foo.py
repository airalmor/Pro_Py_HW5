from util import logger_self, logger_to_file


@logger_self
def summator(a, b):
    result = a + b
    return result


@logger_to_file
def devider(a, b):
    result = a / b
    return result
