from wikipedia import Wikipedia
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

''' Start crawling '''

wiki = Wikipedia(args.subdomain, args.summary)
wiki.crawl(args.time_limit)
