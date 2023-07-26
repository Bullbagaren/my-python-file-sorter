import os 
import sys
import re


def main():
    folders_to_be_sorted = sys.argv
    del folders_to_be_sorted[0] 
    contents = os.listdir(folders_to_be_sorted[0])
    not_hidden_files = [i for i in contents if i[0] != "." if os.path.isdir(folders_to_be_sorted[0] + "/" + i) == False]
    print(not_hidden_files)
    for file in not_hidden_files: 
        check_file_extension = file.split(".")
        print(check_file_extension)
        if len(check_file_extension) > 1:

            match check_file_extension[1]:
                case "jpg" | "png": 
                    os.system("mv " + folders_to_be_sorted[0] + "/" + file + " " + "~/" + "Pictures")

                case "txt" | "doc" | "docx" | "pdf":

                    os.system("mv " + folders_to_be_sorted[0]+ "/" + file + " " + "~/" + "Documents")

                case "mp3" | "flac" | "wav" | "wma":

                    os.system("mv " + folders_to_be_sorted[0] + "/" + file + " " + "~/" + "Music")

                case "mp4" | "webm" | "gif" | "mkv" | "avi":

                    os.system("mv " + folders_to_be_sorted[0] + "/" + file + " " + "~/" + "Videos")

                case _:
                    print(f"{file} has an extension that could not be sorted")

        else:
            print(f"{file} didn't seem to have a file extension and thusly could not be sorted")


    




if __name__ == "__main__":
    main()

