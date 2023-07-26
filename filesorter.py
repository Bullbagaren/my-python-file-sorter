import os 
import sys
import re


def main():
    folders_to_be_sorted = sys.argv
    del folders_to_be_sorted[0] 
    contents = os.listdir(folders_to_be_sorted[0])
    not_hidden_files = [i for i in contents if i[0] != "." if os.path.isdir(folder + "/" + i) == False]
    
    for file in not_hidden_files: 
        check_file_extention = file.splt(".")
        match check_file_extention[1]:
            case "jpg" or "png": 
                os.system("mv " + folders_to_be_sorted + "/" + file + " " + "~/" + "Pictures")

            case "txt" or "doc" or "docx" or "pdf":

                os.system("mv " + folders_to_be_sorted + "/" + file + " " + "~/" + "Document")

            case "mp3" or "flac" or "wav" or "wma":

                os.system("mv " + folders_to_be_sorted + "/" + file + " " + "~/" + "Music")

            case "mp4" or "webm" or "gif" or "mkv" or "avi":

                os.system("mv " + folders_to_be_sorted + "/" + file + " " + "~/" + "Video")

            


    




if __name__ == "__main__":
    main()

