from xml.etree.ElementTree import Element, SubElement, ElementTree
from json import load

class JSON2XML(object):
    def __init__(self, json_file, xml_file):
        self.jsonfile = json_file
        selfxmlfile = xml_file
        self.__do_parse()


    def __do_parse(self):
        params = ['size', 'mtime']
        content = load(open(self.jsonfile))
        root_tag = Element('directories')

        for dir_name in content:
            dir_tag = SubElement(root_tag, 'directory', attrib={'name': dir_name})

            