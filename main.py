from typing import Union


class Material:
    """класс Материал"""
    def __init__(self, name: str, therm_conduct_coef: Union[int, float]):
        """
        :param name: название материала
        :param therm_conduct_coef: коэффициент теплопроводности в Вт/(м·K).
        """
        self.name = name
        self.therm_conduct_coef = therm_conduct_coef

    @property
    def name(self) -> str:
        """
        Возвращает название материала.
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает название материала.

        :param name: название материала

        :raise TypeError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(name, str):
            raise TypeError(f'Параметр "name" должен быть типа str')
        self._name = name

    @property
    def therm_conduct_coef(self) -> Union[int, float]:
        """
        Возвращает коэффициент теплопроводности материала.
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._therm_conduct_coef

    @therm_conduct_coef.setter
    def therm_conduct_coef(self, therm_conduct_coef: Union[int, float]) -> None:
        """
        Устанавливает коэффициент теплопроводности материала.

        :param therm_conduct_coef: коэффициент теплопроводности материала

        :raise TypeError: вызов ошибки если введены данные неверного типа
        :raise ValueError: вызов ошибки если введено равное нулю или отрицательное значение
        """
        if not isinstance(therm_conduct_coef, Union[int, float]):
            raise TypeError(f'Параметр "therm_conduct_coef" должен быть типа int или float')
        if therm_conduct_coef <= 0:
            raise ValueError(f'Коэффициент теплопроводности должен быть положительным числом')
        self._therm_conduct_coef = therm_conduct_coef

    def volume_of_material_calculation(self, area: float, thickness: Union[int, float]) -> dict[str, float]:
        """
        Вычисление объема материала.

        :param area: площадь стены в м2
        :param thickness: толщина материала в м
        :return: словарь с названием материала и его объемом в м3
        """
        volume_of_material = round(area * thickness, 2)
        return {self.name: volume_of_material}

    def __str__(self):
        return f'Материал {self.name}, коэффициент теплопроводности {self.therm_conduct_coef}'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, therm_conduct_coef={self.therm_conduct_coef!r})"


