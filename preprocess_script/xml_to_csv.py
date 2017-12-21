import argparse
import copy


# class for printing csv from dictionaries. First call create header row.
class WriteFiles:
    def __init__(self, write_file, separator):
        self.file = open(write_file, "a")
        self.head = []
        self.separator = separator
    def write_line(self, dict):
        if len(self.head) == 0:
            count = len(dict)
            for item in dict:
                count -= 1
                self.head.append(item)
                self.file.write(str(item))
                if (count != 0):
                    self.file.write(str(self.separator))
            self.file.write("\n")
        count = len(self.head)
        for items in self.head:
            count -= 1
            self.file.write(str(dict[items]))
            if (count != 0):
                self.file.write(str(self.separator))
        self.file.write("\n")
    def __del__(self):
        self.file.close()

parser = argparse.ArgumentParser("LSH")
parser.add_argument('-i', nargs = "+", help='input file in xml format with relative to path where is call progam', required=True)
parser.add_argument('-o', nargs = 2, help='output file name with relative path to where call this program', required=True)
parser.add_argument('-d', help='delimiter in output file', default = ',')
args = parser.parse_args()
write_file_ucast = WriteFiles(args.o[0],args.d)
write_file_hlasy_strana = WriteFiles(args.o[1], args.d)
import xml.etree.ElementTree as ET
for i in args.i:
    tree = ET.parse(i)
    root = tree.getroot()
    for child in root:
        if child.tag != "OBEC":
            continue
        attr = child.attrib
        dict = {}
        for at in attr:
            dict[at] = attr[at]
        for chil in child:
            if chil.tag == "UCAST":
                dict_ucast = copy.deepcopy(dict)
                attrU = chil.attrib
                for atU in attrU:
                    dict_ucast[atU] = attrU[atU]
                write_file_ucast.write_line(dict_ucast)
            if chil.tag == "HLASY_STRANA":
                dict_strany = copy.deepcopy(dict)
                attrS = chil.attrib
                for atS in attrS:
                    dict_strany[atS] = attrS[atS]
                write_file_hlasy_strana.write_line(dict_strany)
