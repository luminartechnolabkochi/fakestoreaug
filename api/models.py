from django.db import models

class Products(models.Model):

    name=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    image=models.ImageField(null=True,upload_to="images")

    def __str__(self):
        return self.name



# ORM
# orm for creating a resourse
#modelname.objects.create(field1=value1,field2=value2,,,,,)
#Products.objects.create(name="samsunga72",price=32000,description="mobile",category="electronics")


# ORM query for fetching all records
#qs=modelname.objects.all()
#
#ORM filter queries
# qs=modelname.objects.filter(category="electronics")


# qs=Products.objects.all().exclude(category="electronics")

# orm query for fetching a specific record
# qs=modelname.objects.get(id=1)


# price > 25000
# qs=Products.objects.filter(price__lt=2500) lessthan
#__lt <
# __lte <=
#__gt >
# __gte >=

# products in range of 20000 to 30000 ?


# return all categories
# Products.objects.values_list('category')