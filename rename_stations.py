import csv
import os

def get_new_stations_names(definitions_file="raw_historic_data/csv/Kody_stacji_pomiarowych.csv"):
    stations = {}

    with open(definitions_file, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader) # skip the header
        for row in reader:
            old_name, new_name = row[2], row[3]
            stations[old_name] = new_name
    return stations


def rename_station_names_in_csv():
    input_dir = "raw_historic_data/csv/"
    stations = get_new_stations_names()

    for root, dirs, files in os.walk(input_dir):
        for csv_file in files:
            if csv_file.endswith(".csv"):
                input_csv = os.path.join(root, csv_file)
                output_csv = input_csv.replace(".csv", "_converted.csv")
                with open(input_csv) as input_file, \
                     open(output_csv, 'w') as output_file:
                  reader = csv.reader(input_file)
                  writer = csv.writer(output_file)

                  # read the header
                  header = next(reader)

                  # modify the column title
                  new_header = []
                  for column in header:
                      new_header.append(stations.get(column, column))

                  # write the new header out
                  writer.writerow(new_header)

                  # copy all other rows unmodified
                  for row in reader:
                    if not (row[0] == "Wskaźnik" or row[0] == "Czas uśredniania"):
                        writer.writerow(row)

                # replace old csv file with the one with new stations' definitons:
                os.rename(input_csv.replace(".csv", "_converted.csv"), input_csv)

rename_station_names_in_csv()
