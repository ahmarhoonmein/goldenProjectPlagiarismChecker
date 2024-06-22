import difflib
from difflib import SequenceMatcher

# Text Files Used are made in the directory of the project.
# Opening Text Files for Checking Plagiarism:
with open("1.txt") as file1, open("2.txt") as file2:

    # Reading Data from the files:
    file1data = file1.read()
    file2data = file2.read()

    # Calculating the Ratio for Similarity of the two files data:
    similarity = SequenceMatcher(None, file1data, file2data).ratio()

    print("---Checking File 1 and File 2---")

    # Displaying Plagiarism Ratio:
    print("Similarity:", similarity*100, "%")
