from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.

def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    input_receiver = request.POST['inputReceiver']
    input_title = request.POST['inputTitle']
    input_content = request.POST['inputContent']
    print(checked_res_list,'/',input_receiver,'/',input_title,'/',input_content)

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>"+input_content+"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다. </p>"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>"+restaurant.restaurant_name+"</h2>"
        mail_html += "<h4>* 상세내용 </h4> <p>" + restaurant.restaurant_name + "</p><br>"

    mail_html += "</body></html>"

    return HttpResponseRedirect(reverse('index'))