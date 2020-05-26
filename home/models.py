# from django.db import models

# # Create your models here.


# class savings(models.Model):
#     username = models.CharField('username', max_length=30)
#     money_to_be_saved = models.CharField(
#         'MoneytobeSaved', max_length=10, null=False)
#     deadline = models.CharField('deadline', max_length=30, null=False)
#     paid_sum = models.CharField('paid_sum',max_length=9,null=False,default='000000000')
#     remaining_days = models.CharField('remaining_days',max_length=30,null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)


# # class transactions(models.Model):
# #     username = models.CharField('username', max_length=30, null = True)
# #     amountpaid = models.CharField("amountpaid", max_length=10, null = True)
# #     timestamp = models.DateTimeField(auto_now_add=True)

# class payment_details(models.Model):
#     username = models.CharField('username', max_length=30, null=True)
#     cardnumber = models.CharField('cardnumber', max_length=16, null=True)
#     nameoncard = models.CharField('nameoncard', max_length=30, null=True)
#     expirymonth = models.CharField('expirymonth', max_length=5, null=True)
#     expiryyear = models.CharField('expiryyear', max_length=5, null=True)
#     cvv = models.CharField('cvv', max_length=5, null=True)


from django.db import models

# Create your models here.
class passenger(models.Model):
    name = models.CharField('name' ,max_length = 20)
    username = models.CharField('username', primary_key =True , max_length =30)
    email = models.EmailField('email' ,max_length = 70 ,blank = True )
    password = models.CharField('password' ,max_length = 25)
    phone = models.CharField('phone' ,max_length = 20)
    class Meta:
        unique_together = ( 'email', 'phone')


class trainDetails(models.Model):
    train_no = models.CharField('train_no',max_length = 10,primary_key = True)
    train_name = models.CharField('train_name',max_length = 20 ,null=True)
    From = models.CharField('from',max_length =20, null = True)
    to = models.CharField( 'To' ,max_length = 20, null = True)
    arrival_time = models.TimeField(null = True)
    departure_time = models.TimeField(null = True)

class bookings(models.Model):    
    username = models.ForeignKey(passenger, on_delete = models.CASCADE)
    train_no = models.ForeignKey(trainDetails , on_delete = models.CASCADE)
    train_name = models.CharField('train_name',max_length = 20)
    journey_date = models.DateField('journey_date',null=True)
    From = models.CharField('From', max_length = 20)
    to = models.CharField('to' , max_length = 20)
    phone = models.CharField('phone' ,max_length = 20)
    name = models.CharField('name' ,max_length = 20)
    nationality = models.CharField('nationality',max_length = 20)
    gender = models.CharField('gender' , max_length = 15)
    age = models.IntegerField('age',null = True, default = 15)
    be = (
        ('Lower' , 'lower'),
        ('Middle' , 'middle'),
        ('Upper' , 'upper'),
    )
    choice_of_berth =models.CharField('choice_of_berth',choices = be ,max_length =10 ,null = True, default = 'lower')
    class Meta:
        unique_together = ('username','train_no','journey_date')
       # verbose_name_plural = "book"
    



class payment_details(models.Model):
    username = models.CharField('username', max_length=30, null=True)
    card_no = models.CharField('Card_no',max_length=17, primary_key = True)
    name_of_card_holder = models.CharField('Name',max_length = 20,null = True)
    expiry_month = models.IntegerField('month', default = 0)
    expiry_year = models.IntegerField('Year', default = 0)
    cvv = models.CharField('cvv', max_length=5, null=True)