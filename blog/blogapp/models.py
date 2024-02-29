from django.db import models

# Create your models here.
# creating  a database with name Product and name, desc etc are columns
class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='gallery')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self, name, desc, img):
        self.name = name
        self.desc = desc
        self.img = img
        self.save()

    def short_description(self):
        # split the description in to words
        words = self.desc.split()
        if len(words) > 50:
        # Join the first 50 words and add "..." at the end
            return ''.join(words[:30]) + '...'
        else:
            return self.desc





