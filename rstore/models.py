from django.db import models

# Create your models here.


class serv(models.Model):
    servname = models.CharField(max_length=16)
    servdesc = models.TextField()
    servcost = models.IntegerField(default=0)
    servpic = models.ImageField(upload_to='assets/images/productimg')
    servishigh = models.BooleanField(default=False)

    def __str__(self):
        return self.servname


class cust(models.Model):
    custfname = models.CharField(max_length=16)
    custlname = models.CharField(max_length=16)
    custemail = models.CharField(max_length=32)
    custphn = models.CharField(max_length=12)
    custpwd = models.CharField(max_length=16)
    custadd1 = models.CharField(max_length=64)
    custadd2 = models.CharField(max_length=64)
    custcity = models.CharField(max_length=16)
    custdist = models.CharField(max_length=16)
    custstate = models.CharField(max_length=16)
    custpincode = models.CharField(max_length=7)

    def __str__(self):
        return self.custfname+' '+self.custlname


class trans(models.Model):
    serv = models.IntegerField(default=0)
    servname = models.CharField(max_length=16)
    servcost = models.IntegerField(default=0)
    servqnt = models.IntegerField(default=0)
    servtotal = models.IntegerField
    cust = models.IntegerField(default=0)
    custname = models.CharField(max_length=16)

    def __str__(self):
        return self.servname


class cart(models.Model):
    serv = models.IntegerField(default=0)
    servname = models.CharField(max_length=16)
    servcost = models.IntegerField(default=0)
    servqnt = models.IntegerField(default=0)
    servtotal = models.IntegerField(default=0)
    cust = models.IntegerField(default=0)
    custname = models.CharField(max_length=16)

    def __str__(self):
        return self.servname


class msg(models.Model):
    mname = models.CharField(max_length=128)
    memail = models.CharField(max_length=128)
    mphone = models.CharField(max_length=128)
    mmsg = models.TextField()

    def __str__(self):
        return self.mname


class clin(models.Model):
    cname = models.CharField(max_length=16)
    cimg = models.ImageField(upload_to='assets/images/clientimg')
    cliishigh = models.BooleanField(default=False)
    clinurl = models.CharField(max_length=64)

    def __str__(self):
        return self.cname