class MainMaterial(Material):
    """
    Класс Основной материал.
    Описывает материал основной несущей конструкции стены
    """

    def __init__(self, name: str, therm_conduct_coef: Union[int, float], thickness: Union[int, float]):
        """
        :param name: название материала
        :param therm_conduct_coef: коэффициент теплопроводности в Вт/(м·K).
        :param thickness: толщина в метрах.
        """
        super().__init__(name, therm_conduct_coef)
        self.thickness = thickness

    @property
    def thickness(self) -> Union[int, float]:
        """
        Возвращает толщину материала.
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._thickness

    @thickness.setter
    def thickness(self, thickness: Union[int, float]) -> None:
        """
        Устанавливает толщину материала.

        :param thickness: толщина материала

        :raise TypeError: вызов ошибки если введены данные неверного типа
        :raise ValueError: вызов ошибки если введено равное нулю или отрицательное значение
        """
        if not isinstance(thickness, Union[int, float]):
            raise TypeError(f'Параметр "thickness" должен быть типа int или float')
        if thickness <= 0:
            raise ValueError(f'Толщина должна быть положительным числом')
        self._thickness = thickness

    def __str__(self):
        return f'{super().__str__()}, толшина: {self.thickness}.'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, " \
               f"therm_conduct_coef={self.therm_conduct_coef!r}, thickness={self.thickness!r})"


class Wall:
    """Класс Стена"""
    def __init__(self, length: Union[int, float], height: Union[int, float], main_material: MainMaterial):
        """
        :param length: длина стены в метрах
        :param height: высота стены в метрах
        :param main_material: основной материал стены
        """
        self._length = length
        self._height = height
        self.main_material = main_material

    @property
    def length(self) -> Union[int, float]:
        """
        Возвращает длину стены.
        Причина инкапсуляции: ограничение возможности изменения длинны стены
        """
        return self._length

    @property
    def height(self) -> Union[int, float]:
        """
        Возвращает высоту стены.
        Причина инкапсуляции: ограничение возможности изменения высоты стены
        """
        return self._height

    @property
    def main_material(self) -> MainMaterial:
        """
        Возвращает основной материал стены.
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._main_material

    @main_material.setter
    def main_material(self, main_material: MainMaterial) -> None:
        """
        Устанавливает основной материал стены.

        :param main_material: основной материал стены

        :raise TypeError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(main_material, MainMaterial):
            raise TypeError(f'Параметр "main_material" должен быть класса MainMaterial')
        self._main_material = main_material

    def __str__(self):
        return f'Стена, материал {self.main_material.name}, '\
               f'толщина основной конструкции {self.main_material.thickness}. '\
               f'Размеры: длина {self.length} м., высота {self.height} м.'

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r}, "\
               f"height={self.height!r}, main_material={self.main_material!r})"

    def area_of_wall_calculation(self) -> float:
        """Вычисление площади стены"""
        return round(self.length * self.height, 2)

    def total_volume_of_materials_calculation(self) -> dict[str, float]:
        """
        Вычисление объема используемого материла

        :return: словарь с названием материала и его объемом в м3
        """
        return self.main_material.volume_of_material_calculation(self.area_of_wall_calculation(),
                                                                 self._main_material.thickness)


class InsulatedWall(Wall):
    """
    Класс Утепленная стена
    """
    R_REQ = 2.99  # требуемое сопротивление теплопередаче конструкции стены для Санкт-Петербурга

    def __init__(self, length: Union[int, float],
                 height: Union[int, float],
                 main_material: MainMaterial,
                 insulator: Material):
        """
        :param length: длина стены в метрах
        :param height: высота стены в метрах
        :param main_material: основной материал стены
        :param insulator: материал утеплителя
        """
        super().__init__(length, height, main_material)
        self.insulator = insulator

    @property
    def insulator(self) -> Material:
        """
        Возвращает материал утеплителя
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._insulator

    @insulator.setter
    def insulator(self, insulator: Material) -> None:
        """
        Устанавливает материал утеплителя

        :param insulator: материал утеплителя
        :raise TypeError: вызов ошибки если введены данные неверного типа
        """
        if not isinstance(insulator, Material):
            raise TypeError(f'Параметр "insulator" должен быть класса Material')
        self._insulator = insulator

    def __str__(self):
        return f'{super().__str__()} Утеплитель: {self.insulator.name}.'

    def __repr__(self):
        return (f"{self.__class__.__name__}(length={self.length!r}, height={self.height!r}, "
                f"main_material={self.main_material!r}, insulator={self.insulator!r})")

    def insulation_thickness_calculation(self) -> float:
        """
        Расчет требуемой толщины утеплителя

        :return: толщина утеплителя в м
        """
        A_INT = 1 / 8.7  # сопротивление теплоотдаче внутренней поверхности стены
        A_EXT = 1 / 23  # сопротивление теплоотдаче наружной поверхности стены

        heat_resistance_main_material = self.main_material.thickness / self.main_material.therm_conduct_coef
        insulation_thickness = ((self.R_REQ - A_INT - heat_resistance_main_material - A_EXT)
                                * self.insulator.therm_conduct_coef)
        return round(insulation_thickness, 2)

    def volume_of_insulator_calculation(self) -> dict[str, float]:
        """
        Вычисление объема утеплителя

        :return: словарь с названием материала утеплителя и его объемом в м3
        """
        return self.insulator.volume_of_material_calculation(self.area_of_wall_calculation(),
                                                             self.insulation_thickness_calculation())

    def total_volume_of_materials_calculation(self) -> list[dict[str, Union[float, str]]]:
        """
        Вычисление объемов используемых материлов.
        Перегрузка метода базового класса для включения утеплителя в возвращаемый результат

        :return: список словарей с названиями материалов и их объемами в м3
        """
        return [super().total_volume_of_materials_calculation(), self.volume_of_insulator_calculation()]


if __name__ == "__main__":
    main_material = MainMaterial("кирпич", 0.51, 0.6)

    insulator = Material("минеральная вата", 0.04)

    wall = Wall(5, 3.1, main_material)
    insulated_wall = InsulatedWall(6, 3, main_material, insulator)

    print(wall,
          "Объем материала: ", wall.total_volume_of_materials_calculation(),
          repr(wall), sep='\n')
    print()
    print(insulated_wall,
          "Объем материала: ", insulated_wall.total_volume_of_materials_calculation(),
          repr(insulated_wall), sep='\n')
