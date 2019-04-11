from django.db import models


class MenuSections(models.Model):
    """This class represents a MenuSection model"""

    name = models.CharField(max_length=255, null=False,
                            blank=False, unique=True)

    def __str__(self):
        """Returns a readable representation of model"""
        return "{}".format(self.name)
