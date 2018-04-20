import datetime
import time
import os
import pyfiglet
import sys

fontBoi = pyfiglet.Figlet(font='roman')
fontBoiSub = pyfiglet.Figlet(font='epic')
ampm = True;
cseparator = ":"

def get_ascii_time():
        """
        Returns the ASCII representation of a date.
        """

	#Set the time zone
        os.environ['TZ'] = 'America/New_York'
        time.tzset()

        # define clock string based on options (12/24)
        if ampm:
            hour = int(time.strftime('%H'))

            suffix = "am"
            if hour >= 12:
                suffix = "pm"

            # fix the hour value into modulus of 12
            hour = hour % 12
            # fix the zero hour value
            if hour == 0:
                hour = 12

            # shows/hides separator for a blinking effect
            #separator = " : "
            
            
            '''
            if self.show_separator:
                separator = self.cseparator
                self.show_separator = False
            else:
                separator = " "
                self.show_separator = True
            '''
                
                
            clock = "%s%s%s%s%s %s" % (hour, cseparator, time.strftime('%M'), cseparator, time.strftime('%S'), suffix)
        else:
            # 24hs format includes seconds
            clock = time.strftime('%H' + cseparator + '%M' + cseparator + '%S')

        
        print fontBoi.renderText(clock)
        
        ''' OLD AND USELESS
        items = []
        for c in clock:
            items.append(self.digmap[c])
        output = ''
        for i in range(6):  # loop lines of chars - Increased to six for extra font line
            temp = ''
            for item in items:
                temp += item.split('\n')[i]
            output += temp + '\n'
        '''
           

while (1==1):
    date_time = datetime.datetime.now()
    print fontBoiSub.renderText(date_time.strftime('%a, %B %d, %Y'))
    print '\n\n\n'
    get_ascii_time()
    time.sleep(1)
    print(chr(27) + "[2J")