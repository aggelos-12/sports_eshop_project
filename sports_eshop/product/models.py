from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
# Create your models here.

# from phonenumber_field.modelfields import PhoneNumberField


# class Customers(models.Model):
#     name = models.CharField(max_length=150)
#     email
#     password = forms.CharField(widget=forms.PasswordInput)
#     shoe_size = models.IntegerField(default=42)
#     clothes_size = models.CharField(max_length=3)
#     address = models.CharField(max_length=150)
#     phoneNumber = PhoneNumberField(null=False, blank=False, unique=True)

#

#
#
# class Orders(models.Model):
#     amount = models.DecimalField(max_digits=4, decimal_places=2)
#     name = models.CharField(max_length=150)
#     submissionDate = models.DateTimeField()
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#
#
# class Listings(models.Model):
#     price = models.IntegerField(default=0)
#     size = models.IntegerField()
#     sellerName = models.CharField(max_length=150)
#     sellerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     productName = models.CharField(max_length=50)
#
#
# class Sizes(models.Model):
#     quantity = models.IntegerField(default=1)
#     size = models.IntegerField()
#     shoeID = models.ForeignKey()

class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    slug = models.SlugField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail