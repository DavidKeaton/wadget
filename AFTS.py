"""
All Fear The Sentinel
"""

from Repository import Repository

import re
import urllib.request


class Repo(Repository):
	_supportsHttps = True
	_baseUrl = "allfearthesentinel.com"

	_search = {
		'url':			"zandronum/wads.php",
		'params': {
			'name':		"name",
			'page':		"page"
		},
		'pagination':	True
	}

	_download = {
		'url':			"zandronum/download.php",
		'params': {
			'name':		"file"
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
	Search for the given wad files.
	
	:returns int
	"""
	def search(self) -> int: # TODO
		url = self._createUrl("search")
		print("SEARCHING AFTS")

		raise NotImplementedError
		return 0

	"""
	Download the given wad files
	
	:returns int
	"""
	def download(self) -> int:	# TODO
		print("DOWNLOADING AFTS")

		raise NotImplementedError
		return 0
