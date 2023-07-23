import os 
import sys
import re


def main():
    folders_to_be_sorted = sys.argv
    del folders_to_be_sorted[0] 
    contents = os.listdir(folders_to_be_sorted[0])

    relevant_files = [i for i in contents if i[0] != "."]
    print(relevant_files)





if __name__ == "__main__":
    main()

