#!/usr/bin/env python3
"""
Searches for or downloads wad files from the chosen repository.


[Changelog]

0.1     - Initial creation.
0.2     - Base Repository class created.
0.3     - Supports "All Fear The Sentinel" basic searching.
0.4(*)  - Supports AFTS searching by pages.
0.5(*)  - Supports AFTS downloading.
"""

import sys
import argparse

import repos
from globals import g, VERSION
from util import dprint, vprint, eprint


VERSION = "0.3"


"""
Program entry point.
"""
def main() -> int:
	parser = argparse.ArgumentParser(
		prog="wadget",
		description="""
		Searches for or downloads DooM wads
		from several available repositories.
		"""
	)

	# version info
	parser.add_argument(
		"--version",
		action="version",
		version="%(prog)s " + VERSION
	)

	# verbose?
	parser.add_argument(
		"--verbose",
		"-v",
		dest="verbose",
		action="count",
		default=0,
		help="Be verbose (more means more)"
	)

	# debug?
	parser.add_argument(
		"--debug",
		"-d",
		dest="debug",
		action="count",
		default=0,
		help="Show debugging messages (more means more)"
	)

	# download?
	parser.add_argument(
		"--download",
		"-g",
		dest="action",
		action="store_const",
		const="download",
		default="search",
		help="should we download instead of search?"
	)

	# repository
	parser.add_argument(
		"--repository",
		"--site",
		"-r",
		dest="repo",
		metavar="repo",
		# nargs=1,
		type=str,
		required=True,
		help="WAD repository to use"
	)

	# <wads>
	parser.add_argument(
		"wads",
		metavar="wad",
		nargs="+"
	)

	g.args = parser.parse_args(sys.argv[1:])

	# get repo handler
	repo = None
	for R in repos.repos:
		if R.knownAs(g.args.repo):
			repo = R(g.args.wads)
			break

	# not given a valid repository
	if repo is None:
		eprint("Unknown repository: {}", g.args.repo)
		return 1

	dprint("wad list: {}", g.args.wads)

	# search
	if g.args.action == "search":
		rc = repo.search()
	# download
	elif g.args.action == "download":
		rc = repo.download()
	# ???
	else:
		eprint("Unknown action: {}", g.args.action)
		return 1

	if rc is None:
		rc = 0

	return rc


if __name__ == "__main__":
	sys.exit(main())
