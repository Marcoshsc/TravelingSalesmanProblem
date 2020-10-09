from run.runner import compare
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--predef', action='store_true', help='Utilizar dados definidos no arquivo resources/dataToCompare.json')

    args = parser.parse_args()

    compare(args.predef)
