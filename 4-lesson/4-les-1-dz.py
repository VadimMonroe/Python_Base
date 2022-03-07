from sys import argv

script_name, hours, zp_hour, bonus = argv


def func_zp(hours=float(hours), zp_hour=float(zp_hour), bonus=float(bonus)):
    return (hours * zp_hour) + bonus


print(func_zp())
