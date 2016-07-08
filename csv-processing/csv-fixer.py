# Fix a "misalignment problem" in a CSV file of the Pettigrew study.
# Tested with Python 2.7
# Here is how I'd like to think about this script:

# @begin CSV_FIXER
# @param csv_infile_name
# @param csv_outfile_name
# @in csv_infile
# @out csv_outfile

# @begin CSV_READER
# @param csv_infile_name
# @in csv_infile
# @out csv_row
# @end CSV_READER

# @begin CSV_WRITER
# @param csv_outfile_name
# @in fixed_row
# @out csv_outfile
# @end CSV_WRITER

# @begin ROW_FIXER
# @in csv_row
# @out fixed_row
# @end ROW_FIXER

# @end CSV_FIXER

# .. and here is the actual code:
import csv

infile = "../openRefineOutput/pettigrewLettersNER.csv"
outfile = "../openRefineOutput/pettigrewLettersNER-fixed.csv"

with open(infile, 'r') as file_in, open(outfile,'w') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)
    
    header = next(reader, None)
    writer.writerow(header)
    
    for row in reader:
        box_list = row[1].split()
        folder_list = row[2].split()
        if folder_list == []:
            # the misaligned case
            box, folder = box_list[1], box_list[3]
        else:
            # the OK case
            box, folder = box_list[1], folder_list[1]
            
        writer.writerow([row[0]] + [box] + [folder] + row[3:])
            

        
