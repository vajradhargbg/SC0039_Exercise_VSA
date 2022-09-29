#This script takes the given .csv file as input and finds the sequence length and adds it as a column in the end.

import pandas as pd
#imports the pandas library.

seg_length = pd.read_csv("brca_cnvs_tcga-1.csv")
#imports the .csv file.

df = pd.DataFrame(seg_length)
#converts seq_length into dataframe

df["seq_length"] = df["loc.end"]-df["loc.start"]
#subtracts the sequence end from sequence start to give seq length and adds new column.

df.to_csv("brca_cnvs_tcga-2.csv")
#exports ouutput as csv file