for i in range(200):
    if "BuiltinImporter" in ().__class__.__base__.__subclasses__()[i].__name__:
        print(i)
        break