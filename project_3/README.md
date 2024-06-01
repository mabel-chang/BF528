##RNAseq##

#Methods section#
The analysis will be conducted in high-performance computing environments. Specifically utilizing Miniconda, Github, and the Boston University Shared Computing Cluster (SCC), which will provide the necessary computational resources. The dataset involves 8 samples from a human source, 4WT and 4KO.
The pipeline will use FastQC(v0.12.1) for quality control on the FastQ files. FastQC performs quality control assessments on sequence data. MultiQC(v1.17) will be utilized to compile the separate FastQC outputs into a unified report.
The pipeline will incorporate STAR(v2.7.10b) for aligning the paired-end RNAseq reads to the genome. Samtools Flagstats(v1.6) will be used to assess the qulity of the resulting alignment. Verse(v0.1.5) will be used to perform gene set enrichment analysis (GSEA) on the RNAseq data. Using R(v4.3.1), the following packages will be used for the differential expression analysis: DESeq2(v1.36.0), tidyverse(v2.0.0), and data.table(v1.14.2). DESeq2 (v1.32.0) will be used for differential expression analysis between WT and KO samples.

#Questions#
-See answers in summary.Rmd-

#Deliverables#
Sample-to-sample distance plot:
  -"images/distance_plot.png"

A CSV containing all of the results from your DE analysis:
  -"DE_result.csv"

A histogram showing the distribution of log2FoldChanges of your DE genes:
  -"images/histogram.png"

A volcano plot:
  -"images/volcano_plot.png"
  
Perform a GSEA (FGSEA) analysis on all the genes discovered in the experiment:
  -FGSEA all: "fgsea_table_all.xlsx"
  -FGSEA significant: "fgsea_table_sig.xlsx"
  
DAVID table:
  -"DAVID_functional_annotation_clustering.txt"