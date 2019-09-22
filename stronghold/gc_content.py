import sys
from Bio import SeqIO

def main(argv):
    fasta_sequences = SeqIO.parse(open(argv[1]),'fasta')
    results = {}
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        results[name] = compute_gc_content(sequence)

    max_name = None
    max_value = 0
    for name in results:
        if max_name is None or results[name] > max_value:
            max_name = name;
            max_value = results[name]
    print(max_name)
    print(max_value)

def compute_gc_content(sequence):
    normalized_sequence = sequence.upper()
    g_count = normalized_sequence.count("G")
    c_count = normalized_sequence.count("C")
    return ((g_count + c_count) / len(sequence)) * 100

if __name__ == "__main__":
   main(sys.argv)
