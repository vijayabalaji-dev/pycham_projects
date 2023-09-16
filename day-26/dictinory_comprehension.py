# import random
#
# new_dict = {"name": "balaji", "age": 18, "country": "india"}
#
# for (key, value) in new_dict.items():
#     print(key, value)
#
# names = ["alex", "freddy", "granny", "vishnu", "vijay"]
#
# dict_comp = {name:random.randint(1, 100) for name in names}
#
# print(dict_comp)
#
# marks_50 = {name: mark for (name, mark) in dict_comp.items() if mark > 50}
#
# print(marks_50)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}


print(result)
