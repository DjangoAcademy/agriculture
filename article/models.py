
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=15, blank=False)
    slug = models.SlugField(unique=True, max_length=20, editable=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bytag', args=[str(self.slug)])

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i').
                       replace('ə', 'e').
                       replace('ö', 'o').
                       replace('ğ', 'g').
                       replace('ç', 'c').
                       replace('ş', 's').
                       replace('ü', 'u').
                       replace('ı', 'i').
                       replace('Ə', 'e').
                       replace('Ö', 'o').
                       replace('Ğ', 'g').
                       replace('Ç', 'c').
                       replace('Ş', 's').
                       replace('Ü', 'u').
                       replace('I', 'i'))

        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Tag, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(unique=True, max_length=60, editable=False)
    thumbnail = models.ImageField(upload_to='article/thumbnails/category/', blank=False)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('bycategory', args=[str(self.slug)])

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i').
                       replace('ə', 'e').
                       replace('ö', 'o').
                       replace('ğ', 'g').
                       replace('ç', 'c').
                       replace('ş', 's').
                       replace('ü', 'u').
                       replace('ı', 'i').
                       replace('Ə', 'e').
                       replace('Ö', 'o').
                       replace('Ğ', 'g').
                       replace('Ç', 'c').
                       replace('Ş', 's').
                       replace('Ü', 'u').
                       replace('I', 'i'))

        return slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Category, self).save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    tags = models.ManyToManyField(Tag, blank=False)
    thumbnail = models.ImageField(blank=False, upload_to='article/thumbnails')
    content = models.TextField(blank=False)
    slug = models.SlugField(unique=True, max_length=60, editable=False)
    publish_date = models.TimeField(auto_now_add=True)
    viewscounter = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_details', args=[str(self.slug)])


    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i').
                       replace('ə', 'e').
                       replace('ö', 'o').
                       replace('ğ', 'g').
                       replace('ç', 'c').
                       replace('ş', 's').
                       replace('ü', 'u').
                       replace('ı', 'i').
                       replace('Ə', 'e').
                       replace('Ö', 'o').
                       replace('Ğ', 'g').
                       replace('Ç', 'c').
                       replace('Ş', 's').
                       replace('Ü', 'u').
                       replace('I', 'i'))
        """""
        unique_slug = slug
        counter = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        """""
        return slug


    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()

        return super(Article, self).save(*args, **kwargs)