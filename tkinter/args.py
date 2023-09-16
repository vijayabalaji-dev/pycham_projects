# *args allows us pass n number of arguments to the function


# def add(*args):
#     print(args)
#     for n in args:
#         print(n)
#
#
# add([1, 2, 3, 4, 5])

# args convers value passed to the fuctions as tuple
# eg add(1, 2, 3, 4, 5)
#
# will be converted into (1, 2, 3, 4, 5)
# *args can be replaced by any name *nums or *names etc...
def add(*nums):
    print(nums[0])
    tot = 0
    for n in nums:
        tot += n
    return tot


print(add(1, 2, 3, 4, 5))


# **kwargs takes keyword arguments as input converts them into dict
# it is recommended to use use kwargs.get("value") because if that argument not
# passed to this function it will simply return None

def calculate(n, **kwargs):
    print(kwargs)
    for (key, val) in kwargs.items():
        print(key, val)
    # below line will break if add or multiply does not pass to the funtion
    # new_dict = {"add": n + kwargs["add"], "multiply": n * kwargs["multiply"]}
    # below will work even if add or multiply does not pass to the function also

    new_dict = {"add": kwargs.get("add"), "multiply": kwargs.get("multiply")}

    print(new_dict)


calculate(4, add=4, divide=9)
