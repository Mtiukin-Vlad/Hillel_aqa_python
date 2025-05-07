class Rombs:
    def __init__(self, сторона_а, кут_а):
        self.сторона_а = сторона_а
        self.кут_а = кут_а

    def __setattr__(self, name, value):
        if name == 'сторона_а':
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більшою за 0.")
        elif name == 'кут_а':
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути в межах від 0 до 180 градусів.")
            object.__setattr__(self, 'кут_б', 180 - value)

        object.__setattr__(self, name, value)

    def __str__(self):
        return f"Ромб: сторона = {self.сторона_а}, кут А = {self.кут_а}, кут Б = {self.кут_б}"
