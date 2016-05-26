import csv
import re

#import subprocess
HEADER = ['IN_INTERFACE','OUT_INTERFACE','SOURCE_IP', 'SOURCE_PORT','DEST_IP','DEST_PORT','PROTOCOL']
resultFile = open("output.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
wr.writerow(HEADER)
filename = '/var/log/iptables.log_1'
RESULT = []
#print text
with open(filename, 'rb') as log_ip:
	for line in log_ip:
		pair_re = re.compile('([^ ]+)=([^ ]+)') 
		data = dict(pair_re.findall(line))
		if 'IN' in data:
			RESULT.append(data['IN'])
		else:
			RESULT.append(' ')
		if 'OUT' in data:
			RESULT.append(data['OUT'])
		else:
			RESULT.append(' ')
		if 'SRC' in data:
			RESULT.append(data['SRC'])
		else:
			RESULT.append(' ')
		if 'SPT' in data:
			RESULT.append(data['SPT'])
		else:
			RESULT.append(' ')
		if 'DST' in data:
			RESULT.append(data['DST'])
		else:
			RESULT.append(' ')
		if 'DPT' in data:
			RESULT.append(data['DPT'])
		else:
			RESULT.append(' ')
		if 'PROTO' in data:
			RESULT.append(data['PROTO'])
		else:
			RESULT.append(' ')
		wr.writerow(RESULT)
		RESULT = []