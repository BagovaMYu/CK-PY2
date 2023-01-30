from typing import Union


class Wall:
    """Класс Стена"""
    def __init__(self, length: float, height: float, main_material: dict[str, Union[float, str]]):
        """
        :param length: длина стены в метрах
        :param height: высота стены в метрах
        :param main_material: словарь с описанием основного материала стены
        """
        self._length = length
        self._height = height
        self.main_material = main_material

    @property
    def length(self) -> float:
        """
        Возвращает длину стены.
        Причина инкапсуляции: ограничение возможности изменения длинны стены
        """
        return self._length

    @property
    def height(self) -> float:
        """
        Возвращает высоту стены.
        Причина инкапсуляции: ограничение возможности изменения высоты стены
        """
        return self._height

    @property
    def main_material(self) -> dict[str, Union[float, str]]:
        """
        Возвращает словарь с описанием основного материала стены.
        Причина инкапсуляции: дополнительные проверки для вводимых данных
        """
        return self._main_material

    @main_material.setter
    def main_material(self, main_material: dict[str, Union[float, str]]) -> None:
        """
        Устанавливает основной материал стены

        :param main_material: словарь с описанием основного материала стены
        """
        parameters_desc = {
            "название материала": str,
            "толщина": float,
            "коэф. теплопроводности": float
        }
        if self.material_checking(parameters_desc, main_material):
            self._main_material = main_material

    def __str__(self):
        return f'Стена, материал {self.main_material["название материала"]},'\
               f' толщина {self.main_material["толщина"]} м. '\
               f'Размеры: длина {self.length} м., высота {self.height} м.'

    def __repr__(self):
        return f"{self.__class__.__name__}(length={self.length!r}, "\
               f"height={self.height!r}, main_material={self.main_material!r})"

    @staticmethod
    def material_checking(parameters_desc: dict[str, type], material: dict[str, Union[float, str]]) -> bool:
        """
        Проверка данных в словаре с описанием основного материала стены

        :param parameters_desc: словарь с требуемыми парметрами и их типами данных для проверки
        :param material: словарь с описанием проверяемого материала

        :raise ValueError: Вызов ошибки при отсутствии параметра или если введены отрицательные числовые значения
        :raise TypeError: Вызов ошибки если введены неверного типа
        """
        for parameter, data_type in parameters_desc.items():
            if parameter not in material:
                raise ValueError(f'Требуется параметр "{parameter}"')
            if not isinstance(material[parameter], data_type):
                raise TypeError(f'Параметр "{parameter}" должен быть {data_type}')
            if data_type is float:
                if material[parameter] <= 0:
                    raise ValueError(f'Параметр "{parameter}" должен быть положительным числом')
        return True

    def area_of_wall_calculation(self) -> float:
        """Вычисление площади стены"""
        return round(self.length * self.height, 2)

    @staticmethod
    def volume_of_material_calculation(material: dict[str, Union[float, str]],
                                       area: float, thickness: float) -> dict[str, float]:
        """
        Вычисление объема материала.
        Причина инкапсуляции: дополнительные проверки для вводимых данных

        :param material: словарь с описанием материала стены
        :param area: площадь стены в м2
        :param thickness: толщина материала в м
        :return: словарь с названием материала и его объемом в м3
        """
        volume_of_material = round(area * thickness, 2)
        return {material["название материала"]: volume_of_material}

    def total_volume_of_materials_calculation(self) -> dict[str, float]:
        """
        Вычисление объема используемого материла

        :return: словарь с названием материала и его объемом в м3
        """
        return self.volume_of_material_calculation(self._main_material,
                                                   self.area_of_wall_calculation(),
                                                   self._main_material["толщина"])


class InsulatedWall(Wall):
    """
    Класс Утепленная стена
    """
    R_REQ = 2.99  # требуемое сопротивление теплопередаче конструкции стены для Санкт-Петербурга

    def __init__(self, length: float, height: float, main_material: dict, insulator: dict[str, Union[float, str]]):
        """
        :param length: длина стены в метрах
        :param height: высота стены в метрах
        :param main_material: словарь с описанием основного материала стены
        :param insulator: словарь с описанием утеплителя
        """
        super().__init__(length, height, main_material)
        self.insulator = insulator

    @property
    def insulator(self) -> dict[str, Union[float, str]]:
        """Возвращает словарь с описанием утеплителя"""
        return self._insulator

    @insulator.setter
    def insulator(self, insulator: dict[str, Union[float, str]]) -> None:
        """
        Устанавливает основной материал утеплителя

        :param insulator: словарь с описанием утеплителя
        """
        parameters_desc = {
            "название материала": str,
            "коэф. теплопроводности": float
        }
        if self.material_checking(parameters_desc, insulator):
            self._insulator = insulator

    def __str__(self):
        return f'{super().__str__()} Утеплитель: {self.insulator["название материала"]}.'

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

        heat_resistance_main_material = self.main_material["толщина"] / self.main_material["коэф. теплопроводности"]
        insulation_thickness = ((self.R_REQ - A_INT - heat_resistance_main_material - A_EXT)
                                * self.insulator["коэф. теплопроводности"])
        return round(insulation_thickness, 2)

    def volume_of_insulator_calculation(self) -> dict[str, float]:
        """
        Вычисление объема утеплителя

        :return: словарь с названием материала утеплителя и его объемом в м3
        """
        return self.volume_of_material_calculation(self.insulator,
                                                   self.area_of_wall_calculation(),
                                                   self.insulation_thickness_calculation())

    def total_volume_of_materials_calculation(self) -> list[dict[str, Union[float, str]]]:
        """
        Вычисление объемов используемых материлов.
        Перегрузка метода базового класса для включения утеплителя в возвращаемый результат

        :return: список словарей с названиями материалов и их объемами в м3
        """
        return [super().total_volume_of_materials_calculation(), self.volume_of_insulator_calculation()]


if __name__ == "__main__":
    main_material = {
        "название материала": "кирпич",
        "толщина": 0.51,
        "коэф. теплопроводности": 0.6
    }

    insulator = {
        "название материала": "минеральная вата",
        "коэф. теплопроводности": 0.04
    }

    wall = Wall(5, 3.1, main_material)
    insulated_wall = InsulatedWall(6, 3, main_material, insulator)

    print(wall,
          "Объем материала: ", wall.total_volume_of_materials_calculation(),
          repr(wall), sep='\n')
    print()
    print(insulated_wall,
          "Объем материала: ", insulated_wall.total_volume_of_materials_calculation(),
          repr(insulated_wall), sep='\n')
