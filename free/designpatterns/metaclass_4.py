class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance



class SingletonInstance(metaclass=SingletonMeta):
    def __init__(self):
        print(id(self))



if __name__ == "__main__":
    s1 = SingletonInstance()
    s2 = SingletonInstance()
    print(s1 is s2)
