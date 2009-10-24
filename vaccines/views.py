# Utils
import datetime
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

# Models
from vaccines.models import Site, Event


def index(request):
	"""
	The homepage.
	"""
	object_list = Event.objects.all().select_related().order_by('date', 'site__location')
	
	today = datetime.datetime.now().date()
	
	upcoming_list = []
	past_list = []
	
	for obj in object_list:
		if obj.date >= today:
			upcoming_list.append(obj)
		else:
			past_list.append(obj)
	
	return direct_to_template(request, 'index.html', {
		'upcoming_list': upcoming_list,
		'past_list': past_list,
		'today': today,
	})
	
def xls(request):
	"""
	A method for exporting to Microsoft Excel lifted from "DjangoSnippet #911":http://www.djangosnippets.org/snippets/911/
	"""
	response = direct_to_template(request, "xls.html", dict(object_list=Event.objects.all().select_related().order_by('date', 'site__location')))
	response['Content-Disposition'] = 'attachment; filename=scores.xls'
	response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
	return response