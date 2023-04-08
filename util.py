from globals import g

"""
Print a message if debug logging is on.

:param level int (kwarg)
	Must be at least this level to print
"""
def dprint(msg, *args, **kwargs):
	# not on at all? jetpack time
	if g.args.debug == 0:
		return
	# not up to level? bail out
	elif ("level" in kwargs) and (g.args.debug < kwargs['level']):
		return

	print(("[DBG] " + msg).format(*args))

"""
Print a message if verbose logging is on.

:param level int (kwarg)
	Must be at least this level to print
"""
def vprint(msg, *args, **kwargs):
	# not on at all? jetpack time
	if g.args.verbose == 0:
		return
	# not up to level? bail out
	elif ("level" in kwargs) and (g.args.verbose < kwargs['level']):
		return

	print("[VRB] " + msg.format(*args))

"""
Print an error message.
"""
def eprint(msg, *args, **kwargs):
	print("[ERR] " + msg.format(*args))
