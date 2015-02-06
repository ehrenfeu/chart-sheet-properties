import xml.etree.ElementTree as etree

def print_table(tables, idx):
    for drow in tables[idx].find('tbody').iter('data_row'):
    print '********************** data row **********************'
    for cell in drow.iter('cell'):
        print cell.text.strip()
        if cell.attrib['colspan'] != '1':
            print 'colspan warning! ------------------------------------------------------------------------------------------'

tree = etree.parse('output.xml')
tables = tree.findall('table')
tables[0].find('title').text

tables[0].find('header').find('header_line').findall('header_element')[0].text
for h_element in tables[0].find('header').find('header_line').iter('header_element'):
    print h_element.text

print_table(tables, 0)
print_table(tables, 1)
print_table(tables, 2)
