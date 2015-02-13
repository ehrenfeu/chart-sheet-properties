#!/usr/bin/env python

import xml.etree.ElementTree as etree
from os.path import join

basedir = '/home/ehrenfeu/usr/packages/OpenSeaMap/S-11_PartB_RegionD_e2.0.5'
filename = 'output.xml'

def print_table(table):
    print('******** Printing table ********')
    print('TITLE: %s ' % table.find('title').text)

    header = ''
    for h_element in table.find('header').find('header_line').iter('header_element'):
        header = header + "," + h_element.text.strip()
    print('HEADER: %s ' % header)

    for drow in table.find('tbody').iter('data_row'):
        row = ''
        for cell in drow.iter('cell'):
            row = row + "," + cell.text.strip()
            if cell.attrib['colspan'] != '1':
                print 'colspan warning! ------------------------------------------------------------------------------------------'
        print(row)
    print('')

def process_pdf2table_xml():
    print('Parsing "%s"...' % join(basedir, filename))
    tree = etree.parse(join(basedir, filename))
    tables = tree.findall('table')

    # for table in tables:
    #     print_table(table)
    print_table(tables[0])
    print_table(tables[1])
    print_table(tables[2])
    print_table(tables[5])


if __name__ == "__main__":
    print('Running XML parser')
    process_pdf2table_xml()
