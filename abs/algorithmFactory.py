from algorithms.nearestNeighbour.classes import NearestNeighbourTSP
from algorithms.bruteForce.classes import BruteForceTSP
from abs.genericAlgorithm import GenericAlgorithm
from abs.enumerator import EnumAlgorithms

class AlgorithmFactory:
    
    def getAlgorithm(self, name: EnumAlgorithms) -> GenericAlgorithm:

        if name == EnumAlgorithms.NEAREST_NEIGHBOUR:
            return NearestNeighbourTSP()
        elif name == EnumAlgorithms.BRUTE_FORCE:
            return BruteForceTSP()
        else:
            raise Exception('Algoritmo Inválido.')