import csv

from django.contrib import messages
from django.shortcuts import render

from .models import Contact


def contact_upload(request):
    template = "contact_upload.html"
    msg = {
        'order': 'Order of the file is (first_name, last_name, email)'
    }

    if request.method == 'GET':
        return render(request, template, msg)

    contact_csv_file = request.FILES['file'].name

    if not contact_csv_file.endswith('.csv'):
        messages.error(request, '.csv files only supported')
    else:
        with open(contact_csv_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            for line in csv_reader:
                Contact.objects.update_or_create(
                    first_name=line[0],
                    last_name=line[1],
                    email=line[2]
                )

    return render(request, template, msg)
