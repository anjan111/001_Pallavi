# convert XML data to Json data

import xmltodict
import pprint
import json

my_xml = """
    <audience>
      <id what="attribute">123</id>
      <name>Anjan</name>
    </audience>
"""

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(json.dumps(xmltodict.parse(my_xml)))
