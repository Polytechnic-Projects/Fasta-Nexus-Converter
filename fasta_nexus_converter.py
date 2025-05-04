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

    ntax = len(seq_dict)
    nchar = max(len(seq) for seq in seq_dict.values())

    nl = '\n'

    header = f"#NEXUS {nl}BEGIN DATA; {nl}DIMENSIONS NTAX={ntax} NCHAR={nchar}; {nl}FORMAT DATATYPE=DNA MISSING=N GAP=-; {nl}"

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