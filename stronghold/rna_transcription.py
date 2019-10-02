import sys

def main(argv):
    filename = argv[1]

    dna_strand = ""
    with open(filename, 'r') as file:
        strand = file.read().replace('\n', '')

    rna_strand = ""
    for raw_amino_acid in strand:
        amino_acid = raw_amino_acid.upper()

        if amino_acid == "T":
            rna_strand += "U"
        else:
            rna_strand += amino_acid

    print(rna_strand)

if __name__ == "__main__":
   main(sys.argv)
