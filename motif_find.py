import sys

def main(argv):
    motif = argv[1]
    filename = argv[2]

    dna_strand = ""
    with open(filename, 'r') as file:
        strand = file.read().replace('\n', '')

    motif_len = len(motif)
    dna_strand_length = len(dna_strand)

    
if __name__ == "__main__":
   main(sys.argv)
