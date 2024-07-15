import os
import sys


import tkinter as tk      # Python 3
	
def main():
	
    # same as 2> /dev/null in the shell
	f = open("/dev/null", "w")
	os.dup2(f.fileno(), 2)
	f.close()

	print("Tcl Version: {}".format(tk.Tcl().eval('info patchlevel')))
	print("Tk Version: {}".format(tk.Tk().eval('info patchlevel')))

	
if __name__ == '__main__':
	sys.exit(main())