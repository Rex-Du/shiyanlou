class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = cls.__instance or super().__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print('s1 is s2:', s1 is s2)
