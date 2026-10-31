class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores  # list

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def to_dict(self):
        return {"name": self.name, "age": self.age, "scores": self.scores}

    def __repr__(self):
        return f"{self.name} (سن: {self.age}, معدل: {self.average():.2f})"