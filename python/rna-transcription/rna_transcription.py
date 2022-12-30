def to_rna(dna_strand):
    dna = "GCTA"
    rna = "CGAU"

    out = ""

    for char in dna_strand:
        if char in dna:
            out += rna[dna.index(char)]

    return out
