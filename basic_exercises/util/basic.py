def print_test(input, expected, actual, title=""):
    msg = ""
    if title:
        msg += title + "\n"
    msg += "INPUT: {input}\nEXPECTED: {expected}\nACTUAL: {actual}".format(
        title=title, input=input, expected=expected, actual=actual)

    print(msg)


def check_user_input(input):
    try:
        return int(input)
    except ValueError:
        return float(input)


def get_num_from_user(maxAttempts=10, attempts=1):
    try:
        return check_user_input(input("Give me a number pls"))
    except ValueError:
        print(attempts)
        if attempts < maxAttempts:
            return get_num_from_user(maxAttempts, attempts+1)
        raise Exception("Max number of attempts reached, aborting.")


def get_nums_from_user(numsAmount):
    nums = []
    for i in range(numsAmount):
        try:
            nums.append(get_num_from_user())
        except:
            print("Does it actually take you this long to enter a number correctly?")

    return nums
