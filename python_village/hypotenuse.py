import sys
import math
def main(argv):
    a = int(argv[1])
    b = int(argv[2])
    c = math.pow(a, 2) + math.pow(b, 2)
    print(str(int(c)))

if __name__ == "__main__":
   main(sys.argv)
