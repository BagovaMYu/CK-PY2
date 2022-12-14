import doctest
from typing import Union


class Watch:
    def __init__(self, hours: int, minutes: int,
                 hours_alarm: Union[int, None] = None, minutes_alarm: Union[int, None] = None):
        """
        Создание и подготовка к работе объекта "Часы"

        :param hours: Отображаемое количество часов
        :param minutes: Отображаемое количество минут

        Примеры:
        >>> watch = Watch(0, 0)
        """
        if not isinstance(hours, int):
            raise TypeError("Отображаемое количество часов должно быть типа int")
        if not 0 <= hours <= 23:
            raise ValueError("Отображаемое количество часов должно находиться в интервале от 0 до 23")
        self.hours = hours

        if not isinstance(minutes, int):
            raise TypeError("Отображаемое количество минут должно быть типа int")
        if not 0 <= minutes <= 59:
            raise ValueError("Отображаемое количество минут должно находиться в интервале от 0 до 59")
        self.minutes = minutes
        self.hours_alarm = hours_alarm
        self.minutes_alarm = minutes_alarm

    def check_the_alarm(self) -> bool:
        """
        Проверка наличия установленного будильника

        :return: Установлен ли будильник

        Примеры:
        >>> watch = Watch(0, 0)
        >>> watch.check_the_alarm()
        """
        ...

    def set_alarm_time(self, hours_alarm: int, minutes_alarm: int) -> None:
        """
        Задание времени срабатывания будильника

        :param hours_alarm: час, в который должен сработать будильник
        :param minutes_alarm: минута, в которую должен сработать будильник

        Примеры:
        >>> watch = Watch(0, 0)
        >>> watch.set_alarm_time(7, 30)
        """
        if not isinstance(hours_alarm, int):
            raise TypeError("Отображаемое количество часов должно быть типа int")
        if not 0 <= hours_alarm <= 23:
            raise ValueError("Отображаемое количество часов должно находиться в интрвале от 0 до 23")

        if not isinstance(minutes_alarm, int):
            raise TypeError("Отображаемое количество минут должно быть типа int")
        if not 0 <= minutes_alarm <= 59:
            raise ValueError("Отображаемое количество минут должно находиться в интрвале от 0 до 59")
        ...

    def turn_off_the_alarm(self) -> None:
        """
        Отключение будильника

        Примеры:
        >>> watch = Watch(0, 0)
        >>> watch.turn_off_the_alarm()
        """
        ...


class ChristmasTree:
    def __init__(self, slots_for_decor: int, decor: dict):
        """
        Создание и подготовка к работе объекта "Новогодняя ёлка"

        :param slots_for_decor: Количество мест для размещения украшений
        :param decor: Украшения на ёлке

        Примеры:
        >>> сhristmas_tree = ChristmasTree(30, {'balloon': 10, 'star': 1})
        """
        if not isinstance(slots_for_decor, int):
            raise TypeError("Количество мест для размещения украшений должно быть типа int")
        self.slots_for_decor = slots_for_decor

        if not isinstance(decor, dict):
            raise TypeError("Украшения на ёлке должны быть типа dict")
        if sum(decor.values()) > slots_for_decor:
            raise ValueError("Недостаточно мест для размещения украшений")
        self.decor = decor

    def free_slots_check(self) -> int:
        """
        Проверка наличия свободных мест для украшений

        :return: Количество свободных мест

        Примеры:
        >>> сhristmas_tree = ChristmasTree(30, {'balloon': 10, 'star': 1})
        >>> сhristmas_tree.free_slots_check()
        """
        ...

    def add_decoration(self, new_decoration: dict, free_slots: int) -> None:
        """
        Добавление украшений на ёлку

        :param new_decoration: Словарь с типом и количеством добавляемых украшений
        :param free_slots: Количество свободных мест для украшений

        :raise ValueError: Если количество добавляемы украшений превышает количество свободных мест, то вызываем ошибку

        Примеры:
        >>> сhristmas_tree = ChristmasTree(30, {'balloon': 10, 'star': 1})
        >>> сhristmas_tree.add_decoration({'candle': 10}, 19)
        """
        if not isinstance(new_decoration, dict):
            raise TypeError("Украшения на ёлке должны быть типа dict")
        if sum(new_decoration.values()) > free_slots:
            raise ValueError("Недостаточно мест для размещения украшений")
        ...


class Bulb:
    def __init__(self, power: int, light_is_on: bool):
        """
        Создание и подготовка к работе объекта "Лампочка"

        :param power: Мощность лампочки
        :param light_is_on: Свет включен/выключен

        Примеры:
        >>> bulb = Bulb(60, True)
        """
        self.power_availability_check(power)

        if not isinstance(light_is_on, bool):
            raise TypeError("Параметр должн быть типа bool")
        self.light_is_on = light_is_on

    def power_availability_check(self, power: int) -> None:
        """
        Проверка возможноти использования лампочки указанной мощности

        :param power: Мощность лампочки

        :raise ValueError: Если указано нестандартное значение мощности, то вызываем ошибку
        """
        standart_power = [20, 40, 60, 75, 100]
        if not isinstance(power, int):
            raise TypeError("Мощность лампочки должна быть типа int")
        if power not in standart_power:
            raise ValueError(f"Допустимые значения мощности {', '.join(str(value) for value in standart_power)}")
        self.power = power

    def power_change(self, new_power: int) -> None:
        """
        Изменение мощности лампочки

        :param new_power: Мощность новой лампочки

        Примеры:
        >>> bulb = Bulb(60, True)
        >>> bulb.power_change(40)
        """
        self.power_availability_check(new_power)

    def switching_mode(self, new_mode: bool) -> None:
        """
        Включение/выключение света

        :param new_mode: Новое состояние

        :raise ValueError:

        Примеры:
        >>> bulb = Bulb(60, True)
        >>> bulb.switching_mode(False)
        """
        if not isinstance(new_mode, bool):
            raise TypeError("Новое состояние должно быть типа bool")
        if self.light_is_on == new_mode:
            if self.light_is_on is False:
                raise ValueError("Свет уже выключен")
            else:
                raise ValueError("Свет уже включен")
        self.light_is_on = new_mode


if __name__ == "__main__":
    doctest.testmod()

    bulb = Bulb(60, True)
    print(f"Лампочка, мощность {bulb.power} Вт, свет включен - {bulb.light_is_on}")
    bulb.power_change(20)
    print(f"Лампочка, мощность {bulb.power} Вт, свет включен - {bulb.light_is_on}")
    # bulb.power_change(30) # недопустимое значение мощности
    # bulb.switching_mode(True) # свет уже включен
    bulb.switching_mode(False)
    print(f"Лампочка, мощность {bulb.power} Вт, свет включен - {bulb.light_is_on}")
