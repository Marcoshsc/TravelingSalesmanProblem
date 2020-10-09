from enum import Enum


class EnumAlgorithms(Enum):

    NEAREST_NEIGHBOUR = 0,
    BRUTE_FORCE = 1

    @staticmethod
    def FromString(value: str) -> 'EnumAlgorithms':
        upperValue = value.upper()
        if upperValue == 'NEARESTNEIGHBOUR':
            return EnumAlgorithms.NEAREST_NEIGHBOUR
        elif upperValue == 'BRUTEFORCE':
            return EnumAlgorithms.BRUTE_FORCE
        else:
            raise Exception('Algoritmo Inválido.')