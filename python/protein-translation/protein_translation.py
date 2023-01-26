def proteins(strand):
    ans = []
    while strand:
        codon = strand[:3]
        
        if codon == "AUG":
            ans.append("Methionine")

        elif codon == "UUU" or codon == "UUC":
            ans.append("Phenylalanine")

        elif codon == "UUA" or codon == "UUG":
            ans.append("Leucine")

        elif codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            ans.append("Serine")

        elif codon == "UAU" or codon == "UAC":
            ans.append("Tyrosine")

        elif codon == "UGU" or codon == "UGC":
            ans.append("Cysteine")

        elif codon == "UGG":
            ans.append("Tryptophan")

        elif codon == "UAA" or codon == "UAG" or codon == "UGA":
            break

        strand = strand[3:]

    return ans
