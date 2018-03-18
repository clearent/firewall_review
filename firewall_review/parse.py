import sys
import re

inputFile = sys.argv[1]

matcher = re.compile(r"hitcnt=(?P<hitcount>\d+)\).(?P<id>.*$)")

with open(inputFile) as file:
    line = file.readline()
    while(line):
        # if the line is an ACL, use the compiled regular expression to parse it for the id and hitcount
        if(line.startswith("access-list") and line.find("object-group") > 0):
            match = matcher.search(line)
            hitcnt = match.group('hitcount')
            id = match.group('id')
            print("id=" + id + ", hitcount=" + hitcnt + ", '" + line + "'")
        line = file.readline()