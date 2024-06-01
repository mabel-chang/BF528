#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help='The input file specified will be the GTF file provided by snakemake',dest="input", required=True)
parser.add_argument("-o", "--output", help='The output file name and path provided by snakemake',dest="output", required=True)

args = parser.parse_args()

# Regex solution using dictionary
import re
id_2_name = {}

genename = r'gene_name\s([^;]*)'
geneid = r'gene_id\s([^;]*)'

with open(args.input, 'r') as r:
    for line in r:
        if line.startswith('#'):
            continue

        gene_name = re.search(genename, line)
        gene_id = re.search(geneid, line)

        if gene_id.group().split('"')[1] in id_2_name:
            continue
        else:
            id_2_name[gene_id.group().split('"')[1]] = gene_name.group().split('"')[1]

with open(args.output, 'wt') as w:
    for k, v in id_2_name.items():
        w.write('{}\t{}\n'.format(k, v))

'''
# Solution using CSV and split

import csv

ids = []
names = []

with open(args.input, 'rt') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if row[0][0] == '#':
            continue
        else:
            if row[2] == 'gene':
                gene_info = row[8].strip().split('; ')
                splits = [_.split('"') for _ in gene_info]
                for l in splits:
                    if l[0].strip() == 'gene_id':
                        ids.append(l[1])
                    if l[0].strip() == 'gene_name':
                        names.append(l[1])

with open(args.output, 'wt') as w:
    for geneid, genename in zip(ids, names):
        w.write('{}\t{}\n'.format(geneid, genename))
'''