from django.db import models


class Course(models.Model):

    CATEGORY = (
        ('Basic Course', 'Basic Course'),
        ('Accounting Course', 'Accounting Course'),
        ('Designing Course', 'Designing Course'),
        ('Spoken English', 'Spoken English'),
        ('Digital Marketing', 'Digital Marketing'),
        ('IT Professional', 'IT Professional'),
    )

    image = models.ImageField(upload_to="images/")
    document = models.FileField(upload_to="documents/", blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="in months")
    price = models.IntegerField()
    category = models.CharField(
        max_length=50, choices=CATEGORY, default='Basic Course')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:30]


class Blog(models.Model):
    image = models.FileField(upload_to='blog/')
    text = models.TextField(help_text="Use HTML Tags to format your Blog.")
    heading = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
