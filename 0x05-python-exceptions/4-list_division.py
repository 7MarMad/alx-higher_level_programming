#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list22 = []
    for i in range(0, list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            list22.append(res)
        except ZeroDivisionError:
            print("division by 0")
            list22.append(0)
        except (ValueError, TypeError):
            print("wrong type")
            list22.append(0)
        except IndexError:
            print("out of range")
            list22.append(0)
        finally:
            pass
    return list22
