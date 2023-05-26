import csv
import tkinter as tk
from tkinter import filedialog

# Create a pop-up window to select the input files
root = tk.Tk()
root.withdraw()

# Inputs from terminal
print('Output file will contain the full line of the Input file 2 if the ID is found in Input file 1')
print('Select Input File 1')
file1 = filedialog.askopenfilename(title="Select Input File 1")
print(file1)
print('Select Input File 2')
file2 = filedialog.askopenfilename(title="Select Input File 2")
print(file2)
print('Save Output File As')
output_file = filedialog.asksaveasfilename(title="Save Output File As")
print(output_file)
col1 = int(input("What is the column number of the first file that you want to compare? "))
col2 = int(input("What is the column number of the second file that you want to compare? "))

with open(file1, 'r') as input1_file, open(file2, 'r') as input2_file, open(output_file, 'w', newline='', encoding='utf-8') as output_file:
    reader1 = csv.reader(input1_file)
    reader2 = csv.reader(input2_file)
    writer = csv.writer(output_file)    
    Col1 = col1
    Col2 = col2
    FirstSet = set()

    for line1 in reader1:
        FirstSet.add(line1[Col1])
    
    for line2 in reader2:
        if  line2[Col2] in FirstSet:
            writer.writerow(line2)


    print('>>>>>>> Executed with success !!!')