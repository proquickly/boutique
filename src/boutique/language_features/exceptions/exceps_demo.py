from loguru import logger


def math_divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    return numerator / denominator


assert math_divide(5, 2) == 2.5
# math_divide(4, 0)


def open_file(file_name):
    return open(file_name, "r")


try:
    f = open_file("doesnt_exist.csv")

except FileNotFoundError:
    f = open("doesnt_exist.csv", "w")
    f.write("header")
    f.close()
    f = open_file("doesnt_exist.csv")
    logger.info("Created new file")

except IOError as e:
    logger.error(e)

else:
    logger.info("Used existing file")

finally:
    assert f.readlines() == ["header"]
    f.close()
