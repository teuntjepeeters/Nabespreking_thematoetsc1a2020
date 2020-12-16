
def read_csv(naam_csv):
    """Inlezen van de csv

    :param naam_csv: - str - naam csv bestand
    :return: chromosomen - lijst - bevat alle chromosomen
    """
    chromosomen = []
    with open(naam_csv, encoding="utf8") as inFile:
        next(inFile)
        for line in inFile:
            chromosoom_loc = line.split("\t")[7]
            if "p" in chromosoom_loc:
                chr = chromosoom_loc.split("p")[0]
                if chr != "X" and chr != "Y":
                    chromosomen.append(int(chr))
                else:
                    chromosomen.append(chr)
            elif "q" in chromosoom_loc:
                chr = chromosoom_loc.split("q")[0]
                if chr != "X" and chr != "Y":
                    chromosomen.append(int(chr))
                else:
                    chromosomen.append(chr)
            elif chromosoom_loc.isdigit():
                chromosomen.append(int(chr))
    return chromosomen



def aantal_chromosomen(chr_nr, chromosomen):
    """Tellen hoe vaak een chromosoom voorkomt

    :return: - int - aantal keren voorkomen van dit chromosoom
    """
    counter = 0
    for c in chromosomen:
        if chr_nr != "X" and chr_nr != "Y":
            if int(chr_nr) == c:
                counter += 1
        else:
            if chr_nr == c:
                counter += 1
    return counter


def unieke_chr(chromosomen):
    """Maak unieke lijst van alle chromosomen

    :param chromosomen:
    :return:
    """
    uniek = []
    for c in chromosomen:
        if c not in uniek:
            uniek.append(c)
    return uniek


def vaakst_minst_vaak(chromosomen, unieke_chromosomen):
    """Check welke het vaakst en minst vaak voorkomt

    :param chromosomen:
    :param unieke_chromosomen:
    :return:
    """
    minst_vaak = 1000000
    chr_minst_vaak = ""
    vaakst = 0
    chr_vaakst = ""

    for uc in unieke_chromosomen:
        counter_chr = aantal_chromosomen(uc, chromosomen)
        if counter_chr < minst_vaak:
            minst_vaak = counter_chr
            chr_minst_vaak = uc
        elif counter_chr > vaakst:
            vaakst = counter_chr
            chr_vaakst = uc

    print("Het chromosoom {} komt het minst vaak voor".format(chr_minst_vaak))
    print("Het chromosoom {} komt het vaakst voor".format(chr_vaakst))


if __name__ == '__main__':
    naam_csv = "gene_with_protein_product.txt"
    chromosomen = read_csv(naam_csv)
    # chr_nr = input("Geef een chr nummer: ")
    chr_nr = "X"
    aantal_chr = aantal_chromosomen(chr_nr, chromosomen)
    print("Het chromosoom {} komt {} keer voor".format(chr_nr, aantal_chr))
    # print(chromosomen)
    # Welke unieke chromosomen zijn er?
    unieke_chromosomen = unieke_chr(chromosomen)
    vaakst_minst_vaak(chromosomen, unieke_chromosomen)