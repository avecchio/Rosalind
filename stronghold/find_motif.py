import sys
import re

def main(argv):
    filename = argv[1]

    dna_strand = ""
    motif = ""
    with open(filename, 'r') as file:
        strand = file.read()
        dna_strand = strand.split('\n')[0]
        motif = strand.split('\n')[1]

    indicies = []
    for match in re.finditer('(?=' + motif + ')', dna_strand, flags=re.VERBOSE):
        indicies.append(str(match.start() + 1))
    print(' '.join(indicies))

if __name__ == "__main__":
    main(sys.argv)
