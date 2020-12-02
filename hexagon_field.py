# TODO: Документация :)
"""
Модуль, отвечающий за реализацию полей гексов.
"""

from functools import wraps
from typing import Callable, Any, Dict, List
from dataclasses import dataclass, field


@dataclass(unsafe_hash=False)
class HexagonPosition:
    """
    Класс-контейнер для координат клеток.
    """

    column: int = field(default_factory=int)
    row: int = field(default_factory=int)

    def __hash__(self):
        return hash((self.column, self.row))


def parity_tester(hexagon_pos: HexagonPosition, is_same_parity: bool = False) -> bool:
    """

    :param hexagon_pos:
    :param is_same_parity:
    :return:
    """
    return (hexagon_pos.row % 2 == hexagon_pos.column % 2) ^ is_same_parity


class HexagonField:
    """
    Класс, отвечающий за хранение данных, связанных с гексами, и валидацию координат.
    """

    def __init__(self) -> None:
        """

        """
        self._data: Dict[HexagonPosition, Any] = dict()

    def __getitem__(self, hexagon_pos: HexagonPosition) -> Any:
        """

        :param hexagon_pos:
        :return:
        """
        return self._data[hexagon_pos]

    def __setitem__(self, hexagon_pos: HexagonPosition, value: Any) -> None:
        """

        :param hexagon_pos:
        :param value:
        :return:
        """
        if not self.validate(hexagon_pos):
            raise ValueError('Incorrect position.')
        self._data.update({hexagon_pos: value})

    def __delitem__(self, hexagon_pos: HexagonPosition) -> None:
        """

        :param hexagon_pos:
        :return:
        """
        self._data.pop(hexagon_pos)

    def get_neighbors(self, hexagon_pos: HexagonPosition) -> List[HexagonPosition]:
        """
        Возвращает список существующих клеток, смежных по стороне с переданной в аргументе.
        Существование клетки определяется функцией-валидатором поля.
        :param hexagon_pos: Клетка, соседей которой нужно вернуть.
        """
        return [HexagonPosition(hexagon_pos.row + delta_row, hexagon_pos.column + delta_column)
                for delta_row in [-1, 0, 1]
                for delta_column in [1, -1]
                if self.validate(HexagonPosition(hexagon_pos.row + delta_row, hexagon_pos.column + delta_column))]

    def set_validator(self, validator: Callable[[HexagonPosition], bool]):
        """

        :param validator:
        :return:
        """
        self.validate = validator

    @staticmethod
    def validate(hexagon_pos: HexagonPosition) -> bool:
        """

        :param hexagon_pos:
        :return:
        """
        return parity_tester(hexagon_pos, False)

