import csv

def write_csv(filename, row):
    # writing to csv file
    with open(filename, 'a') as csvfile:
        csv.writer(csvfile).writerow(row)