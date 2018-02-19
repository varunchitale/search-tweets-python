from datetime import date
from dateutil.rrule import rrule, DAILY
import pandas as pd

import os, subprocess

a = date(2014, 1, 1)
b = date(2018, 1, 1)
daterange = pd.date_range(a,b)
print daterange

for i,date in enumerate(daterange):
    print i
    try:
	    output = subprocess.check_output('python Exporter.py --querysearch narendramodi --toptweets --since %s --until %s --output namo43.csv --maxtweets 100'
	    		%(str(daterange[i].strftime("%Y-%m-%d")),str(daterange[i+1].strftime("%Y-%m-%d"))), shell=True)	
	    print output
	    print str(date.strftime("%Y-%m-%d"))
    except:
    	import traceback
    	print traceback.format_exc()