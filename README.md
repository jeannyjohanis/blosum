# blosum

How to run the program:
User clicks “START” button in the GUI. User will then need to type in the name of the file containing sequences. The program will give outputs of 2D matrix of the sequences, frequency of amino acid substitutions, probabilities of amino acid substitutions, expected substitution rates, odds ratio and log of odds ratios with 20 rows and 9 columns and output of 1D matrix of marginal probabilities of each amino acid with 20 rows and 1 columns.

What the program does:
1. Prompt user for input filename consisting the sequences.
2. Read input file.
3. Store the sequences in a 2D matrix. 1 sequence is stored in 1 row.

All the outputs from method in class MakeBLOSUM will be labelled and will be
displayed sequentially, including the sequences.

What the program can be used for:
Compare protein sequences to judge the quality of the alignment.
Detect local alignments
Research (e.g.: Surface gene variants among hepatitis B virus carriers and reliable prediction of T-cell epitopes.)

Does it show any differences between amino acid (Refer to final matrix)?
Log odd-ratio is the likelihood of an amino acid to be substituted by other amino acids. Scores within a BLOSUM are log-odds scores that measure the logarithm for the ratio of probabilities of amino acid substitutions and the expected substitution rates. A positive score is given to a more likely substitution while a negative score is given to a less likely substitution.
   
