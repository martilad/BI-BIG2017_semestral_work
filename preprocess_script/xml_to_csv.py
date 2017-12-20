import argparse
import copy

def check_childs(root_tag, tags, file, line_to_write,be_first):
    if len(root_tag) == 0:
        print (line_to_write)
    for child in root_tag:
        if child.tag not in tags:
            continue
        attr = child.attrib
        for at in attr:
            if be_first == 0:
                line_to_write.append(args.d)
                be_first = 1
            line_to_write.append(attr[at])
        check_childs(child, tags, "prdel", copy.deepcopy(line_to_write), be_first)

parser = argparse.ArgumentParser("LSH")
parser.add_argument('-i', help='input file in xml format with relative to path where is call progam', required=True)
parser.add_argument('-o', help='output file name with relative path to where call this program', required=True)
parser.add_argument('-t', nargs = "+", help='output file name with relative path to where call this program', required=True)
parser.add_argument('-d', help='output file name with relative path to where call this program', default = ',')
args = parser.parse_args()
import xml.etree.ElementTree as ET
tags = set(args.t)
print (tags)
tree = ET.parse(args.i)
root = tree.getroot()
line_to_write = []
be_first = 0
if root.tag in tags:
    attr = child.attrib
    for at in attr:
        if be_first == 0:
            line_to_write.append(args.d)
            be_first = 1
        line_to_write.append(attr[at])
check_childs(root, tags, "prdel", copy.deepcopy(line_to_write), be_first)



            