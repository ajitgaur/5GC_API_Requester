import requests
import param

def main():
	address = "127.0.0.1"
	nf = input("Select NF: (smf)\n>> ") 
	param_default = param.load_default(nf)
	filename = "src/" + nf
	
	
	urls = []
	methods = []
	
	# Read URL
	with open(filename, 'r') as f:
		api = ""
		port = ""
		
		for line in f.readlines():
			if line[0] == ">":
				port = ":" + line.split(" ")[1]
			elif line[0] == "*":
				api = line.split(" ")[1][:-1]
			else:
				urls.append(address + port + api + line.split("|")[0])
				methods.append(line.split("|")[1][:-1])
	
	for i in range(len(urls)):
		# Replace parameter
		index = [0, 0]
		tmp = ""
		ii = 0
		while ii < len(urls[i]):
			if urls[i][ii] == "[":
				index[0] = ii
			elif urls[i][ii] == "]":
				index[1] = ii
				key = urls[i][index[0] + 1:index[1]]
				urls[i] = urls[i].replace(urls[i][index[0]:index[1] + 1], param_default[key])
				ii = index[0]
			ii += 1
	
	print("\nMETHOD" + " " * 2 + "URL" + " " * 150 + "RESPONSE" + "\n" + "-" * 169)
	for url, method in zip(urls, methods):
		result = method + " " * (8 - len(method)) + url + " " * (150 - len(url))
		if method == "GET":
			result += requests.get(url)
		elif method == "POST":
			result += requests.post(url)
		elif method == "PUT":
			result += requests.put(url)
		elif method == "DELETE":
			result += requests.delete(url)
		elif method == "PATCH":
			result += requests.patch(url)
		else:
			result = "Method Error!"
		print(result)

if __name__ == '__main__':
	main()
