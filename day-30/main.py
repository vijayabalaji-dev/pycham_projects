# try
# except
# else
# finally
#
# else will be excuted only if try block succeeds
# finally will be exected all the time

try:
    file = open("data.txt")
    new_dict = {"key": "value"}
    print(new_dict["fkfj"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("something")
except KeyError as error:
    print(f"the key {error} not found")
else:
    file.read()
finally:
    file.close()


height = float(input("Enter your height?: "))
if height > 3:
    raise ValueError("Human height should not be less than 3")
