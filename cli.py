from pizza import Pizza, Pepperoni, Margherita, Hawaiian
import click
import random

@click.group()
def cli():
    pass


@cli.command()
@click.argument('pizza', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
@click.option('--size', default='L', type=str)
def order(pizza: str, delivery: bool, size: str = 'L') -> None:
    """
    Готовит и доставляет пиццу
    """

    pizza_dict = {
        Margherita(size).name.lower(): Margherita(size),
        Pepperoni(size).name.lower(): Pepperoni(size),
        Hawaiian(size).name.lower(): Hawaiian(size)
    }

    pizza = pizza.lower()

    bake(pizza_dict[pizza])
    if delivery:
        deliver(pizza_dict[pizza])
    else:
        pickup(pizza_dict[pizza])


# TODO: Change menu
@cli.command()
def menu() -> None:
    """
    Выводит меню
    """

    pizza_menu = {
        '— Margherita 🧀': ['tomato sauce', 'mozzarella', 'tomatoes'],
        '— Pepperoni 🍕': ['tomato sauce', 'mozzarella', 'pepperoni'],
        '— Hawaiian 🍍': ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
    }

    for pizza, ingredient in pizza_menu.items():
        print(f'{pizza}: {", ".join(ingredient)}')


def log(message: str) -> callable:
    """
    Декоратор для вывода сообщения о статусе пиццы
    """

    def log_decorator(func):
        def wrapper(*args):
            time_cooking = random.randint(300, 1200)
            if args[0].size == 'XL' and func.__name__ == 'bake':
                time_cooking *= 2
                print('⌛ Мы готовим большую пиццу, вам придется немного подождать')
            func(*args)
            print(message.format(time_cooking // 60, time_cooking % 60))

        return wrapper

    return log_decorator


@log('🍳 Пиццу приготовили за {} мин {} сек')
def bake(pizza: Pizza) -> None:
    """
    Приготовление пиццы
    """
    pass


@log('🛵 Пиццу доставили за {} мин {} сек')
def deliver(pizza: Pizza) -> None:
    """
    Доставка пиццы
    """
    pass


@log('🏠 Пиццу забрали за {} мин {} сек')
def pickup(pizza: Pizza) -> None:
    """
    Самовывоз пиццы
    """
    pass


if __name__ == '__main__':
    cli()
