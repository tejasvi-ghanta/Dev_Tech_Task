import gzip
import pandas as pd

file_locations = "/Users/ramakrishnamoturi/Downloads/name.basics.tsv.gz"
key_word_to_search = "producer"


def open_file(file_location):
    unzip_file = gzip.open(file_location, 'rb')
    return pd.read_csv(unzip_file, sep='\t')


def print_count(file_read, key_word):
    convert_df_tp_list = file_read.values.tolist()
    count = 0
    for row in convert_df_tp_list:
        if row[3] == "\\N" and str(row[4]).__contains__(key_word):
            count = count + 1
    print("The number of people who are alive & producers are ", count)


file = open_file(file_locations)
# Change the file location where the file is
print_count(file, key_word_to_search)
# We can change the primary keyword to anything.
