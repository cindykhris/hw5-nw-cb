# Importing Dependencies
import pytest
from align import NeedlemanWunsch, read_fasta
import numpy as np

def test_nw_alignment():
    """
    TODO: Write your unit test for NW alignment
    using test_seq1.fa and test_seq2.fa by
    asserting that you have correctly filled out
    the your 3 alignment matrices.
    Use the BLOSUM62 matrix and a gap open penalty
    of -10 and a gap extension penalty of -1.
    """
    seq1, _ = read_fasta("./data/test_seq1.fa")
    seq2, _ = read_fasta("./data/test_seq2.fa")
    
    nw = NeedlemanWunsch(seq1, seq2, blosum62, -8)
    nw.align()
    assert nw._matrix[0][0] == 0
    assert nw._matrix[0][1] == -8
    assert nw._matrix[1][0] == -8
    assert nw._matrix[1][1] == 4
    

def test_nw_backtrace():
    """
    TODO: Write your unit test for NW backtracing
    using test_seq3.fa and test_seq4.fa by
    asserting that the backtrace is correct.
    Use the BLOSUM62 matrix. Use a gap open
    penalty of -10 and a gap extension penalty of -1.
    """
    seq3, _ = read_fasta("./data/test_seq3.fa")
    seq4, _ = read_fasta("./data/test_seq4.fa")
    
    nw = NeedlemanWunsch(seq1, seq2, blosum62, -8)
    nw.align()
    nw._backtrace()
    assert nw.seqA_align == "MAVHQLIRRP"
    assert nw.seqB_align == "M---QLIRHP"
    assert nw.alignment_score == 17



