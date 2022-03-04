import json

name = input("Name: ")
email = input("Email: ")
password = input("Password: ")

data = {}
data['creds'] = []
data['creds'].append({
    'name': name.upper(),
    'email': email,
    'password': password
})

with open('creds.json', 'a+') as filehandle:
	json.dump(data, filehandle)

with open('creds.json', 'r+') as json_file:
	print("Checking locally...")
	data = json.load(json_file)
	for p in data['creds']:
		if (p['name']) == str(name.upper()):
			print("Found")
			email = p['email']
			password = p['password']

