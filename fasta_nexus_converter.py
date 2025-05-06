import sys

if len(sys.argv) < 2:
    sys.exit("Something went wrong. Please try again.")

fasta_file = sys.argv[1]

def fasta_dict(file_path):
    """
    Takes a FASTA file as input and returns a dictionary of < name: sequence >.
    """

    seq_dict = {}
    with open(file_path, 'r') as file:
        for lines in file:
            seqs = lines.rstrip("\n")
            if seqs.startswith(">"):
                seq_ident = seqs.lstrip('>').strip()
                seq_dict[seq_ident] = str()
            else:
                seq_dict[seq_ident] += seqs.replace("n", "N")
    
    return seq_dict

def nexus_data_header(seq_dict):
    """
    Takes the FASTA dictionary and returns the NEXUS DATA header.
    """

    def _detect_type(seq):
        """
        Infers the type of data used - DNA, RNA, or protein.
        """
        dna_bases = {"A", "T", "C", "G", "N"}
        rna_bases = {"A", "U", "C", "G", "N"}
        protein_bases = {"A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"}

        seq_set = set("".join(seq).upper())

        for base in seq:
            seq_set.update(set(base.upper()))

        if seq_set.issubset(dna_bases):
            return "DNA"
        elif seq_set.issubset(rna_bases):
            return "RNA"
        elif seq_set.issubset(protein_bases):
            return "PROTEIN"
        else:
            return "UNKNOWN"
    
    datatype = _detect_type(seq_dict.values())

    ntax = len(seq_dict)
    nchar = max(len(seq) for seq in seq_dict.values())

    nl = '\n'

    header = f"#NEXUS {nl}BEGIN DATA; {nl}DIMENSIONS NTAX={ntax} NCHAR={nchar}; {nl}FORMAT DATATYPE={datatype} MISSING=N GAP=-; {nl}"

    return header

def nexus_matrix_block(seq_dict):
    """
    Takes the FASTA dictionary and returns the NEXUS MATRIX block.
    """

    nl = '\n'
    matrix = "MATRIX" + nl

    for name, seq in seq_dict.items():
        matrix += f"{name}    {seq} {nl}"
    
    matrix += ";" + nl + "END;"
    return matrix


if __name__ == "__main__":
    seqs = fasta_dict(fasta_file)
    nexus_header = nexus_data_header(seqs)
    nexus_matrix = nexus_matrix_block(seqs)

    print(nexus_header)
    print(nexus_matrix)