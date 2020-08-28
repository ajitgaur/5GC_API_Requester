test = "Testing"

def load_default(nf):
	if nf == "smf":
		smf_default = {
			"smContextRef": "0",
			"pduSessionRef": "0",
			"subsId": "0"
		}
		return smf_default
	elif ne == "udr":
		udr_default = {
			"ueId": "imsi-2089300007487",
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
		return udr_default
	else:
		return 0
