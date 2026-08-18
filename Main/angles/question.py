class Question:

    def generate(self):
        raise NotImplementedError


    def solve(self):
        raise NotImplementedError


    def draw(self, ax):
        raise NotImplementedError


    def answer_text(self):
        return f"{self.answer:.0f}°"

