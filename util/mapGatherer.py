"""
by every time running function from mapGatherer apis, there should be file
created under {packagename}/ as temporal storage, with map slot added to their name.

eg. map "HB2: Wooden - tau (tyrcs) [Extra (edit)]" from MCNC7K2026QF should be made into 
" VA - MCNC7K2026 3-Quarterfinals[ [HB2] tau (tyrcs) [Extra (edit)] ].osu"
"""

from slider import Beatmap
import slider


def gatherFromFile(oszfile, slotname):
    # process osz into folder
    # unpack osz
    oszfile = slider.beatmap.Beatmap.from_osz_file(oszfile)
    difficulty_list = [y[0] for y in oszfile]
    # select .osu file
    if len(difficulty_list) == 0:
        print("no .osu file found in osz, please retry.")
        return
    elif len(difficulty_list) == 1:
        desired_osu = difficulty_list[0]
    else:
        for i in range(len(difficulty_list)):
            print(f"{i+1}. {difficulty_list[i]}")
        print(f"{len(difficulty_list)+1}. cancel")
        osuid = int(input("multiple .osu files found, select your desired .osu:\n")) - 1

        if osuid == len(difficulty_list):
            return
        elif osuid <= 0 or osuid > len(difficulty_list):
            print("invalid option, please retry.")
            return
        else:
            desired_osu = difficulty_list[osuid - 1]
    
    target_osu_file = oszfile[desired_osu]
    target_osu_file.display_name = slotname + " " + target_osu_file.display_name
    
    pass

def getFromWeb(mapid, slotname):
    pass