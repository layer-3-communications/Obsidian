# This module generates system date, formats to year-month-day, and returns it

import datetime

def generate():
	# open a file for errors
        errorLog = open ('error.txt', 'a')

        # call system time and format it
        try:
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
        except Exception as e:
            errorLog.write('%s\n' %e)
            errorLog.write('Could not generate date.\n')

        errorLog.close()
        return date

