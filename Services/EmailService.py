import imaplib
import email
from tkinter import *

smallText = 18


class EmailService(Frame):
    def __init__(self, parent, *args, **kargs):
        Frame.__init__(self, parent, bg='black')
        self.username = "it414testemail@gmail.com"
        self.password = "IT414Pass"
        self.title = 'Unread Emails'
        self.emailLbl = Label(self, font=('Verdana', smallText), fg="white", bg="black", justify=LEFT, wraplength=800)
        self.emailLbl.pack(side=TOP, anchor=N)
        self.youtubeContainer = Frame(self, bg="black")

        self.read(self.username, self.password)

    def read(self, username, password, sender_of_interest=None):
        emailList = ""
        counter = 0

        # Login to INBOX
        imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        imap.login(username, password)
        imap.select('INBOX')

        # Use search(), not status()
        # Print all unread messages from a certain sender of interest
        if sender_of_interest:
            status, response = imap.uid('search', None, 'UNSEEN', 'FROM {0}'.format(sender_of_interest))
        else:
            status, response = imap.uid('search', None, 'UNSEEN')
        if status == 'OK':
            unread_msg_nums = response[0].split()
        else:
            unread_msg_nums = []
        # imap.store(unread_msg_nums, "-FLAGS", '\Seen')
        data_list = []

        for e_id in unread_msg_nums:
            data_dict = {}
            e_id = e_id.decode('utf-8')
            _, response = imap.uid('fetch', e_id, '(RFC822)')
            imap.uid('STORE', e_id, "-FLAGS", '\SEEN')
            html = response[0][1].decode('utf-8')
            email_message = email.message_from_string(html)
            data_dict['mail_subject'] = email_message['Subject']
            data_dict['mail_from'] = email.utils.parseaddr(email_message['From'])
            data_list.append(data_dict)
        for i in data_list:
            if counter == 3:
                break
            mailFrom = str(i["mail_from"][0])
            mailSubject = str(i["mail_subject"])
            if '?' in mailFrom or '?' in mailSubject:
                continue
            emailList += "From: " + str(i["mail_from"][0]) + " Subject: " + str(i["mail_subject"]) + "\n"
            counter += 1

        self.emailLbl.config(text=emailList)


