library( hash )

args <- commandArgs(trailingOnly = TRUE)

mass_table <- hash( A=71.03711, C=103.00919, D=115.02694, E=129.04259, F=147.06841, G=57.02146, H=137.05891, I=113.08406, K=128.09496, L=113.08406, M=131.04049, N=114.04293, P=97.05276, Q=128.05858, R=156.10111, S=87.03203, T=101.04768, V=99.06841, W=186.07931, Y=163.06333)

protein <- args[1]
amino_acids <- strsplit(protein, "")[[1]]

total <- double(length = 10)
for (amino_acid in amino_acids) {
  total <- sum(total, mass_table[[amino_acid]])
}

sprintf("%.3f", total)
