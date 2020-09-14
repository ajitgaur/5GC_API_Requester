test = "Testing"

def load_default(nf):
	if nf == "smf":
		smf_default = {
			"smContextRef": "0",
			"pduSessionRef": "0",
			"subsId": "0"
		}
		return smf_default
	elif nf == "udr":
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
			"usageMonId": "0",
			"subscriptionId": "0"
 		}
		return udr_default
	elif nf == "udm":
		udm_default = {
			 "ueId": "imsi-2089300007487",
			 "supi": "0",
			 "supi / suci": "0",
			 "subscriptionId": "0",
			 "gpsi": "0",
			 "pduSessionId": "0"
		}
		return udm_default
	elif nf == "amf":
		amf_default = {
			"subscriptionId": "0",
			"ueContextId": "0",
			"n1N2MessageId": "0",
			"n2NotifySubscriptionId": "0"
		}
		return amf_default
	elif nf == "nssf":
		nssf_default = {
			"nfId": "deadbeef",
			"subscriptionId": "0"
		}
		return nssf_default
	elif nf == "ausf":
		ausf_default = {
			"supi": "imsi-2089300007487",
			"authCtxID": "imsi-2089300007487"
		}
		return ausf_default
	elif nf == "nrf":
		nrf_default = {
			"nfInstanceID": "deadbeef",
			"subscriptionID": "0"
		}
		return nrf_default
	elif nf == "pcf":
		pcf_default = {
			"polAssoId": "0",
			"bdtPolicyId": "0",
			"appSessionId": "0",
			"smPolicyId": "0",
			"polAssoId": "0"
		}
		return pcf_default
	else:
		return 0
