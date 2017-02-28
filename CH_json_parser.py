import json
import pprint
import unicodecsv

json_data = open('SHAREHOLDERS_20170214.json').read()
split = json_data.split('\n')
output = [['comany_number', 'address_line_1', 'locality', 'postal_code', 'premises', 'region', 'country_of_residence','date_of_birth_month','date_of_birth_year','etag','individual_person_with_significant_control','links','name','forename','middle_name','surname','title','nationality','natures_of_control','notified_on']] 
for line in split:
	if line.strip() == '' or  line.strip() == '\n':
		continue
	try:
		data = json.loads(line)
		import pprint
		#pprint.pprint(data)
		output.append([
		data.get('company_number', ''),
		data['data'].get('address', {}).get('address_line_1', ''),
		data['data'].get('address', {}).get('locality', ''),
		data['data'].get('address', {}).get('postal_code',''),
		data['data'].get('address', {}).get('premises', ''),
		data['data'].get('address', {}).get('region', ''),
		data['data'].get('country_of_residence',''),
		data['data'].get('date_of_birth', {}).get('month', ''),
		data['data'].get('date_of_birth', {}).get('year', ''),
		data['data'].get('etag', ''),
		data['data'].get('kind', ''),
		data['data'].get('links', {}).get('self', ''),
		data['data'].get('name', ''),
		data['data'].get('name_elements', {}).get('forename', ''),
		data['data'].get('name_elements', {}).get('middle_name',''),
		data['data'].get('name_elements', {}).get('surname', ''),
		data['data'].get('name_elements', {}).get('title',''),
		data['data'].get('nationality', ''),
		data['data'].get('natures_of_control', ''),
		

		])
	except Exception as e:
		print line
		raise e 
	#if len(output) == 5:
	#	pprint.pprint(output)
	#	break
	#pprint.pprint(output)
	

with open(unicode('output.csv'), 'w') as fh:
    csvwriter = unicodecsv.writer(fh)
    csvwriter.writerows(output)

