from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient import errors

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

import auth
def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

http = credentials.authorize(httplib2.Http())
service = discovery.build('gmail', 'v1', http=http)

import send_email

subject = []
text = []
attached_file = []

subject.append("Engineering Conference Sponsorship Request")
subject.append("Engineering Conference Speaker Invitation") 
text.append("Hi there, We are excited to contact you with an opportunity of being a possible sponsor for the inaugural Students in Engineering and Technology conference! Students in Engineering and Technology (SET) is a non-profit, student-run, organization that seeks to incite interest of engineering and technological career opportunities in youth. Our organization was founded by six students at Colonel By Secondary School, with the purpose of creating a one-day engineering conference geared towards high school students interested in pursuing engineering or other technology-related fields. Our conference will feature a series of panels, workshops, and activities to engage students in the emergence of engineering in our daily lives. Students will also have the opportunity to network with engineering students, professionals, and firms. It will be held at the Engineering Faculty at the University of Ottawa on Saturday October 20th. To improve the quality of our conference, we rely on the support of corporate sponsors such as yourself. We are seeking monetary donations to make our conference as affordable as possible, as we are trying to supply all the tools and materials participants may need for our competition. Our Sponsorship Package is attached below for more information over how your company can support us. If you have any questions or concerns, feel free to contact our Director of Corporate Relations, David Chen, at (ottawa.set@gmail.com). You can also visit our website at http://setottawa.com/ for more information on what we do. We look forward to your reply. Sincerely, The Students in Engineering and Technology Team")
text.append("We are excited to invite you to participate as a speaker for this year’s Student in Engineering and Technology (SET) conference! Students in Engineering and Technology (SET) is a non-profit, student-run, organization that seeks to incite interest of engineering and technological career opportunities in youth. Our organisation was founded by six students from Colonel By Secondary School with the purpose of creating an annual one-day engineering conference geared towards high school students who are interested in pursuing engineering or other technology-related fields. We are searching for professionals in the engineering industry that are willing to be a resource to intelligent and motivated students in Ottawa. We would like your assistance in our goal of inspiring and preparing students for their careers in STEM. As a speaker, your task will be to to host a seminar for an audience of high school students. The seminar itself can be on any subject of your choosing and may include any additional interactive element you wish to organize. We simply hope that you can provide students with a taste of your experiences as a student and professional in engineering. We are certain that your contribution to the conference will help make it a memorable experience for everyone. Please let us know if you are interested in presenting at SET 2018. Feel free to contact us by email(ottawa.set@gmail.com) should you have any questions, comments or concerns. Sincerely, The Students in Engineering and Technology Team")
attached_file.append('Sponsorship_Package.pdf')
attached_file.append('Speaker_Invitation_Package.pdf')

n = int(input("To how many emails are you sending?"))
emails = []

for i in range(0, n):
    emails.append(input("Enter email"))
    choice = int(input("Are you trying to contact a sponsor (enter 0) or a speaker (enter 1)?"))
    sendInst = send_email.send_email(service)
    message = sendInst.create_message_with_attachment('ottawa.set@gmail.com', emails[i], subject[choice], text[choice], attached_file[choice])
    sendInst.send_message('me',message)
