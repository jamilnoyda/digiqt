from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _

# Create your models here.


class Movie(models.Model):

    title = models.CharField(max_length=200, db_index=True)
    rating = models.FloatField()
    rank = models.IntegerField()
    year = models.IntegerField()
    # release_date = models.DateTimeField(auto_now_add=True)
    # duration = models.DateTimeField(auto_now=True, editable=False)
    # description = models.CharField(max_length=200)

    class Meta:
        ordering = ("-rating",)
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.title

    # slug = models.SlugField(max_length=200, db_index=True, unique=True)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("categories:category-detail", kwargs={"pk": self.id})

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

