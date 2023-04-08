"""
All Fear The Sentinel
"""

from Repository import Repository

import re
import urllib.request

from util import dprint, vprint, eprint


regex = re.compile(
	r'<a\s*href="/zandronum/download.php\?file=(?P<name>.+?)".*?</a>\s*</td>'
	+ r'\s*<td.*?>\s*(?P<md5>[a-fA-F0-9]{32})\s*</t[hd]>'
	+ r'\s*<td.*?>\s*(?P<size>.+?)\s*</td>'
	+ r'\s*<td.*?>\s*(?:<a.*?>\s*(?P<maintainer>.+?)\s*</a>|-)\s*</td>'
	+ r'\s*<td.*?>\s*(?:<a.*?>\s*(?P<uploader>.+?)\s*</a>|-)\s*</td>'
	+ r'\s*<td.*?>\s*(?P<updated>.+?\s+[AP]M)\s*</td>',
	re.DOTALL
)

hdr = "------------------------------------------------------------"


class Repo(Repository):
	_supportsHttps = True
	_baseUrl = "allfearthesentinel.com"

	_search = {
		'url':			"zandronum/wads.php",
		'params': {
			'name':		"name",
			'page':		"page"
		},
		'pagination':	True,

		're': {
			'all':		regex
		}
	}

	_download = {
		'url':			"zandronum/download.php",
		'params': {
			'name':		"file"
		},

		're': {
			'all': 		regex
		}
	}

	"""
	:param name
	"""
	@staticmethod
	def knownAs(name: str) -> bool:
		return name in [
			"afts",
			"allfearthesentinel",
			"all fear the sentinel"
		]

	"""
	Print results from a search.
	
	:param results
		Array of search results.
	"""
	# TODO: make columns instead of by rows
	def showResults(self, results): # TODO
		if len(results) > 0:
			for r in results:
				entry = (
					hdr
					+ "\nName:        {name}"
					+ "\nMD5:         {md5}"
					+ "\nSize:        {size}"
					+ "\nMaintainer:  {maintainer}"
					+ "\nUploader:    {uploader}"
					+ "\nUpdated:     {updated}"
				)
				print(entry.format(**r))
			print(hdr)
		else:
			print("No results found")

		#raise NotImplementedError
		return

	"""
	Search for the given wad files.
	
	:returns int
	"""
	# TODO: pagination support
	def search(self) -> int:
		url = self._createUrl(
			"search",
			name=self._wads[0]
		)

		vprint(
			"Searching 'All Fear The Sentinel' for {}",
			self._wads
		)

		# open and read URL
		try:
			dprint("Opening URL...")
			content = urllib.request.urlopen(url)
			dprint("Reading page contents...")
			buf = content.read().decode()
			dprint("page contents:\n{}", buf, level=2)
		except Exception as e:
			eprint(e)
			return 1

		rex = self._search['re']['all']

		results = []
		for m in rex.finditer(buf):
			if m:
				o = m.groupdict()

				if o['maintainer'] is None:
					o['maintainer'] = "-"
				if o['uploader'] is None:
					o['uploader'] = "-"

				dprint("Found result: {}", o['name'])
				results.append(o)

		vprint("found {} results", len(results))

		# show the results
		self.showResults(results)

		return 0

	"""
	Download the given wad files
	
	:returns int
	"""
	def download(self) -> int:	# TODO
		print("DOWNLOADING AFTS")

		raise NotImplementedError
		return 0
