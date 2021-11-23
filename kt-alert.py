import urllib.request
import re
import time
import os
from bs4 import BeautifulSoup
from datetime import datetime

location_arr = ['238', '243', '242', '232', '237', '235', '240', '239', '241', '251']
locationname_arr = ['Eatontown', 'Freehold', 'Toms River', 'Bakers Basin', 'Delanco', 'Camden', 'Edison', 'South Plainfield', 'Flemington', 'West Deptford']
base_url_link = 'https://telegov.njportal.com/njmvc/AppointmentWizard/17/'
required_months = ['November', 'December', 'January']


def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\n\nDate Time: ", dt_string, "\n\n")
    i = 0
    found = 0
    for location in location_arr:
        print(location)
        with urllib.request.urlopen(base_url_link+location) as response:
            page_html = response.read()
        soup = BeautifulSoup(page_html, 'lxml')
        unavailable = soup.find('div', attrs={'class': 'alert-danger'})
        if unavailable is not None:
            # print('No appointments are available in '+locationname_arr[i])
            dt_string = ""
        else:
            dates_html = soup.find('div', attrs={'class': 'col-md-8'})
            date_string = dates_html.find('label', attrs={'class': 'control-label'})
            if set(required_months) & set(date_string.text.split()):
                # print("Matching required months")
                date_string = re.sub('Time of Appointment for ',  '',  date_string.text)
                date_string = re.sub(':', '', date_string)
                message = 'KNOWLEDGE TESTING: '+locationname_arr[i]+' / ('+location+') : '+date_string
                print(message)
                os.system('signal-cli -u +44123456789 send -m "DMV Appoitment Available" +44123456789')
                found = 1
        i = i+1

while True:
    try:
        job()
    except:
        print("Something went wrong")
        time.sleep(60)
    else:
        time.sleep(60)
