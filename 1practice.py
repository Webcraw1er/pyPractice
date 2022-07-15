import module1

print("1prctice(main) printed")
if __name__ == "module1":
    print("in main, __name__ is module1")
if __name__ == "__main__":
    print("in main, __name__ is __main__")

print("anyways, in main, __name__ is : ", __name__)