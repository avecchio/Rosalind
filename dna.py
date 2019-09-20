import sys

def main(argv):
    filename = argv[1]

    dna_strand = ''
    with open(filename, 'r') as file:
        dna_strand = file.read().replace('\n', '')

    adenine = 0
    thymine = 0
    cytosine = 0
    guanine = 0

    for raw_amino_acid in dna_strand:
        amino_acid = raw_amino_acid.upper()

        print(amino_acid)
        if amino_acid == "A":
            adenine += 1
        elif amino_acid == "T":
            thymine += 1
        elif amino_acid == "C":
            cytosine += 1
        else:
            guanine += 1

    print("{0} {1} {2} {3}".format(adenine, cytosine, guanine, thymine))

if __name__ == "__main__":
   main(sys.argv)
