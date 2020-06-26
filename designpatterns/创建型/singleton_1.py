class Singleton:
    """
    单例模式
    """
    class _A:
        def display(self):
            return id(self)
    
    __instance__ = None

    def __init__(self):
        __class__._instance = __class__.__instance__ or __class__._A()

    def __getattr__(self, attr):
        return getattr(__class__._instance, attr)
    
    def __setattr__(self, attr, value):
        setattr(__class__._instance, attr, value)


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print('id(s1):', id(s1))    # 6
    print('id(s2):', id(s2))

    print('s1.display():', s1.display())    # 7
    print('s2.display():', s2.display())

    s1.name = 'James'    # 8
    print('s1.name:', s1.name)
    print('s2.name:', s2.name)