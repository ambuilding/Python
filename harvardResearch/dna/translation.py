def read_seq(inputfile):
    """Reads and returens the input sequence with special characters removed."""
    with open(inputfile, "r") as f:
        seq = f.read()
        
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq

# NM_207618.2
#inputfile = "dna.txt"
#f = open(inputfile, "r")
#seq = f.read()
#
#seq = seq.replace("\n", "")
#seq = seq.replace("\r", "")

def translate(seq):
    """Translate a stirng containing a nucleotide sequence into a string
    containing the corresponding sequence of amino adids.
    Nucleotids are translated in triplets using the table dictionary;
        each amino acid is encoded with a stirng of length 1."""
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    # check that  the sequence length is divisible by 3
        # loop over the sequence 
            # extract a single codon 
            # lookup the codon and store the result
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i : i+3]
            protein += table[codon]
    
    return protein

dna = read_seq("dna.txt")
prt = read_seq("protein.txt")

translate(dna[20:938]) == prt
translate(dna[20:935]) == prt
print(translate(dna[20:938])[:-1] == prt)