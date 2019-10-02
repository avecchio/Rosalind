import sys

def main(argv):
    filename = argv[1]

    dna_strand = ""
    with open(filename, 'r') as file:
        strand = file.read().replace('\n', '')

    complete_strand = ""
    for raw_amino_acid in strand:
        amino_acid = raw_amino_acid.upper()

        if amino_acid == "A":
            complete_strand = "T" + complete_strand
        elif amino_acid == "T":
            complete_strand = "A" + complete_strand
        elif amino_acid == "C":
            complete_strand = "G" + complete_strand
        else:
            complete_strand = "C" + complete_strand

    print(complete_strand)

if __name__ == "__main__":
   main(sys.argv)
