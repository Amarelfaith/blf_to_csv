import csv
from openpyxl import Workbook


def read_blf_file(blf_file):
    with open(blf_file, 'r') as f:  # Open the file in text mode to read strings
        # Read each line from the .blf file
        lines = f.readlines()
        # Strip any leading or trailing whitespace and newline characters
        lines = [line.strip() for line in lines]
    return lines


def write_excel_file(lines, excel_file):
    wb = Workbook()
    ws = wb.active
    # Write each element of the array in a single column
    for i, line in enumerate(lines, start=1):
        ws.cell(row=i, column=1, value=line)

    # Save the workbook to the specified Excel file
    wb.save(excel_file)


if __name__ == "__main__":
    # Change 'input.blf' and 'output.xlsx' to your input and output file names respectively
    input_file = 'scraped.blf'
    output_file = 'output1.xlsx'

    # Read data from .blf file
    lines_data = read_blf_file(input_file)

    # Write data to Excel file
    write_excel_file(lines_data, output_file)

    print("Conversion completed successfully.")
