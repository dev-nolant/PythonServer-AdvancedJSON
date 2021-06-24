import api_json_handler, os

# STARTS the combination of the .JSON files in 'databases/'
api_json_handler.start()

# Ignore
print('----------------------------------------')

# STARTS the FLASK server for the api
os.system('python api_server.py')