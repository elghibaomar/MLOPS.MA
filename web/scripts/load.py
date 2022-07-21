import csv
from Email_Marketing.models import Email


def run():
    file = open('/app/scripts/data_email_marketing.csv')
    read_file = csv.reader(file)

    Email.objects.all().delete()

    count = 1

    for email in read_file:
        if count == 1 :
            pass
        else :
            Email.objects.create(Customer_id = email[1] , Product_id = email[2] , Date = email[3] , Gender = email[4] , 
            Template = email[5] , Countries = email[6] , Purchase = email[7] , Marital = email[8] , Age = email[9]  )
        count = count + 1