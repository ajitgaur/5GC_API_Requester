import requests

udr_default = {"ueId": "imsi-2089300007487", 
			   "servingPlmnId": "20893", 
			   "subsId": "0", 
			   "pduSessionId": "0", 
			   "ueGroupId": "0", 
			   "appId": "0", 
			   "influenceId": "0", 
			   "bdtReferenceId": "0", 
			   "sponsorId": "0", 
			   "usageMonId": "0"
			}
address = "127.0.0.1"

filename = input("Select NF: (udr / amf)\n>> ")
with open(filename, 'r') as f:
	api = ""
	port = ""
	url = ""

	# Read urls
	for i in f.readlines():
		method = ""
		if i[0] == ">":
			port = ":" + i.split(" ")[1]
		elif i[0] == "*":
			api = i.split(" ")[1][:-1]
		else:
			url = address + port + api + i.split("|")[0]
			method = i.split("|")[1]
			
			parameter = ""
			flag = 0
			index = []
			for i in range(len(url)):
				if url[i] == "[":
					flag = 1
					index.append(i)
					continue
				elif url[i] == "]":
					flag = 0
					index.append(i)
					url = url.replace(url[index[0]:index[1] + 1], udr_default[parameter])
					index = []
					parameter = ""
					
				if flag == 1:
					parameter += url[i]
				else:
					pass

		print(url, method)

