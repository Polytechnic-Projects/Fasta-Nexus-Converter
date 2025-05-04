import pytest
from fasta_nexus_converter import fasta_dict
from fasta_nexus_converter import nexus_data_header
from fasta_nexus_converter import nexus_matrix_block

def test_fasta_dict(tmp_path): #tmp_path creates a temporary file for the function to be able to run
    nl = '\n'
    tmp_file_data = f">Aurelia1{nl}atgcgnatg{nl}>Aurelia2{nl}tca--gccg"

    tmp_file = tmp_path / "test_file.fasta"
    tmp_file.write_text(tmp_file_data)

    expected_result = {
        "Aurelia1": "atgcgnatg".replace("n", "N"),
        "Aurelia2": "tca--gccg".replace("n", "N")
    }

    result = fasta_dict(tmp_file)

    assert result == expected_result


def test_nexus_data_header(tmp_path):
    seqs = {
        "Aurelia1": "atgcgnatg",
        "Aurelia2": "tca--gccg"
    }

    header = nexus_data_header(seqs)
    
    assert header.startswith("#NEXUS")
    assert "BEGIN DATA;" in header.upper()

    assert "NTAX=2" in header
    assert "NCHAR=9" in header

    assert "FORMAT DATATYPE=DNA MISSING=N GAP-;" in header in header or "BEGIN DATA;" in header


def test_nexus_matrix_block(tmp_path):
    seqs = {
        "Aurelia1": "atgcgnatg",
        "Aurelia2": "tca--gccg"
    }

    matrix_block = nexus_matrix_block(seqs)

    assert matrix_block.upper().startswith("MATRIX")
    assert matrix_block.strip().endswith("END;")

    for taxon, seq in seqs.items():
        expected_line = f"{taxon}    {seq}"
        assert expected_line in matrix_block, f"Missing or incorrect line for {taxon}"