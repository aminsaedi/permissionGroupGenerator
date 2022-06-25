import yaml
import json
import pprint
from PyQt5.QtWidgets import QApplication


template_files = ('blue', 'black', 'gray', 'green')

complete_list = []

for file_name in template_files:
    with open('templates/'+file_name+'.yml', 'r') as template:
        parsed_template = yaml.safe_load(template)
    with open('fields/'+file_name+'.yml', 'r') as fields_file:
        fields = yaml.safe_load(fields_file)
        if (fields != None):
            for field in fields:
                for template_obj in parsed_template:
                    mydict = template_obj.copy()
                    mydict['name'] = field
                    complete_list.append(mydict)

with open('result.json', 'w+') as file:
    generated_json = json.dumps(complete_list, indent=4)
    file.write(generated_json)