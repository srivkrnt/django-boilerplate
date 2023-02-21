class CustomEnumMeta(type):
    """
    Meta class to ConstantEnum class
    """

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj.__values__ = []
        obj.__keys__ = []
        for key, val in vars(obj).items():
            if isinstance(val, str) and not key.startswith("__"):
                obj.__values__.append(val)
                obj.__keys__.append(key)
        obj.keys = lambda: obj.__keys__
        obj.values = lambda: obj.__values__
        return obj

    def __getitem__(cls, key):
        return getattr(cls, key)

    def __iter__(cls):
        return zip(cls.__values__, cls.__keys__)


class ConstantEnum(metaclass=CustomEnumMeta):
    """
    Inheriting this class will provide below operations on the derived class
    1. list(DerivedCls) -> list down all the class attributes and their values
    2. DerivedCls.attr -> return the string representation of attr value
    3. DerivedCls['enum'] -> return the string representation of attr value
    4. 'attr' in DerivedCls -> existence check for given attr
    """
