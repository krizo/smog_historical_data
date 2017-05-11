import pyexcel
import glob
import os

raw_data_dir = "raw_historic_data/"
input_dir = raw_data_dir + "xlsx/"
output_dir = raw_data_dir + "csv/"
pm10_files = glob.glob(input_dir + "/*PM10_1g*")
for input_file in  pm10_files:
    input_base_file = os.path.basename(input_file)
    output_file = output_dir + input_base_file.split('.')[0] + ".csv"
    pyexcel.save_as(file_name=input_file, dest_file_name=output_file)
