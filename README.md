# Language detector

Reads a CSV file.  
Detects language for a given column.  
Saves it to CSV as "language" column.  

**Usage**

`python3 detect.py FILE.csv`

Options:
`--output_file` - set path for output, e.g. `OUT.csv`  
`--text_column` - The column number (starting from 1) that contains the text for language detection.  
`--has_header` - Indicates if the input CSV file has a header row.
