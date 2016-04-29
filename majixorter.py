#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  adrianssorter.py
#  
#  Copyright 2016 David Hayes <david@blackbricksoftware.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv
import sys
import os.path

def main():
	
	# defaults
	linesperfile = 500
	
	#~ print sys.argv
	
	# make sure enough arguements are passed
	if len(sys.argv)<3:
		print "Requires two arguements: filename.csv \"Column Heading\" to sort on; optional 3rd arguement for the number of lines to cache in each file (default 500)"
		return 0
	
	# make sure a valid file is passed
	filename = sys.argv[1]
	if filename=="" or not os.path.isfile(filename):
		print "Please give us a file to munch on"
		return 0
		
	# make sure a column heading is passes
	sorty = sys.argv[2]
	if sorty=="":
		print "Please give us heading to sorty by"
		return 0
		
	# overrride default lines per file
	if len(sys.argv)>=4:
		tmp = int(sys.argv[3])
		if tmp>0:
			linesperfile=tmp
	
	# open the file
	reader = csv.reader(open("companylist.csv", "r"))
	lineno = -2
	linecache = []
	tmpfiles = []
	
	# iterate over rows in the source file, breaking them into `linesperfile` chunks, sorting those chunks, and writing them to temp files
	for row in reader:

		lineno += 1

		if lineno == -1:
			header = row
			if sorty not in header:
				print sorty + " is not a value column heading in " + filename
				return 0
			headerref = dict()
			col = 0
			for v in header:
				headerref[v] = col
				col += 1
			#~ print headerref
			continue
		
		linecache.append(row)
	
		if lineno>0 and lineno%linesperfile == 0:
		
			# sort our line cache
			linecache.sort(key=lambda tup: tup[headerref[sorty]])
			
			# write our line cache out to a temporary directory
			tmpfile = 'tmp_' + str(lineno/linesperfile) + '.csv'
			tmpfiles.append(tmpfile)
			csv.writer(open(tmpfile,'w')).writerows(linecache)
			
			# clear the line cache
			linecache = []	
	
	print tmpfiles	
	
	return 0

if __name__ == '__main__':
	main()

