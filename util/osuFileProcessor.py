import regex as re

def editfile(filepath, roundname, slotname):
    
    keynames= ["Version", "Title", "TitleUnicode", "AudioFilename"]    

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    keys = "|".join(keynames)
    pattern = rf"^({keys})(:\s*)(.*)$"

    info = {}

    for match in re.finditer(pattern, content, flags=re.MULTILINE):
        key = match.group(1)   # Typename
        val = match.group(3)   # Typeinfo
        info[key] = val

    bgpattern = r"\[Events\]\n(//Background and Video events)?\n(.*),(.*),\"(.*)\",(.*),(.*)"
    bgmatch = re.search(bgpattern, content, flags=re.MULTILINE)
    print(bgmatch)
    if bgmatch:
        info["Background"] = bgmatch.group(4)
    else:
        info["Background"] = ""

    print("--- 提取到的原始信息 ---")
    print(info)
    


