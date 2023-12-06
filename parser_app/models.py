from django.db import models

class ParserModel(models.Model):
    title_name = models.CharField(max_length=100)
    title_url = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.title_name

