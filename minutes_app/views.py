# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods

from forms import MeetingForm
from models import Meeting


# main function that handles all requests.
@require_http_methods(["GET", "POST"])
def meeting(request, meeting_slug=''):
    if request.method == 'POST':
    
        if meeting_slug == '':
            # first time post, adding a new meeting
            meeting_form = MeetingForm(data=request.POST)
            
            if meeting_form.is_valid():
                meeting = meeting_form.save()

#             subject, from_email = 'New Minutes of Meeting created', 'arundhaj@arundhaj.com'
#             html_content = render_to_string('email.html', {'mom_url': "%s%s/" % (request.build_absolute_uri(), meeting.url_ref)})
#             text_content = strip_tags(html_content)
#             msg = EmailMultiAlternatives(subject, text_content, from_email, [meeting.email])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()

            return redirect("%s/" % meeting.url_ref)
        else: 
            # edit an existing meeting
            meeting = Meeting.objects.get(url_ref=meeting_slug)
            meeting_form = MeetingForm(data=request.POST, instance=meeting)
            meeting_form.save()

            # return redirect("%s/" % meeting_slug)
            return render(request, 'meeting.html', {'meeting_form' : meeting_form, 'save_btn' : 'Update', 'delete_btn' : 'true', 'meeting_slug' : meeting.url_ref})
    
    elif request.method == 'GET':
    
        if meeting_slug == '':
            # first time visit, blank form
            meeting_form = MeetingForm()
            return render(request, 'meeting.html', {'meeting_form' : meeting_form, 'save_btn': 'Save', 'delete_btn' : 'false'})
        
        else:
            meeting = Meeting.objects.get(url_ref=meeting_slug)
            meeting_form = MeetingForm(instance=meeting)
            return render(request, 'meeting.html', {'meeting_form' : meeting_form, 'save_btn': 'Update', 'delete_btn' : 'true', 'meeting_slug' : meeting.url_ref})