'''from collections import Counter
def count_words(text):
    text=text.lower()
    skips = ['.', ',', ';', ':', '"', "'"]
    for ch in skips:
        text = text.replace(ch, '')

    word_counts = Counter(text.split(" "))
    return word_counts

print(len(count_words("This comprehension check is to check for comprehension.")))


'''
"""
def read_seq(inputfile):
   # '''
    Reads and returns the input sequence with special char
    removed
    :param inputfile: string, the path of file and file itself.
    :return: spec. chars removed file
   # '''
    with open(inputfile, 'r') as f:
        seq = f.read()
    seq = seq.replace('\n', '')
    seq = seq.replace('\r', '')
    return seq



def translate(seq):
    #'''
    Trasnlate a string containing a nucleotide sequence into a string containing the
    corresponding sequence of amino acids. nucleotides are translated in triplets
    using the table dictionary: each amino acid
    is encoded with a string of length 1.

    :param seq: Takes the 3 letters amonoacid letter
    :return: decoded aminoacid PROTEIN
   # '''
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }

    protein = ""

    # check that the sequnce lenght is diisible by 3
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i: i + 3]
            protein += table[codon]

    return protein

prt = read_seq('proteinSeq.txt')
dna = read_seq('dnaseq.txt')
print(translate(dna[20:938]))
"""




text =" This i s my test text wer are keeping this text short to keep thigs" \
      "managable"
def count_words(text):
    '''
    :param text: COunt the number of
    times each word occur sin text, and skips punctuation
    :return: dictionary word counts
    '''
    text = text.lower()
    skips = [".", ",", ";", ":" ,"'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        # known word
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


        #unknown word

from collections import Counter

def count_words_fast(text):
    '''
    :param text: COunt the number of
    times each word occur sin text, and skips punctuation
    :return: dictionary word counts
    '''
    text = text.lower()
    skips = [".", ",", ";", ":" ,"'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

print(count_words_fast(text)==count_words(text))



def read_book(title_path):
    '''
    Read a book and return it as a string.
    :param title_path:
    :return: returns string
    '''
    with open(title_path, 'r', encoding='utf8') as currentfile:
        text = currentfile.read()
        text = text.replace('\n', '').replace("\r", "")
    return text


def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
text = read_book("./Books/English/shakespeare/Romeo and Juliette.")


# next course
import os
import pandas as pd
stats = pd.DataFrame(columns=('language', 'author', 'title', 'lenght', 'unique'))
title_num = 1
book_dir = "./Books"

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir +"/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            input_file = book_dir + "/" + language + "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))


