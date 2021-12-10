# 595proj-data

In this file are .txt files containing the raw textual data of memes we have collected
from various social media sources, along with their gold labels. Each entry is represented
in two lines: the labels (each represented by an integer) and the text.
"datatojson.py" is a Python script to convert raw data into json files.

Input data to datatojson.py should be in the format:

10 11 12
This is a sample sentence, and the numbers above correspond to gold labels
1 2 3 4 5
This is a sample\nsentence with\n\nnewline characters
2 3 4 5 6
\"This is another\n\nsample sentence with quotation marks\"

This is a sentence with no labels
1 2 3
hello world


Important: the output of the script will turn all “\n” to “\\n” and many “\"” to “\\\"”, so you’ll have to manually go back and fix them; I recommend using CTRL-G in VSCode to do this quickly.
