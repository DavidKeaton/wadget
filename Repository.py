"""
Base class for Repositories.
"""

import re
import urllib.parse
import urllib.request

from util import dprint, vprint, eprint


class Repository:
	_supportsHttps = None
	_baseUrl = None

	_search = {
		'url': None,
		'params': {
			'name': None,
			'page': None
		},
		# does this repository use pages in its search?
		'pagination': None,

		# Regular Expressions
		're': {
		}
	}

	_download = {
		'url':			None,
		'params': {
			'name':			None,
			'page':			None
		},
		'pagination':		None,

		# Regular Expressions
		're': {
		}
	}

	"""
	:param wads
		List of wads.
	"""
	def __init__(self, wads):
		self._wads = wads

		# TODO: validate all needed instance vars are declared
		# self.__validate()
		pass

	"""
	"""
	def __validate(self): # TODO
		raise NotImplementedError

	"""
	Create a URL for the given action, using the parameters provided.
	
	:param action
		"search" or "download"
	:param **kwargs
		URL parameters
	:returns str
	:raises KeyError
		If given an invalid action.
	"""
	def _createUrl(self, action: str, **kwargs) -> str:
		url = ""

		# get action reference
		if action == "search":
			aref = self._search
		elif action == "download":
			aref = self._download
		else:
			raise KeyError("Not a valid action: {}".format(action))

		# does it support HTTPS?
		if self._supportsHttps is True:
			url += "https://"
		elif self._supportsHttps is False:
			url += "http://"

		# add base URL
		url += self._baseUrl

		# append url for given action
		url += "/{}".format(aref['url'])

		# build query string
		if len(kwargs) >= 1:
			params = {}

			for kw in kwargs:
				# make sure the parameter exists for this action
				if kw not in aref['params']:
					# TODO: log as warning
					continue

				# convert kw -> param name
				params[aref['params'][kw]] = kwargs[kw]

			qs = urllib.parse.urlencode(params)
			url += "?{}".format(qs)

		dprint("created URL: {}", url)
		return url

	"""
	Get 
	"""
	def _nextPage(self): # TODO
		raise NotImplementedError

	"""
	Does this Repository go by this name or alias?
	
	(These names are used in determining if '--repository <name>'
	refers to this Repository.)
	
	:param name
		Repository "name" or "alias".
	:returns bool
	"""
	@staticmethod
	def knownAs(name: str) -> bool:
		raise NotImplementedError

	"""
	Print results from a search.
	
	:param results
		Array of results from a search.
	"""
	def showResults(self, results): # TODO
		raise NotImplementedError

	"""
	Searches for the given wad files.
	
	:returns int
	"""
	def search(self) -> int:
		raise NotImplementedError

	"""
	Downloads the given wad files.
	
	:returns int
	"""
	def download(self) -> int:
		raise NotImplementedError
