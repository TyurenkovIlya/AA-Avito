from typing import List


class Pizza:
    """Базовый класс пиццы"""

    def __init__(self, name: str, recipe: List[str], emoji: str, size: str = 'L') -> None:
        """
        :param name: название
        :param size: размер
        :param recipe: рецепт
        :param emoji: смайл отражающий наполнение
        """
        self.name = name
        self.size = size
        self.recipe = recipe
        self.emoji = emoji

    def __eq__(self, other) -> bool:
        """
        Метод проверки равенства двух пицц
        :param other: пицца, с который сравниваем указанную
        :return: равенство двух пицц
        """
        return self.size == other.size and self.recipe == other.recipe

    def dict(self) -> dict:
        """
        Метод возвращающий рецепт пиццы в виде словаря
        :return: рецепт пиццы в виде словаря
        """
        return {self.name + ' ' + self.emoji: self.recipe}


class Margherita(Pizza):
    """Класс пиццы маргариты"""

    def __init__(self, size: str = 'L'):
        super().__init__(
            name='Margherita',
            size=size,
            recipe=['tomato sauce', 'mozzarella', 'tomatoes'],
            emoji='🧀'
        )


class Pepperoni(Pizza):
    """Класс пиццы пепперони"""

    def __init__(self, size: str = 'L'):
        super().__init__(
            name='Pepperoni',
            size=size,
            recipe=['tomato sauce', 'mozzarella', 'pepperoni'],
            emoji='🍕'
        )


class Hawaiian(Pizza):
    """Класс пиццы гавайской"""

    def __init__(self, size: str = 'L'):
        super().__init__(
            name='Hawaiian',
            size=size,
            recipe=['tomato sauce', 'mozzarella', 'chicken', 'pineapples'],
            emoji='🍍'
        )


if __name__ == '__main__':
    Hawaiian().__eq__(Margherita())
    pass