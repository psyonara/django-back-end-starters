from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Each blog post has a category so that the blog can be subdivided into these categories.
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, db_index=True, blank=True, default="")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    """
    This is the main model that contains all the posts' data.
    """
    # The date on which the post must appear on the blog
    publish_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, blank=True, default="")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    # A separate image that is displayed as the main image of the post
    main_image = models.ImageField(upload_to="uploads/%Y/%m/%d/", null=True, blank=True)
    # The main content of the blog post
    content = models.TextField()

    def __str__(self):
        if self.publish_date:
            return f"{self.publish_date:%Y-%m-%d}: {self.title}"

        return f"(DRAFT) {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
