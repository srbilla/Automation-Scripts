
import re

# Write your regex here
regex = r"[aeiou]"

# Enter your test string here
test_str = "test my python"

matches = re.finditer(regex, test_str, re.MULTILINE | re.IGNORECASE)

for matchNumber, match in enumerate(matches):
    matchNumber = matchNumber + 1

    print ("Match {matchNumber} was found at {start}-{end}: {match}".format(matchNumber=matchNumber, start=match.start(),
                                                                         end=match.end(), match=match.group()))

    for groupNumber in range(0, len(match.groups())):
        groupNumber = groupNumber + 1

        print ("Group {groupNumber} found at {start}-{end}: {group}".format(groupNumber=groupNumber, start=match.start(groupNumber),
                                                                         end=match.end(groupNumber),
                                                                         group=match.group(groupNumber)))

