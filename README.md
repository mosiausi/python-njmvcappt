*** This is not for Knowledge Test Appointment ***

Pre-Requisites:
Install Python and its required libraries

Mostly you may need Beatiful soup and lxml package. Install those with the below commands.

pip install bs4
pip install lxml


If you want to search for appointment only on specific locations say Eatontown and Freehold, then update the location_arr and locationname_arr variables
location_arr = ['238', '243']
locationname_arr = ['Eatontown', 'Freehold']


if you want to be notified only when appt is available on specific month, for example only on "April" then update the required moths variable accordingly.
required_months = ['April']

