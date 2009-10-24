import csv
import time, datetime
from vaccines.models import Site, Event

def flush():
	[i.delete() for i in Event.objects.all()]
	[i.delete() for i in Site.objects.all()]

def transform_datestring(string):
	string = string.strip()
	time_tuple = time.strptime(string, '%m/%d/%y')
	epoch_seconds = time.mktime(time_tuple) 
	return datetime.datetime.fromtimestamp(epoch_seconds)

def clean_name(string):
	string = string.strip()
	string = string.replace('Dist.-DRIVE THRU', 'District')
	string = string.replace('Rec Ctr', 'Recreation Center')
	string = string.replace('Rec. Ctr', 'Recreation Center')
	string = string.replace('Dept.', 'Department')
	string = string.replace('Com Ctr', 'Community Center')
	string = string.replace('Santa Monica college', 'Santa Monica College')
	string = string.replace('Watts Labor Cmty Action Cmttee', 'Watts Labor Community Action Committee')
	string = string.replace('Cal State University, LA-Gym.', 'Cal State University, LA Gym')
	string = string.replace('Ctr', 'Center')
	return string

def run():
	"""
	Load the LA County CSV file into our models.
	
	from vaccines import load; load.run();
	"""
	flush()
	
	table = csv.reader(open('./vaccines/data/lacounty.csv'))
	table.next()
	
	for i, row in enumerate(table):
		SPA,SupDist,Date,Day,Location,Street,City,ZIPCode,HoursOfOperation = row
		
		site, site_created = Site.objects.get_or_create(
			spa=SPA,
			supervisor_district=SupDist,
			location=clean_name(Location),
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
		