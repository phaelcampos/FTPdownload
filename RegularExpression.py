import re
import extract
Information = {

}
Bias_compiled = []
BStart_compiled = []


file=extract.extracted()

with open (file,"r") as file:

    for line in file:
        match_bias = re.match("(.*)([DSB][ ]{2}[A-Z][0-9]{3})", line)
        if match_bias:
            new_line =match_bias.group()
            str_line=str(new_line)
            BIAS = str_line[1:4]
            SVN = str_line[6:10]
            Bias_compiled.append(BIAS)
            Information.setdefault("BIAS",[]).append(BIAS)
            Information.setdefault("SVN", []).append(SVN)
        match_Value = re.match("((.*)[0-9][\.][0-9]{4})", line)
        if match_Value:
            new_line = match_Value.group()
            str_line = str(new_line)
            PRN = str_line[11:14]
            ObsOne = str_line[25:28]
            ObsTwo = str_line[30:33]
            BStart = str_line[35:49]
            BEnd =  str_line[50:64]
            Unit = str_line[65:67]
            Value = str_line[84:91]
            StdDev = str_line[97:108]
            if (len(BStart_compiled))<len((Bias_compiled)):
               Information.setdefault("PRN",[]).append(PRN)
               Information.setdefault("BIAS START", []).append(BStart)
               Information.setdefault("OBS1", []).append(ObsOne)
               Information.setdefault("OBS2", []).append(ObsTwo)
               Information.setdefault("BIAS END", []).append(BEnd)
               Information.setdefault("UNIT", []).append(Unit)
               Information.setdefault("VALUE", []).append(Value)
               Information.setdefault("STD DEV", []).append(StdDev)
               BStart_compiled.append(BStart)

print(Information["BIAS"])
print(Information["SVN"])
print(Information["PRN"])
print(Information["OBS1"])
print(Information["OBS2"])
print(Information["BIAS START"])
print(Information["BIAS END"])
print(Information["VALUE"])
print(Information["STD DEV"])
