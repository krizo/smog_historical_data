import pyexcel
import glob
import os

raw_data_dir = "raw_historic_data/"
input_dir = raw_data_dir + "xlsx/"
output_base_dir = raw_data_dir + "csv/"
metrics_to_convert = [  "Kody*" , "*PM2.5_1g*", "*PM10_1g*", "*CO_1g*",
                        "*NO2_1g*", "*C6H6_1g*", "*NOx_1g*", "*O3_1g*", "SO2_1g*" ]
for metric in metrics_to_convert:
    files_to_convert = glob.glob(input_dir + metric)
    for input_file in  files_to_convert:
        input_base_file = os.path.basename(input_file)
        if metric.startswith("Kody"):
            output_file = output_base_dir + input_base_file.split('.xlsx')[0] + ".csv"
        else:
            output_dir = output_base_dir + metric.replace("*", "") + "/"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file =  output_dir + input_base_file.split('.')[0] + ".csv"

        if not os.path.exists(output_file):
            pyexcel.save_as(file_name=input_file, dest_file_name=output_file)
