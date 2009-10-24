import csv
import time, datetime
from vaccines.models import Site, Event

def transform_datestring(string):
	string = string.strip()
	time_tuple = time.strptime(string, '%m/%d/%y')
	epoch_seconds = time.mktime(time_tuple) 
	return datetime.datetime.fromtimestamp(epoch_seconds)

def run():
	"""
	Load the LA County CSV file into our models.
	
	from vaccines import load; load.run();
	"""
	table = csv.reader(open('./vaccines/data/lacounty.csv'))
	table.next()
	for i, row in enumerate(table):
		SPA,SupDist,Date,Day,Location,Street,City,ZIPCode,HoursOfOperation = row
		
		site, site_created = Site.objects.get_or_create(
			spa=SPA,
			supervisor_district=SupDist,
			location=Location,
			street=Street,
			city=City,
			zipcode=ZIPCode,
			)
		if site_created:
			print "Added site %s" % site
			
		event, event_created = Event.objects.get_or_create(
			site = site,
			date = transform_datestring(Date),
			hours_of_operation = HoursOfOperation,
		)
		if event_created:
			print "Added event %s" % event
		