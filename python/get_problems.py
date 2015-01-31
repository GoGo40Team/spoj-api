# -*- coding: ISO-8859-1 -*-


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Copyright (c) 2015, GoGoCoding Team
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this 
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may 
be used to endorse or promote products derived from this software without specific 
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

----
Written by: Péricles Lopes Machado

Script: get_problems.py

Description: This script get the problem list from SPOJ (www.spoj.com)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from HTMLParser import HTMLParser
from subprocess import call
import pycurl
import cStringIO
import time
import string
import json
import re
import os
import sys

my_location = os.path.dirname(os.path.realpath(__file__)) + "/"

print "Script location = " + my_location

######################################################################
"""
Utilities
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


####################################################################
"""
Download the link content and create a file.
"""
use_wget = True
fn = my_location + "get_buffer"
pause_duration = 2

def get_file(link):
	global use_wget, fn, my_location

	print "Downloading " + link + "..."
	files_list = ""
	
	if use_wget:
		call(["wget", link, "-O", fn, "-o", my_location + "log_spoj"])

		files_list = ""

		with open(fn) as files_list:
			for l in f:
				files_list = files_list + l
	else:
		buf = cStringIO.StringIO()
	
		c = pycurl.Curl()
		c.setopt(c.URL, link)
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()
		
		files_list = buf.getvalue()
		buf.close()
		
		return files_list

	print link + " downloaded!"
	
	time.sleep(pause_duration)
	
	return files_list



