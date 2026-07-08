class Environment:
    def __init__(self):
        self.values = {}

    def define(self, name: str, value):
        self.values[name] = value

    def get(self, name: str):
        if name in self.values:
            return self.values[name]
        raise NameError(f"Variable {name!r} is not defined")

    def assign(self, name: str, value):
        # TODO: update an existing name; otherwise raise NameError.
        raise NotImplementedError("TODO: implement assign()")

    def __repr__(self) -> str:
        return f"Environment({self.values})"
