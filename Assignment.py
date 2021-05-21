import gzip
import pandas as pd


def open_file(file_location):
    unzip_file = gzip.open(file_location, 'rb')
    return pd.read_csv(unzip_file, sep='\t')


def print_count(file_read):
    convert_df_tp_list = file_read.values.tolist()
    count = 0
    for row in convert_df_tp_list:
        if row[3] == "\\N" and str(row[4]).__contains__("producer"):
            count = count + 1
    print("The number of people who are alive & producers are  ", count)


file = open_file("/Users/ramakrishnamoturi/Downloads/name.basics.tsv.gz")
print_count(file)
