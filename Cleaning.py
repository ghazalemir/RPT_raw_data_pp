
import re
import pandas as pd

    
#The raw data output from the RPT system need clean up before any manipulation
#Read the RPT raw text file with the correct encoding

#Write the forth coloumn of the raw data (the only data to be extracted) 
#in counts.txt
with open("Data.txt", "r",encoding='latin-1') as input_file:
    with open("counts.txt", "w") as output_file:
        for line in input_file:
            columns = line.split()
            if len(columns) >= 4:
                output_file.write(columns[3] + "\n")

#open the file
with open('counts.txt', 'r') as file:
    text = file.read()

# Replace all superscript 3 characters with an empty string
text = re.sub(r'³', ' ', text)

# Write the modified text 
with open('counts.txt', 'w') as file:
    file.write(text)
    
#open the file
with open('counts.txt', 'r') as file:
    lines = file.readlines()

#Delete the first 3 lines of the clean_count.txt
with open('counts.txt', 'w') as file:
    file.writelines(lines[3:])


