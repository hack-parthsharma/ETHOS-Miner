#!/usr/bin/python
import os
from daemon import runner

TTYSN = 0

class MinerApp():
	def __init__(self):
		self.stdin_path = "/dev/ttyS" + TTYSN
		self.stdout_path = "/dev/ttyS" + TTYSN
		self.stderr_path = "/dev/null"
		self.pidfile_path = "/tmp/miner.pid"
		self.pidfile_timeout = 5
	def run(self):
		while True:
			d = input()
			if d == "r":
				print "ok"
				os.system("reboot")
			elif d == "s":
				print "ok"
				os.system("poweroff")
			elif d == "mr":
				os.system("minestart")
				print "ok"
			elif d == "ms":
				os.system("minestop")
				print "ok"
		
app = MinerApp()
r = runner.DaemonRunner(app)
r.do_action()
