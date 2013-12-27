__author__ = 'nic'

import epubdiff

checker = epubdiff.EpubDiff("tests/cc-shared-culture-20120130.epub", "tests/cc-shared-culture-20120130-TEST.epub")

checker.check()
print " "
print "Summary:"
print "---------------------------------"
for item in checker.difflog:
    print item[0][1], item[1]


print " "
print "Details:"
print "---------------------------------"

for item in checker.difflog:

    print item[0][1], item[1]
    if len(item) > 2:
        print "checksums: ", item[2], " => ", item[3]

    if len(item) > 4:
        print "diff: "
        print item[4]

    print " "