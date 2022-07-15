print("module1 printed")

if __name__ == "module1":
    print("in module1, __name__ is module1")
if __name__ == "__main__":
    print("in module1, __name__ is __main__")

print("anyways, in module1, __name__ is : ", __name__)