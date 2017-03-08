import json
import urllib.request
import sys

def random_title(subdomain):
	''' Returns the title of a random Wikipedia article '''
	url = "https://"+subdomain+".wikipedia.org/w/api.php?format=json&action=query&list=random&rnnamespace=0"
	json_doc = urllib.request.urlopen(url).read().decode("utf-8")
	parsed = json.loads(json_doc)
	return parsed["query"]["random"][0]["title"]

def get(title, summary, subdomain):
	''' Returns full or summarized Wikipedia article specified by given name '''
	if title==None or title=="":
		return None

	if summary:
		summary_param="&exintro"
	else:
		summary_param=""

	url = "https://"+subdomain+".wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exlimit=max&explaintext&redirects"+summary_param+"&titles="+urllib.parse.quote_plus(title)
	json_doc = urllib.request.urlopen(url).read().decode("utf-8")
	parsed = json.loads(json_doc)
	pages = parsed["query"]["pages"]

	try:
		for i in pages:
			return pages[i]["extract"].encode(sys.stdout.encoding, errors="replace").decode(sys.stdout.encoding).strip()
	except KeyError:
		return None

