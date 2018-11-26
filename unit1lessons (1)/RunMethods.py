fileName = "lesson_02_understanding_strings.py"
exec("from "+fileName[0:fileName.index(".")]+" import *")
file = open(fileName);
i=1
str = ""
while i<200:
    str=file.readline()
    if str.startswith("def"):
        functionName = str[str.index(" "):str.index(":")].strip()
        print("***Executing "+functionName+" ***")
        exec(str[str.index(" "):str.index(":")].strip())

    i+=1
