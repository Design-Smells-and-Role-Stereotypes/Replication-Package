import argparse
from read_input_data import read_original_data
from write_csv_data import write_csv_data
from final_ds_file import final_ds_output
import os


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='design smell extraction args')
    parser.add_argument('--regex', required=True,
                        help='the regular expression for extracting design smells')
    parser.add_argument('--output', required=True,
                        help='the output filename with .csv extension. Example ds_project_name.csv')                    

    args = parser.parse_args()
    # replace this line with the path to you design smell .ini files path.
    # it should following the follow the convention "src/data/..."
    design_smells_path = "src/data/K9/Design Smell detection/"
    ds_files = read_original_data(design_smells_path)
    write_csv_data(design_smells_path, ds_files, args.regex)

    # final output file
    final_ds_output(design_smells_path, args.output)