from django.conf.urls import patterns, url

urlpatterns = patterns('minutes_app.views',
    url(r'^$', 'meeting'), # create a new meeting
    # url(r'meeting/^$', 'meeting'), # create a new meeting
    # url(r'^meeting/(?P<meeting_id>[0-9]+)/$', 'meeting'), # show an existing meeting
    url(r'^(?P<meeting_slug>[a-zA-Z0-9]{5})/$', 'meeting'), # show an existing meeting
)