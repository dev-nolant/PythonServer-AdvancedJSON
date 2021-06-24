from os import walk, remove
import json

# Important variables and lists
data_raw =  walk('databases')
unparsed_databases = ((data_raw).__next__())[2]

filter = 'ignore'
prefix = '['
suffix = ']'
output_file = 'ParsedData_ignore.json'
parsed_names = []

# JSON Writing Handler
def json_writer(data):
    print("Step 3")
    
    _prefix_writer = open('databases/' + output_file, 'a'); _prefix_writer.write('{}'.format(prefix)); _prefix_writer.close(); print("Prefix added: {}".format(prefix))
    for stringed_data in data: write_data = open('databases/' + output_file, 'a'); write_data.write(stringed_data); write_data.close()
    _suffix_writer = open('databases/' + output_file, 'a'); _suffix_writer.write('{}'.format(suffix)); _suffix_writer.close(); print("Suffix added: {}".format(suffix))
    
    print("Finished merging {}".format(parsed_names))
    
# JSON Combining Handler
def json_combine():
    print("Step 2")

    temp_json_data_holder = []

    pointer = 0

    try: remove('databases/'+output_file)
    except:
        pass

    for current_file in parsed_names:
        pointer += 1
        temp_data_holster = open('databases/'+str(current_file), 'r').read()
        temp_data_parsed = (temp_data_holster.replace(']', '')).replace('[', '')

        if pointer < len(parsed_names): json_delimiter = ','
        else: json_delimiter = ''
        temp_json_data_holder.append(temp_data_parsed+json_delimiter)

    json_writer(temp_json_data_holder)

# STARTS the combination
def start():

    file_pointer = 0

    print("Started")

    while file_pointer < len(unparsed_databases):
        if filter not in unparsed_databases[file_pointer] and '.json' in unparsed_databases[file_pointer]: parsed_names.append(unparsed_databases[file_pointer]);file_pointer += 1
        else: file_pointer += 1
    json_combine()