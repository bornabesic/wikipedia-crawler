import wikipedia
import time
import os
import argparse

''' A script used to randomly collect Wikipedia articles '''

''' Parse command line arguments '''

parser = argparse.ArgumentParser()

parser.add_argument(
	"time_limit",
	type=int,
	help="crawling time limit in seconds"
)
parser.add_argument(
	"subdomain",
	type=str,
	help="crawling subdomain"
)
parser.add_argument(
	"-s",
	"--summary",
	action="store_true",
	help="collect summaries instead of full articles"
)

args = parser.parse_args()

''' Create directory where data will be saved '''

try:
	os.mkdir("./data/")
except FileExistsError:
	pass

''' Start crawling '''

start = time.time()
while True:
	title = wikipedia.random_title(subdomain=args.subdomain)
	clean_title = "".join(c for c in title if c.isalnum())
	path = "./data/"+clean_title+".txt"
	if os.path.exists(path):
		continue

	content = wikipedia.get(title, summary=args.summary, subdomain=args.subdomain)
	if content==None or content=="":
		continue

	with open(path, "wt", encoding="utf-8") as f:
		f.write(content)

	end = time.time()
	if end-start>args.time_limit:
		break

