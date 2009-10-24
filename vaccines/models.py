from django.db import models


class Site(models.Model):
	"""
	The location of a H1N1 vaccination station.
	"""
	SPA_CHOICES = (
		# Source: http://publichealth.lacounty.gov/spa/spamap.htm
		('1', 'Antelope Valley'),
		('2', 'San Fernando'),
		('3', 'San Gabriel'),
		('4', 'Metro'),
		('5', 'West'),
		('6', 'South'),
		('7', 'East'),
		('8', 'South Bay'),
	)
	spa = models.CharField(verbose_name='Service Planning Area', max_length=1, choices=SPA_CHOICES)
	SUPERVISOR_CHOICES = (
		('1', 'District 1, Gloria Molina'),
		('2', 'District 2, Mark Ridley-Thomas'),
		('3', 'District 3, Zev Yaroslavsky'),
		('4', 'District 4, Don Knabe'),
		('5', 'District 5, Michael Antonovich'),
	)
	supervisor_district = models.CharField(max_length=1, choices=SUPERVISOR_CHOICES)
	location = models.TextField()
	street = models.TextField()
	city = models.TextField()
	zipcode = models.CharField(max_length=5)
	latitude = models.FloatField(null=True, blank=True)
	longitude = models.FloatField(null=True, blank=True)

	class Meta:
		ordering = ('location',)

	def __unicode__(self):
		return u'%s (%s)' % (self.location, self.city)


class Event(models.Model):
	"""
	The date and time of a H1N1 vaccination event.
	"""
	site = models.ForeignKey(Site)
	date = models.DateField()
	hours_of_operation = models.TextField(blank=True)
	
	class Meta:
		ordering = ('date',)
		get_latest_by = 'date'
	
	def __unicode__(self):
		return u'%s on %s' % (self.site, self.date)