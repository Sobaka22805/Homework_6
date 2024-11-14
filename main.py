import inspect


def inspect_class(cls):
    print(f"\nІнспекція класу {cls.__name__}:")

    attributes = [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]
    print(f"Список атрибутів: {attributes}")

    methods = [method[0] for method in inspect.getmembers(cls, predicate=inspect.isfunction)]
    print(f"Список методів: {methods}")


inspect_class(Student)

inspect_class(Worker)
