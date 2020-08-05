# XML to dict

import xmltodict
import pprint
import json

my_xml = """
    <audience>
      <id what="attribute">123</id>
      <name>Shubham</name>
    </audience>
"""
my_dict = xmltodict.parse(my_xml)
print(my_dict['audience']['id'])
print(my_dict['audience']['id']['@what'])
