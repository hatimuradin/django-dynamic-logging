import enum

@enum.unique
class AutoNameEnum(str, enum.Enum):
    @classmethod
    def get_members(cls):
        return [e.name for e in cls.__members__.values()]

    @classmethod
    def get_labels(cls):
        return [e.value for e in cls.__members__.values()]

    @classmethod
    def as_dict(cls):
        return [{e.name: e.value} for e in cls.__members__.values()]

    @classmethod
    def as_tuple(cls):
        return [(e.name, e.value) for e in cls.__members__.values()]

    @property
    def text(self):
        return (self.value)

    def __str__(self) -> str:
        return self.value

    def _generate_next_value_(name, start, count, last_values):
        return name