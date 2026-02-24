import os

from slider import Beatmap
import zipfile

import slider
import util.packageMaker as packageMaker
import util.mapGatherer as mapGatherer
def clearcache():
    pass

songid_set = set()

if __name__ == "__main__":
    # interaction with user

    foldername = input("Desired Tourney Round Name:")
    
    # create folder from foldername as temp
    os.mkdir(foldername)

    while True:
        slotname = input("slotname:\nPress enter to exit.\n")
        if(slotname == ''):
            break

        if(slotname in songid_set):
            print("WARNING: YOU HAVE TWO MAPS WITH SAME SLOTNAME")
        option = input("get map from:\n(1) file\n(2) web\n(3) cancel\n")
        if option == '1':
            input("put your desired .osz file under current folder, then press enter.")
            osz_list = [f for f in os.listdir('.') if f.endswith('.osz')]
            desired_osz = ""
            if len(osz_list) == 0:
                print("no .osz file found, please retry.")
                continue
            elif len(osz_list) == 1:
                desired_osz = osz_list[0]
            else:
                for i in range(len(osz_list)):
                    print(f"{i+1}. {osz_list[i]}")
                print(f"{len(osz_list)+1}. cancel")
                oszid = int(input("multiple .osz files found, select your desired osz:\n")) - 1

                if oszid == len(osz_list):
                    continue
                elif oszid <= 0 or oszid > len(osz_list):
                    print("invalid option, please retry.")
                    continue
                else:
                    desired_osz = osz_list[oszid - 1]
            
            # 
        elif option == '2':
            pass
        elif option == '3':
            continue
        else:
            print("invalid option name.")

    packageMaker.makefile(foldername)
    print("mappack created successfully on current directory.")
    input("press enter to exit.")
    clearcache()