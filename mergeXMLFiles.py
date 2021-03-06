#!/usr/bin/env python

import logging, os, os.path, sys
import glob
from xml.etree import ElementTree
import pprint


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

logging.debug('Start of program')
def run(files):
    xml_files = glob.glob(files +"/*.xml")
    logging.debug(xml_files)
    xml_element_tree = None
    for xml_file in xml_files:
        # get root
        logging.debug(xml_file)
        data = ElementTree.parse(xml_file).getroot()
        # print ElementTree.tostring(data)
        for result in data.iter('result'):
            if xml_element_tree is None:
                xml_element_tree = data 
            else:
                xml_element_tree.extend(result) 
    if xml_element_tree is not None:
        print(ElementTree.tostring(xml_element_tree))
        #pp=pprint.PrettyPrinter(indent=4)
        #pp.pprint(ElementTree.tostring(xml_element_tree))
        aTree=str(ElementTree.tostring(xml_element_tree, encoding='unicode', method='xml'))
        #pp.pprint(aTree)
        file=open("testfile.xml","w")
        file.write('<?xml version="1.0" encoding="utf-8"?>')
        file.write(aTree)
        file.close







def main():
    files="."
    run(files) 
    logging.debug('End of program')

if __name__ == '__main__':
    main()
